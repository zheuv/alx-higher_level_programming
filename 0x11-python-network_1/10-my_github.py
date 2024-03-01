#!/usr/bin/python3


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    pwd = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, pwd))
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)
