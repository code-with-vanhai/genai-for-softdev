import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import openai
import requests
import json
from io import BytesIO
from config_manager import load_config
from image_manager import save_image_data
from datetime import datetime

# Load configuration
config = load_config()
api_key = config["api"]["key"]
api_url = config["api"]["base_url"]
model = config["settings"]["model"]
n_images = config["settings"]["n"]
image_size = config["settings"]["size"]

# Initialize OpenAI API Key
openai.api_key = api_key

class DalleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DALL-E 3 Image Generator")
        self.root.geometry("600x700")

        # Title
        self.label_title = tk.Label(root, text="DALL-E 3 Image Generator", font=("Arial", 16))
        self.label_title.pack(pady=10)

        # Prompt Input
        self.label_prompt = tk.Label(root, text="Enter your prompt:")
        self.label_prompt.pack()
        self.entry_prompt = tk.Entry(root, width=50)
        self.entry_prompt.pack(pady=5)

        # Generate Button
        self.btn_generate = tk.Button(root, text="Generate Image", command=self.generate_image)
        self.btn_generate.pack(pady=10)

        # Image Display Area
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Save Button (Initially Disabled)
        self.btn_save = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.btn_save.pack(pady=10)

        self.generated_image = None  # Store generated image
        self.image_url = None  # Store image URL

    def generate_image(self):
        prompt = self.entry_prompt.get().strip()
        if not prompt:
            messagebox.showerror("Error", "Please enter a prompt.")
            return

        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            payload = {
                "model": model,
                "prompt": prompt,
                "n": n_images,
                "size": image_size
            }

            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code != 200:
                messagebox.showerror("Error", f"Failed to generate image: {response.text}")
                return

            response_json = response.json()
            self.image_url = response_json["data"][0]["url"]

            image_response = requests.get(self.image_url)
            self.generated_image = Image.open(BytesIO(image_response.content))

            # Display Image in GUI
            self.display_image()

            # Enable Save Button
            self.btn_save.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_image(self):
        if self.generated_image:
            img_resized = self.generated_image.resize((256, 256))
            img_tk = ImageTk.PhotoImage(img_resized)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep reference

    def save_image(self):
        if not self.generated_image or not self.image_url:
            return

        user_name = simpledialog.askstring("User Info", "Enter your name:")
        if not user_name:
            messagebox.showerror("Error", "User name is required to save the image.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
        )

        if file_path:
            self.generated_image.save(file_path)

            # Save Metadata with User Info
            image_metadata = {
                "prompt": self.entry_prompt.get().strip(),
                "user": user_name,
                "file_path": file_path,
                "image_url": self.image_url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save_image_data(image_metadata)

            messagebox.showinfo("Success", f"Image saved successfully at {file_path}")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = DalleApp(root)
    root.mainloop()
