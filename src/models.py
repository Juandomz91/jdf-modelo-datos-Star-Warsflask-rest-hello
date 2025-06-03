from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


class Favorites(db.model):



class Planets(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    gravity: Mapped[int] = mapped_column
    population: Mapped[int] = mapped_column
    galaxy: Mapped[str] = mapped_column


class Person(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[int] = mapped_column
    gender: Mapped[str] = mapped_column
    planet_of_birth[str] = mapped_column(ForeignKey)





    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
