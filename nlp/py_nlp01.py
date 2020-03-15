"""python自然语言处理 字符串操作"""
import string

import nltk
from nltk import word_tokenize, re, edit_distance, jaccard_distance
from nltk.corpus import stopwords
from nltk.tokenize.util import spans_to_relative

"""分词、正则与分词器，更多参考 https://docs.python.org/zh-cn/3.8/library/re.html"""
# text = " Welcome readers. I hope you find it interesting. Please do reply."
# sent_tokenize(text)
input_text = " Hello everyone. Hope all are fine and doing well. Hope you find the book interesting"
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
out = tokenizer.tokenize(input_text)
print(out)

input_text = 'PierreVinken , 59 years old , will join as a nonexecutive director on Nov. 29 .>>'
out = nltk.word_tokenize(input_text)
print(out)

# r = input("Please write a text:")
# print("count text words: ", len(nltk.word_tokenize(r)))

# tokenizer = nltk.TreebankWordTokenizer()
# tokenizer = nltk.WordPunctTokenizer()
tokenizer = nltk.RegexpTokenizer("[\w]+")
out = tokenizer.tokenize('PierreVinken , 59 years old , will join as a nonexecutive director on Nov. 29 .>>')
out = nltk.regexp_tokenize(input_text, pattern='\w+|\$[\d\.]+|\S+')
out = list(nltk.WhitespaceTokenizer().span_tokenize(input_text))
out = list(spans_to_relative(nltk.WhitespaceTokenizer().span_tokenize(input_text)))
print(out)

"""标准化"""
# 消除标点符号
tokenized_docs = [word_tokenize(doc) for doc in input_text]  # 分词
print(tokenized_docs)
x = re.compile('[%s]' % re.escape(string.punctuation))
print(x)  # re.compile('[!"\\#\\$%\\&\'\\(\\)\\*\\+,\\-\\./:;<=>\\?@\\[\\\\\\]\\^_`\\{\\|\\}\\~]')
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review:
        """re是regular expression的所写，表示正则表达式 sub是substitute的所写，表示替换"""
        """re.sub(pattern, repl, string, count=0, flags=0)"""
        """x.sub()"""
        new_token = x.sub(u'', token)  # 不匹配正则的用空字符(u'')替换掉
        if not new_token == u'':
            new_review.append(new_token)
        if len(new_review) == 0:  # 跳过空格
            continue
        tokenized_docs_no_punctuation.append(new_review)  # breakpoint
print(tokenized_docs_no_punctuation)

print("分词 nltk_data\\corpora\\stopwords\\*")
lang = stopwords.fileids()
print("语言：", lang)
stops = set(stopwords.words("english"))
print("英语单词-停顿词：", stops)
words = ["Don't", 'hesitate', 'to', 'ask', 'questions']
out = [word for word in words if word not in stops]
print(out)

"""相似性度量（比较）算法 参考源码 distance.py"""
out = edit_distance('relate', 'relation')  # 动态规划方法（y=x映射）
print(out)
X = set([10, 20, 30, 40])
Y = set([20, 30, 60])
print(jaccard_distance(X, Y))  # 集合相交法  交集长/并集长
"""
史密斯-沃特曼算法 nlp/Smith-Waterman-Algorithm-Example.gif
基于生物信息学的知识来匹配蛋白序列或者DNA序列的算法  找出两个序列中具有高相似度的片段
参考wiki https://zh.wikipedia.org/wiki/%E5%8F%B2%E5%AF%86%E6%96%AF-%E6%B2%83%E7%89%B9%E6%9B%BC%E7%AE%97%E6%B3%95
该算法主要分两步，计算得分矩阵和寻找最优比对序列
    得分矩阵的作用是对两序列中两两位置进行打分以逐步记录最优比对。矩阵的长度和宽度分别为两序列长度+1。额外的首行和首列是为了让序列的末端可以和空位匹配。首行和首列均设为0。
    空位罚分决定了插入或者删除的分值。最基本的空位罚分方式为每次插入或者删除的得分相同。
    打分
    回溯
初始化得分矩阵->定置换矩阵及空位罚分方法->打分->回溯
"""
