#!/usr/bin/python3
"""
Contains script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    dict_list = res.json()
    count = 1
    for item in dict_list:
        sha = item.get('sha')
        author = item.get('commit').get('author').get('name')
        print(f'{sha}: {author}')
        count += 1
        if count > 10:
            break
