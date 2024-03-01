#!/usr/bin/python3
"""  Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body Response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
