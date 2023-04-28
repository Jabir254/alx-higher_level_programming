#!/usr/bin/python3
"""
python script to fetches data:
    use requests
"""

import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response.content.decode('utf-8')

    print("Body response:")
    print(" -   type: {}\n  - content: {}".format(type(body), body))
