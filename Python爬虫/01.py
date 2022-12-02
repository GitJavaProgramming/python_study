import json

import pymongo
import requests

# 爬取boss直聘某个json信息存入mongodb和文件中
client = pymongo.MongoClient('localhost', 27017)  # mongodb作为数据库
mydb = client['mydb']
boss = mydb['boss']
cookie = 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1667869862,1668665827,1668767953,1669941608; lastCity=101240100; wd_guid=fee76e4c-ae42-4a7b-87f3-367ddd77fa29; historyState=state; _bl_uid=4kls35UUzn50w8jvdwb0ms7s6hs1; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend&r=&g=&s=3&friend_source=0; JSESSIONID=8B1B6448766735B8D1FB651FB3B1DC22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1669941775; wt2=Dn5DhDv42U94G75W-e4W76dOCOUXjPQ4EIFv_mgQ1LV-_tqaHCZYsLgSswbeLItkvaw7-NAtJqNpIXBqNoICUBg~~; wbg=0; __zp_stoken__=01ffeCGJEZTJvWw41YhlIVFkydw8AXi5ffyQYfG14dm0pVEp6R3ASVCAqTVAiUE8gQCNHNWdEa0IiSy9zcE1sI21PCz5QdChfYjsQfmFkEVVxRXcaekYDRyVkV2FHTG5KPDsTOw01LhhhOlpUf0VQJAtwBGQ%2FLEZXVEpQWAUrKgYCEgpuDTYpMHUAeyoFdVxDOERsGFp0fA%3D%3D; __c=1669941599; __a=28571064.1632302123.1668767950.1669941599.46.10.8.18'
headers = {
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'connection': 'keep-alive'
}


# 抓取github网站图标
def print_ico():
    r = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


# 抓取数据写入文件
def into_file(filename, json_data):
    f = open(filename, 'w')
    f.write(str(json_data))
    f.close()


def get_page(url, params={}):
    html = requests.get(url, data=params, headers=headers)
    json_data = json.loads(html.text)
    json_data.setdefault('req_name', '请求名')
    # 存入文件
    into_file('file.txt', json_data)
    # 插入mongodb
    boss.insert_one(json_data)  # 插入数据库
    print(json_data)


if __name__ == '__main__':
    try:
        url = 'https://www.zhipin.com/wapi/zpgeek/agreement/update/tip.json'
        get_page(url)
        print_ico()
    except ConnectionError:
        pass
