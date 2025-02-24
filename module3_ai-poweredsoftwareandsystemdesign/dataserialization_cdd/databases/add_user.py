from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from dbsetup import engine, User
import re  # Add regex validation

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name: str, email: str):
    try:
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return False

        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User '{name}' added successfully.")
        return True
    except IntegrityError:
        session.rollback()
        print("Error: Duplicate entry. Email already exists.")
        return False
    except Exception as e:
        session.rollback()
        print("Error adding user:", e)
        return False
    finally:
        session.close()

