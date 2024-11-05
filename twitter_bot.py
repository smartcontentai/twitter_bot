import tweepy
import random

# Import environment variables (your Twitter API keys and tokens)
import os

API_KEY = os.getenv('wfkNBVCjzz4PL2YEiCEoFWBcq')
API_KEY_SECRET = os.getenv('OYbxtxhPJFxFTgLHCeLTiWsJnpOSpS5mBJvzmRQqhNRnuPwtob')
ACCESS_TOKEN = os.getenv('1853403986298122240-nFmIJgW4mk7I2ig7GXG8N9qN93DdWW')
ACCESS_TOKEN_SECRET = os.getenv('AAAAAAAAAAAAAAAAAAAAALofwwEAAAAAiiF%2F8BECjiGw3slAGPrnSdICYaA%3DSk7RPLIqQelh4Z0eH4pgDJ0vKipsggBPhOq2937ZCZqpyUxPLS')

print("API_KEY:", API_KEY)
print("API_KEY_SECRET:", API_KEY_SECRET)
print("ACCESS_TOKEN:", ACCESS_TOKEN)
print("ACCESS_TOKEN_SECRET:", ACCESS_TOKEN_SECRET)

# Authorize with Tweepy
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# List of finance quotes
finance_quotes = [
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. – Phillip Fisher",
    "In investing, what is comfortable is rarely profitable. – Robert Arnott",
    "The four most dangerous words in investing are: 'this time it’s different.' – Sir John Templeton",
    # Add more quotes here
]

# Function to post a random quote
def post_random_quote():
    quote = random.choice(finance_quotes)
    client.create_tweet(text=quote)
    print(f"Tweeted: {quote}")

# Run the bot to tweet a quote
if __name__ == "__main__":
    post_random_quote()
