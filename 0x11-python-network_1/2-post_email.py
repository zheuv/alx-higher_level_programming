#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8) """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys[1]
    email = sys[2]
    data = urllib.parse.urlencode({email:email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.openurl(req) as response:
        print(response.read().decode('utf-8'))
