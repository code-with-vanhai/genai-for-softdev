from sqlalchemy.orm import sessionmaker
from dbsetup import engine, User  # Import User model and engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to update user email
def update_user_email(user_id: int, new_email: str):
    try:
        # Find the user by ID
        user = session.query(User).filter_by(user_id=user_id).first()

        if user:
            # Update email
            user.email = new_email
            session.commit()
            print(f"User ID {user_id}'s email updated to {new_email}.")
            return True
        else:
            print(f"User with ID {user_id} not found.")
            return False
    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print("Error updating user email:", e)
        return False
    finally:
        session.close()  # Close the session

# Example Usage
update_user_email(1, "johndoe@example.com")  # Update user ID 1
