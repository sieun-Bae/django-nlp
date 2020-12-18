import sys

from nrclex import NRCLex

from nltk.corpus import stopwords
from nltk.corpus import wordnet 
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

#import time

#DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#f = open(f'./test/{DATE}.txt', 'r')

stopword = set(stopwords.words('english'))
score = list()

def preprocessing(data):
	data = data.lower()
	words = RegexpTokenizer(r'[a-z]+').tokenize(data)
	words = [ w for w in words if not w in stopword ]

	for pos in [wordnet.NOUN, wordnet.VERB, wordnet.ADJ, wordnet.ADV]:
		words = [ WordNetLemmatizer().lemmatize(x, pos) for x in words ]

	return " ".join(words)

def processing(data):
	l = preprocessing(data)
	return NRCLex(l).raw_emotion_scores #[('anticipation', 0.3333333333333333)]

# python3 NRCLex.py data
if __name__ == '__main__':
	processing(sys.argv[1])