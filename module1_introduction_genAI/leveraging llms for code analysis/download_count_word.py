import requests
from collections import Counter
import re

def download_text(url):
    """Download text content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def count_word_occurrences(text):
    """Count occurrences of each word in the given text."""
    words = re.findall(r'\b\w+\b', text.lower())  # Convert to lowercase and extract words
    word_counts = Counter(words)
    return word_counts

def main():
    url = input("Enter the URL to download text from: ")
    text = download_text(url)
    if text:
        word_counts = count_word_occurrences(text)
        for word, count in word_counts.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
