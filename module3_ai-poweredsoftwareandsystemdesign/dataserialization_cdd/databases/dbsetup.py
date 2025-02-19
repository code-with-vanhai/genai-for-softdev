from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Database connection
DATABASE_URL = "sqlite:///sqllite_sample.db"  # SQLite file-based database
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Users Table
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationship: One user can place multiple orders
    orders = relationship("Order", back_populates="user")

# Products Table
class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # Relationship: A product can be part of multiple order items
    order_items = relationship("OrderItem", back_populates="product")

# Orders Table
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    # Relationship: An order belongs to a user
    user = relationship("User", back_populates="orders")

    # Relationship: An order can contain multiple order items
    order_items = relationship("OrderItem", back_populates="order")

# Order_Items Table (Many-to-Many between Orders and Products)
class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Relationships
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

# Create the database tables
Base.metadata.create_all(engine)
print("Database and tables created successfully.")
