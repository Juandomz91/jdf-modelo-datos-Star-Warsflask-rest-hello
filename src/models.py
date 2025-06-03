from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
  
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship("Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Planet(db.Model):
   
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gravity: Mapped[str] = mapped_column(String(50))
    population: Mapped[int] = mapped_column()
    galaxy: Mapped[str] = mapped_column(String(100))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "population": self.population,
            "galaxy": self.galaxy
        }

class Person(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column()
    gender: Mapped[str] = mapped_column(String(10))
    planet_of_birth_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    
    planet_of_birth = relationship("Planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "planet_of_birth": self.planet_of_birth.name if self.planet_of_birth else None
        }

class Favorite(db.Model):
    __tablename__ = "favorite"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    person = relationship("Person")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet.serialize() if self.planet else None,
            "person": self.person.serialize() if self.person else None
        }
