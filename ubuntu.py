
import requests
import os
from urllib.parse import urlparse
import hashlib

def sanitize_filename(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  
        # Generate unique filename if URL has no file part
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
    return filename

def is_duplicate(filepath, content):
    """Check if file with same content already exists."""
    if not os.path.exists(filepath):
        return False
    with open(filepath, "rb") as f:
        existing_content = f.read()
    return existing_content == content

def fetch_image(url):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
        response.raise_for_status()
        
        # Only allow image content types
        if "image" not in response.headers.get("Content-Type", ""):
            print(f"✗ Skipped (not an image): {url}")
            return

        filename = sanitize_filename(url)
        filepath = os.path.join("Fetched_Images", filename)
        
        # Prevent duplicates
        if is_duplicate(filepath, response.content):
            print(f"✗ Duplicate skipped: {filename}")
            return
        
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Create directory
    os.makedirs("Fetched_Images", exist_ok=True)
    
    # Accept multiple URLs separated by commas
    urls = input("Please enter one or more image URLs (comma separated): ")
    url_list = [u.strip() for u in urls.split(",") if u.strip()]
    
    for url in url_list:
        fetch_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

