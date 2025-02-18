Here’s a **detailed `README.md` file** with **step-by-step instructions** to help a **newbie** use this DALL-E 3 Image Generator project.

---

## **README.md**

# 🎨 DALL·E 3 Image Generator - Python GUI App  

This is a simple **Python-based GUI application** that allows users to **generate AI images** using OpenAI's **DALL·E 3 API**.  
Users can **enter a text prompt**, generate an image, **view it in the GUI**, and **save it with user details**.

---

## **📌 Features**
✅ **Graphical User Interface (GUI)** with an easy-to-use interface.  
✅ **Uses OpenAI's DALL·E 3 API** to generate images based on text prompts.  
✅ **Displays the generated image** in the app.  
✅ **Allows users to save the image** with their name and metadata.  
✅ **Stores metadata (prompt, user, timestamp, and file path) in a file for later use.**  

---

## **🛠 Prerequisites**
Before running this project, ensure you have:
- **Python 3.7+** installed on your system.
- A valid **OpenAI API key** to access the DALL·E 3 model.

---

## **📥 Installation**
### **1️⃣ Clone the Repository**
Download the project from GitHub or create a new folder and clone it:
```bash
git clone https://github.com/code-with-vanhai/genai-for-softdev.git
cd /genai-for-softdev/module3_ai-poweredsoftwareandsystemdesign/dataserialization_cdd/pickle/dalle3_gen_img_app
```

### **2️⃣ Install Required Packages**
Install the required Python packages:
```bash
pip install openai requests pillow
```

---

## **📝 Configuration Setup**
Before running the app, you need to **set up your API key**.

### **1️⃣ Open `config.json` File**
Edit the file `config.json` and **replace** `"your-dalle-api-key"` with your **actual OpenAI API Key**.

#### **Example: `config.json`**
```json
{
  "api": {
    "key": "your-dalle-api-key",
    "base_url": "https://api.openai.com/v1/images/generations"
  },
  "settings": {
    "model": "dall-e-3",
    "n": 1,
    "size": "1024x1024"
  },
  "logging": {
    "level": "info",
    "file": "app.log"
  }
}
```
🔹 **Note:** Your API key is required for generating images with OpenAI. You can get it from [OpenAI's website](https://platform.openai.com/).

---

## **🚀 How to Run the Application**
After setting up the API key, you can **run the app**.

### **1️⃣ Run the App**
In your terminal, run:
```bash
python app.py
```

### **2️⃣ Enter a Text Prompt**
- A **GUI window** will open.
- Enter a **text description** (e.g., `"A futuristic cityscape with neon lights"`).
- Click the **"Generate Image"** button.

### **3️⃣ View the Generated Image**
- The image **will appear in the app** once generated.

### **4️⃣ Save the Image**
- Click the **"Save Image"** button.
- Enter your **name** (this will be stored with the image metadata).
- Choose a **file location** to save the image.

---

## **💡 How It Works (For Beginners)**
1. The program **loads configuration** (`config.json`) to get API details.
2. When the user enters a **prompt**, the app **sends a request** to OpenAI’s API.
3. OpenAI **generates an image** based on the prompt and returns an image URL.
4. The app **downloads the image** and **displays it** in the GUI.
5. Users can **save the image**, along with:
   - **Prompt**
   - **User name**
   - **File location**
   - **Timestamp**
6. The image metadata is **saved using `pickle`** for later use.

---

## **📂 Project Structure**
```
dalle3-image-generator/
│── app.py                # Main GUI application
│── config.json           # API settings (edit this with your API key)
│── config_manager.py     # Handles loading/saving configuration
│── image_manager.py      # Handles saving/loading generated image metadata
│── generated_images.pkl  # (Automatically created) Stores image metadata
│── README.md             # Project documentation (this file)
```

---

## **❓ FAQ**
### **1️⃣ Where can I get an OpenAI API key?**
You can get an API key by signing up at [OpenAI’s API page](https://platform.openai.com/).

### **2️⃣ What if the API key doesn’t work?**
- Make sure you **copied the key correctly**.
- Ensure your **OpenAI account has enough credits**.
- If the issue persists, check OpenAI’s [API status](https://status.openai.com/).

### **3️⃣ How do I uninstall the project?**
To remove this project, simply delete the folder:
```bash
rm -rf dalle3-image-generator
```

### **4️⃣ Can I change the image size?**
Yes! Edit the `size` parameter in `config.json`:
```json
"size": "512x512"
```

---

## **📌 Future Enhancements**
✅ Allow users to **browse previously saved images**.  
✅ Let users **select different image sizes** from the GUI.  
✅ Improve **error handling and logging**.  

---

## **💬 Support**
If you run into any issues:
- Open an **issue** on GitHub.
- Ask for help in the **OpenAI developer community**.

Happy coding! 🚀🎨

---