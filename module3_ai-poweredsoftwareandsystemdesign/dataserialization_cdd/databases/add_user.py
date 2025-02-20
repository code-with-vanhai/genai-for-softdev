from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import the User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a new user
def add_user(name: str, email: str):
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User '{name}' added successfully with ID {new_user.user_id}.")
    except Exception as e:
        session.rollback()  # Rollback if there is an error
        print("Error adding user:", e)
    finally:
        session.close()  # Always close the session

# Example Usage
add_user("John Doe", "john@example.com")
