import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Function to set up and scrape TikTok user data
def fetch_tiktok_user_info(username):
    # Set up Selenium WebDriver (headless mode for running without GUI)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open TikTok user's page
    driver.get(f"https://www.tiktok.com/@{username}")

    # Allow time for page to load
    time.sleep(3)

    # Get page source
    page_source = driver.page_source

    # Parse with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Example: Extract user data (You may need to adjust the classes/ids based on actual structure)
    user_data = {}
    try:
        user_data['username'] = username
        user_data['avatar_url'] = soup.find('img', {'class': 'avatar'})['src']
        user_data['followers'] = soup.find('strong', {'title': 'Followers'}).text.strip()
        user_data['following'] = soup.find('strong', {'title': 'Following'}).text.strip()
        user_data['likes'] = soup.find('strong', {'title': 'Likes'}).text.strip()
        user_data['videos'] = soup.find('strong', {'title': 'Videos'}).text.strip()
        user_data['nickname'] = soup.find('h1', {'class': 'username'}).text.strip()
    except Exception as e:
        st.error(f"Error extracting data: {e}")
        user_data = None

    driver.quit()  # Close the browser

    return user_data

# Streamlit UI
st.title("TikTok User Info Fetcher")

# Input field for TikTok username
username = st.text_input("Enter TikTok Username:", "")

if username:
    st.write(f"Fetching data for: {username}")

    # Fetch the user info
    user_info = fetch_tiktok_user_info(username)

    if user_info:
        # Display user info
        st.image(user_info.get('avatar_url', ''), width=150)
        st.write(f"**Username:** {user_info.get('username')}")
        st.write(f"**Nickname:** {user_info.get('nickname')}")
        st.write(f"**Followers:** {user_info.get('followers')}")
        st.write(f"**Following:** {user_info.get('following')}")
        st.write(f"**Likes:** {user_info.get('likes')}")
        st.write(f"**Videos:** {user_info.get('videos')}")
    else:
        st.warning("User data not found.")
