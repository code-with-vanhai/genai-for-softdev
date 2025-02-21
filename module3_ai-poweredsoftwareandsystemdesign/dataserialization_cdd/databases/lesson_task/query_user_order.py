from sqlalchemy.orm import sessionmaker
from ecommerce_crud import engine, User, Order

Session = sessionmaker(bind=engine)
session = Session()

def get_orders_by_user(user_id):
    """
    Retrieve all orders placed by a specific user.
    :param user_id: ID of the user
    :return: List of orders placed by the user
    """
    orders = session.query(Order).filter(Order.user_id == user_id).all()
    return orders

# Example usage
if __name__ == "__main__":
    user_id = 1  # Replace with a valid user ID
    user_orders = get_orders_by_user(user_id)
    for order in user_orders:
        print(f"Order ID: {order.id}, User ID: {order.user_id}")
