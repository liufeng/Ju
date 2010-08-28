#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web.contrib.template import render_mako
from web import form

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

vemail = form.regexp(r".*@.*", "must be a valid email address")
comment_form = form.Form(
    form.Textbox('username', description="Username"),
    form.Textbox('email', vemail, description="Email"),
    form.Textbox('content', description="Content"),
    form.Button('submit', type='submit', description="Submit"),
    validators = [
        form.Validator("Email must be offered", lambda i: i.email != None)
        ]
    )

class product:
    def GET(self,id):
        myvar = dict(id=id)
        item = db.select('item', myvar, where="id=$id")
        return render.product(item=item[0], comment_form=comment_form)
    
    def POST(self):
        f = comment_form()
        return None

if __name__ == "__main__":
    app.run()
