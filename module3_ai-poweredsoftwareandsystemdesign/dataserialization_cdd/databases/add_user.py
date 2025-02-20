from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User
import re  # For email validation

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a user securely
def add_user(name: str, email: str):
    try:
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return False

        # Check if email already exists to prevent duplicates
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            print("Error: Email already exists.")
            return False

        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User '{name}' added successfully with ID {new_user.user_id}.")
        return True
    except Exception as e:
        session.rollback()
        print("Error adding user:", e)
        return False
    finally:
        session.close()

# Example usage
add_user("John Doe", "john@example.com")
