import pickle

# Step 1: Define a custom class
class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def introduce(self):
        return f"My name is {self.name}, I'm {self.age} years old, and I enjoy {', '.join(self.hobbies)}."

# Step 2: Create multiple Person objects
person1 = Person("Alice", 30, ["reading", "cycling", "coding"])
person2 = Person("Bob", 25, ["gaming", "hiking"])
person3 = Person("Charlie", 35, ["photography", "traveling"])

# Pickle multiple objects
with open("people.pkl", "wb") as f:
    pickle.dump([person1, person2, person3], f)

print("✅ Multiple person objects saved!")

# Load the pickled list
with open("people.pkl", "rb") as f:
    people_list = pickle.load(f)

# Print all unpickled objects
for person in people_list:
    print(person.introduce())
