from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import the User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to read a user by email or ID
def get_user(identifier):
    try:
        if isinstance(identifier, int):  # Search by user_id
            user = session.query(User).filter(User.user_id == identifier).first()
        elif isinstance(identifier, str):  # Search by email
            user = session.query(User).filter(User.email == identifier).first()
        else:
            print("Invalid identifier type.")
            return None

        if user:
            print(f"User Found: ID={user.user_id}, Name={user.name}, Email={user.email}")
            return user
        else:
            print("User not found.")
            return None
    except Exception as e:
        print("Error reading user:", e)
        return None
    finally:
        session.close()

# Example Usage
get_user("john@example.com")
get_user(1)


# Function to read all users
def get_all_users():
    try:
        users = session.query(User).all()
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
        return []
    finally:
        session.close()

# Example Usage
get_all_users()

