"""词类是以语言中的词汇为对象，按照语法作用的不同，将词分为不同的类。"""
import nltk
from nltk import DefaultTagger
from nltk.corpus import treebank, words

"""词性则是以个别词为对象，根据其语法作用，兼顾其意义，将其归类得到的结果。"""
"""参考wiki: https://zh.wikipedia.org/zh-cn/汉语词类"""
nltk.help.upenn_tagset('NNS')
nltk.help.upenn_tagset('VB.*')

text = nltk.word_tokenize("I cannot bear the pain of bear")
out = nltk.pos_tag(text)
out = nltk.tag.str2tuple('bear/NN')
print(out)
print((out[0], out[1]))
print(nltk.tag.tuple2str(out))

treebank_tagged = treebank.tagged_words(tagset='universal')
tag = nltk.FreqDist(tag for (word, tag) in treebank_tagged)
out = tag.most_common()
print(out)

tag = DefaultTagger('NN')
out = tag.tag(['Beautiful', 'morning'])
print(out)
"""英语的十大词类
1.名词noun n.
2.代词pronoun pron.
3.形容词adjective adj.
4.副词 adverb adv.
5.动词verb v.
6.数词numeral num.
7.冠词article art.
8.介词preposition prep.
9.连词conjunction conj.
10.感叹词interjection interj.
"""
print("**********************************")
out = nltk.corpus.words.fileids()
print(out)
print([len(words.words('en')), len(words.words('en-basic'))])

"""机器学习算法：线性回归、Logistic 回归、线性判别分析、朴素贝叶斯、KNN、随机森林等"""
