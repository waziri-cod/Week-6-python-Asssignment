# Week-6-python-Asssignment
# 🌍 Ubuntu Image Fetcher

**“I am because we are.” – Ubuntu Philosophy**

A Python tool for mindfully collecting and organizing images from the web. Inspired by the wisdom of Ubuntu, this program emphasizes **community, respect, sharing, and practicality**.

## ✨ Features

* 📥 **Fetch images from the web** using a provided URL
* 📂 **Organizes downloads** into a `Fetched_Images` directory
* ⚠️ **Graceful error handling** for failed connections or invalid URLs
* 📝 **Meaningful filenames** are extracted from the URL (or auto-generated)
* 🌱 **Extensible**: designed to grow with community-driven improvements

## 📖 Ubuntu Principles in Code

* **Community**: Connects you to the wider web by fetching shared images
* **Respect**: Handles errors without crashing, respecting unreliable networks
* **Sharing**: Stores images neatly for later appreciation or collaboration
* **Practicality**: A real, usable tool for everyday image fetching

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.7+** installed and the following package:

```bash
pip install requests
```

### Clone Repository

```bash
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests

### Run the Program

```bash
python ubuntu_fetcher.py

## 🖼️ Example

**Terminal Output:**

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.

**Result:**
An image named `ubuntu-wallpaper.jpg` will be saved in the `Fetched_Images` folder.

## ⚡ Challenge Extensions

* 🖇 **Multiple URLs**: Support for downloading several images at once
* 🔒 **Security Precautions**: Validate content type, limit file size
* 🛑 **Duplicate Prevention**: Skip or rename existing images
* 📑 **HTTP Headers Check**: Respect `Content-Type` and `Content-Length` before saving

## 🛡️ Precautions When Downloading

* ✅ Always validate **Content-Type** (e.g., `image/jpeg`, `image/png`)
* ✅ Beware of **malware** hidden in non-image files
* ✅ Avoid downloading from **untrusted sources**

## 💡 Ubuntu Wisdom

> *"A person is a person through other persons."*
> This project reflects Ubuntu’s spirit: every image fetched is a connection to someone’s shared work.
