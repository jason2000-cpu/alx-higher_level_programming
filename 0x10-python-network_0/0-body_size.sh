#!/bin/bash

# Bash script that  takes in a URL, sends a request to that URL
# and displays the size of the body of the response

# Get the URL from the command line argument
url=$1

# Send the request and save the response body to a file
response=$(curl -s -w '\n%{size_download}' $url -o response.txt)

# Get the size of the response body from the response string
size=$(echo "$response" | tail -n 1)

# Print the size of the response body
echo $size 
