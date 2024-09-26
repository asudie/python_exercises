import redis
import json
import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Redis setup
r = redis.Redis()

# Function to generate a 10-digit account number
def generate_account():
    return random.randint(1000000000, 9999999999)

# Function to create the JSON message
def create_message():
    message = {
        "metadata": {
            "from": generate_account(),
            "to": generate_account()
        },
        "amount": random.randint(-10000, 10000)  # Random amount
    }
    return message

# Publish messages to Redis queue
def main():
    for _ in range(10):  # Generate 10 messages
        message = create_message()
        r.publish('transactions', json.dumps(message))
        logging.info(f"Sent: {json.dumps(message)}")

if __name__ == "__main__":
    main()
