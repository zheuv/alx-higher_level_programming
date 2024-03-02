#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays the body of the response.
    handles error code """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
        exit()
    print(response.text)
