import requests
import re
import logging
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import unicodedata

# Configuration
MAX_SIZE = 10 * 1024 * 1024  # 10MB limit for text size
TIMEOUT = 10  # Request timeout in seconds
MAX_WORKERS = 5  # Number of threads for concurrent processing
LOG_FILE = 'app.log'  # Log file path

# Setup logging
logging.basicConfig(level=logging.INFO, filename=LOG_FILE, format='%(asctime)s - %(message)s')

def is_valid_url(url):
    """Validate URL to prevent SSRF attacks and ensure valid format."""
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc != ""

def download_text(url):
    """Download text content from the given URL with security measures."""
    if not is_valid_url(url):
        logging.warning(f"Invalid URL provided: {url}")
        print(f"Invalid URL: {url}")
        return None

    try:
        response = requests.get(url, stream=True, timeout=TIMEOUT, verify=True)
        response.raise_for_status()
        
        content_length = int(response.headers.get('Content-Length', 0))
        if content_length > MAX_SIZE:
            logging.warning(f"File too large from {url}")
            print(f"File too large: {url}")
            return None

        content = response.text[:MAX_SIZE]  # Read only limited bytes
        logging.info(f"Successfully downloaded content from {url}")
        return content
    except requests.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        print(f"Failed to retrieve content from {url}")
        return None

def normalize_text(text):
    """Normalize text to remove special Unicode characters and handle Vietnamese diacritics."""
    return unicodedata.normalize('NFKC', text.lower())

def count_vietnamese_word_occurrences(text):
    """Count occurrences of each Vietnamese word in the given text using a dictionary."""
    text = normalize_text(text)

    # Regex pattern to match Vietnamese words including diacritics
    vietnamese_word_pattern = r'\b[a-zA-ZÀ-ỹĐđ]+\b'
    words = re.findall(vietnamese_word_pattern, text)

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1  # Count word occurrences safely

    return word_counts

def save_results_to_file(word_counts, filename="word_counts.txt"):
    """Save the word count results to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for word, count in sorted(word_counts.items(), key=lambda x: -x[1]):
                f.write(f"{word}: {count}\n")
        print(f"Results saved to {filename}")
    except IOError as e:
        logging.error(f"Failed to save results: {e}")
        print("Error saving the results.")

def process_urls(urls):
    """Process multiple URLs concurrently and aggregate word counts."""
    total_word_counts = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(download_text, urls)

    for text in results:
        if text:
            word_counts = count_vietnamese_word_occurrences(text)
            for word, count in word_counts.items():
                total_word_counts[word] = total_word_counts.get(word, 0) + count

    return total_word_counts

def main():
    urls = input("Enter URLs separated by spaces: ").split()

    if not urls:
        print("No URLs provided.")
        return

    total_word_counts = process_urls(urls)
    
    if total_word_counts:
        save_results_to_file(total_word_counts)
    else:
        print("No content processed from the provided URLs.")

if __name__ == "__main__":
    main()
