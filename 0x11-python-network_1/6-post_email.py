#!/usr/bin/python3
"""
Contains  script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == '__main__':
    import sys
    import requests

    data = {}
    data['email'] = sys.argv[2]
    url = sys.argv[1]
    with requests.post(url, data=data) as res:
        print(res.text)
