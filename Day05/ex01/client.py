import requests
import sys

SERVER_URL = 'http://127.0.0.1:8888'

def list_files():
    response = requests.get(f'{SERVER_URL}/list')
    if response.status_code == 200:
        print("Files:", response.json())
    else:
        print("Failed to list files:", response.text)

def upload_file(filepath):
    with open(filepath, 'rb') as file:
        files = {'file': file}
        response = requests.post(f'{SERVER_URL}/upload', files=files)
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print("Failed to upload file:", response.text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py [list|upload] [filepath]")
        sys.exit(1)

    action = sys.argv[1]

    if action == 'list':
        list_files()
    elif action == 'upload' and len(sys.argv) == 3:
        upload_file(sys.argv[2])
    else:
        print("Invalid command or missing filepath for upload")
