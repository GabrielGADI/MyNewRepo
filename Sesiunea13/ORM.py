# ORM- Object Relational Mapping

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# connect to DB
engine = create_engine("sqlite:///users.db")

# create tables
Base.metadata.create_all(engine)

# start session
Session = sessionmaker(bind=engine)
session = Session()

# add user
u = User(name="Andrei", age=20)
u2 = User(name="Eva", age=27)
# session.add(u)
# session.add(u2)
# session.commit()

# querry all users
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
print(50 * "*")

# update
user = session.query(User).filter_by(name="Andrei").first()
user.age = 20
user.name = "George"
session.commit()
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
