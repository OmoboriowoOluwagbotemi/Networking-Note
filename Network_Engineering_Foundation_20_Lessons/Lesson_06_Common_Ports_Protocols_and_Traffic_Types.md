# LESSON 6: COMMON PORTS, PROTOCOLS, AND TRAFFIC TYPES

## TRAINING FOCUS

This lesson is part of the FEMTECT Network Engineering Foundation course. It is written to help students build strong networking fundamentals through clear explanations, real enterprise context, practical troubleshooting logic, and certification-aware technical depth.


## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 6.1 Ports, Protocols, and Traffic Types

Ports, protocols, and traffic types describe what kind of network communication is happening between devices. In Lesson 5, TCP and UDP were explained as Transport layer protocols that use port numbers to deliver traffic to the correct application or service. Lesson 6 focuses on the common ports and protocols that IT support technicians, network engineers, cybersecurity analysts, and exam candidates must recognize.

A protocol is a set of rules that controls how a service communicates. HTTP defines how web clients and web servers exchange web content. DNS defines how names are translated into IP addresses. SMTP defines how email is sent between mail systems. SSH defines secure remote command-line access.

A port number identifies a specific service or application on a device. An IP address gets traffic to the correct host, but a port number gets traffic to the correct service on that host. For example, a server may have one IP address but run HTTPS on TCP port `443`, SSH on TCP port `22`, DNS on UDP/TCP port `53`, and RDP on TCP port `3389`. The destination port tells the server which service should receive the traffic.

A traffic type describes the general purpose or behavior of the communication. Web traffic, email traffic, file-transfer traffic, remote-administration traffic, voice traffic, database traffic, logging traffic, monitoring traffic, and name-resolution traffic are examples of traffic types. Understanding traffic types helps engineers design firewall rules, troubleshoot application failures, identify suspicious activity, and prioritize important services.

### 6.2 Technical Importance: Ports and Protocols Matter

Ports and protocols matter because firewalls, servers, clients, load balancers, proxies, intrusion detection systems, and cloud security groups use them to control and inspect traffic. If the correct port is blocked, the application may fail even when IP routing is working. If the wrong protocol is allowed, the network may be exposed to unnecessary risk.

For example, a server may respond to ping but still fail to load a website because TCP port `443` is blocked. A client may have Internet access but fail to resolve names because UDP port `53` is blocked. A remote administrator may fail to connect because SSH on TCP port `22` is disabled or blocked. A Windows file share may fail because SMB on TCP port `445` is filtered. A VoIP system may register but calls may fail because SIP or RTP-related traffic is blocked.

Ports also matter for cybersecurity. Attackers scan ports to discover exposed services. Insecure protocols such as Telnet and FTP can expose credentials in clear text. Open database ports can expose sensitive systems if they are reachable from untrusted networks. Remote access ports such as RDP must be protected carefully because they are common targets for brute-force attacks and exploitation.

For CCNA and CompTIA Network+, students must know the common protocols, default ports, transport protocol, secure alternatives, and troubleshooting relevance. Memorizing port numbers is useful, but professional competence requires understanding what each protocol does and what failure looks like.

### 6.3 Well-Known, Registered, and Dynamic Ports

TCP and UDP port numbers range from `0` to `65535`. These numbers are divided into categories.

Well-known ports range from `0` to `1023`. They are commonly used by standard network services such as FTP, SSH, Telnet, SMTP, DNS, DHCP, HTTP, HTTPS, POP3, IMAP, LDAP, SMB, and others. These are important for exams and troubleshooting because they appear frequently in real networks.

Registered ports range from `1024` to `49151`. They are used by many vendor applications, databases, management tools, and services. SQL Server on TCP port `1433` and RDP on TCP port `3389` are common examples.

Dynamic or ephemeral ports range from `49152` to `65535` in many modern systems, although the exact ephemeral range can vary by operating system. Clients often use temporary source ports from this range when connecting to servers. For example, a client may connect from source port `52000` to a web server destination port `443`.

Port Ranges

| Port Range | Name | Common Use |
|---|---|---|
| 0-1023 | Well-known ports | Standard services |
| 1024-49151 | Registered ports | Vendor and application services |
| 49152-65535 | Dynamic/ephemeral ports | Temporary client source ports |

Important Point

Servers usually listen on known destination ports. Clients usually connect from temporary source ports. When troubleshooting, always ask whether you are looking at the source port or the destination port.

## 6.4 FILE TRANSFER PROTOCOLS

### FTP - File Transfer Protocol

FTP, or File Transfer Protocol, is used to transfer files between a client and a server. It commonly uses TCP port `21` for control traffic and TCP port `20` for data traffic in active mode. FTP is one of the older file transfer protocols.

FTP exists because users and systems often need to upload and download files across a network. Before modern cloud storage platforms and secure web portals became common, FTP was widely used for website file uploads, software repositories, backups, and system-to-system file transfers.

Technically, FTP separates control and data connections. The control connection handles commands such as login, directory listing, upload, and download. The data connection transfers the actual file data. FTP can operate in active mode or passive mode, which affects how data connections are established. Passive FTP is common when clients are behind firewalls or NAT.

The major weakness of traditional FTP is security. FTP sends usernames, passwords, and data in clear text unless protected by additional security mechanisms. For this reason, secure alternatives such as SFTP, FTPS, HTTPS-based file portals, or secure managed file transfer systems are preferred in enterprise environments.

FTP Characteristics

- Transfers files between client and server.
- Uses TCP.
- Common control port is TCP `21`.
- Data behavior may involve TCP `20` or passive-mode ports.
- Sends data and credentials in clear text by default.
- Should not be used for sensitive data without protection.

FTP Troubleshooting Clues

- Login works but file transfer fails: check passive-mode ports and firewall rules.
- FTP works internally but fails externally: check NAT and firewall inspection.
- Credentials exposed: replace plain FTP with secure alternatives.
- Connection timeout: check server listening state and TCP port `21`.

### TFTP - Trivial File Transfer Protocol

TFTP, or Trivial File Transfer Protocol, is a simple file transfer protocol that uses UDP port `69`. It is much simpler than FTP and does not provide authentication, encryption, directory browsing, or advanced session control.

TFTP exists because some network devices need a lightweight way to transfer configuration files, firmware images, boot files, or small system files. Cisco devices and other network equipment have historically used TFTP for backing up configurations or loading IOS images in lab and controlled environments.

Technically, TFTP uses UDP and is connectionless. It is easy to implement, but it is not secure. Because TFTP has no authentication or encryption, it should be used only on trusted management networks or lab environments.

TFTP Characteristics

- Simple file transfer protocol.
- Uses UDP port `69`.
- No authentication by default.
- No encryption.
- Commonly used for network device images and configurations.
- Suitable for controlled environments, not public exposure.

TFTP Troubleshooting Clues

- If transfer fails, check UDP port `69`.
- Check whether the TFTP server has file permissions set correctly.
- Check whether the network device can reach the TFTP server.
- Check local firewall settings on the TFTP server.
- Avoid using TFTP over untrusted networks.

## 6.5 REMOTE ADMINISTRATION PROTOCOLS

### SSH - Secure Shell

SSH, or Secure Shell, is used for secure remote command-line administration. It commonly uses TCP port `22`. SSH encrypts the communication between client and server, protecting usernames, passwords, commands, and output from being read in clear text.

SSH exists because administrators need a secure way to manage servers, routers, switches, firewalls, and Linux systems remotely. In enterprise networks, SSH is preferred over Telnet because it provides encryption and stronger authentication options.

Technically, SSH can support password authentication, public-key authentication, secure tunneling, secure file copy, and command execution. Network engineers commonly use SSH to manage Cisco IOS devices. Linux administrators use SSH to manage servers. Cloud engineers use SSH to access virtual machines.

SSH Characteristics

- Secure remote command-line access.
- Uses TCP port `22`.
- Encrypts traffic.
- Supports password and key-based authentication.
- Preferred for device hardening.
- Replaces Telnet in professional environments.

SSH Troubleshooting Clues

- If ping works but SSH fails, test TCP port `22`.
- Check whether SSH service is enabled.
- Check username, password, keys, and access control.
- Check firewall or ACL rules.
- On Cisco devices, confirm domain name, username, VTY configuration, and crypto keys.

### Telnet

Telnet is an older remote command-line protocol that commonly uses TCP port `23`. It allows administrators to connect to devices and issue commands remotely, but it sends traffic in clear text.

Telnet exists historically because it provided simple remote terminal access before secure alternatives became standard. Today, Telnet should generally be avoided in production networks because usernames, passwords, and commands can be captured by anyone who can sniff the traffic.

Telnet may still appear in labs, legacy systems, industrial environments, or troubleshooting tests, but it is not recommended for secure administration. Modern device hardening requires SSH instead of Telnet.

Telnet Characteristics

- Remote command-line access.
- Uses TCP port `23`.
- Sends credentials and commands in clear text.
- Insecure for production use.
- Replaced by SSH in secure environments.

Telnet Troubleshooting and Security Notes

- If Telnet is enabled on a network device, it should usually be disabled.
- If a legacy device requires Telnet, restrict access using ACLs and management VLANs.
- Use SSH wherever possible.
- Telnet can be used as a simple TCP port test tool, but this does not mean Telnet service should be enabled.

### RDP - Remote Desktop Protocol

RDP, or Remote Desktop Protocol, is used for graphical remote access to Windows systems. It commonly uses TCP port `3389` and may also use UDP `3389` for performance improvements in modern implementations.

RDP exists because administrators and users often need to access a full Windows desktop remotely. It is common in server administration, remote support, jump servers, and virtual desktop environments.

RDP is powerful but risky if exposed carelessly. Publicly exposed RDP is a common target for brute-force attacks, credential theft, and exploitation. Enterprises should protect RDP using VPN, zero-trust access, multi-factor authentication, jump hosts, account lockout policies, and firewall restrictions.

RDP Characteristics

- Graphical remote access.
- Commonly uses TCP `3389`.
- May use UDP `3389`.
- Common for Windows administration.
- High-risk if exposed to the public Internet.

RDP Troubleshooting Clues

- Check whether Remote Desktop is enabled on the target.
- Test TCP port `3389`.
- Check Windows Firewall.
- Check user permission to log in remotely.
- Check Network Level Authentication settings.
- Never expose RDP directly to the Internet without strong protections.

## 6.6 EMAIL PROTOCOLS

### SMTP - Simple Mail Transfer Protocol

SMTP, or Simple Mail Transfer Protocol, is used to send email. It commonly uses TCP port `25` for server-to-server mail transfer. Submission from clients to mail servers often uses TCP port `587`, and secure SMTP over implicit TLS historically uses TCP port `465`.

SMTP exists because email systems need a standard way to transfer messages between mail servers and accept outgoing mail from authenticated users. When a user sends an email, the message is submitted to a mail server, and that server may use SMTP to deliver it to another mail server.

Technically, SMTP is a mail sending protocol, not a mail retrieval protocol. Users typically retrieve mail using IMAP, POP3, or webmail, but those are outside the specific Lesson 6 list. SMTP is central to email flow and troubleshooting.

SMTP Characteristics

- Sends email.
- Uses TCP.
- TCP `25` is common for server-to-server mail transfer.
- TCP `587` is common for authenticated mail submission.
- TCP `465` is commonly associated with SMTPS.
- Requires proper DNS records such as MX, SPF, DKIM, and DMARC in real email environments.

SMTP Troubleshooting Clues

- If email cannot send, test SMTP submission settings.
- Check authentication and TLS settings.
- Check firewall rules for TCP `25`, `587`, or `465`.
- Check spam filtering, relay restrictions, and DNS records.
- Many ISPs block outbound TCP `25` from residential or untrusted networks to reduce spam.

### SMTPS

SMTPS refers to SMTP protected with SSL/TLS, commonly associated with TCP port `465`. In modern email, SMTP submission often uses STARTTLS on TCP port `587`, but TCP `465` is still widely recognized as SMTPS in port memorization and many configurations.

The purpose of SMTPS is to protect email submission by encrypting the connection between the mail client and the mail server. This helps prevent credentials and message content from being exposed in transit.

SMTPS Characteristics

- Secure SMTP variant.
- Commonly associated with TCP `465`.
- Encrypts SMTP communication.
- Used for secure mail submission in many environments.
- Must be configured with valid certificates and supported TLS versions.

SMTPS Troubleshooting Clues

- Check port `465`.
- Check TLS certificate trust.
- Check username and password.
- Check mail client encryption settings.
- If port `465` fails, verify whether the server expects STARTTLS on port `587` instead.

## 6.7 NAME, ADDRESSING, AND AUTOMATIC CONFIGURATION PROTOCOLS

### DNS - Domain Name System

DNS, or Domain Name System, translates human-readable names into IP addresses and supports many other naming records. DNS commonly uses UDP port `53` for normal queries and TCP port `53` for zone transfers and larger responses. Modern DNS can also use encrypted variants such as DNS over HTTPS or DNS over TLS, but traditional DNS port `53` remains foundational.

DNS exists because humans prefer names such as `www.example.com`, while networks use IP addresses. Without DNS, users would need to remember IP addresses for websites, servers, applications, and services.

DNS is one of the most important services in enterprise networking. If DNS fails, users may report that "the Internet is down" even when IP routing is working. Internal applications, Active Directory, email, cloud services, and security tools often depend heavily on DNS.

DNS Characteristics

- Translates names to IP addresses.
- Uses UDP `53` for many queries.
- Uses TCP `53` for zone transfers and large responses.
- Critical for web, email, authentication, and cloud services.
- Failure often looks like application or Internet failure.

DNS Troubleshooting Clues

- If ping to IP works but names fail, check DNS.
- Use `nslookup`, `dig`, or `Resolve-DnsName`.
- Check configured DNS server.
- Check firewall rules for UDP/TCP `53`.
- Check whether the record exists and points to the correct address.

### DHCP - Dynamic Host Configuration Protocol

DHCP automatically assigns IP configuration to network devices. It commonly uses UDP port `67` for the DHCP server and UDP port `68` for the DHCP client in IPv4.

DHCP exists because manually configuring IP addresses on every device is inefficient and error-prone. DHCP can assign IP address, subnet mask, default gateway, DNS servers, lease time, and other options.

Technically, DHCP uses a process often remembered as DORA: Discover, Offer, Request, Acknowledge. This process will be explained deeply in Lesson 19. In this lesson, students should understand DHCP as the service that gives clients their network settings.

DHCP Characteristics

- Automatically assigns IP settings.
- Uses UDP `67` for server.
- Uses UDP `68` for client.
- Reduces manual configuration.
- Essential in enterprise client networks.
- Can require DHCP relay or IP helper across routed networks.

DHCP Troubleshooting Clues

- If a Windows client has `169.254.x.x`, DHCP may have failed.
- Check whether the DHCP scope has available addresses.
- Check VLAN and DHCP relay configuration.
- Check firewall rules for DHCP traffic.
- Check whether rogue DHCP servers are present.

## 6.8 WEB PROTOCOLS

### HTTP - Hypertext Transfer Protocol

HTTP, or Hypertext Transfer Protocol, is used for web communication. It commonly uses TCP port `80`. HTTP allows browsers and web clients to request web pages, APIs, images, files, and other content from web servers.

HTTP exists because users and applications need a standard way to request and receive web resources. Many websites, APIs, dashboards, portals, and web-based applications are built around HTTP behavior.

The major weakness of plain HTTP is that it is not encrypted. Data can be read or modified in transit by an attacker with access to the traffic path. For this reason, HTTPS is preferred for almost all modern web communication.

HTTP Characteristics

- Web communication protocol.
- Uses TCP port `80`.
- Not encrypted by default.
- Used for websites, APIs, and web services.
- Often redirected to HTTPS.

HTTP Troubleshooting Clues

- Test TCP port `80`.
- Check web server service status.
- Check proxy or firewall policy.
- Check HTTP response codes.
- If sensitive data is involved, use HTTPS instead.

### HTTPS - Hypertext Transfer Protocol Secure

HTTPS is HTTP secured using TLS encryption. It commonly uses TCP port `443`. HTTPS protects confidentiality and integrity and helps authenticate the server using digital certificates.

HTTPS exists because web communication often carries sensitive information such as passwords, financial data, personal records, business documents, cookies, and application tokens. Encryption helps prevent eavesdropping and tampering.

Technically, HTTPS uses TLS to encrypt the communication between client and server. The client validates the server certificate, negotiates encryption settings, and then exchanges encrypted HTTP data.

HTTPS Characteristics

- Secure web communication.
- Uses TCP port `443`.
- Encrypts traffic using TLS.
- Uses certificates.
- Standard for modern websites and APIs.
- Required for secure login pages and sensitive applications.

HTTPS Troubleshooting Clues

- If ping works but HTTPS fails, test TCP `443`.
- Check firewall, proxy, or load balancer rules.
- Check certificate expiration and hostname match.
- Check TLS version support.
- Check web server and application logs.

## 6.9 TIME, MONITORING, DIRECTORY, AND LOGGING PROTOCOLS

### NTP - Network Time Protocol

NTP synchronizes time across network devices and systems. It commonly uses UDP port `123`.

NTP exists because accurate time is critical for logs, authentication, certificates, Kerberos, troubleshooting, compliance, event correlation, and security investigations. If devices have different times, logs become confusing and authentication may fail.

In enterprise networks, routers, switches, servers, firewalls, domain controllers, cloud systems, and endpoints should synchronize time from trusted sources.

NTP Characteristics

- Synchronizes system time.
- Uses UDP port `123`.
- Important for logs and authentication.
- Supports troubleshooting and security investigations.
- Should use trusted time sources.

NTP Troubleshooting Clues

- Check whether devices have correct time.
- Check UDP `123`.
- Check time zone and NTP source.
- Check firewall rules.
- For authentication issues, verify clock skew.

### SNMP - Simple Network Management Protocol

SNMP is used for monitoring and managing network devices. It commonly uses UDP port `161` for queries and UDP port `162` for traps or notifications.

SNMP exists because administrators need visibility into device health, interface status, bandwidth usage, CPU, memory, errors, and alerts. Monitoring systems use SNMP to collect information from routers, switches, firewalls, servers, printers, UPS devices, and other infrastructure.

Older SNMP versions such as SNMPv1 and SNMPv2c use community strings and do not provide strong security. SNMPv3 supports authentication and encryption and is preferred in secure environments.

SNMP Characteristics

- Used for monitoring and management.
- Uses UDP `161` for polling.
- Uses UDP `162` for traps.
- Common on routers, switches, servers, printers, and UPS systems.
- SNMPv3 is preferred for security.

SNMP Troubleshooting Clues

- Check community string or SNMPv3 credentials.
- Check ACLs allowing the monitoring server.
- Check UDP `161` and `162`.
- Check whether SNMP is enabled on the device.
- Check monitoring server configuration.

### LDAP - Lightweight Directory Access Protocol

LDAP is used to access and query directory services. It commonly uses TCP and UDP port `389`. Directory services store information about users, groups, computers, printers, permissions, and organizational objects.

LDAP exists because organizations need centralized identity and directory lookup. Microsoft Active Directory uses LDAP as one of its important access protocols. Applications may use LDAP to authenticate users or look up user information.

Plain LDAP is not encrypted by default. Sensitive directory communication should use LDAPS or LDAP with StartTLS where supported.

LDAP Characteristics

- Directory access protocol.
- Uses TCP/UDP `389`.
- Common with Active Directory and identity systems.
- Used by applications for authentication and lookup.
- Plain LDAP should be protected in secure environments.

LDAP Troubleshooting Clues

- Check domain controller or directory server reachability.
- Check TCP/UDP `389`.
- Check bind credentials.
- Check DNS records for domain controllers.
- Check time synchronization in Active Directory environments.

### LDAPS

LDAPS is LDAP over TLS/SSL. It commonly uses TCP port `636`. It protects directory communication by encrypting traffic between the client and directory server.

LDAPS exists because directory queries and authentication-related communication may contain sensitive information. Encryption helps protect credentials and directory data from interception.

LDAPS Characteristics

- Secure LDAP.
- Uses TCP `636`.
- Encrypts directory communication.
- Requires valid certificates.
- Common in secure identity integrations.

LDAPS Troubleshooting Clues

- Test TCP `636`.
- Check certificate trust and expiration.
- Check hostname match.
- Check directory server configuration.
- Check application bind settings.

### Syslog

Syslog is used to send log messages from devices and systems to a centralized logging server. It commonly uses UDP port `514`, though TCP `514` and TLS-secured syslog may also be used in some environments.

Syslog exists because administrators and security teams need centralized visibility. Routers, switches, firewalls, Linux servers, appliances, and applications can send logs to a syslog server for monitoring, troubleshooting, compliance, and incident investigation.

Traditional UDP syslog is simple but does not guarantee delivery. Critical environments may use TCP or TLS-based logging when supported.

Syslog Characteristics

- Sends logs to a central server.
- Commonly uses UDP `514`.
- May use TCP `514` or TLS variants.
- Important for troubleshooting and security monitoring.
- Common on network devices and Linux systems.

Syslog Troubleshooting Clues

- Check whether device logging is configured.
- Check syslog server IP address.
- Check UDP/TCP `514`.
- Check firewall rules.
- Check timestamps and NTP synchronization.

## 6.10 FILE SHARING, DATABASE, AND VOICE PROTOCOLS

### SMB - Server Message Block

SMB is used for file sharing, printer sharing, and other network resource access, especially in Windows environments. Modern SMB commonly uses TCP port `445`.

SMB exists because users and systems need shared access to files, folders, printers, and named resources. Windows file shares, mapped drives, and many enterprise file services rely on SMB.

SMB has had serious security history, especially when exposed to untrusted networks. SMB should not be exposed directly to the public Internet. It should be protected with segmentation, firewall rules, patching, access control, and secure versions.

SMB Characteristics

- File and printer sharing.
- Uses TCP `445`.
- Common in Windows networks.
- Supports mapped drives and file shares.
- Should be restricted to trusted networks.

SMB Troubleshooting Clues

- Test TCP `445`.
- Check file share permissions.
- Check NTFS permissions.
- Check Windows Firewall.
- Check DNS name resolution.
- Check whether SMB is blocked between VLANs.

### SQL Server

Microsoft SQL Server commonly uses TCP port `1433` for database connections. SQL Server is used by many business applications to store and retrieve structured data.

SQL Server traffic exists because applications need database services. A user may not connect to SQL Server directly, but the application they use may depend on it. If the database connection fails, the application may fail even when the web server is reachable.

Database ports should be protected carefully. SQL Server should not be exposed broadly to untrusted networks. Access should be limited to application servers, administrators, and approved systems.

SQL Server Characteristics

- Database service.
- Commonly uses TCP `1433`.
- Used by business applications.
- Requires authentication and authorization.
- Should be restricted by firewall and segmentation.

SQL Server Troubleshooting Clues

- Test TCP `1433`.
- Check SQL Server service status.
- Check database listener configuration.
- Check firewall and security group rules.
- Check application connection strings.
- Check database authentication and permissions.

### SIP - Session Initiation Protocol

SIP is used to establish, manage, and terminate voice and video communication sessions. It commonly uses TCP or UDP port `5060` for unencrypted SIP and TCP `5061` for SIP over TLS.

SIP exists because IP phones, softphones, call managers, and voice systems need a standard way to set up calls. SIP usually handles call signaling, while the actual voice media often uses RTP on separate dynamic UDP ports.

Technically, SIP does not carry all voice audio by itself. SIP sets up the call, negotiates session details, and coordinates endpoints. RTP commonly carries the media stream. This distinction matters during troubleshooting because call setup may work while audio fails.

SIP Characteristics

- Voice and video signaling protocol.
- Uses TCP/UDP `5060`.
- SIP over TLS commonly uses TCP `5061`.
- Often works with RTP for audio/video media.
- Sensitive to NAT, firewall, latency, jitter, and packet loss.

SIP Troubleshooting Clues

- If phones fail to register, check SIP server reachability and port `5060` or `5061`.
- If calls connect but there is no audio, check RTP/media paths and firewall rules.
- Check NAT traversal settings.
- Check voice VLAN and QoS.
- Check latency, jitter, and packet loss.

## 6.11 TRAFFIC TYPES IN ENTERPRISE NETWORKS

Traffic types help engineers understand what the network is carrying and how it should be treated. Not all traffic has the same business importance or behavior.

Web traffic includes HTTP and HTTPS. It is common, user-facing, and often filtered through proxies or firewalls. Email traffic includes SMTP and secure mail submission. File traffic includes FTP, TFTP, SMB, and cloud file synchronization. Management traffic includes SSH, SNMP, Syslog, and sometimes RDP. Directory traffic includes LDAP and LDAPS. Database traffic includes SQL Server. Voice signaling includes SIP, while voice media often uses RTP. Infrastructure traffic includes DNS, DHCP, and NTP.

Traffic classification matters for security and performance. Guest Wi-Fi users should not reach SMB file shares or SQL servers. Voice traffic may need QoS to reduce delay and jitter. Management traffic should be restricted to administrators and management networks. Logging traffic should reliably reach monitoring systems. DNS and DHCP must be available for basic network operation.

Enterprise Traffic Categories

| Traffic Type | Example Protocols | Enterprise Importance |
|---|---|---|
| Web | HTTP, HTTPS | User access to web apps and cloud services |
| Email | SMTP, SMTPS | Business communication |
| Name/Address Services | DNS, DHCP | Basic network operation |
| File Transfer/Sharing | FTP, TFTP, SMB | Files, configs, shared storage |
| Remote Administration | SSH, RDP, Telnet | Device and server management |
| Monitoring/Logging | SNMP, Syslog, NTP | Visibility, time, alerts, investigations |
| Directory/Identity | LDAP, LDAPS | Authentication and user lookup |
| Database | SQL Server | Application data storage |
| Voice/Video Signaling | SIP | Call setup and unified communications |

## 6.12 SECURITY: SECURE VS INSECURE PROTOCOLS

Some protocols were designed before modern security expectations. They may send credentials or data in clear text. In professional networks, insecure protocols should be replaced, restricted, or protected.

Insecure protocols include Telnet, FTP, TFTP, plain HTTP, and plain LDAP when sensitive data is involved. These protocols may still exist in labs, legacy systems, or controlled management networks, but they should not be exposed broadly.

Secure or safer alternatives include SSH instead of Telnet, SFTP or FTPS instead of FTP, HTTPS instead of HTTP, LDAPS instead of LDAP, SNMPv3 instead of SNMPv1/v2c, and secure mail submission using TLS instead of unprotected SMTP authentication.

Secure vs Insecure Protocols

| Insecure / Higher Risk | Safer Alternative | Reason |
|---|---|---|
| Telnet | SSH | SSH encrypts remote administration |
| FTP | SFTP / FTPS / HTTPS portal | Protects credentials and files |
| TFTP | Secure file transfer or restricted management network | TFTP has no authentication or encryption |
| HTTP | HTTPS | HTTPS encrypts web traffic |
| LDAP | LDAPS or StartTLS | Protects directory communication |
| SNMPv1/v2c | SNMPv3 | Supports authentication and encryption |

Cybersecurity Reminder

Open ports increase attack surface. A service should be reachable only by the users, devices, and networks that need it. Firewalls, ACLs, segmentation, VPNs, MFA, patching, logging, and secure configuration are all part of protocol security.

## 6.13 TROUBLESHOOTING WITH PORTS AND PROTOCOLS

When an application fails, do not only ask whether the server is reachable. Ask whether the correct service port is reachable and whether the correct protocol is allowed.

If ping works but the application fails, Layer 3 reachability may be working while Layer 4 or Layer 7 is failing. If DNS resolution fails, test UDP/TCP `53`. If a secure website fails, test TCP `443`. If SSH fails, test TCP `22`. If Windows file sharing fails, test TCP `445`. If RDP fails, test TCP `3389`. If DHCP fails, check UDP `67` and `68`, VLANs, and DHCP relay. If logs are missing, check Syslog and NTP. If monitoring fails, check SNMP credentials and UDP `161`.

Windows Commands

```powershell
Test-NetConnection <server> -Port 443
nslookup <name>
Resolve-DnsName <name>
netstat -ano
ipconfig /all
```

Linux Commands

```bash
ss -tulnp
nc -vz <server> 443
dig <name>
curl -I https://example.com
```

Cisco IOS Commands

```text
show access-lists
show running-config
show ip interface brief
ping <destination>
traceroute <destination>
```

Troubleshooting Rule

Successful ping does not prove the application works. Ping tests ICMP reachability. Applications depend on specific TCP or UDP ports, server processes, authentication, certificates, and security rules.

## 6.14 CLOUD NETWORKING RELEVANCE

Cloud platforms use ports and protocols heavily. Security groups, network security groups, cloud firewalls, load balancer listeners, container ingress rules, Kubernetes services, and private endpoints all depend on protocol and port decisions.

For example, an Azure Network Security Group may allow TCP `443` to a web application but block TCP `3389` to protect virtual machines. An AWS security group may allow TCP `22` only from an administrator's public IP address. A cloud load balancer may listen on TCP `443` and forward traffic to backend servers on TCP `8080`. A managed database may allow TCP `1433` only from application subnets.

Cloud troubleshooting often begins with the same questions: What protocol is being used? What destination port is required? Is the service listening? Is the security group allowing it? Is the route table correct? Is the load balancer health check passing? Is DNS pointing to the correct endpoint?

Cloud Reminder

Cloud networking does not remove ports and protocols. It makes them policy-driven and often software-defined.

## 7. COMMON PORTS MASTER TABLE

| Protocol | Port(s) | Transport | Main Purpose | Security Note |
|---|---:|---|---|---|
| FTP | 20/21 | TCP | File transfer | Insecure by default |
| SSH | 22 | TCP | Secure remote administration | Preferred over Telnet |
| Telnet | 23 | TCP | Remote administration | Insecure clear text |
| SMTP | 25 | TCP | Mail transfer between servers | Often restricted to reduce spam |
| DNS | 53 | UDP/TCP | Name resolution | Critical infrastructure service |
| DHCP | 67/68 | UDP | Automatic IP configuration | Watch for rogue DHCP |
| TFTP | 69 | UDP | Simple file transfer | No authentication/encryption |
| HTTP | 80 | TCP | Web traffic | Not encrypted |
| NTP | 123 | UDP | Time synchronization | Important for logs and authentication |
| SNMP | 161/162 | UDP | Monitoring and traps | Use SNMPv3 where possible |
| LDAP | 389 | TCP/UDP | Directory access | Use LDAPS/StartTLS for sensitive traffic |
| HTTPS | 443 | TCP | Secure web traffic | Uses TLS certificates |
| SMB | 445 | TCP | File and printer sharing | Do not expose to Internet |
| Syslog | 514 | UDP/TCP | Centralized logging | UDP is common but not guaranteed |
| SMTPS | 465 | TCP | Secure SMTP | Check server expectations |
| LDAPS | 636 | TCP | Secure directory access | Requires certificates |
| SQL Server | 1433 | TCP | Microsoft SQL database | Restrict to application/admin hosts |
| RDP | 3389 | TCP/UDP | Remote Windows desktop | Protect with VPN/MFA/restrictions |
| SIP | 5060/5061 | TCP/UDP | Voice/video signaling | Media often uses RTP separately |

## 8. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Port Number | Transport layer identifier used to deliver traffic to a service or application. |
| Protocol | A rule set that defines how a network service communicates. |
| Traffic Type | A category of communication such as web, email, voice, database, or management traffic. |
| Well-Known Port | Port from 0 to 1023 commonly assigned to standard services. |
| Registered Port | Port from 1024 to 49151 used by applications and vendors. |
| Ephemeral Port | Temporary client-side source port used for outbound connections. |
| FTP | File Transfer Protocol for transferring files. |
| SSH | Secure Shell for encrypted remote administration. |
| Telnet | Insecure remote terminal protocol. |
| SMTP | Simple Mail Transfer Protocol for sending email. |
| DNS | Domain Name System for name resolution. |
| DHCP | Dynamic Host Configuration Protocol for automatic IP settings. |
| TFTP | Trivial File Transfer Protocol for simple file transfer. |
| HTTP | Web protocol without encryption by default. |
| HTTPS | HTTP protected with TLS encryption. |
| NTP | Network Time Protocol for time synchronization. |
| SNMP | Simple Network Management Protocol for monitoring. |
| LDAP | Lightweight Directory Access Protocol for directory services. |
| LDAPS | LDAP protected with TLS. |
| SMB | Server Message Block for file and printer sharing. |
| Syslog | Protocol for sending log messages to a central server. |
| SQL Server | Microsoft database service commonly using TCP 1433. |
| RDP | Remote Desktop Protocol for graphical Windows remote access. |
| SIP | Session Initiation Protocol for voice/video signaling. |

## 9. COMPARISON TABLES

### 9.1 Secure vs Insecure Alternatives

| Insecure Protocol | Port | Secure Alternative | Port |
|---|---:|---|---:|
| Telnet | 23 | SSH | 22 |
| HTTP | 80 | HTTPS | 443 |
| LDAP | 389 | LDAPS | 636 |
| FTP | 20/21 | SFTP/FTPS/HTTPS-based transfer | 22/990/443 depending on design |
| SNMPv1/v2c | 161/162 | SNMPv3 | 161/162 |

### 9.2 TCP vs UDP Services

| Transport | Common Protocols | Typical Behavior |
|---|---|---|
| TCP | FTP, SSH, Telnet, SMTP, HTTP, HTTPS, SMB, SMTPS, LDAPS, SQL Server, RDP | Connection-oriented services where reliable delivery matters |
| UDP | DHCP, TFTP, NTP, SNMP, Syslog, many DNS queries, many SIP deployments | Low-overhead services, discovery, monitoring, time, voice signaling |
| TCP and UDP | DNS, LDAP, SIP, RDP in modern implementations | Protocols or platforms that may use both depending on function |

### 9.3 Troubleshooting by Symptom

| Symptom | Protocol/Port to Check |
|---|---|
| Website does not open securely | HTTPS TCP 443 |
| Website redirects or insecure web app fails | HTTP TCP 80 |
| Cannot resolve names | DNS UDP/TCP 53 |
| Client receives APIPA address | DHCP UDP 67/68 |
| Cannot SSH to device | SSH TCP 22 |
| Windows file share fails | SMB TCP 445 |
| Remote Desktop fails | RDP TCP/UDP 3389 |
| Email cannot send | SMTP/SMTPS TCP 25, 587, 465 |
| Device monitoring fails | SNMP UDP 161/162 |
| Logs missing from SIEM/syslog server | Syslog UDP/TCP 514 |
| SQL application cannot connect | SQL Server TCP 1433 |
| IP phones fail to register | SIP TCP/UDP 5060 or TLS 5061 |

## 10. REAL-WORLD EXAMPLE / ANALOGY

Think of a large office building with many departments. The building address is like the IP address. It gets a visitor to the correct building. The room number is like the port number. It gets the visitor to the correct department or service inside the building.

If a visitor goes to the correct building but the room is locked, the building address is not the problem. The service access is the problem. In networking, this is like being able to ping a server but failing to connect to TCP port `443`.

Different departments also have different security rules. The public reception area may be open, but the finance office, server room, and security office require authorization. In the same way, a network may allow HTTPS to a public web server but block SMB, SQL Server, SSH, and RDP from ordinary users.

## 11. CISCO PACKET TRACER / PRACTICAL LAB

### Practice Lab: Match Services to Ports

Build or use a simple topology with:

- One PC.
- One switch.
- One router.
- One server.

Enable services on the server if available:

- HTTP.
- HTTPS if supported.
- DNS.
- DHCP.
- FTP.

Student tasks:

1. Configure the PC to receive an IP address using DHCP.
2. Use DNS to resolve a server name.
3. Access the server web page using HTTP.
4. Test FTP access if enabled.
5. Disable one service at a time and observe the failure.
6. Use simulation mode to identify the protocol and port involved.
7. Explain why ping may still work when the service is disabled.

Expected learning outcome:

Students should understand that network reachability and application service availability are not the same thing. A device can be reachable by IP while a specific service port is closed, blocked, or stopped.

## 12. QUICK-RECAP CHEAT SHEET

- Ports identify services on a host.
- Protocols define how services communicate.
- TCP services usually require connection establishment.
- UDP services may fail silently because there is no handshake.
- FTP uses TCP 20/21 and is insecure by default.
- SSH uses TCP 22 and is preferred for secure administration.
- Telnet uses TCP 23 and should be avoided.
- SMTP uses TCP 25 for mail transfer; submission often uses TCP 587; SMTPS uses TCP 465.
- DNS uses UDP/TCP 53.
- DHCP uses UDP 67/68.
- TFTP uses UDP 69 and is insecure.
- HTTP uses TCP 80.
- HTTPS uses TCP 443.
- NTP uses UDP 123.
- SNMP uses UDP 161/162.
- LDAP uses TCP/UDP 389.
- LDAPS uses TCP 636.
- SMB uses TCP 445.
- Syslog commonly uses UDP 514.
- SQL Server commonly uses TCP 1433.
- RDP uses TCP/UDP 3389.
- SIP commonly uses TCP/UDP 5060 and TLS 5061.
- Successful ping does not prove a service port is open.
- Open ports should be limited to business need.

## 13. REVIEW QUESTIONS

1. What is a port number?
2. Why can one server use many ports?
3. What is the difference between a protocol and a port?
4. Which protocol uses TCP port 22?
5. Why is SSH preferred over Telnet?
6. Which protocol uses TCP port 23?
7. What is FTP used for, and why is plain FTP risky?
8. What port does DNS commonly use?
9. Why does DNS use both UDP and TCP?
10. What ports does DHCP use?
11. What is HTTP used for?
12. What is the secure alternative to HTTP?
13. What is NTP used for?
14. What is SNMP used for?
15. What is LDAP used for?
16. What is the secure version of LDAP commonly called?
17. What is SMB used for?
18. Why should RDP not be exposed directly to the Internet?
19. What is SIP used for?
20. Why does successful ping not prove that an application is working?

## 14. SUGGESTED ANSWER GUIDE

1. A port number identifies a service or application on a host.
2. One server can run many services, each listening on different ports.
3. A protocol defines communication rules, while a port identifies the service endpoint.
4. SSH uses TCP port 22.
5. SSH encrypts remote administration traffic, while Telnet sends data in clear text.
6. Telnet uses TCP port 23.
7. FTP transfers files, but plain FTP is risky because it sends credentials and data in clear text.
8. DNS commonly uses UDP/TCP port 53.
9. DNS often uses UDP for normal queries and TCP for zone transfers or larger responses.
10. DHCP uses UDP ports 67 and 68.
11. HTTP is used for web communication.
12. HTTPS is the secure alternative to HTTP.
13. NTP synchronizes time across systems.
14. SNMP monitors and manages network devices.
15. LDAP accesses directory services such as user and group information.
16. LDAPS.
17. SMB is used for file and printer sharing.
18. RDP is a common attack target and should be protected with VPN, MFA, firewall restrictions, and strong policies.
19. SIP is used for voice and video call signaling.
20. Ping tests ICMP reachability, but applications require specific services, ports, authentication, certificates, and server processes.

