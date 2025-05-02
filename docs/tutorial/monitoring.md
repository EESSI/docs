!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Monitoring CernVM-FS

There are multiple options available to automatize the monitoring of CVMFS clients (see [CVMFS Documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#monitoring) ):

- Nagios
- Telemetry Aggregator
- HTTP Tracing Header

## Nagios
!!! TODO

## Telemetry Aggregator

The [Telemetry Aggregator](https://cvmfs.readthedocs.io/en/stable/cpt-telemetry.html#cpt-telemetry) allows remote monitoring of the internal state of the client. These counters count access to internal data structures and number of errors, and can be accessed locally via `cvmfs_talk -i <repo> internal affairs`. The Telemetry Aggregator extends this data by also providing the timestamp of the counter collection, the current revision of the repository, and providing these counters in absolute values and delta values relative to the previous measurement. This e.g. allows monitoring if some clients fall behind in updating the repository to the latest revision.

By default, the data is sent in Influx data format. The Influx Telemetry Aggregator also allows defining custom user-defined, static tags and fields.
Other formats are possible but must be provided as a source code plugin.

To activate it the following lines need to be added to the client config (e.g. `/etc/cvmfs/default.local`):
```
CVMFS_TELEMETRY_SEND=ON
CVMFS_TELEMETRY_RATE=<rate in seconds> # minimum send rate >= 5 sec
CVMFS_INFLUX_HOST=localhost                 # IP address
CVMFS_INFLUX_PORT=8092                      # Port
CVMFS_INFLUX_METRIC_NAME=<measurement name> # "Table" name
CVMFS_INFLUX_EXTRA_TAGS="some_tag=42,some_tag2=27" # optional // tags are always sent
CVMFS_INFLUX_EXTRA_FIELDS="somefield=3"            # optional // fields are only sent in absolute data
```

## HTTP Tracing Header

CVMFS offers to add user-defined, static key-value pairs to the HTTP header for any of its client HTTP request. This includes download of uncached files, selection of proxy and servers (S0/S1).

For this the following lines need to be added to the client config (e.g. `/etc/cvmfs/default.local`):
```
CVMFS_HTTP_TRACING=on 
CVMFS_HTTP_TRACING_HEADERS='node:pn214|tag2:some_tag'
```

This results to the following header
```
(download) CURL Header for URL: /data/81/7c882d4a2e9dd7f9c5c2bfb4e04ff316e436dfC is:
Connection: Keep-Alive
Pragma:
User-Agent: cvmfs Fuse 2.12.6
X-CVMFS-node: pn214
X-CVMFS-tag2: some_tag
X-CVMFS-PID: 481270
X-CVMFS-GID: 0
X-CVMFS-UID: 0
```


