from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean 

db = SQLAlchemy()

class User(db.Model):
    
    id = Column(Integer, primary_key=True) 
    name = Column(String(120), unique=False, nullable=False) 
    last_name = Column(String(120), unique=False, nullable=False) 
    city = Column(String(120), unique=False, nullable=False) 
    email = Column(String(120), unique=True, nullable=False) 
    password = Column(String(250), nullable=False) 
    is_active = Column(Boolean(), nullable=False) 


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }