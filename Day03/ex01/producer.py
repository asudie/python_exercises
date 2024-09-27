import redis
import json
import random
import logging

logging.basicConfig(level=logging.INFO)

r = redis.Redis()

def generate_account():
    return random.randint(1000000000, 9999999999)

def create_message():
    message = {
        "metadata": {
            "from": generate_account(),
            "to": generate_account()
        },
        "amount": random.randint(-10000, 10000)
    }
    return message

def main():
    for _ in range(10):
        message = create_message()
        r.publish('transactions', json.dumps(message))
        logging.info(f"Sent: {json.dumps(message)}")

if __name__ == "__main__":
    main()
