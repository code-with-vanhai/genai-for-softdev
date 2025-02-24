from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User, Product, Order, OrderItem
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
import time

def get_session():
    """Creates a new database session."""
    Session = sessionmaker(bind=engine)
    return Session()

# CRUD Operations for Products
def add_product(name: str, price: float):
    session = get_session()
    try:
        new_product = Product(name=name, price=price)
        session.add(new_product)
        session.commit()
        print(f"Product '{name}' added successfully.")
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print("Error adding product:", e)
        return False
    finally:
        session.close()


def get_all_products():
    session = get_session()
    try:
        products = session.query(Product).all()
        for product in products:
            print(f"Product ID={product.product_id}, Name={product.name}, Price={product.price}")
        return products
    except SQLAlchemyError as e:
        print("Error fetching products:", e)
        return []
    finally:
        session.close()


# CRUD Operations for Orders
def place_order(user_id: int, product_orders: list):
    """Places an order for a user with a list of (product_id, quantity)."""
    session = get_session()
    try:
        new_order = Order(user_id=user_id)
        session.add(new_order)
        session.commit()
        
        for product_id, quantity in product_orders:
            order_item = OrderItem(order_id=new_order.order_id, product_id=product_id, quantity=quantity)
            session.add(order_item)
        
        session.commit()
        print(f"Order {new_order.order_id} placed successfully for User {user_id}.")
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print("Error placing order:", e)
        return False
    finally:
        session.close()


def get_orders_by_user(user_id: int):
    """Fetches all orders placed by a specific user."""
    session = get_session()
    try:
        orders = session.query(Order).filter(Order.user_id == user_id).all()
        if not orders:
            print(f"No orders found for User ID {user_id}.")
            return []
        
        for order in orders:
            print(f"Order ID={order.order_id}, Date={order.order_date}")
        return orders
    except SQLAlchemyError as e:
        print("Error fetching user orders:", e)
        return []
    finally:
        session.close()


def get_total_quantity_sold():
    """Fetches total quantity sold for each product."""
    session = get_session()
    try:
        products = session.query(Product).all()
        for product in products:
            total_quantity = session.query(OrderItem).filter(OrderItem.product_id == product.product_id).with_entities(func.sum(OrderItem.quantity)).scalar() or 0
            print(f"Product: {product.name}, Total Quantity Sold: {total_quantity}")
        return True
    except SQLAlchemyError as e:
        print("Error fetching total quantity sold:", e)
        return False
    finally:
        session.close()

def get_total_quantity_sold_debug():
    """Fetch total quantity sold for each product with EXPLAIN for debugging."""
    session = get_session()
    try:
        products = session.query(Product).all()
        
        for product in products:
            # Generate the SQL query
            stmt = session.query(OrderItem).filter(OrderItem.product_id == product.product_id).with_entities(func.sum(OrderItem.quantity)).statement

            # Convert to a fully rendered SQL query (No bind parameters)
            compiled_stmt = stmt.compile(bind=session.bind, compile_kwargs={"literal_binds": True})

            # Print the actual SQL Query
            print("\n🔍 SQL Query for Product:", product.name)
            print(compiled_stmt)

            # Measure query execution time
            start_time = time.time()

            # Run EXPLAIN on the fully rendered SQL statement
            explain_stmt = text(f"EXPLAIN {compiled_stmt}")
            explain_result = session.execute(explain_stmt)

            execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds

            # Print EXPLAIN output
            print("🚀 EXPLAIN Output:")
            for row in explain_result:
                print(row)
            
            print(f"⏱ Query Execution Time: {execution_time:.2f} ms")

    except SQLAlchemyError as e:
        print("Error debugging total quantity sold:", e)
    finally:
        session.close()

def get_total_quantity_sold_debug_op():
    """Fetch total quantity sold for all products in a single query (optimized) with execution time measurement."""
    session = get_session()
    try:
        stmt = session.query(Product.name, func.sum(OrderItem.quantity))\
            .join(OrderItem, Product.product_id == OrderItem.product_id)\
            .group_by(Product.name).statement

        # Convert to a fully rendered SQL query (No bind parameters)
        compiled_stmt = stmt.compile(bind=session.bind, compile_kwargs={"literal_binds": True})

        # Measure query execution time
        start_time = time.time()

        explain_stmt = text(f"EXPLAIN {compiled_stmt}")
        explain_result = session.execute(explain_stmt)
        
        execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        print("\n🔍 Optimized SQL Query:")
        print(compiled_stmt)

        print("🚀 EXPLAIN Output:")
        for row in explain_result:
            print(row)
        
        print(f"⏱ Query Execution Time: {execution_time:.2f} ms")
    
    except SQLAlchemyError as e:
        print("Error optimizing query:", e)
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    add_product("Laptop", 1200.00)
    add_product("Mouse", 25.00)
    get_all_products()
    place_order(1, [(1, 2), (2, 5)])
    get_orders_by_user(1)
    get_total_quantity_sold()
    get_total_quantity_sold_debug()
    get_total_quantity_sold_debug_op()
