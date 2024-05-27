#!/usr/bin/python3
""" Write a Python script that
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    handles the json response"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)

    try:
        jsonfile = response.json()
        if jsonfile:
            print("[{}] {}".format(jsonfile["id"], jsonfile["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
