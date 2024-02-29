#!/bin/bash
#body size returned
curl -sw '%{size_download}/n' -o /dev/null "$1"
