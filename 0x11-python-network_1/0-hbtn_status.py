#!/usr/bin/python3
"""
a python script that fetches data and display.
"""
if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()

        print('- Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('utf-8'))
