#!/usr/bin/python3
"""  Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body Response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    -utf8 content:", content.decode('utf-8'))
