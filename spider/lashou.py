#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re

url = 'http://www.lashou.com/'
# url = 'http://open.client.lashou.com/list/goods/cityid/1591'
sock = urllib.urlopen(url)
htmlSource = sock.read()
sock.close()

# print htmlSource

item_url = re.compile(r'''(http://www.lashou.com/index.php\?id=.*?)" class="intfz"''', re.DOTALL).findall(htmlSource)[0]
title = re.compile(r'<h1><FONT color="#ff0000">济南</FONT>(.*?)</h1>', re.DOTALL).findall(htmlSource)[0]
price = re.compile(r'<div class="l price" style="text-align:center;font-size:30px;">\s+(.*?)\s+</div>', re.DOTALL).findall(htmlSource)[0]
orig_price = re.compile(r'<li>原价<br /><h4 title="(.*?)">', re.DOTALL).findall(htmlSource)[0]
discount = re.compile(r'<li>折扣<br /><h3>(.*?)折</h3></li>', re.DOTALL).findall(htmlSource)[0]
save = re.compile(r'<li class="red">节省<br /><h3>(.*?)</h3></li>', re.DOTALL).findall(htmlSource)[0]
people_num = re.compile(r'已经有(.*?)人购买', re.DOTALL).findall(htmlSource)[0]
pic_url = re.compile(r'''<div class="image">
						 <img src="(.*?)"
			  />''', re.DOTALL).findall(htmlSource)[0]
description = re.compile(r'''<h3>本单详情</h3>(.*?)<h3>大家点评：</h3>''', re.DOTALL).findall(htmlSource)[0]

print item_url
print title.decode('utf-8')
print price
print orig_price
print discount
print save
print people_num
print pic_url
print description
