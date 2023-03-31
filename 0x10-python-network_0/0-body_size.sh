#!/bin/bash
url=$1
size=$(curl -s -w '\n%{size_download}' $url | tail -n 1)
echo $size 
