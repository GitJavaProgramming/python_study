import json

import requests
from bs4 import BeautifulSoup

# name attrs string
soup = BeautifulSoup('<p>hello</p>', 'lxml')
print(soup.p.string)

# 抓取体彩中心数据，然后解析其中部分数据存入文件
url = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1"
body = requests.get(url)
print(type(body.text))
json_data = json.loads(body.text)
result = dict(json_data)
print(type(result['value']['list']))  # list
lottery_draw = result['value']['list']
# lottery_draw.sort(reverse=True)
lottery_draw.reverse()
f = open('lottery', 'wb')
for r in lottery_draw:
    line = '{} {}'.format(r['lotteryDrawNum'], r['lotteryDrawResult'])
    f.write(line.encode())
    f.write('\n'.encode())
f.close()


def sort_lottery():
    f1 = open('lotteryDraw', 'r')
    lines = f1.readlines()
    lines.reverse()
    f1.close()
    f1 = open('lotteryDraw', 'w')
    f1.writelines(lines)
    f1.close()


sort_lottery()
