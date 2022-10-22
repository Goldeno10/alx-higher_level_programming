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
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    with requests.post(url, q) as res:
        try:
            dic_t = res.json()
            id = dic_t.get('id')
            name = dic_t.get('name')
            if len(dic_t) == 0 or not id or not name:
                print('No result')
            else:
                print(f"[{data['id']}] {data['name']}")
        except Exception:
            print('Not a valid JSON')
