# -*- coding: UTF-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
headers = {'Authorization': "Client-ID {ClientID}"}
url = "https://api.imgur.com/3/image"

import sqlite3
conn = sqlite3.connect('cards.cdb')
c = conn.cursor()

cardlist = ['8384771','40318957','86157908','92767273',
            '47075569','53025096','42002073','69211541',
            '73511233','41209827','66768175']

cardlist2 = ['45206713','19580308','74583607','46796664',
             '72291412','987311','8463720','73360025',
             '82956492','11609969']

import codecs
with codecs.open('card_desc_pics.md','w',encoding='utf8') as f:
    f.write(u'''# 冠亞軍賽 Last Encho
## 游矢
|卡名|卡圖  |效果說明  |ID  |
| - | - | - | - |
''')    
    for card in cardlist:
        c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(card))
        (name,desc) = c.fetchone()
        payload = open('./pics/{0}.jpg'.format(card),'rb')
        response = requests.request("POST", url, files={'image':(None, payload),'album':(None, '{ablumDeleteHash}')},headers=headers)
        f.write(u'''|{0}|![]({3})|{1}|{2}|\r\n'''.format(name,desc.replace('\r\n','<br/>'),card,response.json()[u'data'][u'link']))
    
    f.write(u'''
## 零兒
|卡名|卡圖  |效果說明  |ID  |
| - | - | - | - |
''')
    for card in cardlist2:
        c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(card))
        (name,desc) = c.fetchone()
        payload = open('./pics/{0}.jpg'.format(card),'rb')
        response = requests.request("POST", url, files={'image':(None, payload),'album':(None, '{ablumDeleteHash}')},headers=headers)
        f.write(u'''|{0}|![]({3})|{1}|{2}|\r\n'''.format(name,desc.replace('\r\n','<br/>'),card,response.json()[u'data'][u'link']))
    f.close()

c.close
