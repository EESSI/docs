---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: libcurl is a free and easy-to-use client-side URL transfer library,
    supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS,
    POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. libcurl supports
    SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload,
    proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate,
    Kerberos), file transfer resume, http proxy tunneling and more.
  license: Not confirmed
  name: cURL
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''cURL/7.86.0-GCCcore-12.2.0'', ''cURL/8.0.1-GCCcore-12.3.0'',
    ''cURL/8.3.0-GCCcore-13.2.0'']'
  url: https://curl.haxx.se
---

cURL
====


libcurl is a free and easy-to-use client-side URL transfer library, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos), file transfer resume, http proxy tunneling and more.

https://curl.haxx.se
# Available modules


The overview below shows which cURL installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using cURL, load one of these modules using a `module load` command like:

```shell
module load cURL/8.3.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|cURL/8.3.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|cURL/8.0.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|cURL/7.86.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
