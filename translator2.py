from translate import Translator


translator = Translator(from_lang='english', to_lang='arabic')
translation = translator.translate("I am a python developer.")
print(translation)