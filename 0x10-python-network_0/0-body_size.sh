#!/bin/bash
# sends a request to that URL, and displays the size of the body
#The size must be displayed in bytes.
curl -s "$1" | wc -c
