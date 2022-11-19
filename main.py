from lang_identifier.identifier import LangIdentifier
from lang_identifier.checker import TextChecker

text = 'In this example, we will illustrate'
tc = TextChecker()
identifier = LangIdentifier()
if tc.check(text):
    print(identifier.detect(text))
else:
    print('Incorrect value!')
