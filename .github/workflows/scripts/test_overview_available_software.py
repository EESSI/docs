import os
import json
from bs4 import BeautifulSoup

path = os.path.dirname(os.path.realpath(__file__))
path_overview = "/../../../docs/available_software/overview.md"
path_data = "/../../../docs/available_software/data/json_data.json"
if os.path.exists(path + path_overview) and os.path.exists(path + path_data):
    with open(path + path_data) as json_data:
        data = json.load(json_data)
    with open(path + path_overview) as f:
        soup = BeautifulSoup(f, "html.parser")
else:
    os.write(1, b'Error: Could not find overview.md and/or data/json_data.json')

# parse the numbers for the different targets
targets = data["targets"]
ARM_targets = []
x86_targets = []
amd_targets = []
intel_targets = []
nvidia_targets = []

for target in targets:
    t = target.split('/')
    if t[7] == 'aarch64':
        ARM_targets.append(target)
    else:
        x86_targets.append(target)
    if t[8] == "amd":
        amd_targets.append(target)
    elif t[8] == "intel":
        intel_targets.append(target)
    elif t[8] == 'nvidia':
        nvidia_targets.append(target)

# parse the overview.md page to check the number of colums in rows
table = soup.find("table", {"class": "table"})
for row in table.find_all("tr"):
    for column in row.find_all('th'):
        if column.text == "x86_64":
            print(f'the value for x86_64 is {column.get("colspan")} in the overview page but there are {len(x86_targets)} targets in json_data.json.)
            if int(column.get("colspan")) != len(x86_targets):
                os.write(2, b'Error: Please make sure the values for x86_64 in json_data.json and overview.md are the same.')
        elif column.text == "aarch64":
            print(f'the value for aarch64 is {column.get("colspan")} in the overview page but there are {len(ARM_targets)} targets in json_data.json.)
            if int(column.get("colspan")) != len(ARM_targets):
                os.write(2, b'Error: Please make sure the values for aarch64 in json_data.json and overview.md are the same.')
        elif column.text == "amd":
            print(f'the value for amd is {column.get("colspan")} in the overview page but there are {len(amd_targets)} targets in json_data.json.)
            if int(column.get("colspan")) != len(amd_targets):
                os.write(2, b'Error:  Please make sure the values for amd in json_data.json and overview.md are the same.')
        elif column.text == "intel":
            print(f'the value for intel is {column.get("colspan")} in the overview page but there are {len(intel_targets)} targets in json_data.json.)
            if int(column.get("colspan")) != len(intel_targets):
                os.write(2, b'Error:  Please make sure the values for intel in json_data.json and overview.md are the same.')
        elif column.text == "nvidia":
            print(f'the value for nvidia is {column.get("colspan")} in the overview page but there are {len(nvidia_targets)} targets in json_data.json.)
            if int(column.get("colspan")) != len(nvidia_targets):
                os.write(2, b'Error: Please make sure the values for nvidia in json_data.json and overview.md are the same.')
last_row = table.find_all("tr")[-1]
print(f'there are {len(last_row.find_all("th"))} columns in the overview page but {len(targets)} targets in json_data.json.')
if len(last_row.find_all("th")) != len(targets):
    os.write(2, b'Error: Please make sure there are correct number of <th> elements in the last <tr> element in overview.md for JavaScript to generate the table.')
