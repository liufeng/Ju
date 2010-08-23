#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def add_item(title, price, area, people_num):
    conn = sqlite3.connect('test.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute('INSERT INTO item (title, price, area, people_num) VALUES (?, ?, ?, ?)',\
                  (title, price, area, people_num))
    conn.commit()
    c.close()

if __name__ == '__main__':
    add_item('可乐', 3.5, '济南', 300)
    add_item('雪碧', 2.5, '济南', 30)
    add_item('美年达', 2.0, '济南', 50)
