# Option 3: Ansible 

Start by cloning the EESSI filesystem-layer repo:

```bash
git clone https://github.com/EESSI/filesystem-layer.git
```

Make sure that the `inventory/hosts` file contains the list of hosts where the CVMFS client should be
installed. Furthermore, you can define a list of (local) proxy servers that your clients should use
in `inventory/local_site_specific_vars.yml` using the parameter `local_cvmfs_http_proxies`.  See
`inventory/local_site_specific_vars.yml.example` for more details. If you just want to roll out one
client without a proxy, you can leave this out.

Finally, install the client by running the playbook:

```bash
ansible-playbook -b -K -e @inventory/local_site_specific_vars.yml client.yml
```

