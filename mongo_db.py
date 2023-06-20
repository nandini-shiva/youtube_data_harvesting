import pymongo

# MongoDB configuration
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"  # Update with your MongoDB connection string
MONGO_DB_NAME = "youtube_data"  # Update with your desired database name
MONGO_COLLECTION_NAME = "channel_data"  # Update with your desired collection name

def store_data_in_mongodb(channel_data):
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        db = client[MONGO_DB_NAME]
        collection = db[MONGO_COLLECTION_NAME]

        # Insert channel data into the collection
        collection.insert_one(channel_data)

        st.success("Data stored in MongoDB successfully.")

    except pymongo.errors.PyMongoError as e:
        st.error(f"Error storing data in MongoDB: {e}")

def main():
    # ...

    if st.button("Retrieve Channel Data"):
        channel_data = get_channel_data(channel_id)
        st.write("Channel Name:", channel_data["Channel Name"])
        st.write("Subscriber Count:", channel_data["Subscriber Count"])
        st.write("Video Count:", channel_data["Video Count"])
        store_data_in_mongodb(channel_data)

    # ...

if __name__ == '__main__':
    main()
