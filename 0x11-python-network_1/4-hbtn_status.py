#!/usr/bin/python3
""" Contains script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as res:
        print('Body response:')
        print(f'\t- type: {type(res.text)}')
        print(f'\t- content: {res.text}')
