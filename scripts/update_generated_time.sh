#!/usr/bin/env bash

# Get the new date
NEW_DATE="$(date '+%a, %d %b %Y at %H:%M:%S %Z')"
# Inject it into the target file
sed -i 's/\(generated_time: "\)[^"]*\(".*\)/\1'"${NEW_DATE}"'\2/' $1
