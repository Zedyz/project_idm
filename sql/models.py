from sqlalchemy import Column, String, DECIMAL, TIMESTAMP, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define your database models
Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    user_id = Column(String(255), primary_key=True)

class Category(Base):
    __tablename__ = 'Categories'
    category_id = Column(String(255), primary_key=True)
    category_code = Column(String(255), default=None)

class Product(Base):
    __tablename__ = 'Products'
    product_id = Column(String(255), primary_key=True)
    category_id = Column(String(255), ForeignKey('Categories.category_id'))
    brand = Column(String(255), default=None)
    price = Column(DECIMAL(10, 2))
    category = relationship("Category")

class Event(Base):
    __tablename__ = 'Events'
    event_id = Column(BigInteger, primary_key=True, autoincrement=True)
    event_time = Column(TIMESTAMP)
    event_type = Column(String(50))
    product_id = Column(String(255), ForeignKey('Products.product_id'))
    user_id = Column(String(255), ForeignKey('Users.user_id'))
    user_session = Column(String(255))
    product = relationship("Product")
    user = relationship("User")