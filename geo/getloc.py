import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
import os


def get(address):
    # 根据链家网 URL 组织规律构建访问指定区域指定页面的 URL
    url = f"https://restapi.amap.com/v3/geocode/geo?address={address}&key=ec5c55297825f1225268f8595753ffca&city=北京"
    # 下载 HTML 数据并保存为文件
    res = requests.get(url, headers=headers)
    # with open("test.html", "w", encoding="utf-8") as f:
    #     f.write(res.text)
    return res.text


longitudes = []
latitudes = []
names = []
scores = []
prices = []
types = []
re_names = []
re_scores = []
re_prices = []
re_types = []

# 设定请求头
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36", }

filePath = r"C:\Users\M17\Desktop\网络\meituan\data"
namelist = os.listdir(filePath)
print(namelist)
regionlist = []
for i in namelist:
    with open("C://Users//M17//Desktop//网络//meituan//data//" + i, 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)
        for j in data:
            names.append(j['name'])
            scores.append(j['avgScore'])
            prices.append(j['avgPrice'])
            types.append(j['type'])
        print(len(data))
#    regionlist = np.concatenate((regionlist, data), axis=None)

for i in range(len(names)):
    res = get(names[i])
    json_data = json.loads(res)
    print(i)
    print(names[i])
    if(json_data.__contains__('geocodes')):
        if(type(json_data['geocodes'][0]['location']) == str):
            content = json_data['geocodes'][0]['location']
            longitude = content.split(',')[0]
            latitude = content.split(',')[1]
            longitudes.append(longitude)
            latitudes.append(latitude)
            re_names.append(names[i])
            re_prices.append(prices[i])
            re_scores.append(scores[i])
            re_types.append(types[i])
            print(longitude, latitude)

price = [10, 10]
data = {'name': re_names, 'lng': longitudes, 'lat': latitudes, 'prices': re_prices, 'scores': re_scores, 'types': re_types}#, 'count': price}
df = pd.DataFrame(data)
# df.to_excel('C:\\Users\\M17\\Desktop\\geotest.xls')
df.to_json('C:\\Users\\M17\\Desktop\\test.json', orient='records', force_ascii=False)

print(df)
