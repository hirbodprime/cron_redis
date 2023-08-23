import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Specify the key for the cached data
cache_key = 'camera_data'

# Retrieve and print the cached data
cached_data = r.get(cache_key)
if cached_data is not None:
    print("Cached Data:")
else:
    print("No data found in cache.")

# Close the Redis connection
r.close()
