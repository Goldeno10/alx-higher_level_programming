#!/usr/bin/python3
"""
Contains script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    with requests.get(url) as res:
        if res.status_code < 400:
            print(res.text)
        else:
            print(f'Error code: {res.status_code}')
