#!/usr/bin/env python
#
# Copyright 2023-2023 Ghent University
#
# SPDX license identifier: GPL-3.0-or-later
#
"""
Python script to generate an overview of available modules across different CPU and GPU targets,
in MarkDown format.

@author: Michiel Lachaert (Ghent University)
@author: Lara Peeters (Ghent University)
"""
import copy
import json
import os
import re
import subprocess
import sys
import time
import yaml
from typing import Union, Tuple
from string import Template
import numpy as np
from mdutils.mdutils import MdUtils
from natsort import natsorted
from functools import cmp_to_key

EESSI_TOPDIR = "/cvmfs/riscv.eessi.io/versions/20240402"

# some CPU targets are excluded for now, because software layer is too incomplete currently
EXCLUDE_CPU_TARGETS = []


# --------------------------------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------------------------------

def main():
    os.environ["SHELL"] = "/bin/bash"
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path_data_dir = os.path.join(root_dir, "docs/available_software/data")

    # Generate the JSON overviews
    modules = modules_eessi()
    print(modules)
    print("Generate JSON overview... ", end="", flush=True)
    generate_json_overview(modules, path_data_dir)
    print("Done!")

    # Generate the JSON detail
    json_data = generate_json_detailed_data(modules)
    json_data = get_extra_info_eessi(json_data)
    print("Generate JSON detailed... ", end="", flush=True)
    json_path = generate_json_detailed(json_data, path_data_dir)
    print("Done!")

    # Generate detail markdown pages
    print("Generate detailed pages... ", end="", flush=True)
<<<<<<< HEAD
    generate_detail_pages(json_path, os.path.join(root_dir, "docs/available_software/riscv-detail"))
=======
    generate_detail_pages(json_path, os.path.join(root_dir, "docs/available_software/detail"))
>>>>>>> 22e40ab0 (Generate RISC-V available software and modify left menu)
    print("Done!")


# --------------------------------------------------------------------------------------------------------
# Functions to run bash commands
# --------------------------------------------------------------------------------------------------------

def bash_command(cmd: str) -> np.ndarray:
    bash = os.getenv("SHELL")
    proc = subprocess.run(
        [bash, '-c', cmd],
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return np.array(proc.stdout.split())


# --------------------------------------------------------------------------------------------------------
# Functions to run "module" commands
# --------------------------------------------------------------------------------------------------------

def module(*args, filter_fn=lambda x: x) -> np.ndarray:
    """
    Function to run "module" commands.

    @param args: Extra arguments for the module command.
    @param filter_fn: Filter function on the output.
    @return: Array with the output of the module command.
    """
    lmod = os.getenv('LMOD_CMD')
    if lmod is None:
        sys.stderr.write("Lmod not found (via $LMOD_CMD)!\n")
        sys.exit(1)

    proc = subprocess.run(
        [lmod, "python", "--terse"] + list(args),
        encoding="utf-8",
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    exec(proc.stdout)
    return filter_fn(np.array(proc.stderr.strip().split("\n")))


def module_avail(name: str = "", filter_fn=lambda x: x) -> np.ndarray:
    """
    Function to run "module avail" commands.

    @param name: Module name, or empty string to return all available modules.
    @param filter_fn: Filter on the output.
    @return: List of all available modules of name, or all if name is not given.
    """
    return module("avail", name, filter_fn=filter_fn)


def module_swap(name: str) -> None:
    """
    Function to run "module swap" commands.

    @param name: Name of module you want to swap to.
    """
    module("swap", name)


def module_use(path: str) -> None:
    """
    Function to run "module use" commands.

    @param path: Path to the directory with all the modules you want to use.
    """
    module("use", path)


def module_unuse(path: str) -> None:
    """
    Function to run "module unuse" commands.

    @param path: Path to the directory with all the modules you want to unuse.
    """
    module("unuse", path)


def module_whatis(name: str) -> dict:
    """
    Function to run "module whatis" commands.

    @param name: Name of module you want the whatis info for.
    """
    whatis = {}
    data = module("show", name)
    for line in data[np.char.startswith(data, "whatis")]:
        content = re.sub(pattern=r'whatis\((.*)\)', repl='\\1', string=line).strip('"')
        key, value = tuple(content.split(":", maxsplit=1))
        whatis[key.strip()] = value.strip()
    return whatis


def module_info(info: str) -> dict:
    """
    Function to parse through lua file.

    @param info: String with the contents of the lua file.
    """
    whatis = {}
    data = np.array(info.split("\n"))
    # index of start description to handle multi lined description
    i = np.flatnonzero(np.char.startswith(data, "whatis([==[Description"))[0]
    if np.char.endswith(data[i], "]==])"):
        content = re.sub(pattern=r'whatis\(\[==\[(.*)\]==\]\)', repl='\\1', string=data[i]).strip('"')
    else:
        description = re.sub(pattern=r'whatis\(\[==\[(.*)', repl='\\1', string=data[i]).strip('"')
        while not np.char.endswith(data[i], "]==])"):
            i += 1
            description += data[i]
        content = re.sub(pattern=r'(.*)\]==\]\)', repl='\\1', string=description).strip('"')
    key, value = tuple(content.split(":", maxsplit=1))
    whatis[key.strip()] = value.strip()

    for line in data[np.char.startswith(data, "whatis")]:
        if not np.char.startswith(line, "whatis([==[Description"):
            content = re.sub(pattern=r'whatis\(\[==\[(.*)\]==\]\)', repl='\\1', string=line).strip('"')
            key, value = tuple(content.split(":", maxsplit=1))
            whatis[key.strip()] = value.strip()
    return whatis


# --------------------------------------------------------------------------------------------------------
# Fetch data EESSI
# --------------------------------------------------------------------------------------------------------

def filter_fn_eessi_modules(data: np.ndarray) -> np.ndarray:
    """
    Filter function for the output of all software modules for EESSI (excl. 'target').
    @param data: Output
    @return: Filtered output
    """
    return data[~np.char.endswith(data, ":")]


def targets_eessi() -> np.ndarray:
    """
    Returns all the target names of EESSI.
    @return: target names
    """
    if not os.path.exists(EESSI_TOPDIR):
        sys.stderr.write(f"ERROR: {EESSI_TOPDIR} does not exist!\n")
        sys.exit(1)

    commands = [
        f"find {EESSI_TOPDIR}/software/linux/*/* -maxdepth 0 \\( ! -name 'intel' -a ! "
        "-name 'amd' -a ! -name 'nvidia' \\) -type d",
        f'find {EESSI_TOPDIR}/software/linux/*/{{amd,intel,nvidia}}/* -maxdepth 0  -type d'
    ]
    targets = np.array([])

    for command in commands:
        targets = np.concatenate([targets, bash_command(command)])

    return targets


def eessi_target_compare(a, b):
    """
    A comparison function to compare the EESSI targets and order them.
    First the main architecture is ordered alphabetically, then within them
    the CPU targets are again ordered alphabetically, except for the
    generic target, which always comes first. Targets that include an extra
    vendor subdir always after those without a vendor subdir.
    @return: 0, 1, -1
    """
    if a == b:
        return 0

    a_split = a.rsplit('/')
    b_split = b.rsplit('/')

    # We first compare the main architecture (aarch64, x86_64, ...), which is the 7th field
    if a_split[7] == b_split[7]:
        # Check if one item is for generic builds (last field), These should always be listed first
        if a_split[-1] == 'generic':
            return -1
        if b_split[-1] == 'generic':
            return 1
        # If the number of fields are not equal, one has an extra vendor subdirectory (e.g. amd, intel, nvidia).
        # These should always come after the ones without this extra level.
        if len(a_split) != len(b_split):
            return 1 if len(a_split) > len(b_split) else -1

    # In all other cases we just do an alphabetical sort of the strings.
    return 1 if a > b else -1


def modules_eessi() -> dict:
    """
    Returns names of all software module that are installed on EESSI.
    They are grouped by target.
    @return: Dictionary with all the modules per target
    """
    print("Start collecting modules:")
    data = {}

    modulepath = os.getenv('MODULEPATH')
    if modulepath:
        module_unuse(modulepath)

    targets = targets_eessi()

    # Order targets
    eessi_target_compare_key = cmp_to_key(eessi_target_compare)
    ordered_targets = sorted(targets, key=eessi_target_compare_key)

    targets = [t for t in ordered_targets if not any(t.endswith(x) for x in EXCLUDE_CPU_TARGETS)]

    for target in targets:
        print(f"\t Collecting available modules for {target}... ", end="", flush=True)
        module_use(target + "/modules/all/")
        data[target] = module_avail(filter_fn=filter_fn_eessi_modules)
        print(f"found {len(data[target])} modules!")
        module_unuse(os.getenv('MODULEPATH'))

    print("All data collected!\n")
    return data


def get_extra_info_eessi(json_data) -> dict:
    """
    add Description, homepage and a list of extensions (only for software with extensions)
    @return: Dictionary with all the modules and their site_packages
    """
    modules = json_data['software']
    for software in modules:
        for mod in modules[software]['versions']:
            if software == "Java":
                # TODO handle specific naming schema for Java
                # code cannot handle "Java/11(@Java/11.0.20)"
                continue
            base_path = modules[software]['versions'][mod]['targets'][0] + '/modules/all/'
            path = base_path + mod + ".lua"
            f = open(path, 'r')
            info = f.read()
            if info != "":
                whatis = module_info(info)
                json_data['software'][software]['description'] = whatis['Description']
                if "Homepage" in whatis.keys():
                    json_data['software'][software]['homepage'] = whatis['Homepage']
                if "Extensions" in whatis.keys():
                    json_data["software"][software]["versions"][mod]["extensions"] = whatis['Extensions']
    return json_data


# --------------------------------------------------------------------------------------------------------
# Util functions
# --------------------------------------------------------------------------------------------------------

def analyze_module(mod: str) -> Tuple:
    return (
        mod.split("/", 1)[0],
        mod.split("/", 1)[1] if "/" in mod else ""
    )


def mod_names_to_software_names(mod_list: np.ndarray) -> np.ndarray:
    """
    Convert a list of module names to a list of the software names.

    @param mod_list: List of the module names
    @return: List of the corresponding software names
    """
    return np.unique([analyze_module(mod)[0] for mod in mod_list])


def get_unique_software_names(data: Union[dict, list, np.ndarray]) -> Union[dict, list, np.ndarray]:
    """
    Simplify list of modules by removing versions and duplicates.

    @param data: List of modules
    @return: List of software names.
    """

    if isinstance(data, dict):
        simplified_data = {target: mod_names_to_software_names(data[target]) for target in data}
    else:
        simplified_data = mod_names_to_software_names(data)

    return simplified_data


def dict_sort(dictionary: dict) -> dict:
    """
    Sort a dictionary by key.

    @param dictionary: A dictionary
    @return: Sorted dictionary
    """
    return dict(natsorted(dictionary.items()))


# --------------------------------------------------------------------------------------------------------
# Generate detailed markdown
# --------------------------------------------------------------------------------------------------------

def generate_software_table_data(software_data: dict, targets: list) -> list:
    """
    Construct the data for the detailed software table.

    @param software_data: Software specific data.
    @param targets: List with all the target names
    @return: 1D list with all the data for the table
    """
<<<<<<< HEAD
    table_data = [" "] + [target[55:] for target in targets]
=======
    table_data = [" "] + [target[57:] for target in targets]
>>>>>>> 22e40ab0 (Generate RISC-V available software and modify left menu)

    for module_name, available in list(software_data.items())[::-1]:
        row = [module_name]

        for target in targets:
            row += ("x" if target in available["targets"] else "-")
        table_data += row

    return table_data


# LD+JSON Template with placeholders
ldjson_template = Template("""
{
    "json_ld": {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "$name",
        "url": "$homepage",
        "softwareVersion": "$version",
        "description": "$description",
        "operatingSystem": "LINUX",
        "applicationCategory": "DeveloperApplication",
        "softwareRequirements": "See https://www.eessi.io/docs/ for how to make EESSI available on your system",
        "license": "Not confirmed",
        "review": {
            "@type": "Review",
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": 5
            },
            "author": {
                "@type": "Organization",
                "name": "EESSI"
            },
            "reviewBody": "Application has been successfully made available on all architectures supported by EESSI"
        },
        "offers": {
            "@type": "Offer",
            "price": 0
        }
    }
}
""")


def generate_software_detail_page(
        software_name: str,
        software_data: dict,
        generated_time: str,
        targets: list,
        path: str
) -> None:
    """
    Generate one software specific detail page.

    @param software_name: Name of the software
    @param software_data: Additional information about the software (version, etc...)
    @param generated_time: Timestamp when the data was generated
    @param targets: List with all the target names
    @param path: Path of the directory where the detailed page will be created.
    """
    sorted_versions = dict_sort(software_data["versions"])
    newest_version = list(sorted_versions.keys())[-1]
    ldjson_software_data = copy.deepcopy(software_data)

    filename = f"{path}/{software_name}.md"
    md_file = MdUtils(file_name=filename, title=f"{software_name}")
    if 'description' in software_data.keys():
        description = software_data['description']
        md_file.new_paragraph(f"{description}")
    else:
        ldjson_software_data['description'] = ''
    if 'homepage' in software_data.keys():
        homepage = software_data['homepage']
        md_file.new_paragraph(f"{homepage}")
    else:
        ldjson_software_data["homepage"] = ''

    md_file.new_header(level=1, title="Available modules")

    md_file.new_paragraph(f"The overview below shows which {software_name} installations are available for RISC-V "
                          f"architecture in EESSI, ordered based on software version (new to old).")
    md_file.new_paragraph(f"To start using {software_name}, load one of these modules using a `module load` command "
                          f"like:")
    md_file.insert_code(f"module load {newest_version}", language="shell")
    md_file.new_paragraph(f"(This data was automatically generated on {generated_time})", bold_italics_code="i")
    md_file.new_line()

    md_file.new_table(
        columns=len(targets) + 1,
        rows=len(sorted_versions) + 1,
        text=generate_software_table_data(sorted_versions, targets)
    )

    for version, details in list(sorted_versions.items())[::-1]:
        if 'extensions' in details:
            md_file.new_paragraph(f"### {version}")
            md_file.new_paragraph("This is a list of extensions included in the module:")
            packages = details['extensions']
            md_file.new_paragraph(f"{packages}")

    md_file.create_md_file()

    with open(filename) as f:
        read_data = f.read()
    with open(filename, 'w') as f:
        # Add the software name
        ldjson_software_data['name'] = software_name
        # Just output the supported versions (with toolchains)
        ldjson_software_data["version"] = list(sorted_versions.keys())
        # Make the description safe for json (and remove surrounding quotes)
        ldjson_software_data['description'] = json.dumps(ldjson_software_data['description'])[1:-1]
        json_str = ldjson_template.substitute(ldjson_software_data)  # Replace placeholders
        json_topmatter = json.loads(json_str)
        # Remove the TOC
        json_topmatter["hide"] = ["toc"]
        yaml_topmatter = yaml.dump(json_topmatter)
        f.write("---\n" + yaml_topmatter + "---\n" + read_data)


def generate_detail_pages(json_path, dest_path) -> None:
    """
    Generate all the detailed pages for all the software that is available.
    """

    with open(json_path) as json_data:
        data = json.load(json_data)

    all_targets = data["targets"]

    time_generated_template = os.environ.get('TIME_GENERATED_TEMPLATE')
    for software, content in data["software"].items():
        if time_generated_template:
            time_generated = time_generated_template
        else:
            time_generated = data["time_generated"]
        generate_software_detail_page(software, content, time_generated, all_targets, dest_path)


# --------------------------------------------------------------------------------------------------------
# Generate overview markdown
# --------------------------------------------------------------------------------------------------------

def generate_table_data(avail_mods: dict) -> Tuple[np.ndarray, int, int]:
    """
    Generate data that can be used to construct a MarkDown table.

    @param avail_mods: Available modules
    @return: Returns tuple (Table data, #col, #row)
    """
    avail_mods = get_unique_software_names(avail_mods)
    all_modules = get_unique_software_names(np.concatenate(list(avail_mods.values())))

    final = np.array([" "])
    final = np.append(final, list(avail_mods.keys()))

    for package in all_modules:
        final = np.append(final, package)

        for target in avail_mods:
            final = np.append(final, "X" if package in avail_mods[target] else " ")

    return final, len(avail_mods.keys()) + 1, len(all_modules) + 1


def generate_module_table(data: dict, md_file: MdUtils) -> None:
    """
    Generate the general table of the overview.

    @param data: Dict with all the data. Keys are the target names.
    @param md_file: MdUtils object.
    """
    print("Generating markdown table... ", end="", flush=True)
    structured, col, row = generate_table_data(data)
    md_file.new_table(columns=col, rows=row, text=list(structured), text_align='center')
    print("Done!")


def generate_markdown_overview(modules: dict) -> None:
    """
    Generate the general overview in a markdown file.
    It generates a list of all the available software and indicates for which target it is available.
    """
    md_fn = 'module_overview.md'
    md_file = MdUtils(file_name=md_fn, title='Overview of available modules per target architecture in EESSI')
    generate_module_table(modules, md_file)
    md_file.create_md_file()
    print(f"Module overview created at {md_fn}")


# --------------------------------------------------------------------------------------------------------
# Generate JSON
# --------------------------------------------------------------------------------------------------------
# -----------
# OVERVIEW
# -----------

# FORMAT OVERVIEW JSON
# {
#   "targets": [
#     "/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic",
#     "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"
#   ],
#   "modules": {
#     "Markov": [1, 0],
#     "cfd": [1, 1],
#     "llm": [0, 1],
#     "science": [1, 1]
#   }
# }
def generate_json_overview_data(modules: dict) -> dict:
    """
    Generate the data for the json overview in the above format.

    @param modules: Dictionary with all the modules per target. Keys are the target names.
    @return: Dictionary with the required JSON structure.

    """
    json_data = {
        "targets": list(modules.keys()),
        "modules": {},
        "time_generated": time.strftime("%a, %d %b %Y at %H:%M:%S %Z")
    }
    avail_software = get_unique_software_names(modules)
    all_software = get_unique_software_names(np.concatenate(list(modules.values())))

    # creates a list of booleans for each software that indicates
    # if the software is available for the corresponding target.
    for soft in all_software:
        available = []
        for target in json_data["targets"]:
            available.append(int(soft in avail_software[target]))
        json_data["modules"][soft] = available
    return json_data


def generate_json_overview(modules: dict, path_data_dir: str) -> str:
    """
    Generate the overview in a JSON format.

    @param modules: Dictionary with all the modules per target. Keys are the target names.
    @param path_data_dir: Path to the directory where the JSON will be placed.
    @return: Absolute path to the json file.
    """

    # get data
    json_data = generate_json_overview_data(modules)

    filepath = os.path.join(path_data_dir, "riscv_json_data.json")
    # write it to a file
    with open(filepath, 'w') as outfile:
        json.dump(json_data, outfile)

    return filepath


# -----------
# DETAILED
# -----------

# FORMAT DETAILED JSON:
#
# {
#   "targets": [
#     "/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic",
#     "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"
#   ],
#   "software": {
#     "cfd": {
#       "targets": [
#         "/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic",
#         "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"
#       ],
#       "versions": {
#         "2.3.1": ["/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic"],
#         "2.3.2": [
#           "/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/generic",
#           "/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2"
#         ]
#       }
#     }
#   }
# }

def generate_json_detailed_data(modules: dict) -> dict:
    """
    Generate the data for the detailed JSON in the above format.

    @param modules: Dictionary with all the modules per target. Keys are the target names.
    @return: Dictionary with the required JSON structure.
    """
    json_data = {
        "targets": list(modules.keys()),
        "software": {},
        "time_generated": time.strftime("%a, %d %b %Y at %H:%M:%S %Z")
    }

    # Loop over every module in every target
    for target in modules:
        for mod in modules[target]:
            software, version = analyze_module(mod)

            # Exclude modules with no version
            if version != "":
                # If the software is not yet present, add it.
                if software not in json_data["software"]:
                    json_data["software"][software] = {
                        "targets": [],
                        "versions": {}
                    }

                # If the version is not yet present, add it.
                if mod not in json_data["software"][software]["versions"]:
                    json_data["software"][software]["versions"][mod] = {'targets': []}

                # If the target is not yet present, add it.
                if target not in json_data["software"][software]["targets"]:
                    json_data["software"][software]["targets"].append(target)

                # If the target is not yet present, add it.
                if target not in json_data["software"][software]["versions"][mod]["targets"]:
                    json_data["software"][software]["versions"][mod]["targets"].append(target)

    return json_data


def generate_json_detailed(json_data: dict, path_data_dir: str) -> str:
    """
    Generate the detailed JSON.

    @param modules: Dictionary with all the modules per target. Keys are the target names.
    @param path_data_dir: Path to the directory where the JSON will be placed.
    @return: Absolute path to the json file.
    """
    filepath = os.path.join(path_data_dir, "riscv_json_data_detail.json")
    with open(filepath, 'w') as outfile:
        json.dump(json_data, outfile)

    return filepath


if __name__ == '__main__':
    main()
