from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import User model and engine
import re  # For email validation

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to update user email
def update_user_email(user_id: int, new_email: str):
    try:
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            print("Invalid email format.")
            return False

        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            # Ensure new email is not already in use
            if session.query(User).filter(User.email == new_email).first():
                print("Error: Email already exists.")
                return False

            user.email = new_email
            session.commit()
            print(f"User ID {user_id}'s email updated to {new_email}.")
            return True
        else:
            print(f"User with ID {user_id} not found.")
            return False
    except Exception as e:
        session.rollback()
        print("Error updating user email:", e)
        return False
    finally:
        session.close()

# Example Usage
update_user_email(1, "newemail@example.com")

