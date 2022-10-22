#!/usr/bin/python3
""" Contains script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        page = response.read()
    print('Body response:')
    print('\t- type: ', type(page))
    print('\t- content: ', page)
    print('\t- utf8 content: ', page.decode('utf8'))
