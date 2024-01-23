# Setting up a Stratum 1

Setting up a Stratum 1 involves the following steps:

- set up the Stratum 1, preferably by running the Ansible playbook that we provide;
- request a Stratum 0 firewall exception for your Stratum 1 server;
- request a `<your site>.stratum1.cvmfs.eessi-infra.org` DNS entry;
- open a pull request to include the URL to your Stratum 1 in the EESSI configuration.

The last two steps can be skipped if you want to host a "private" Stratum 1 for your site.


## Requirements for a Stratum 1

The main requirements for a Stratum 1 server are a good network connection to the clients it is going to serve,
and sufficient disk space. For the EESSI repository, a few hundred gigabytes should suffice, but for production
environments at least 1 TB would be recommended.

In terms of cores and memory, a machine with just a few (~4) cores and 4-8 GB of memory should suffice.

Various Linux distributions are supported, but we recommend one based on RHEL 7 or 8.

Finally, make sure that ports 80 (for the Apache web server) and 8000 are open.


## Step 1: set up the Stratum 1

The recommended way for setting up an EESSI Stratum 1 is by running the Ansible playbook `stratum1.yml`
from the [filesystem-layer repository on GitHub](https://github.com/EESSI/filesystem-layer).

Installing a Stratum 1 requires a GEO API license key, which will be used to find the (geographically) closest Stratum 1 server for your client and proxies.
More information on how to (freely) obtain this key is available in the CVMFS documentation: https://cvmfs.readthedocs.io/en/stable/cpt-replica.html#geo-api-setup.

You can put your license key in the local configuration file `inventory/local_site_specific_vars.yml`.

Furthermore, the Stratum 1 runs a Squid server. The template configuration file can be found at `templates/eessi_stratum1_squid.conf.j2`.
If you want to customize it, for instance for limiting the access to the Stratum 1, you can make your own version of this template file 
and point to it by setting `local_stratum1_cvmfs_squid_conf_src` in `inventory/local_site_specific_vars.yml`.
See the comments in the example file for more details.

Start by installing Ansible:

```bash
sudo yum install -y ansible
```

Then install Ansible roles for EESSI:

```bash
ansible-galaxy role install -r requirements.yml -p ./roles --force
```

Make sure you have enough space in `/srv` (on the Stratum 1) since the snapshot of the Stratum 0
will end up there by default. To alter the directory where the snapshot gets copied to you can add
this variable in `inventory/host_vars/<url-or-ip-to-your-stratum1>`:

```bash
cvmfs_srv_mount: /srv
```

Make sure that you have added the hostname or IP address of your server to the
`inventory/hosts` file. Finally, install the Stratum 1 by running the playbook:


``` bash
# -b to run as root, optionally use -K if a sudo password is required
ansible-playbook -b [-K] -e @inventory/local_site_specific_vars.yml stratum1.yml
```

Running the playbook will automatically make replicas of all the repositories defined in `group_vars/all.yml`.


## Step 2: request a firewall exception

(This step is not implemented yet and can be skipped)

You can request a firewall exception rule to be added for your Stratum 1 server by
[opening an issue on the GitHub page of the filesystem layer repository](https://github.com/EESSI/filesystem-layer/issues/new).

Make sure to include the IP address of your server.

## Step 3: Verification of the Stratum 1

When the playbook has finished your Stratum 1 should be ready. In order to test your Stratum 1, even
without a client installed, you can use `curl`.

```bash
curl --head http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io/.cvmfspublished
```
This should return:

```bash
HTTP/1.1 200 OK
...
X-Cache: MISS from <url-or-ip-to-your-stratum1>
```

The second time you run it, you should get a cache hit:

```bash
X-Cache: HIT from <url-or-ip-to-your-stratum1>

```

Example with the Norwegian Stratum 1:

```bash
curl --head http://bgo-no.stratum1.cvmfs.eessi-infra.org/cvmfs/software.eessi.io/.cvmfspublished
```

You can also test access to your Stratum 1 from a client, for which you will have to install the CVMFS
[client](https://github.com/EESSI/filesystem-layer#clients). 

Then run the following command to add your newly created Stratum 1 to the existing list of EESSI Stratum 1 servers by creating a local CVMFS configuration file:

```bash
echo 'CVMFS_SERVER_URL="http://<url-or-ip-to-your-stratum1>/cvmfs/@fqrn@;$CVMFS_SERVER_URL"' | sudo tee -a /etc/cvmfs/domain.d/eessi-hpc.org.local
```

If this is the first time you set up the client you now run:

```bash
sudo cvmfs_config setup
```

If you already had configured the client before, you can simply reload the config:

```bash
sudo cvmfs_config reload -c software.eessi.io
```

Finally, verify that the client connects to your new Stratum 1 by running:

```bash
cvmfs_config stat -v software.eessi.io
```

Assuming that your new Stratum 1 is the geographically closest one to your client, this should return:

```bash
Connection: http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io through proxy DIRECT (online)
```


## Step 4: request an EESSI DNS name

In order to keep the configuration clean and easy, all the EESSI Stratum 1 servers have a DNS name
`<your site>.stratum1.cvmfs.eessi-infra.org`, where `<your site>` is often a short name or
abbreviation followed by the country code (e.g. `rug-nl` or `bgo-no`).  You can request this for
your Stratum 1 by mentioning this in the issue that you created in Step 2, or by opening another
issue.

## Step 5: include your Stratum 1 in the EESSI configuration

If you want to include your Stratum 1 in the EESSI configuration, i.e. allow any (nearby) client to be able to use it,
you can open a pull request with updated configuration files. You will only have to add the URL to your Stratum 1 to the 
`urls` list of the `eessi_cvmfs_server_urls` variable in the
[`all.yml` file](https://github.com/EESSI/filesystem-layer/blob/main/inventory/group_vars/all.yml).
