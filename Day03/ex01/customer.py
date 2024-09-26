import redis
import json
import argparse

# Redis setup
r = redis.Redis()

# Function to process incoming messages
def process_message(message, bad_guys):
    transaction = json.loads(message)
    metadata = transaction['metadata']
    amount = transaction['amount']

    # Swap sender and receiver if recipient is a bad guy and amount is positive
    if metadata['to'] in bad_guys and amount > 0:
        metadata['from'], metadata['to'] = metadata['to'], metadata['from']
    
    return transaction

# Main consumer function
def main(bad_guys):
    pubsub = r.pubsub()
    pubsub.subscribe('transactions')

    print(f"Listening for transactions...")

    for message in pubsub.listen():
        if message['type'] == 'message':
            processed_transaction = process_message(message['data'], bad_guys)
            print(json.dumps(processed_transaction))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consumer for Redis transactions")
    parser.add_argument("-e", "--exclude", required=True, help="Comma-separated list of bad guy account numbers")
    
    args = parser.parse_args()
    bad_guys = args.exclude.split(",")

    main(bad_guys)
