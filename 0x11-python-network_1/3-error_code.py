#!/usr/bin/python3
"""
Contains script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
