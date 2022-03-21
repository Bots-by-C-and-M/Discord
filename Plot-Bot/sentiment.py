"""
Might need to import flair. It has a pretrained sentiment analysis model

Also the first time running might take a bit because it downloads the TextClassifier (en-sentiment)
"""

from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('en-sentiment')

def sentiment_analysis(message):
    sentence = Sentence(message)
    classifier.predict(sentence)
    return sentence.labels

# print sentence with predicted labels
discord_message = "No nicknames, your suggestion works. I’ll get more of the bot done this weekend. The full thing is going to take some time work out. Saoirse has a birthday party tomorrow afternoon/evening. But I’ll work on it in the morning"
print('Sentence above is: ', sentiment_analysis(discord_message))