"""
A Peewee Model for storing Journal Post's in a Database
Author: Zachary Collins
Date: August, 2018
"""

import datetime

from peewee import *

DB = SqliteDatabase('journal.db')


class Post(Model):
    title = TextField()
    date = DateTimeField(default=datetime.datetime.now)
    time_spent = IntegerField()
    details = TextField()
    remember = TextField()

    class Meta:
        database = DB
        order_by = ('-date',)


def initialize():
    DB.connect()
    DB.create_tables([Post], safe=True)
    DB.close()

