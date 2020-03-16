"""统计语言建模"""
"""计算句子中某种语言模式出现概率的统计模型 把自然语言作为模型进行统计分析"""
import nltk
from nltk import ngrams, BigramCollocationFinder, BigramAssocMeasures, unique_list, KneserNeyProbDist
from nltk.corpus import alpino, webtext, stopwords

"""单词分组 util.py"""
n = 4
grams = ngrams(alpino.words(), n)
# for i in grams:
# print(i)
out = list(ngrams([1, 2, 3, 4, 5], 3))
print(out)  # [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

set = set(stopwords.words('english'))
stops_filter = lambda w: len(w) < 3 or w in set
tokens = [t.lower() for t in webtext.words('grail.txt')]
words = BigramCollocationFinder.from_words(tokens)
words.apply_word_filter(stops_filter)
out = words.nbest(BigramAssocMeasures.likelihood_ratio, 10)
print(out)

"""最大似然估计的目的就是：利用已知的样本结果，反推最有可能（最大概率）导致这样结果的参数值。"""
"""最大似然估计wiki https://zh.wikipedia.org/zh-cn/%E6%9C%80%E5%A4%A7%E4%BC%BC%E7%84%B6%E4%BC%B0%E8%AE%A1"""
"""隐马尔科夫模型估计 HMM"""
corpus = nltk.corpus.brown.tagged_sents(categories='adventure')[:700]
print(len(corpus))
tag_set = unique_list(tag for sent in corpus for (word, tag) in sent)
print(len(tag_set))

"""平滑"""
# gt = lambda fd, bins:SimpleGoodTuringProbDist(fd, bins=1e5)
# train_and_test(gt)
corpus = [[((x[0], y[0], z[0]), (x[1], y[1], z[1])) for x, y, z in nltk.trigrams(sent)]
          for sent in corpus[:100]]  # 平滑语料库
tag_set = unique_list(tag for sent in corpus for (word, tag) in sent)
print(len(tag_set))
symbols = unique_list(word for sent in corpus for (word, tag) in sent)
print(len(symbols))
trainer = nltk.tag.HiddenMarkovModelTrainer(tag_set, symbols)
train_corpus = []
test_corpus = []
for i in range(len(corpus)):
    if i % 10:
        train_corpus += [corpus[i]]
    else:
        test_corpus += [corpus[i]]
print(len(train_corpus))
print(len(test_corpus))
kn = lambda fd, bins: KneserNeyProbDist(fd)
# train_and_test(kn)
