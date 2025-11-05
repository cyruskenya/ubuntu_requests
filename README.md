🌿 Ubuntu Image Fetcher

A mindful, community-driven Python tool for collecting images from the web responsibly.
The Ubuntu Image Fetcher encourages thoughtful use of the internet — fetching images safely, preventing duplicates, and promoting respect for shared digital spaces.

🧭 Overview

The Ubuntu Image Fetcher allows users to download one or more images directly from given URLs while ensuring:

✅ Safety – checks HTTP headers to confirm files are real images.

✅ Community care – prevents downloading duplicate or unsafe content.

✅ Convenience – accepts multiple URLs at once.

✅ Respectful connectivity – uses timeouts and error handling to avoid unnecessary network strain.

At the end of each session, it reminds users of Ubuntu’s guiding principle:

“Connection strengthened. Community enriched.”

🛠 Features
Feature	Description
🌐 Multiple URL Support	Enter several URLs at once, separated by commas.
🧩 Smart File Naming	Automatically handles duplicate filenames.
🔒 Safe Downloading	Verifies content type before saving any file.
♻️ Duplicate Detection	Uses SHA-256 hashing to prevent saving the same image twice.
⚙️ Robust Error Handling	Gracefully manages timeouts, network errors, and unexpected responses.
💻 Example Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (comma-separated): https://example.com/ubuntu-wallpaper.jpg, https://example.com/logo.png

Fetching from: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Fetching from: https://example.com/logo.png
⚠️ Skipped: Duplicate image detected.

Connection strengthened. Community enriched.

📦 Installation

Clone or download this repository:

git clone https://github.com/yourusername/ubuntu-image-fetcher.git
cd ubuntu-image-fetcher


Install dependencies:

pip install requests


Run the program:

python ubuntu_image_fetcher.py

⚠️ Responsible Use

Before downloading images:

🧠 Verify the source is safe and legal.

🌍 Respect copyright and usage rights.

⏳ Avoid excessive requests to the same server.

The Ubuntu spirit is about community and mindfulness — use this tool responsibly and respectfully.

🧪 Technical Details

Language: Python 3.8+

Libraries: requests, os, hashlib, urllib.parse

Storage: Images are saved in the Fetched_Images/ directory.

Duplicate Detection: Implemented via SHA-256 hashing.

🧡 Inspired by Ubuntu Philosophy

“I am because we are.”
The Ubuntu Image Fetcher is built on the belief that technology can strengthen connection and mutual respect in our shared digital ecosystem.

🤝 Contributing

Contributions are welcome!
If you have ideas to make the fetcher more secure, efficient, or educational, please open a pull request or start a discussion.
