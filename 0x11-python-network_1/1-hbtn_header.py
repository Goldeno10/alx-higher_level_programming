#!/usr/bin/python3
""" 
Contains  script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        page = response.info()
    print(page['X-Request-Id'])
