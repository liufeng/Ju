#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import sqlite3

db = web.database(dbn='sqlite', db='test.db')

urls = (
    '/', 'index',
    '/data', 'data',
)

render = web.template.render('templates/')

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index()

class data:
    def GET(sefl):
        items = db.select('item', order='price DESC', limit=20)
        return render.data(items)

if __name__ == "__main__":
    app.run()
