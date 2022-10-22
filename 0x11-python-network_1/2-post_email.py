#!/usr/bin/python3
""" 
Contains  script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    value = {}
    value['email'] = sys.argv[2]
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        page = response.read()
    print(page)
