"""单词的形态"""
from nltk import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer, WordNetLemmatizer
from polyglot.downloader import downloader

"""（英语？）词干提取器 nltk.stem"""
stemmer = PorterStemmer()
stemmer = LancasterStemmer()
stemmer = RegexpStemmer('ing')
out = [stemmer.stem('working'), stemmer.stem('happiness'), stemmer.stem('pairing')]
print(out)
print(SnowballStemmer.languages)
stemmer = SnowballStemmer('spanish')
out = stemmer.stem('comiendo')
print(out)
stemmer = SnowballStemmer('french')
out = stemmer.stem('manager')
print(out)
"""词形还原"""
lemmatizer = WordNetLemmatizer()
out = [lemmatizer.lemmatize('working'), lemmatizer.lemmatize('working', pos='v'), lemmatizer.lemmatize('works')]
print(out)

"""非英语单词提取器 安装polyglot词典"""
# print(downloader.supported_languages_table('morph2'))
