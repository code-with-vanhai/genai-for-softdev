import json

CONFIG_FILE = "config.json"

# Load JSON Configuration
def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
        return {}

# Save JSON Configuration
def save_config(config_data):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)
