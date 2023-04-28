#!/usr/bin/python3
"""takes a URL, sends a request to the URL and displays the value of the
X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    # get URL from command line argument
    url = sys.argv[1]
    # send request and get response
    with urllib.request.urlopen(url) as response:
        # extract X-Request-Id from response headers
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
