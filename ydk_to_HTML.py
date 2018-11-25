# -*- coding: UTF-8 -*-
import markdown
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def md2html(mdstr):
    exts = ['markdown.extensions.nl2br','markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="zh-tw">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <style>
    body{font-family:Helvetica,arial,sans-serif;font-size:14px;line-height:1.6;padding-top:10px;padding-bottom:10px;background-color:white;padding:30px}body>*:first-child{margin-top:0!important}body>*:last-child{margin-bottom:0!important}a{color:#4183C4}a.absent{color:#cc0000}a.anchor{display:block;padding-left:30px;margin-left:-30px;cursor:pointer;position:absolute;top:0;left:0;bottom:0}h1,h2,h3,h4,h5,h6{margin:20px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative}h1:hover a.anchor,h2:hover a.anchor,h3:hover a.anchor,h4:hover a.anchor,h5:hover a.anchor,h6:hover a.anchor{background:url("../../images/modules/styleguide/para.png") no-repeat 10px center;text-decoration:none}h1 tt,h1 code{font-size:inherit}h2 tt,h2 code{font-size:inherit}h3 tt,h3 code{font-size:inherit}h4 tt,h4 code{font-size:inherit}h5 tt,h5 code{font-size:inherit}h6 tt,h6 code{font-size:inherit}h1{font-size:28px;color:black}h2{font-size:24px;border-bottom:1px solid #cccccc;color:black}h3{font-size:18px}h4{font-size:16px}h5{font-size:14px}h6{color:#777777;font-size:14px}p,blockquote,ul,ol,dl,li,table,pre{margin:15px 0}hr{background:transparent url("../../images/modules/pulls/dirty-shade.png") repeat-x 0 0;border:0 none;color:#cccccc;height:4px;padding:0}body>h2:first-child{margin-top:0;padding-top:0}body>h1:first-child{margin-top:0;padding-top:0}body>h1:first-child+h2{margin-top:0;padding-top:0}body>h3:first-child,body>h4:first-child,body>h5:first-child,body>h6:first-child{margin-top:0;padding-top:0}a:first-child h1,a:first-child h2,a:first-child h3,a:first-child h4,a:first-child h5,a:first-child h6{margin-top:0;padding-top:0}h1 p,h2 p,h3 p,h4 p,h5 p,h6 p{margin-top:0}li p.first{display:inline-block}ul,ol{padding-left:30px}ul :first-child,ol :first-child{margin-top:0}ul :last-child,ol :last-child{margin-bottom:0}dl{padding:0}dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px}dl dt:first-child{padding:0}dl dt>:first-child{margin-top:0}dl dt>:last-child{margin-bottom:0}dl dd{margin:0 0 15px;padding:0 15px}dl dd>:first-child{margin-top:0}dl dd>:last-child{margin-bottom:0}blockquote{border-left:4px solid #dddddd;padding:0 15px;color:#777777}blockquote>:first-child{margin-top:0}blockquote>:last-child{margin-bottom:0}table{padding:0}table tr{border-top:1px solid #cccccc;background-color:white;margin:0;padding:0}table tr:nth-child(2n){background-color:#f8f8f8}table tr th{font-weight:bold;border:1px solid #cccccc;text-align:left;margin:0;padding:6px 13px}table tr td{border:1px solid #cccccc;text-align:left;margin:0;padding:6px 13px}table tr th :first-child,table tr td :first-child{margin-top:0}table tr th :last-child,table tr td :last-child{margin-bottom:0}img{max-width:100%}span.frame{display:block;overflow:hidden}span.frame>span{border:1px solid #dddddd;display:block;float:left;overflow:hidden;margin:13px 0 0;padding:7px;width:auto}span.frame span img{display:block;float:left}span.frame span span{clear:both;color:#333333;display:block;padding:5px 0 0}span.align-center{display:block;overflow:hidden;clear:both}span.align-center>span{display:block;overflow:hidden;margin:13px auto 0;text-align:center}span.align-center span img{margin:0 auto;text-align:center}span.align-right{display:block;overflow:hidden;clear:both}span.align-right>span{display:block;overflow:hidden;margin:13px 0 0;text-align:right}span.align-right span img{margin:0;text-align:right}span.float-left{display:block;margin-right:13px;overflow:hidden;float:left}span.float-left span{margin:13px 0 0}span.float-right{display:block;margin-left:13px;overflow:hidden;float:right}span.float-right>span{display:block;overflow:hidden;margin:13px auto 0;text-align:right}code,tt{margin:0 2px;padding:0 5px;white-space:nowrap;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px}pre code{margin:0;padding:0;white-space:pre;border:none;background:transparent}.highlight pre{background-color:#f8f8f8;border:1px solid #cccccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px}pre{background-color:#f8f8f8;border:1px solid #cccccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px}pre code,pre tt{background-color:transparent;border:none}
    </style>
    '''+'''
    <style>
    img{
        max-width: 200px;
    }
    </style>
    </head>
    <body>
    %s
    </body>
    </html>
    ''' % (markdown.markdown(mdstr,extensions=exts))
    return html

from Tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw() # we don't want a full GUI, so keep the root window from appearing
root.focus_force()
cdbfilename = askopenfilename(parent=root,filetypes=[('牌組資料庫', '.cdb')],
                                        title=u'選擇牌組資料庫開啟') # show an "Open" dialog box and return the path to the selected file
mainPath = '/'.join(cdbfilename.split('/')[:-1])
ydkfilename = askopenfilename(parent=root,filetypes=[('牌組', '.ydk')],
                                        title=u'選擇牌組開啟',initialdir=mainPath+"/deck") # show an "Open" dialog box and return the path to the selected file

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
conn = sqlite3.connect(cdbfilename)
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
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))

if len(extraCardList) > 0:
    f.write(u'''
# 額外牌組
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
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))

if len(sideCardList) > 0:
    f.write(u'''
# 備用牌組
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
                f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))
            lastCard = card
            counter = 1
    c.execute(''' SELECT `name`,`desc` FROM `texts` WHERE `id` = "{0}" '''.format(lastCard))
    (name,desc) = c.fetchone()
    f.write(u'''|{0}|![]({3})|{1}|{2}|{4}|\r\n'''.format(name,counter,lastCard,u"{1}/pics/{0}.jpg".format(lastCard,mainPath),desc.replace('\r\n','<br/>')))

c.close()
f.close()
root.destroy()

f = codecs.open('{0}.md'.format(ydkfilename.split('/')[-1][:-4]),'r',encoding='utf8')
md = f.read()
f.close()

print("Open")
of = codecs.open('{0}.html'.format(ydkfilename.split('/')[-1][:-4]),'w',encoding='utf8')
of.write(md2html(md))
of.close()

print("Done")
