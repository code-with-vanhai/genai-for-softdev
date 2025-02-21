from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from ecommerce_crud import engine, OrderItem, Product

Session = sessionmaker(bind=engine)
session = Session()

def get_total_quantity_sold():
    """
    Retrieve the total quantity of each product sold.
    :return: List of tuples (product_name, total_quantity_sold)
    """
    product_sales = (
        session.query(Product.name, func.sum(OrderItem.quantity))
        .join(OrderItem, Product.id == OrderItem.product_id)
        .group_by(Product.id)
        .all()
    )
    return product_sales

# Example usage
if __name__ == "__main__":
    sales = get_total_quantity_sold()
    for product_name, total_quantity in sales:
        print(f"Product: {product_name}, Total Quantity Sold: {total_quantity}")
