#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

url = 'http://list.jd.com/list.html?cat=9987%2C653%2C655&page=2'
# url = 'http://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_8557&go=0&JL=3_%E5%93%81%E7%89%8C_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89'
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")
items = soup.select('li.gl-item')
# print len(items)
for item in items:
    # print the item in a standard format
    # print item.prettify()

    # find the jd-id of the phone
    sku = item.find('div')['data-sku']
    print sku,

    # get the phone price 
    price_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(sku)
    price = requests.get(price_url).json()[0]['p']
    print price,

    # find and get the url of the phone 
    nameinfo = item.find('div', class_="p-name").find('a')
    # name = nameinfo['title']
    item_url = 'http:' + nameinfo['href']
    print item_url,

    # find and get the phone name via re module
    temp_em = item.find_all('em')
    # print type(temp_em[1])
    pattern = re.compile("em>(.*?)</em>")
    result = pattern.findall(str(temp_em[1].encode('utf-8')))
    name = result[0]
    print name,

    # get the NO. of the comment
    commit = item.find('div', class_="p-commit").find('a')
    if commit:
        print commit.get_text()
