# -*- coding: UTF-8 -*-
from Tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw() # we don't want a full GUI, so keep the root window from appearing
root.focus_force()
ydkfilename = askopenfilename(parent=root,filetypes=[('牌組', '.ydk')],
                                        title=u'選擇牌組開啟',initialdir="./deck") # show an "Open" dialog box and return the path to the selected file
#cdbfilename = askopenfilename(parent=root,filetypes=[('牌組資料庫', '.cdb')],
#                                        title=u'選擇牌組資料庫開啟') # show an "Open" dialog box and return the path to the selected file

ydkFile = open(ydkfilename,'r');
deckText = ydkFile.read()
ydkFile.close()

main = deckText.split('!')[0].split('#')[2]
extra = deckText.split('!')[0].split('#')[3]                
side = deckText.split('!')[1]

import re
mainCardList = sorted(re.findall(r'(\d+)', main))
extraCardList = sorted(re.findall(r'(\d+)', extra))
sideCardList = sorted(re.findall(r'(\d+)', side))

import codecs
f = codecs.open('{0}.md'.format(ydkfilename.split('/')[-1][:-4]),'w',encoding='utf8')

import sqlite3
conn = sqlite3.connect('cards.cdb')
c = conn.cursor()

if len(mainCardList) > 0:
    f.write(u'''# 主要牌組
|卡名|卡圖  |數量  |ID  |卡片效果|
| - | - | - | - | - |
''')
    
    lastCard = '';
    counter = 1;

    for card in mainCardList:
        if(card == lastCard):
            counter = counter + 1
        else:
            if(lastCard != ''):
                c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
                (name,desc) = c.fetchone()
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))

if len(extraCardList) > 0:
    f.write(u'''# 額外牌組
|卡名|卡圖  |數量  |ID  |卡片效果|
| - | - | - | - | - |
''')
    
    lastCard = '';
    counter = 1;

    for card in extraCardList:
        if(card == lastCard):
            counter = counter + 1
        else:
            if(lastCard != ''):
                c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
                (name,desc) = c.fetchone()
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))

if len(sideCardList) > 0:
    f.write(u'''# 備用牌組
|卡名|卡圖  |數量  |ID  |卡片效果|
| - | - | - | - | - |
''')
    
    lastCard = '';
    counter = 1;

    for card in sideCardList:
        if(card == lastCard):
            counter = counter + 1
        else:
            if(lastCard != ''):
                c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
                (name,desc) = c.fetchone()
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"./pics/{0}.jpg".format(lastCard),desc.replace('\r\n','<br/>')))

c.close()
f.close()
root.destroy()
