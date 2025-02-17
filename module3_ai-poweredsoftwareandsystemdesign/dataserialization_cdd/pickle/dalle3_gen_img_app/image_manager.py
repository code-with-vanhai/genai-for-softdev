import pickle
from datetime import datetime

IMAGE_DATA_FILE = "generated_images.pkl"

# Save generated image data with user info
def save_image_data(image_data):
    try:
        with open(IMAGE_DATA_FILE, "ab") as file:  # Append mode to store multiple images
            pickle.dump(image_data, file)
        print("Image data saved successfully!")
    except Exception as e:
        print(f"Error saving image data: {e}")

# Load all saved images
def load_all_images():
    images = []
    try:
        with open(IMAGE_DATA_FILE, "rb") as file:
            while True:
                try:
                    images.append(pickle.load(file))
                except EOFError:
                    break
    except FileNotFoundError:
        print("No saved image data found.")
    return images
