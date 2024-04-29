#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) """
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode()
    reqst = request.Request(argv[1], email)
    with request.urlopen(reqst) as resp:
        print(resp.read().decode("utf8"))
