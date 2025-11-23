# utils.py
import requests
import os

def download_media(media_url):
    """Download media from Twilio and save it locally."""
    response = requests.get(media_url, stream=True)
    if response.status_code == 200:
        filename = os.path.basename(media_url.split("?")[0])  # Extract filename without query params
        filepath = os.path.join('./uploads', filename)
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filepath
    else:
        raise Exception("Failed to download media")
