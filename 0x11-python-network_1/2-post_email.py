#!/usr/bin/python3

"""A script that:
takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # encode the email as a parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # make the POST request and read the response
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        # print the response body
        print(body)
