from nltk.corpus import stopwords
from nltk.corpus import wordnet 
import time

DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))
f = open(f'./test/{DATE}.txt', 'r')

stopword = set(stopwords.words('english'))
data = list()


def preprocessing(data):
	data = data.lower()
	words = RegexpTokenizer(r'[a-z]+').tokenize(data)
	words = [ w for w in words if not w in stopword ]

	for pos in [wordnet.NOUN, wordnet.VERB, wordnet.ADJ, wordnet.ADV]:
		words = [ WordNetLemmatizer().lemmatize(x, pos) for x in words ]

	return " ".join(words)

def main():
	lines = f.readlines()
	for line in lines:
		new_line = preprocessing(line)
		data.append(new_line)

	

if __init__ == '__main__':
	main()
	f.close()