
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# Set up YouTube API credentials
API_KEY = "AIzaSyDCOzq1D2niR3FuvsfdFi4bU44xEeinpCE"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_channel_data(channel_id):
    try:
        # Create a service object for making API requests
        credentials = service_account.Credentials.from_service_account_file(
            r"C:\Users\Nandini G\Desktop\youtube_data_harvesting\diesel-ellipse-388310-798d1c2a397f.json"
        )
        service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

        # Make API request to retrieve channel data
        response = service.channels().list(
            part="snippet,statistics",
            id=channel_id
        ).execute()

        # Check if "items" key is present in the response
        if "items" in response:
            # Extract relevant information from the API response
            channel_data = response["items"][0]
            channel_name = channel_data["snippet"]["title"]
            subscriber_count = channel_data["statistics"]["subscriberCount"]
            video_count = channel_data["statistics"]["videoCount"]

            return {
                "Channel Name": channel_name,
                "Subscriber Count": subscriber_count,
                "Video Count": video_count
            }
        else:
            st.error("No channel data found for the given channel ID.")

    except HttpError as e:
        st.error(f"Error: {e}")



def get_channel_data11(channel_id):
    try:
        # Create a service object for making API requests
        credentials = service_account.Credentials.from_service_account_file(
    r"C:\Users\Nandini G\Desktop\youtube_data_harvesting\diesel-ellipse-388310-798d1c2a397f.json"
)

        service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

        # Make API request to retrieve channel data
        response = service.channels().list(
            part="snippet,statistics",
            id=channel_id
        ).execute()

        # Extract relevant information from the API response
        channel_data = response["items"][0]
        channel_name = channel_data["snippet"]["title"]
        subscriber_count = channel_data["statistics"]["subscriberCount"]
        video_count = channel_data["statistics"]["videoCount"]

        return {
            "Channel Name": channel_name,
            "Subscriber Count": subscriber_count,
            "Video Count": video_count
        }

    except HttpError as e:
        st.error(f"Error: {e}")

def main():
    st.title("YouTube Data Harvesting and Warehousing")
    
    channel_id = st.text_input("Enter YouTube Channel ID:")
    if st.button("Retrieve Channel Data"):
        channel_data = get_channel_data(channel_id)
        st.write("Channel Name:", channel_data["Channel Name"])
        st.write("Subscriber Count:", channel_data["Subscriber Count"])
        st.write("Video Count:", channel_data["Video Count"])
    
    # Add more UI elements and functionality as needed

if __name__ == '__main__':
    main()