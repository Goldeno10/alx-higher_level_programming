#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response using curl A variable "email" sent with the value "test@gmail.com" A variable 'subject' sent with the value "I will always be here for PLD"
curl -sX POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
