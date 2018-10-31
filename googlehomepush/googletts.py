# -*- coding: utf-8 -*-
from gtts.tokenizer import pre_processors, Tokenizer, tokenizer_cases
from gtts.utils import _minimize, _len, _clean_tokens
from gtts.lang import tts_langs

from gtts_token import gtts_token
import urllib
import requests
import logging

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Speed:
    """Read Speed
    The Google TTS Translate API supports two speeds:
        'slow' <= 0.3 < 'normal'
    """
    SLOW = 0.3
    NORMAL = 1

class GoogleTTS:
    """TTS -- Google Text-to-Speech.
    An interface to Google Translate's Text-to-Speech API.
    Args:
        text (string): The text to be read.
        lang (string, optional): The language (IETF language tag) to
            read the text in. Defaults to 'en'.
        slow (bool, optional): Reads text more slowly. Defaults to ``False``.
        lang_check (bool, optional): Strictly enforce an existing ``lang``,
            to catch a language error early. If set to ``True``,
            a ``ValueError`` is raised if ``lang`` doesn't exist.
            Default is ``True``.
    See Also:
        :doc:`Pre-processing and tokenizing <tokenizer>`
    Raises:
        AssertionError: When ``text`` is ``None`` or empty; when there's nothing
            left to speak after pre-precessing, tokenizing and cleaning.
        ValueError: When ``lang_check`` is ``True`` and ``lang`` is not supported.
        RuntimeError: When ``lang_check`` is ``True`` but there's an error loading
            the languages dictionnary.
    """

    GOOGLE_TTS_URL = "https://translate.google.com/translate_tts"

    def __init__(
            self,
            text,
            lang='en',
            slow=False,
            lang_check=True
    ):
        # Text
        assert text, 'No text to speak'
        self.text = text

        # Language
        if lang_check:
            try:
                langs = tts_langs()
                if lang.lower() not in langs:
                    raise ValueError("Language not supported: %s" % lang)
            except RuntimeError as e:
                log.debug(str(e), exc_info=True)
                log.warning(str(e))

        self.lang_check = lang_check
        self.lang = lang.lower()

        # Read speed
        if slow:
            self.speed = Speed.SLOW
        else:
            self.speed = Speed.NORMAL

        # Google Translate token
        self.token = gtts_token.Token()

    def url(self):
        """ 
        generate url to call google tts
        """

        try:
            # Calculate token
            part_tk = self.token.calculate_token(self.text)
        except requests.exceptions.RequestException as e:  # pragma: no cover
            log.debug(str(e), exc_info=True)
            raise gTTSError(
                "Connection error during token calculation: %s" %
                str(e))

        payload = {'ie': 'UTF-8',
                    'q': self.text,
                    'tl': self.lang,
                    'ttsspeed': self.speed,
                    'total': 1,
                    'idx': 0,
                    'client': 'tw-ob',
                    'textlen': _len(self.text),
                    'tk': part_tk}

        return self.GOOGLE_TTS_URL + "?" + urllib.parse.urlencode(payload)


class gTTSError(Exception):
    """Exception that uses context to present a meaningful error message"""

    def __init__(self, msg=None, **kwargs):
        self.tts = kwargs.pop('tts', None)
        self.rsp = kwargs.pop('response', None)
        if msg:
            self.msg = msg
        elif self.tts is not None and self.rsp is not None:
            self.msg = self.infer_msg(self.tts, self.rsp)
        else:
            self.msg = None
        super(gTTSError, self).__init__(self.msg)

    def infer_msg(self, tts, rsp):
        """Attempt to guess what went wrong by using known
        information (e.g. http response) and observed behaviour
        """
        # rsp should be <requests.Response>
        # http://docs.python-requests.org/en/master/api/
        status = rsp.status_code
        reason = rsp.reason

        cause = "Unknown"
        if status == 403:
            cause = "Bad token or upstream API changes"
        elif status == 404 and not tts.lang_check:
            cause = "Unsupported language '%s'" % self.tts.lang
        elif status >= 500:
            cause = "Uptream API error. Try again later."

        return "%i (%s) from TTS API. Probable cause: %s" % (
            status, reason, cause)