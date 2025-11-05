import requests
import os
import hashlib
from urllib.parse import urlparse

def is_safe_content_type(content_type):
    """Check if the response content type looks like an image."""
    return content_type.startswith("image/")

def file_already_downloaded(file_hash, hash_list):
    """Check if an image with the same hash already exists."""
    return file_hash in hash_list

def hash_file_content(content):
    """Generate a SHA-256 hash of the downloaded content."""
    return hashlib.sha256(content).hexdigest()

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user (comma-separated)
    urls = input("Please enter one or more image URLs (comma-separated): ").split(",")
    urls = [url.strip() for url in urls if url.strip()]  # Clean whitespace and skip empties
    
    # Create output directory
    os.makedirs("Fetched_Images", exist_ok=True)

    # Track downloaded file hashes to prevent duplicates
    downloaded_hashes = set()

    for url in urls:
        print(f"\nFetching from: {url}")
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()  # Ensure response is OK (200)

            # Check content type before downloading
            content_type = response.headers.get("Content-Type", "")
            if not is_safe_content_type(content_type):
                print(f"✗ Skipped: Content type '{content_type}' is not an image.")
                continue

            # Read image bytes
            content = response.content

            # Generate a hash to detect duplicates
            file_hash = hash_file_content(content)
            if file_already_downloaded(file_hash, downloaded_hashes):
                print("⚠️ Skipped: Duplicate image detected.")
                continue
            downloaded_hashes.add(file_hash)

            # Extract filename or assign a safe default
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
            filepath = os.path.join("Fetched_Images", filename)

            # Avoid filename conflicts
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(filepath):
                filepath = os.path.join("Fetched_Images", f"{base}_{counter}{ext}")
                counter += 1

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.Timeout:
            print("✗ Connection timed out. Please try again later.")
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
