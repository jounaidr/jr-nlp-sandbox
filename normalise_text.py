import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#nltk.download('stopwords')
#nltk.download('punkt')

input = 'I like go walking! I was interested in dancing.'

out = input.lower() #lower case everything
print(out)
out = re.sub(r'[^\w\s]', '', out) #remove punctuation (could add exceptions but not applicable to input)
print(out)
out = nltk.word_tokenize(out) #tokenize
print(out)
out = [word for word in out if not word in stopwords.words()] #remove stop words
print(out)
out = [PorterStemmer().stem(word) for word in out] #stem tokens
print(out)

#Could lemmatize instead of stem: https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908