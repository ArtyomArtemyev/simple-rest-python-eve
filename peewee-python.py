from peewee import *
import peewee as pw
from datetime import date

db = pw.PostgresqlDatabase(
    'people',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='postgres',  # Ditto.
    host='localhost',
    port='32770')
connection = db.connect()

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'

if __name__ == '__main__':
    Person.create_table()
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
    uncle_bob.save()