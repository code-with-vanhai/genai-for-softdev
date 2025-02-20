from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to delete a user by user_id
def delete_user(user_id: int):
    try:
        # Find the user by ID
        user = session.query(User).filter_by(user_id=user_id).first()

        if user:
            session.delete(user)  # Delete the user
            session.commit()  # Commit the transaction
            print(f"User ID {user_id} deleted successfully.")
            return True
        else:
            print(f"User with ID {user_id} not found.")
            return False
    except Exception as e:
        session.rollback()  # Rollback changes if an error occurs
        print("Error deleting user:", e)
        return False
    finally:
        session.close()  # Close the session

# Example Usage
delete_user(1)  # Delete user with ID 1
