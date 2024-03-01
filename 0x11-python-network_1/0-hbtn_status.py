#!/usr/bin/python3
"""  Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(f"Body response:\n\t- type: {type(content)}\n\t\
- content: {content}\n\t- utf8 content: {content.decode('utf-8')}")
