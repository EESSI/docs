#!/bin/bash

# Return an error when a variable is not set.
set -u


# example: $LMOD_CMD python --terse avail cluster/
python="$1"
terse="$2"
mod_cmd="$3"
mod_args="${4:-}"

# Emulated avail command.
if [ "$mod_cmd" = "avail" ]; then
  if [ "$mod_args" = "cluster/" ]; then
    cat "${MOCK_FILE_AVAIL_CLUSTER}" >&2
  else
    cat "${MOCK_FILE_AVAIL}" >&2
  fi


# Emulated swap command.
elif [ "$mod_cmd" = "swap" ]; then
  # extract the cluster name from the 4th argument
  cluster=$(echo "$mod_args" | cut -d "/" -f 1)
  cluster_name=$(echo "$mod_args" | cut -d "/" -f 2)

  if [ "$cluster" = "cluster" ]; then
    # Substitute CLUSTER by the cluster_name
    cat ${MOCK_FILE_SWAP/CLUSTER/${cluster_name}} >&1
  else
    echo "${mod_args} is not a cluster." >&2
    exit 1
  fi


# Emulate show command
elif [ "$mod_cmd" = "show" ]; then
      cat "${MOCK_FILE_SHOW}" >&2


elif [ "$mod_cmd" = "use" ]; then
      cvmfs=$(echo "$mod_args" | cut -d "/" -f 2)
      repo=$(echo "$mod_args" | cut -d "/" -f 3)
      if [ "cvmfs" = "cvmfs" ]; then
          if echo "$mod_args" | grep -q -E "amd"; then
              cluster_name=$(echo "$mod_args" | cut -d "/" -f 10)
              # Substitute CLUSTER by the cluster_name
              cat ${MOCK_FILE_SWAP/CLUSTER/${cluster_name}} >&1
          elif echo "$mod_args" | grep -q -E "intel"; then
              cluster_name=$(echo "$mod_args" | cut -d "/" -f 10)
              # Substitute CLUSTER by the cluster_name
              cat ${MOCK_FILE_SWAP/CLUSTER/${cluster_name}} >&1
          else
              cluster_name=$(echo "$mod_args" | cut -d "/" -f 9)
              # Substitute CLUSTER by the cluster_name
              cat ${MOCK_FILE_SWAP/CLUSTER/${cluster_name}} >&1
          fi
      else
          echo "${mod_arg} in not a cvmfs repo"
          exit 1
      fi


else
    echo "Module subcommand '${mod_cmd}' not supported yet in $0" >&2
  exit 1
fi
