#!/bin/bash
# sends a request to that URL, and displays the size in bytes.
curl -s "$1" | wc -c
