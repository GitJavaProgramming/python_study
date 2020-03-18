"""句法分析-形式语言与自动机"""
import nltk
from nltk import FreqDist, Nonterminal, nonterminals, Production
from nltk.corpus import treebank, sinica_treebank
from nltk.grammar import toy_pcfg2

print(str(nltk.corpus.treebank).replace('\\\\', '/'))
out = treebank.fileids()
print(out)
print(treebank.words('wsj_0007.mrg'))
print(treebank.tagged_words('wsj_0007.mrg'))
print(treebank.parsed_sents('wsj_0007.mrg')[2])
# 语法树
# treebank_chunk.chunked_sents()[1].draw()
# out = treebank_chunk.chunked_sents()[1].leaves()
# out = treebank_chunk.chunked_sents()[1].pos()
# out = treebank_chunk.chunked_sents()[1].productions()
# print(out)
fd = FreqDist()
fd.items()
print(sinica_treebank.sents())
print(sinica_treebank.parsed_sents()[27])

"""上下文无关文法（Context-free Grammar, CFG）
参考wiki 
自动机理论 https://zh.wikipedia.org/zh-cn/%E8%87%AA%E5%8B%95%E6%A9%9F%E7%90%86%E8%AB%96
在计算机科学中，若一个形式文法 G = (V, Σ, P, S) 的产生式规则都取如下的形式：A -> α，则谓之。其中 A∈V ，α∈(V∪Σ)* 。
上下文无关文法取名为“上下文无关”的原因就是因为字符 A 总可以被字符串 α 自由替换，而无需考虑字符 A 出现的上下文。
一个CFG由以下部分组成：
    非终结符的有限集合（N）
    终结符的有限集合（T）
    开始符号（S）
    产生式的有限集合（P），形如：A->a
"""
# 非终结符
nonterminal1 = Nonterminal('NP')
nonterminal2 = Nonterminal('VP')
nonterminal3 = Nonterminal('PP')
print((nonterminal1 == nonterminal2))
print((nonterminal2 == nonterminal3))
print((nonterminal1 == nonterminal3))

S, NP, VP, PP = nonterminals('S, NP, VP, PP')
N, V, P, DT = nonterminals('N, V, P, DT')
# 产生式
production1 = Production(S, [NP, VP])
production2 = Production(NP, [DT, NP])
production3 = Production(VP, [V, NP, NP, PP])
print(production1.lhs(), production1.rhs())
print(production2.lhs(), production2.rhs())
print(production3.lhs(), production3.rhs())

# 语法解析
gram1 = nltk.data.load('grammars/large_grammars/atis.cfg')
# print(gram1)
sent = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sent = nltk.parse.util.extract_test_sentences(sent)
testingsent = sent[25]
sent = testingsent[0]
"""FAQ. 递归下降分析 增量式 earley算法
通过保存增量解析步骤的结果和确保每一个解析函数在同一个输入位置只被调用一次，就可以把任意解析表达文法转化成一个Packrat Parser，
可以实现线性的时间复杂度解析，其代价是足够大量的空间占用。
形式语言->编译原理 https://zh.wikipedia.org/zh-cn/解析表达文法
人工智能NLP语法解析 https://www.evget.com/serializedetail/479
计算机科学 采用预测策略的Earley算法 http://www.jsjkx.com/CN/Y2010/V37/I1/229
"""
parser1 = nltk.parse.BottomUpChartParser(gram1)  # 自底向上解析
parser1 = nltk.parse.BottomUpLeftCornerChartParser(gram1)  # 自底向上 LL分析
parser1 = nltk.parse.LeftCornerChartParser(gram1)  # 自底向上 过滤器的左角语法解析？？
parser1 = nltk.parse.IncrementalBottomUpChartParser(gram1)  # 增量式自底向上
parser1 = nltk.parse.IncrementalBottomUpLeftCornerChartParser(gram1)  # 增量式自底向上 LL分析
parser1 = nltk.parse.IncrementalBottomUpLeftCornerChartParser(gram1)  # 增量式自底向上 LL分析
parser1 = nltk.parse.IncrementalLeftCornerChartParser(gram1)  # 使用了自底向上过滤器的增量式左角语法解析
parser1 = nltk.parse.TopDownChartParser(gram1)  # 自顶向下解析
parser1 = nltk.parse.IncrementalTopDownChartParser(gram1)  # 增量式自顶向下解析
parser1 = nltk.parse.EarleyChartParser(gram1)  # Earley算法
chart1 = parser1.chart_parse(sent)
# print((chart1.num_edges()))
# print((len(list(chart1.parses(gram1.start())))))

tokens = "Jack told Bob to bring my cookie".split()
grammar = toy_pcfg2
print(grammar)

# nltk.parse.earleychart.demo(print_times=False, trace=1, sent='I saw a dog', numparses=2)  # 报错
nltk.parse.chart.demo(2, print_times=False, trace=1, sent='I saw a dog', numparses=1)
