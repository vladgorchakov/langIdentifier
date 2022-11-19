import langid
from iso639 import Lang


class LangIdentifier:
    @staticmethod
    def get_lang_from_code(lang_code):
        return Lang(lang_code)[0]

    def detect(self, text):
        lang_code = langid.classify(text)
        return self.get_lang_from_code(lang_code[0])
