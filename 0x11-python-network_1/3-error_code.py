#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        reqst = request.Request(argv[1])
        with request.urlopen(reqst) as resps:
            print(resps.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
