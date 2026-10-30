
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

document = "Machine learning cannot be mastered in two months; it needs years of practice and study."
tokens = word_tokenize(document.lower())
filtered = [word for word in tokens if word.isalpha() and word not in set(stopwords.words("english"))]
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]

print("tokens:", tokens)
print("stopword removal:", filtered)
print("stemming:", stemmed)
