import sys

def decypher_message(message):
    words = message.split()
    
    secret_word = ''.join(word[0] for word in words)
    
    return secret_word

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decypher.py \"Your message here\"")
        sys.exit(1)
    
    message = sys.argv[1]
    
    result = decypher_message(message)
    
    print(result)
