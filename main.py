import requests
from bs4 import BeautifulSoup

def get_tiktok_user_data(username):
    url = f"https://www.tiktok.com/@{username}"
    
    # Set a user-agent to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Fetch the page content
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the user data (e.g., followers, likes, etc.)
        # This part depends on the HTML structure of the TikTok page
        # As an example, let's try extracting the title
        title = soup.title.text
        
        return {"title": title}
    else:
        return {"error": "Failed to fetch user data"}

# Test the function
username = "tiktok"
data = get_tiktok_user_data(username)
print(data)
