#!/bin/bash

# Return an error when a variable is not set.
set -u


# example: /bin/bash -c "echo hello"
bash="$0"
cflag="$1"
cmd="$2"

# Emulate find command.
if echo "$cmd" | grep -q -E "find"; then
   if echo "$cmd" | grep -q -E "amd,intel"; then
       cat "${MOCK_FILE_AVAIL_CLUSTER_AMD_INTEL}" >&1
   else
       cat "${MOCK_FILE_AVAIL_CLUSTER}" >&1
   fi
fi
