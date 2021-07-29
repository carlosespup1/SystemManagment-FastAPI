from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:root@localhost:3306/store')

meta = MetaData()

conn = engine.connect()

