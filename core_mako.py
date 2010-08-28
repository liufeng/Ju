#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web.contrib.template import render_mako
import os

db = web.database(dbn='sqlite', db='test.db')

urls = (
    '/', 'index',
    '/product/all', 'product_all',
    '/product/(\d+)', 'product',
)

# render = web.template.render('templates/')
render = render_mako(
    directories = ['templates_mako'],
    input_encoding = 'utf-8',
    output_encoding = 'utf-8',
    )

# app = web.application(urls, globals())
app = web.application(urls, globals(), autoreload=True)

class index:
    def GET(self):
        return render.index()

class product_all:
    def GET(sefl):
        items = db.select('item', order='people_num DESC', limit=20)
        return render.product_all(items=items)

class product:
    def GET(self,id):
        return "Single product, id=%s" % id

if __name__ == "__main__":
    app.run()
