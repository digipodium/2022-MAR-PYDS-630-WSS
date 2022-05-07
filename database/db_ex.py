from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base() # fixed code

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    phone = Column(String(15))
    address = Column(String(100))
    message = Column(String(100))
    created_on = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f'{self.name} => {self.phone}'

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    price = Column(Integer)
    brand = Column(String(25))
    created_on = Column(DateTime, default=datetime.now)

    def __str__(self):
        return self.name

    
if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sqlite', echo=True)
    Base.metadata.create_all(engine)