#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to
#+ the URL, and displays the body of the response using curl.
#+ A header variable X-School-User-Id must be sent with the value 98
curl -sG -H "X-School-User-Id: 98" "$1"
