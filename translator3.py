from textblob import TextBlob


text = TextBlob("this is a python library for translation")
text.translate(to='ar')