import asyncio
from playwright.sync_api import sync_playwright

def get_tiktok_user_data(username):
    url = f"https://www.tiktok.com/@{username}"

    # Initialize Playwright to open a browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless means no UI
        page = browser.new_page()
        page.goto(url)
        
        # Wait for content to load (you may need to adjust this based on the page structure)
        page.wait_for_selector('h1')  # Example selector, you should adjust this to match TikTok's structure
        
        # Extract data, you can refine this based on what specific info you need
        user_data = {
            'title': page.title(),
            'followers': page.inner_text('h1')  # You can replace 'h1' with a more specific selector for followers
        }
        
        browser.close()
        return user_data

# Test the function
username = "tiktok"  # Replace with any TikTok username
data = get_tiktok_user_data(username)
print(data)
