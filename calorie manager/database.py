import sqlite3
from flask import Flask,render_template,g,request


def connect_db():
    sql = sqlite3.connect('/C:/Users/SUMIT/Desktop/calorie manager/food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db