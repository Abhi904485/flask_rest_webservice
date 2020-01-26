from sqlalchemy import Column, INTEGER, String, CheckConstraint

from blog import db, ma


class User(db.Model):
    __tablename__ = "User"
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(50), nullable=False, )
    age = Column(INTEGER, CheckConstraint('age>0'), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name=None, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name} , age = {self.age} , email = {self.email})"


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


db.create_all()
