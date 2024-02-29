#!/bin/bash
#curl the allowed methods
curl -sI "$1" | grep -i "^Allow:" | awk '{sub("^Allow: ", ""); print}'
