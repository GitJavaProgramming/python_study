"""信息检索(Information Retrieval)、信息检索系统"""
import nltk

"""语篇分析
宏观（超越句子）：语境、篇章模式和体裁等
微观：语法联结、词汇衔接和逻辑联系等。
参考：黄国文 《语篇分析的理论与实践》 《语篇分析概要》
"""
expr_read = nltk.sem.DrtExpression.fromstring
expr1 = expr_read('([x], [John(x), Went(x)]) + ([y], [Sam(y), eats(y)])')
print(expr1)
expr1.draw()
print(expr1.fol())

"""NLP系统的评估"""

"""总结
语言形式化
语：形声字，言（声旁）表意。
言：舌头，音。
语言是一类复合交流系统，某种具体语言是语言的个例。
形式指事物的样子和结构，区别于该物构成的材料（实质）
自然语言处理
自然语言（英語：Natural language）通常是指一种自然地随文化演化的语言。
文化：事物的变化，以文做言。
文=纹身=图形，一切皆文。化：两个人形，正立和倒立，表示变化。
"""
