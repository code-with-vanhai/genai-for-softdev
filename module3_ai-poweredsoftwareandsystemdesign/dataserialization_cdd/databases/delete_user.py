from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to delete a user by user_id
def delete_user(user_id: int):
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"User ID {user_id} deleted successfully.")
            return True
        else:
            print(f"User with ID {user_id} not found.")
            return False
    except Exception as e:
        session.rollback()
        print("Error deleting user:", e)
        return False
    finally:
        session.close()

# Example Usage
delete_user(1)

