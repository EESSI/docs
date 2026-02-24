# Macros implemented in Python that can be used in MarkDown files,
# see also https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
#
# author: Kenneth Hoste (Ghent University)
# license (SPDX): GPL-2.0-only
#
import json
import os
import urllib.request
from pathlib import Path

EESSI_API_SOFTWARE_JSON_URL = 'https://www.eessi.io/api_data/data/eessi_api_metadata_software.json'

CPU_ARCHS = {
    'x86_64': ['AMD', 'Intel'],
    'aarch64': ['Arm'],
    'riscv64': ['RISC-V'],
}
GPU_ARCHS = {
    'amd': 'AMD',
    'accel/amd': 'AMD',
    'nvidia': 'NVIDIA',
    'accel/nvidia': 'NVIDIA',
}


def define_env(env):

    @env.macro
    def load_json_eessi_software():
        """
        Load JSON with metadata for software.eessi.io repository,
        and return Python dictionary with relevant info to generate software overview in EESSI documentation.
        """
        # https://eessi.io/api_data/data/eessi_api_metadata_software.json is expected to be downloaded to docs/available_software/data/
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        json_path = os.path.join(root_dir, 'docs', 'available_software', 'data', 'eessi_api_metadata_software.json')
        if os.path.exists(json_path):
            with open(json_path) as fp:
                data = json.loads(fp.read())
        else:
            with urllib.request.urlopen(EESSI_API_SOFTWARE_JSON_URL) as response:
                data = json.loads(response.read().decode('utf-8'))

        data_software = data['software']
        names = data_software.keys()

        ext_parents = {}

        res = {
            'timestamp': data['timestamp'],
            'n_software': len(names),
            'software': [],
        }
        for name in names:
            name_data = data_software[name]
            versions = name_data['versions']

            # use description is last version
            descr = ' '.join(versions[-1]['description'].strip().splitlines())
            descr = descr.replace('<', 'less than ').replace('>', 'more than ')

            # use all homepages
            homepages = set(x['homepage'].rstrip('/') for x in versions)
            homepages = ', '.join("<a href='%(h)s'>%(h)s</a>" % {'h': h} for h in homepages)

            licenses = ', '.join(y for x in versions for y in x['license'])

            # determine set of supported CPU families (first part of CPU target names, like x86_64 or aarch64)
            cpu_families = set()
            for version in versions:
                for cpu_arch in version['cpu_arch']:
                    cpu_family = cpu_arch.split('/')[0]
                    cpu_families.update(CPU_ARCHS.get(cpu_family, [cpu_family]))

            # determine set of supported GPU families
            gpu_families = set()
            for version in versions:
                for gpu_arch in [y for x in version['gpu_arch'].values() for y in x]:
                    gpu_family = '/'.join(gpu_arch.split('/')[:-1])
                    gpu_families.add(GPU_ARCHS.get(gpu_family, gpu_family))

            # EESSI versions in which this software is available
            eessi_versions = set()

            software = {
                'name': name,
                'homepages': homepages,
                'description': descr,
                'n_versions': len(versions),
                'licenses': licenses,
                'cpu_families': ', '.join(x for x in sorted(cpu_families)),
                'gpu_families': ', '.join(x for x in sorted(gpu_families)),
                'is_extension': False,
            }

            for version in versions:

                # determine EESSI version in which this software version is installed
                req_mods = version['required_modules']
                if req_mods and req_mods[0].get('module_name') == 'EESSI':
                    eessi_versions.add(req_mods[0]['module_version'])

                # pick up on extensions included in this software installation (if any)
                for ext in version['extensions']:
                    ext_key = ext['type'] + ':' + ext['name']

                    # keep track of "parents" for this extension name (per extension version)
                    if ext_key in ext_parents:
                        parents = ext_parents[ext_key]
                    else:
                        parents = {}
                        ext_parents[ext_key] = parents
                        # new extension, so also add it to list of software
                        res['software'].append({
                            'is_extension': True,
                            'name': ext['name'],
                            'type': ext['type'],
                            'parents': parents,
                        })
                    parent = {'name': name, 'full_module_name': version['module']['full_module_name']}
                    parents.setdefault(ext['version'], []).append(parent)

            software['eessi_versions'] = ', '.join(sorted(eessi_versions))
            res['software'].append(software)

        res['software'] = sorted(res['software'], key=lambda x: x['name'].lower())

        # collect names of all parents per extension
        for ext in (x for x in res['software'] if x['is_extension']):
            ext['all_parent_names'] = set([y['name'] for x in ext['parents'].values() for y in x])

        res['n_extensions'] = len([x for x in res['software'] if x['is_extension']])

        print(f"[software overview] {res['n_software']=}, {res['n_extensions']=}")

        return res
