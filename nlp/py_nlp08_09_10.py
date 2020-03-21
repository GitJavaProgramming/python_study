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
