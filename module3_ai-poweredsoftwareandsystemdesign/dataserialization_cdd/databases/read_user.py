from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import the User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to read a user by email or ID
def get_user(identifier):
    try:
        if isinstance(identifier, int):  # If searching by user_id
            user = session.query(User).filter_by(user_id=identifier).first()
        else:  # If searching by email
            user = session.query(User).filter_by(email=identifier).first()

        if user:
            print(f"User Found: ID={user.user_id}, Name={user.name}, Email={user.email}")
            return user
        else:
            print("User not found.")
            return None
    except Exception as e:
        print("Error reading user:", e)
    finally:
        session.close()  # Close the session

# Function to read all users
def get_all_users():
    try:
        users = session.query(User).all()  # Retrieve all users

        if users:
            print("All Users:")
            for user in users:
                print(f"ID={user.user_id}, Name={user.name}, Email={user.email}")
            return users
        else:
            print("No users found.")
            return []
    except Exception as e:
        print("Error reading users:", e)
    finally:
        session.close()  # Close the session

# Example Usage
get_all_users()

# Example Usage
get_user("1john@example.com")  # Search by email
get_user(1)  # Search by user_id
