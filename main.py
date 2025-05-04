import streamlit as st
import requests

# Function to fetch TikTok user info
def fetch_tiktok_user_info(username):
    url = f"https://jaefu3p97g.execute-api.us-east-1.amazonaws.com/default/smttab?username={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if status code is 4xx/5xx
        data = response.json()

        # Return the data if found
        if data and 'data' in data:
            return data['data']
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

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
        st.image(user_info.get("avatar_url", ""), width=150)
        st.write(f"**Username:** {user_info.get('username')}")
        st.write(f"**Nickname:** {user_info.get('nickname')}")
        st.write(f"**Bio:** {user_info.get('bio_description')}")
        st.write(f"**Followers:** {user_info.get('follower_count')}")
        st.write(f"**Following:** {user_info.get('following_count')}")
        st.write(f"**Likes:** {user_info.get('likes_count')}")
        st.write(f"**Videos:** {user_info.get('video_count')}")
        st.write(f"**Region:** {user_info.get('region')}")
    else:
        st.warning("User data not found.")
