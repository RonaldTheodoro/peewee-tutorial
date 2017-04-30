import os
import peewee

BASE_DIR = os.path.dirname(__file__)
database = peewee.SqliteDatabase(os.path.join(BASE_DIR, 'db.sqlite3'))


class Author(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database


class Book(peewee.Model):
    title = peewee.CharField()
    author = peewee.ForeignKeyField(Author)

    class Meta:
        database = database