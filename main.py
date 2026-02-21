# Macros implemented in Python that can be used in MarkDown files,
# see also https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
#
# author: Kenneth Hoste (Ghent University)
# license (SPDX): GPL-2.0-only
#
import json
import urllib.request
from pathlib import Path

EESSI_API_SOFTWARE_JSON_URL = 'https://www.eessi.io/api_data/data/eessi_api_metadata_software.json'

CPU_ARCHS = {
    'x86_64': ['AMD', 'Intel'],
    'aarch64': ['Arm'],
    'riscv64': ['RISC-V'],
}


def define_env(env):

    @env.macro
    def load_json_eessi_software():
        """
        Load JSON with metadata for software.eessi.io repository,
        and return Python dictionary with relevant info to generate software overview in EESSI documentation.
        """
        with urllib.request.urlopen(EESSI_API_SOFTWARE_JSON_URL) as response:
            data = json.loads(response.read().decode('utf-8'))

        data_software = data['software']
        names = data['software'].keys()

        res = {
            'timestamp': data['timestamp'],
            'n_software': len(names),
            'software': [],
            'extensions': {},
        }
        for name in sorted(names):
            name_data = data['software'][name]
            versions = name_data['versions']

            # use description is last version
            descr = ' '.join(versions[-1]['description'].strip().splitlines())
            descr = descr.replace('<', 'less than ').replace('>', 'more than ')

            # use all homepages
            homepages = set(x['homepage'].rstrip('/') for x in versions)
            homepages = ', '.join("<a href='%(h)s'>%(h)s</a>" % {'h': h} for h in homepages)

            licenses = ', '.join(y for x in versions for y in x['license'])

            # determine set of supported CPU families (first part of CPU target names, like x86_64 or aarch64)
            cpu_families = set(c for v in versions for x in v['cpu_arch'] for c in CPU_ARCHS[x.split('/')[0]])

            # EESSI versions in which this software is available
            eessi_versions = set()

            software = {
                'name': name,
                'homepages': homepages,
                'description': descr,
                'n_versions': len(versions),
                'licenses': licenses,
                'cpu_families': ', '.join(x for x in sorted(cpu_families)),
            }

            for version in versions:

                req_mods = version['required_modules']
                if req_mods and req_mods[0].get('module_name') == 'EESSI':
                    eessi_versions.add(req_mods[0]['module_version'])

                for ext in version['extensions']:
                    ext_key = ext['type'] + ':' + ext['name']
                    if ext_key in res['extensions']:
                        res['extensions'][ext_key]['parents'].add(name)
                    else:
                        res['extensions'][ext_key] = {
                            'name': ext['name'],
                            'type': ext['type'],
                            'parents': set([name]),
                        }

            software['eessi_versions'] = ', '.join(sorted(eessi_versions))

            res['software'].append(software)

        res['n_extensions'] = len(res['extensions'])

        return res
