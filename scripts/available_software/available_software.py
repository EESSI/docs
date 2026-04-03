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
import yaml
from mdutils.tools.Table import Table
from string import Template

AARCH64 = "aarch64"
AMD = "amd"
GENERIC = "generic"
INTEL = "intel"
NVIDIA = "nvidia"
X86_64 = "x86_64"


# --------------------------------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------------------------------


def main():
    os.environ["SHELL"] = "/bin/bash"
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # Allow for test data and target
    target_directory = os.environ.get("AVAIL_SOFTWARE_TEST_DIRECTORY") or os.path.join(
        root_dir, "docs", "available_software"
    )
    path_data_dir = os.path.join(target_directory, "data")

    # Generate software-specific pages using data from https://eessi.io/api_data/data/eessi_api_metadata_software.json
    print("Generating software-specific pages... ", end="", flush=True)
    api_data_software_json = os.path.join(path_data_dir, "eessi_api_metadata_software.json")
    generate_software_pages(api_data_software_json, os.path.join(target_directory, "detail"))

    print("Done!")

    # Also handle RISC-V
    print("Generating software-specific pages for RISC-V... ", end="", flush=True)
    api_data_software_json = os.path.join(path_data_dir, "eessi_api_metadata-riscv_software.json")
    generate_software_pages(api_data_software_json, os.path.join(target_directory + "_riscv", "detail"))

    print("Done!")


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


def format_cpu_arch_list(cpu_archs):

    res = []

    # generic CPU targets
    gen_cpu_targets = [c for c in cpu_archs if c.endswith("/" + GENERIC)]
    res.append("`generic`: " + ", ".join(["`" + x.split("/", maxsplit=1)[0] + "`" for x in gen_cpu_targets]) + "<br/>")

    # Arm CPU targets
    arm_cpu_targets = [c for c in cpu_archs if c.startswith(AARCH64) and not c.endswith("/" + GENERIC)]
    label = '<span class="software-cpu-arm">Arm</span>'
    res.append(label + ": " + ", ".join(["`" + x.split("/", maxsplit=1)[1] + "`" for x in arm_cpu_targets]) + "<br/>")

    # x86_64 AMD CPU targets
    amd_cpu_targets = [c for c in cpu_archs if c.startswith(X86_64 + "/" + AMD)]
    label = '<span class="software-cpu-amd">AMD</span>'
    res.append(label + ": " + ", ".join(["`" + x.split("/", maxsplit=2)[2] + "`" for x in amd_cpu_targets]) + "<br/>")

    # x86_64 Intel CPU targets
    intel_cpu_targets = [c for c in cpu_archs if c.startswith(X86_64 + "/" + INTEL)]
    label = '<span class="software-cpu-intel">Intel</span>'
    res.append(label + ": " + ", ".join(["`" + x.split("/", maxsplit=2)[2] + "`" for x in intel_cpu_targets]) + "<br/>")

    return res


def format_gpu_arch_list(gpu_archs):

    res = []

    all_gpu_archs = set([y for x in gpu_archs.values() for y in x])

    # AMD GPU targets
    amd_gpu_targets = sorted([g for g in all_gpu_archs if g.startswith(AMD + "/")])
    if amd_gpu_targets:
        label = '<span class="software-gpu-amd">AMD</span>'
        res.append(
            label + ": " + ", ".join(["`" + x.split("/", maxsplit=1)[1] + "`" for x in amd_gpu_targets]) + "<br/>"
        )

    # NVIDIA GPU targets
    nvidia_gpu_targets = sorted([g for g in all_gpu_archs if g.startswith(NVIDIA + "/")])
    if nvidia_gpu_targets:
        label = '<span class="software-gpu-nvidia">NVIDIA</span>'
        res.append(
            label + ": " + ", ".join(["`" + x.split("/", maxsplit=1)[1] + "`" for x in nvidia_gpu_targets]) + "<br/>"
        )

    return res


def generate_software_page(software_name: str, software_data: dict, path: str) -> None:
    """
    Generate one software specific detail page.

    @param software_name: Name of the software
    @param software_data: Additional information about the software (version, etc...)
    @param generated_time: Timestamp when the data was generated
    @param targets: List with all the target names
    @param path: Path of the directory where the detailed page will be created.
    """
    filename = os.path.join(path, f"{software_name}.md")

    md_lines = [
        f"# {software_name}",
        "",
    ]
    if "description" in software_data.keys():
        description = software_data["description"]
        md_lines.extend(
            [
                "",
                f"{description}",
                "",
            ]
        )

    if "homepage" in software_data.keys():
        homepage = software_data["homepage"]
        md_lines.append(f'<small>homepage: </small><span class="software-link">[{homepage}]({homepage})</span>')

    md_lines.extend(
        [
            "",
            "## Available installations",
            "",
        ]
    )

    table_data = [
        f"{software_name} version",
        "Supported CPU targets",
        "Supported GPU targets",
        "EESSI version",
        "Module",
    ]
    n_cols = len(table_data)

    n_rows = 1
    for version in sorted(software_data["versions"], key=lambda x: x["version"]):
        cpu_targets = format_cpu_arch_list(version["cpu_arch"])
        gpu_targets = format_gpu_arch_list(version["gpu_arch"])

        req_mods = version["required_modules"]
        if req_mods and req_mods[0].get("module_name") == "EESSI":
            eessi_version = req_mods[0]["module_version"]
            eessi_version_no_dots = eessi_version.replace(".", "")
            eessi_version_label = f'<span class="software-eessi-version-{eessi_version_no_dots}">{eessi_version}</span>'
        else:
            eessi_version_label = "*???*"

        table_data.extend(
            [
                version["version"],
                "".join(cpu_targets),
                "".join(gpu_targets) or "*(none)*",
                eessi_version_label,
                "`" + version["module"]["full_module_name"] + "`",
            ]
        )
        n_rows += 1

    table = Table().create_table(columns=n_cols, rows=n_rows, text=table_data)
    md_lines.extend(table.splitlines())

    exts = {}
    for version in software_data["versions"]:
        for ext_data in version["extensions"]:
            ext_details = exts.setdefault(ext_data["name"], {})
            ext_version = ext_details.setdefault(ext_data["version"], set())
            ext_version.add(version["module"]["full_module_name"])

    if exts:
        md_lines.extend(
            [
                "",
                "## Extensions",
                "",
                f"Overview of extensions included in {software_name} installations",
                "",
            ]
        )

        table_header = ["`%s` version", f"{software_name} modules that include it"]
        n_cols = len(table_header)

        for ext_name, ext_details in sorted(exts.items(), key=lambda x: x[0].lower()):

            md_lines.extend(
                [
                    "",
                    f"### {ext_name}",
                    "",
                ]
            )

            table_data = table_header[:]
            table_data[0] = table_data[0] % ext_name

            n_rows = 1
            for ext_version, ext_version_mods in sorted(ext_details.items(), key=lambda x: x[0]):
                n_rows += 1
                table_data.extend(
                    [
                        ext_version,
                        "<br/>".join("`" + m + "`" for m in sorted(ext_version_mods)),
                    ]
                )

            table = Table().create_table(columns=n_cols, rows=n_rows, text=table_data)
            md_lines.extend(table.splitlines())

    md_txt = "\n".join(md_lines)

    with open(filename, "w") as fp:
        fp.write(md_txt)

    # Add ldjson data topmatter
    with open(filename) as f:
        read_data = f.read()
    ldjson_software_data = copy.deepcopy(software_data)
    if "description" not in software_data.keys():
        ldjson_software_data["description"] = ""
    if "homepage" not in software_data.keys():
        ldjson_software_data["homepage"] = ""
    with open(filename, "w") as f:
        # Add the software name
        ldjson_software_data["name"] = software_name
        # Just output the supported versionsq
        ldjson_software_data["version"] = sorted(
            list(set([version["version"] for version in software_data["versions"]])), reverse=True
        )
        # Make the description safe for json (and remove surrounding quotes)
        ldjson_software_data["description"] = json.dumps(ldjson_software_data["description"])[1:-1]
        json_str = ldjson_template.substitute(ldjson_software_data)  # Replace placeholders
        json_topmatter = json.loads(json_str)
        yaml_topmatter = yaml.dump(json_topmatter)
        f.write("---\n" + yaml_topmatter + "---\n" + read_data)


def generate_software_pages(json_path, dest_path) -> None:
    """
    Generate software-specific pages
    """

    with open(json_path) as json_data:
        data = json.load(json_data)

    for name in data["software"]:
        generate_software_page(name, data["software"][name], dest_path)


if __name__ == "__main__":
    main()
