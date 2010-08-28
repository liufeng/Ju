#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re

url = 'http://www.groupon.cn/html/product/JN/JN1962.html'
sock = urllib.urlopen(url)
htmlSource = sock.read()
sock.close()

htmlSource = htmlSource.decode('gb2312')

# item_url = re.compile(r'''(http://www.lashou.com/index.php\?id=.*?)" class="intfz"''', re.DOTALL).findall(htmlSource)[0]
title = re.compile(r' A</b> <b>(.*?)</b>', re.DOTALL).findall(htmlSource)[0]
price = re.compile(r'<DIV class=amount><img src="http://www.17tuanbao.com/images/rmb_1.gif" />&nbsp;<b>(.*?)</b>', re.DOTALL).findall(htmlSource)[0]

# We have a problem here. It seems the people_num in this site is
# dynamically loaded. Thus it seems hard to take out.

# people_num = re.compile(r'已经有(.*?)人购买', re.DOTALL).findall(htmlSource)[0]

pic_url = re.compile(r'''<IMG src="(.*?)"''', re.DOTALL).findall(htmlSource)[0]
description = re.compile(r'''<DIV class="article description">(.*?)<div class="groupon_voice" id="voice">''', re.DOTALL).findall(htmlSource)[0]

# print item_url
print title
print price
# print orig_price
# print discount
# print save
# print people_num
print pic_url
print description
