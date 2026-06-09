---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n libcurl is a free and easy-to-use client-side URL transfer library,\n\
    \ supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP,\n\
    \ LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP.\n libcurl\
    \ supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP\n form based\
    \ upload, proxies, cookies, user+password authentication (Basic,\n Digest, NTLM,\
    \ Negotiate, Kerberos), file transfer resume, http proxy tunneling\n and more.\n"
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
  softwareVersion: '[''8.14.1'', ''8.11.1'']'
  url: https://curl.haxx.se
---
# cURL



 libcurl is a free and easy-to-use client-side URL transfer library,
 supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP,
 LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP.
 libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP
 form based upload, proxies, cookies, user+password authentication (Basic,
 Digest, NTLM, Negotiate, Kerberos), file transfer resume, http proxy tunneling
 and more.


<small>homepage: </small><span class="software-link">[https://curl.haxx.se](https://curl.haxx.se)</span>

## Available installations


|cURL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|8.14.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cURL/8.14.1-GCCcore-14.3.0`|
|8.11.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cURL/8.11.1-GCCcore-14.2.0`|