import webbrowser
import subprocess
import os
import sys

def open_application(app_name):
    """Open an application from the APP_PATHS."""
    app_name = app_name.lower()
    for key, path in open_application.apps.items():
        if key in app_name:
            try:
                subprocess.Popen(path)
                return f"Opening {key}, Sir."
            except Exception as e:
                return f"Sorry Sir, I could not open {key}: {e}"
    return "I could not locate that application, Sir."
def open_website(site_name):
    """Open a website from the SITE_MAP."""
    site_name = site_name.lower()
    for key, url in open_website.SITE_MAP.items():
        if key in site_name:
            webbrowser.open(url)
            return f"Opening {key}, Sir."
    return "Sorry Sir, I could not find that website in my map."

open_website.SITE_MAP = {
    # Original Sites
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.com",
    "google": "https://www.google.com",

    # Social Media
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",

    # Shopping & Affiliate
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "meesho": "https://www.meesho.com",
    "amazon associates": "https://affiliate-program.amazon.in",
    "iphone": "https://www.apple.com",

    # Entertainment & Streaming
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",

    # Developer & Education
    "github": "https://www.github.com",

    # Communication & Tools
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com"
}

open_application.apps = {
    "calculator": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
    "spotify": "SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify",
    "camera": "Microsoft.WindowsCamera_8wekyb3d8bbwe!App",
    "whatsapp" : "5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
    "github desktop" : "com.squirrel.GitHubDesktop.GitHubDesktop",
    "telegram" : "Telegram.TelegramDesktop",
    "notepad": "notepad.exe",
    "google chrome" :  "Chrome",
    "Canva" : "com.canva.CanvaDesktop",
    "Brave" :  "Brave"
    }
