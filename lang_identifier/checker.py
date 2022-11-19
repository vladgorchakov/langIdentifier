class TextChecker:
    @staticmethod
    def is_digits(value):
        return value.replace(' ', '').replace('.', '').isdigit()

    def check(self, text):
        if len(text) == 0:
            return False
        elif self.is_digits(text):
            return False

        return True
