from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

user = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(120)),
    Column('email', String(255)),
    Column('password', String(255)),
)

meta.create_all(engine)