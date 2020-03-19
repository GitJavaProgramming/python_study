"""语义分析"""
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import conll2002, brown
from nltk.corpus import wordnet as wn

out = nltk.boolean_ops()
input_expr = nltk.sem.Expression.fromstring
out = input_expr('X|(Y->Z)')
out = input_expr('-(X & Y)')
out = input_expr('X & Y')
out = input_expr('X <-> -- X')
out = nltk.Valuation([('X', True), ('Y', False), ('Z', True)])
print(out['Z'])
print(out)
expression = input_expr('run(marcus)', type_check=True)
print(expression.argument)
print(expression.argument.type)
print(expression.function)
print(expression.function.type)
sign = {'run': '<e, t>'}
expression = input_expr('run(marcus)', signature=sign)
print(expression.function.type)
nltk.data.show_cfg('grammars/book_grammars/sql1.fcfg')

"""命名实体识别(英语：Named Entity Recognition，简称NER)
指识别文本中具有特定意义的实体
参考wiki 
https://baike.baidu.com/item/命名
https://zh.wikipedia.org/zh-cn/实体
https://baike.baidu.com/item/%E5%91%BD%E5%90%8D%E5%AE%9E%E4%BD%93
命名：指给予名称；定名。
    清代陈昌治刻本【说文解字】名【卷二】【口部】名 自命也。从口从夕。夕者，冥也。冥不相見，故以口自名。武并切。
    就是说晚上看不清，口说一些东西作为自己的代号。（代/号 左人旁 上口旁）
实体（英语：Entity）是有可区别性且内于其自身而独立存在的某种事物。但它不需是物理存在。尤其是抽象和法律拟制也通常被视为实体。
命名实体(named entity)所谓的命名实体就是人名、机构名、地名以及其他所有以名称为标识的实体。
为什么命名实体可以识别？？因为它们是以数学和形式语言为基础，已经做了一个最初的假设，命名实体按我理解可以说成是概念！！
"""
print('**********命名实体识别**********')
sentences1 = nltk.corpus.treebank.tagged_sents()[17]
print(nltk.ne_chunk(sentences1, binary=True))
for documents in conll2002.chunked_sents('ned.train')[25]:
    print(documents)
"""使用词性标注识别命名实体"""
pos_tag(word_tokenize("John and Smith are going to NY and Germany"))
tagger = nltk.tag.UnigramTagger(brown.tagged_sents(categories='news'))
sentences1 = ['John', 'and', 'Smith', 'are', 'going', 'to', 'NY', 'and', 'Germany']
for word, tag in tagger.tag(sentences1):
    print(word, '->', tag)  # 其中有些词性为None，是因为机器还不认识这些概念，所以还需要机器学习
"""使用Wordnet生成同义词集id、语义相似度算法
Wordnet可以定义为一个英语词汇数据库。通过同义词集，可以完善词的概念。
语义相似度算法：略 查找相关资料吧^_^
"""
out = wn.synsets('cat', pos=wn.VERB)
print(out)
out = wn.synset('cat.n.01')
print(out)
print(out.definition())
print(len(out.examples()))
print(out.lemmas())
print([str(lemma.name()) for lemma in out.lemmas()])
print(wn.lemma('cat.n.01.cat').synset())
lion = wn.synset('lion.n.01')
out = lion.path_similarity(out)
print(out)
