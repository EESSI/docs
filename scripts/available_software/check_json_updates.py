#!/usr/bin/env python
#
# Copyright 2023-2023 Ghent University
#
# SPDX license identifier: GPL-3.0-or-later
#
"""
Python script to check for differences between provided JSON files
that contain data on available software.

@author: Kenneth Hoste (Ghent University)
"""
import json
import sys

if len(sys.argv) != 3:
    sys.stderr.write(f"Usage: {sys.argv[0]} <one.json> <two.json>\n")
    sys.exit(1)

json1_path = sys.argv[1]
json2_path = sys.argv[2]

with open(json1_path) as json1:
    json1_data = json.load(json1)
with open(json2_path) as json2:
    json2_data = json.load(json2)

json1_data_filtered = {k: v for (k, v) in json1_data.items() if k != 'time_generated'}
json2_data_filtered = {k: v for (k, v) in json2_data.items() if k != 'time_generated'}

if json1_data_filtered == json2_data_filtered:
    print("no changes")
else:
    print("differences found")
