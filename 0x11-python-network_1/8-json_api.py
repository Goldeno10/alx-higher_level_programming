#!/usr/bin/python3
"""
Contains  script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    with requests.post(url, data={'q': q}) as res:
        try:
            dic_t = res.json()
            id = dic_t.get('id')
            name = dic_t.get('name')
            if len(dic_t) == 0 or not id or not name:
                print('No result')
            else:
                print(f"[{id}] {name}")
        except Exception:
            print('Not a valid JSON')
