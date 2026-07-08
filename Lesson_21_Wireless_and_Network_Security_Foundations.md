# LESSON 21: WIRELESS AND NETWORK SECURITY FOUNDATIONS

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 21.1 What Is Network Security?

Network security is the combination of technologies, policies, processes, and human actions used to protect network devices, services, communications, systems, and data from unauthorized access, misuse, alteration, disruption, or destruction.

Network security is not one device and it is not one product. A firewall is part of network security, but a firewall alone cannot protect an organization. Wireless encryption is part of security, but encryption alone cannot stop a user from entering credentials into a phishing website. Antivirus is useful, but it cannot replace patching, backups, segmentation, authentication, monitoring, or user awareness.

Security answers four basic questions:

```text
What must be protected?
What threats could affect it?
Which controls reduce the risk?
How will the organization detect, respond to, and recover from an incident?
```

In previous lessons, students built the technical foundation: switches, routers, VLANs, routing, NAT, DHCP, DNS, access points, controllers, SSIDs, and guest networks. This lesson explains how security protects those systems and the information that travels through them.

### 21.2 Why Network Security Matters

Organizations depend on networks for communication, payments, customer records, identity services, cloud applications, email, voice, databases, CCTV, file sharing, remote work, and business operations. A security incident can therefore become a business incident.

Examples include:

| Environment | Security Impact |
|---|---|
| Bank | Stolen credentials, fraudulent transactions, service outage |
| Hospital | Loss of access to clinical systems or patient data exposure |
| School | Student records exposed or online learning disrupted |
| Factory | Production network interrupted or industrial devices manipulated |
| Retail shop | Payment systems compromised or customer data stolen |
| Government office | Sensitive information exposed or services disrupted |
| Small business | Ransomware, financial loss, and prolonged downtime |

Security matters because attackers do not only target large companies. Smaller organizations may have weaker controls, less monitoring, and fewer recovery resources. A compromised email account, exposed Remote Desktop service, weak Wi-Fi password, unpatched server, or stolen administrator credential can create serious damage.

### 21.3 How Security Risk Is Created

Risk exists when a threat can exploit a vulnerability and cause an impact.

```text
Risk = likelihood of exploitation combined with potential impact
```

A threat is anything capable of causing harm. A vulnerability is a weakness that can be exploited. An exploit is a method or code used to take advantage of a vulnerability. A control is a safeguard used to reduce risk.

Security Risk Terms

| Term | Meaning | Example |
|---|---|---|
| Asset | Something valuable that must be protected | Server, data, router, user account |
| Threat | Something capable of causing harm | Attacker, malware, fire, insider misuse |
| Vulnerability | Weakness that can be exploited | Unpatched software, weak password |
| Exploit | Method used to abuse a vulnerability | Malicious code targeting a software flaw |
| Risk | Possibility and impact of harm | Customer database may be stolen |
| Control | Safeguard that reduces risk | MFA, firewall, backup, segmentation |

Security does not usually eliminate all risk. It reduces risk to an acceptable level while supporting business operations.

## 21.4 The CIA Triad

The CIA triad is a foundational security model built around confidentiality, integrity, and availability.

```text
Confidentiality
Integrity
Availability
```

These three objectives help administrators understand what a security control protects and what an attack damages.

### 21.4.1 Confidentiality

Confidentiality means information is accessible only to authorized people, systems, or processes.

Confidentiality protects data from unauthorized disclosure. Examples include employee records, passwords, customer information, financial data, medical records, private emails, encryption keys, and business plans.

Controls that support confidentiality include:

| Control | How It Supports Confidentiality |
|---|---|
| Encryption | Makes intercepted data unreadable without the key |
| Authentication | Verifies identity |
| Authorization | Limits what authenticated identities may access |
| VLANs and firewalls | Restrict network reachability |
| Access control lists | Permit or deny specific traffic |
| Physical security | Prevents unauthorized access to equipment |
| Data classification | Identifies how sensitive data must be handled |

A confidentiality failure occurs when information is exposed to someone who should not see it.

### 21.4.2 Integrity

Integrity means information and systems remain accurate, complete, and unaltered except by authorized actions.

Integrity protects against unauthorized modification. A payroll record changed from one salary to another is an integrity problem. A router configuration secretly changed to redirect traffic is an integrity problem. Malware modifying system files is an integrity problem.

Controls that support integrity include:

| Control | How It Supports Integrity |
|---|---|
| Hashing | Detects whether data has changed |
| Digital signatures | Verifies origin and detects alteration |
| File integrity monitoring | Alerts when protected files change |
| Change management | Controls and documents authorized changes |
| Role-based access | Limits who can modify systems |
| Backups and versioning | Restore trusted copies |
| Logging | Records who changed what and when |

An integrity failure may be difficult to notice because the system can remain available while producing false or manipulated information.

### 21.4.3 Availability

Availability means authorized users can access systems and data when needed.

Availability protects business continuity. A website taken offline by a DDoS attack, a switch powered off by unstable electricity, a server encrypted by ransomware, or a WAN link cut by construction all affect availability.

Controls that support availability include:

| Control | How It Supports Availability |
|---|---|
| Redundancy | Provides alternate devices or paths |
| UPS and backup power | Keeps equipment running during power problems |
| Backups | Supports recovery after data loss or ransomware |
| Load balancing | Distributes service demand |
| DDoS protection | Absorbs or filters attack traffic |
| Monitoring | Detects faults and attacks quickly |
| Patch management | Reduces exploitable outages |
| Disaster recovery planning | Restores services after major incidents |

Security decisions must balance all three parts of the CIA triad. Encrypting data strongly supports confidentiality, but losing the only encryption key destroys availability.

## 21.5 Security Control Categories

Security controls can be grouped by implementation type and by purpose.

Control Types

| Type | Meaning | Examples |
|---|---|---|
| Administrative | Policies and management processes | Security policy, training, risk assessment |
| Technical | Hardware or software controls | Firewall, MFA, encryption, EDR |
| Physical | Controls protecting buildings and equipment | Locks, guards, CCTV, access badges |

Control Functions

| Function | Purpose | Example |
|---|---|---|
| Preventive | Stops an incident | Firewall rule, MFA, locked server room |
| Detective | Identifies an incident | IDS, SIEM alert, CCTV |
| Corrective | Fixes or limits damage | Malware removal, patch deployment |
| Deterrent | Discourages attacks or misuse | Warning banner, visible cameras |
| Compensating | Alternative when preferred control is unavailable | Extra monitoring for legacy system |
| Recovery | Restores operations | Backups, disaster recovery site |

A strong security program uses several control categories. Technical controls without policy, training, physical security, or recovery planning leave major gaps.

## 21.6 Defense-in-Depth

Defense-in-depth is the use of multiple layers of security controls so that one failed control does not expose the entire organization.

For example, consider a malicious email attachment:

1. Email filtering may block it.
2. User awareness may prevent the user from opening it.
3. Endpoint protection may detect it.
4. Application control may stop it from running.
5. Least privilege may limit its permissions.
6. Network segmentation may limit its movement.
7. IDS/IPS and logging may detect suspicious traffic.
8. Backups may support recovery.

Defense-in-Depth Layers

| Layer | Example Controls |
|---|---|
| Physical | Locked rooms, CCTV, access badges, environmental controls |
| Perimeter | Firewalls, VPN gateways, DDoS protection |
| Network | VLANs, ACLs, segmentation, IDS/IPS, NAC |
| Identity | MFA, AAA, least privilege, password policy |
| Endpoint | Patching, anti-malware, EDR, host firewall |
| Application | Secure configuration, input validation, WAF |
| Data | Encryption, backups, access controls, classification |
| Monitoring | Syslog, SIEM, alerts, audit logs |
| People and Process | Training, incident response, change management |

Defense-in-depth does not mean adding products without design. Every layer should have a clear purpose, owner, configuration standard, and monitoring plan.

## 21.7 Zero Trust and Least Privilege

Zero Trust is a security approach based on continuously verifying access rather than automatically trusting a user or device because it is inside the network.

The central idea is:

```text
Never trust automatically; verify explicitly and limit access.
```

Least privilege means users, devices, applications, and administrators receive only the permissions required to perform their tasks.

Examples:

| Poor Practice | Better Practice |
|---|---|
| Every staff member is a local administrator | Standard accounts with approved elevation |
| Guest Wi-Fi can reach internal servers | Guest VLAN receives internet-only policy |
| One shared administrator account | Named administrator accounts with MFA |
| IoT devices can reach every subnet | IoT VLAN permitted only to required services |
| All switchports are active | Unused ports disabled and placed in parking VLAN |

Zero Trust does not remove the need for VLANs, firewalls, identity systems, or monitoring. It uses these controls more deliberately.

## 21.8 Wireless Security Evolution

Wireless traffic travels through the air, so it requires strong authentication and encryption. Early wireless security methods were weak and should not be used.

Wireless Security Evolution

| Technology | Status | Main Security Method | Practical Position |
|---|---|---|---|
| Open Wi-Fi | No traditional password encryption | None or enhanced open where supported | Unsafe for sensitive traffic without additional protection |
| WEP | Obsolete | RC4 with weak design | Must not be used |
| WPA | Legacy | TKIP | Must not be used for modern deployments |
| WPA2 | Widely supported | AES-CCMP preferred | Still common when securely configured |
| WPA3 | Newer security generation | SAE for Personal, stronger Enterprise options | Preferred where clients support it |

WEP and original WPA/TKIP are obsolete because their protections are no longer adequate. Modern enterprise deployments should use WPA2 with AES-CCMP or WPA3, depending on device support and organizational requirements.

## 21.9 WPA2

WPA2 means Wi-Fi Protected Access 2. It became the long-standing standard for securing Wi-Fi and is closely associated with IEEE 802.11i.

WPA2 commonly uses AES-based CCMP encryption. It can operate in Personal mode or Enterprise mode.

WPA2 Modes

| Mode | Authentication | Typical Use |
|---|---|---|
| WPA2-Personal | Pre-shared key | Home, small office, simple device networks |
| WPA2-Enterprise | 802.1X/EAP with RADIUS | Business, school, government, enterprise |

WPA2-Personal is easy to deploy, but every user commonly knows the same shared key. If an employee leaves or the key is exposed, the organization may need to change the key on every device.

WPA2-Enterprise provides individual authentication. Users or devices can be identified separately, access can be revoked centrally, and authentication events can be logged.

## 21.10 WPA3

WPA3 means Wi-Fi Protected Access 3. It improves wireless security while retaining Personal and Enterprise deployment models.

WPA3-Personal replaces the traditional pre-shared key exchange with Simultaneous Authentication of Equals, or SAE. SAE improves resistance to offline password-guessing attacks and provides stronger protection for the authentication exchange.

WPA3 also requires Protected Management Frames in WPA3 deployments. Protected Management Frames help defend important wireless management traffic from forgery and certain disconnection attacks.

WPA3 Features

| Feature | Security Benefit |
|---|---|
| SAE in Personal mode | Stronger password-authenticated key exchange |
| Protected Management Frames | Protects selected management traffic |
| Stronger Enterprise option | Supports higher-security enterprise environments |
| Enhanced Open/OWE ecosystem support | Can encrypt traffic on supported open networks |

WPA3 requires compatible clients and infrastructure. During migration, organizations may use transition modes that support both WPA2 and WPA3. Transition modes improve compatibility but may not provide the full security benefit of WPA3-only operation.

## 21.11 WPA2 vs WPA3

WPA2 and WPA3 both protect wireless communication, but WPA3 improves key establishment and management-frame protection.

WPA2 vs WPA3

| Feature | WPA2 | WPA3 |
|---|---|---|
| Personal Authentication | Pre-shared key | SAE |
| Offline Password Guessing Resistance | Depends heavily on password strength | Improved through SAE |
| Protected Management Frames | Optional in many WPA2 deployments | Required |
| Legacy Client Support | Very broad | Requires newer support |
| Enterprise Use | 802.1X/EAP | 802.1X/EAP with stronger options |
| Recommended Direction | Secure legacy/compatible deployment | Preferred modern deployment |

WPA3 does not make weak operational practices acceptable. Administrators still need strong passwords where passwords are used, secure certificates, correct RADIUS validation, patched devices, monitoring, segmentation, and careful transition planning.

## 21.12 Personal vs Enterprise Wireless Authentication

Personal mode uses a shared password or passphrase. Enterprise mode authenticates individual users or devices using 802.1X and an authentication server.

Personal vs Enterprise

| Feature | Personal Mode | Enterprise Mode |
|---|---|---|
| Credentials | Shared passphrase | Individual user/device credentials |
| Authentication Server | Not required | Usually RADIUS |
| User Accountability | Limited | Stronger individual logging |
| Revocation | Change shared key or remove device | Disable one account/certificate |
| Scalability | Small environments | Medium and large organizations |
| Common Risk | Key sharing | Certificate or identity misconfiguration |

Personal mode may be appropriate for small offices, guest networks, or device groups that cannot use 802.1X. Enterprise mode is preferred for staff networks where identity, accountability, and centralized access control matter.

## 21.13 IEEE 802.1X Authentication

IEEE 802.1X is a framework for port-based network access control. It can protect wired switchports and wireless networks.

802.1X has three main roles:

| Role | Meaning | Wireless Example |
|---|---|---|
| Supplicant | Device requesting access | Laptop or smartphone |
| Authenticator | Network device controlling access | Access point or WLC |
| Authentication Server | Server validating credentials | RADIUS server |

The supplicant provides identity information. The authenticator passes authentication messages between the supplicant and authentication server. The RADIUS server validates the identity and returns an access decision.

The authenticator does not normally verify the user's password itself. It controls network access based on the RADIUS result.

## 21.14 EAP and RADIUS

EAP means Extensible Authentication Protocol. EAP provides a framework for different authentication methods. RADIUS means Remote Authentication Dial-In User Service. It transports authentication, authorization, and accounting information between network devices and an identity service.

Common EAP Methods

| EAP Method | Credentials | Practical Notes |
|---|---|---|
| EAP-TLS | Client and server certificates | Strong security; requires certificate infrastructure |
| PEAP | Server certificate plus protected user credentials | Common in Windows environments |
| EAP-TTLS | Protected tunnel with inner authentication | Supported in many enterprise environments |

EAP-TLS is often considered a strong enterprise method because it uses certificates for both client and server authentication. Its operational challenge is certificate enrollment, renewal, revocation, and device management.

RADIUS commonly uses UDP ports 1812 for authentication and 1813 for accounting, although older deployments may use UDP 1645 and 1646.

## 21.15 Enterprise 802.1X Authentication Process

A simplified enterprise wireless authentication process is:

| Step | Action |
|---|---|
| 1 | Client selects the enterprise SSID |
| 2 | AP/WLC permits authentication traffic but blocks normal access |
| 3 | Client and RADIUS server exchange EAP messages through AP/WLC |
| 4 | Client validates the server certificate where applicable |
| 5 | RADIUS validates user/device credentials or certificate |
| 6 | RADIUS returns accept or reject |
| 7 | Controller applies VLAN, ACL, or role policy |
| 8 | Client receives DHCP configuration and normal access |

Certificate validation is critical. If users ignore certificate warnings or clients are configured to trust any authentication server, an attacker may create a fake enterprise SSID and attempt to steal credentials.

## 21.16 RADIUS Policy and Dynamic Access

RADIUS can return more than an allow or deny decision. It can return attributes that place users into specific VLANs or apply roles and access policies.

Example:

| Identity | RADIUS Result | Access |
|---|---|---|
| Employee | VLAN 10 | Internal applications and internet |
| Contractor | VLAN 50 | Limited project systems |
| Guest sponsor account | VLAN 30 | Internet only |
| Managed IoT device | VLAN 60 | Required services only |
| Unknown/noncompliant device | Quarantine VLAN | Remediation services only |

This combines identity with network segmentation. It is stronger than placing everyone who knows one shared password into the same VLAN.

## 21.17 Common Wireless Attacks

Wireless attacks target radio availability, authentication, user trust, and network access.

Wireless Attack Types

| Attack | What Happens | Security Impact |
|---|---|---|
| Evil Twin | Fake AP copies a trusted SSID | Credential theft or traffic interception |
| Rogue AP | Unauthorized AP is connected or deployed | Bypasses policy and creates access path |
| Deauthentication Attack | Forged management frames disconnect clients | Availability disruption |
| Weak PSK Attack | Attacker guesses or cracks shared password | Unauthorized WLAN access |
| Wi-Fi Eavesdropping | Attacker captures unprotected traffic | Confidentiality loss |
| WPS Attack | Weak WPS design/PIN is abused | Network key exposure |
| Jamming | RF interference blocks communication | Availability loss |

Protected Management Frames can reduce some forged management-frame attacks, but no single wireless feature stops every attack.

## 21.18 Denial-of-Service and Distributed Denial-of-Service

A denial-of-service attack attempts to make a service unavailable. A distributed denial-of-service attack uses many systems or sources to generate the attack.

DoS and DDoS may target:

| Target | Example |
|---|---|
| Internet link | Flood consumes available bandwidth |
| Firewall | Connection table or CPU exhausted |
| Web server | Application requests overwhelm service |
| DNS server | Query flood prevents name resolution |
| Wireless network | Jamming or authentication floods |
| User account | Repeated logins trigger lockout |

DoS may come from one source. DDoS commonly uses a botnet of compromised devices. Defenses can include rate limiting, upstream ISP filtering, content delivery networks, DDoS mitigation services, redundant links, application controls, and monitoring.

## 21.19 Man-in-the-Middle Attacks

A man-in-the-middle, or MITM, attack occurs when an attacker secretly places themselves between communicating parties to observe, alter, or redirect traffic.

MITM techniques may involve:

- Evil twin wireless access points.
- ARP spoofing on a LAN.
- DNS spoofing or poisoning.
- Rogue DHCP giving an attacker-controlled gateway.
- SSL stripping or certificate deception.
- Compromised routers, proxies, or VPN endpoints.

MITM attacks threaten confidentiality and integrity. Encryption with correct certificate validation is a major defense. Network segmentation, DHCP snooping, Dynamic ARP Inspection, secure DNS, VPNs, monitoring, and user awareness also reduce risk.

## 21.20 Spoofing Attacks

Spoofing means pretending to be a trusted device, user, service, or address.

Common Spoofing Types

| Type | Description |
|---|---|
| IP Spoofing | Forging source IP information |
| MAC Spoofing | Changing or impersonating a MAC address |
| ARP Spoofing | Sending false ARP information |
| DNS Spoofing | Providing false name-resolution answers |
| Email Spoofing | Forging sender identity |
| Caller ID Spoofing | Displaying a false phone number |
| Website Spoofing | Creating a fake site that resembles a trusted service |

Spoofing is often part of another attack. For example, email spoofing supports phishing, ARP spoofing supports MITM, and an evil twin AP spoofs a trusted SSID.

## 21.21 Social Engineering

Social engineering manipulates people into revealing information, performing an unsafe action, or bypassing security controls.

Attackers exploit trust, fear, urgency, authority, curiosity, or helpfulness.

Social Engineering Types

| Type | Description | Example |
|---|---|---|
| Phishing | Fraudulent message sent to many targets | Fake password reset email |
| Spear Phishing | Targeted phishing | Email designed for finance manager |
| Whaling | Targeting senior leaders | Fake legal request to CEO |
| Vishing | Voice-based social engineering | Fake bank support call |
| Smishing | SMS-based social engineering | Fake delivery link |
| Pretexting | Invented scenario used to gain trust | Attacker claims to be IT support |
| Baiting | Enticing victim with something attractive | Infected USB labeled "Payroll" |
| Tailgating | Following an authorized person into secure area | Entering server room without badge |

Technical controls help, but users must be trained to verify unusual requests. A password reset request, payment instruction, MFA prompt, or emergency access request should be verified using a trusted channel.

## 21.22 Password Attacks

Password attacks attempt to discover, steal, or reuse credentials.

Password Attack Types

| Attack | Explanation |
|---|---|
| Brute Force | Tries many possible passwords |
| Dictionary Attack | Tries likely words and common passwords |
| Password Spraying | Tries a few common passwords against many accounts |
| Credential Stuffing | Reuses stolen username/password pairs |
| Keylogging | Records keystrokes |
| Phishing | Tricks users into entering credentials |
| Offline Cracking | Attacker guesses against captured password data |

Defenses include MFA, long unique passwords, password managers, account lockout/rate limits, breached-password detection, phishing-resistant authentication, secure password storage, and monitoring.

## 21.23 Malware

Malware means malicious software. It is software designed to damage systems, steal data, spy on users, disrupt operations, gain unauthorized access, or support further attacks.

Malware can arrive through phishing, malicious websites, pirated software, infected USB drives, exposed services, software vulnerabilities, supply-chain compromise, or stolen credentials.

Malware Categories

| Category | Main Behavior |
|---|---|
| Virus | Attaches to files and spreads when executed |
| Worm | Self-propagates across systems or networks |
| Trojan | Pretends to be legitimate software |
| Ransomware | Encrypts or steals data and demands payment |
| Spyware | Secretly monitors activity and steals information |
| Adware | Displays unwanted advertising, sometimes with tracking |
| Rootkit | Hides malicious activity and maintains privileged access |
| Keylogger | Captures keystrokes |
| Bot/Botnet Agent | Makes device part of remotely controlled network |
| Backdoor | Creates hidden unauthorized access |
| Logic Bomb | Activates when a condition is met |
| Fileless Malware | Uses trusted system tools and memory to reduce file artifacts |

### 21.23.1 Virus vs Worm

A virus usually needs a host file and user action to spread. A worm can spread automatically across networks by exploiting vulnerabilities or weak services.

Virus vs Worm

| Feature | Virus | Worm |
|---|---|---|
| Requires Host File | Usually | No |
| User Action | Often required | May spread automatically |
| Network Impact | Depends on execution | Can spread rapidly |
| Main Defense | Endpoint protection, safe behavior | Patching, segmentation, endpoint/network controls |

### 21.23.2 Trojan

A Trojan appears useful or legitimate but performs malicious actions. A fake software installer, cracked application, or fraudulent attachment may install a remote-access Trojan.

The name comes from the idea of hiding danger inside something that appears safe.

### 21.23.3 Ransomware

Ransomware encrypts data or systems and demands payment. Modern ransomware operations may also steal data before encryption and threaten to publish it.

Ransomware affects confidentiality, integrity, and availability:

| CIA Objective | Ransomware Impact |
|---|---|
| Confidentiality | Data may be stolen |
| Integrity | Files and configurations may be altered |
| Availability | Systems and data become inaccessible |

Ransomware defenses include patching, MFA, restricting exposed services, email security, endpoint detection, segmentation, least privilege, tested offline or immutable backups, logging, and incident response planning.

### 21.23.4 Spyware and Keyloggers

Spyware secretly collects information such as browsing activity, credentials, screenshots, or documents. Keyloggers specifically record keyboard input.

These threats primarily affect confidentiality but can also support account takeover and further compromise.

### 21.23.5 Rootkits and Backdoors

A rootkit attempts to hide malicious activity or maintain privileged access. A backdoor creates an unauthorized method of entering a system while bypassing normal authentication.

Rootkits can be difficult to detect because they may manipulate what the operating system reports. Strong endpoint detection, secure boot, integrity checking, and rebuilding from trusted media may be necessary.

### 21.23.6 Botnets

A botnet is a group of compromised devices controlled by an attacker. Botnets may send spam, perform DDoS attacks, steal data, distribute malware, or conduct credential attacks.

IoT devices with default passwords and unpatched firmware are frequent botnet targets. IoT segmentation and restricted outbound access reduce the potential impact.

## 21.24 Indicators of Compromise

An indicator of compromise, or IOC, is evidence that a device, account, or network may have been compromised.

Common IOCs

| Indicator | Possible Meaning |
|---|---|
| Unusual outbound traffic | Malware communication or data exfiltration |
| Repeated failed logins | Password attack |
| Login from unusual location | Stolen account |
| New unknown administrator account | Persistence |
| Disabled security tools | Attacker evasion |
| Unexpected DNS queries | Malware command-and-control |
| Files renamed or encrypted | Ransomware |
| High CPU/network use | Cryptomining, botnet, DoS, or malfunction |
| Unknown AP/SSID | Rogue or evil twin wireless activity |
| Configuration changed without ticket | Unauthorized change |

One indicator is not always proof of compromise. Administrators correlate logs, timestamps, user activity, network flows, endpoint alerts, and configuration history.

## 21.25 Security Monitoring and Logging

Security controls must generate useful evidence. Logs support detection, troubleshooting, incident response, compliance, and accountability.

Important Log Sources

| Source | Security Value |
|---|---|
| Firewall | Allowed/denied traffic, NAT, VPN events |
| WLC/AP | Client association, authentication, rogue AP alerts |
| RADIUS | Authentication success/failure and identity |
| Switch | Port state, MAC changes, security violations |
| Router | Routing changes, ACL events, management access |
| DNS | Queried domains and suspicious patterns |
| DHCP | Device address assignments |
| Windows/Linux | Login, process, service, and system events |
| EDR/Antivirus | Malware and behavior alerts |
| Cloud Platform | Identity, API, configuration, and workload events |

Time synchronization is essential. If devices have different times, incident timelines become difficult to reconstruct. NTP supports accurate log correlation.

## 21.26 Basic Incident Response

Incident response is the organized process used to prepare for, detect, contain, remove, and recover from security incidents.

Incident Response Lifecycle

| Phase | Main Activities |
|---|---|
| Preparation | Policies, tools, contacts, backups, training |
| Detection and Analysis | Confirm alert, collect evidence, determine scope |
| Containment | Isolate affected systems and limit spread |
| Eradication | Remove malware, close vulnerabilities, reset credentials |
| Recovery | Restore systems, monitor, return to service |
| Lessons Learned | Document cause, response, gaps, and improvements |

Do not immediately erase a compromised device without considering evidence and business impact. In a real organization, follow the incident response procedure and escalation path.

For an infected endpoint, containment may include disabling the switchport, moving the device to a quarantine VLAN, disconnecting Wi-Fi, revoking credentials, or blocking malicious destinations.

## 21.27 Windows Security Verification

Windows provides tools for checking wireless security, firewall state, endpoint protection, active connections, and event logs.

Useful Windows Security Commands

| Command | Purpose |
|---|---|
| `netsh wlan show interfaces` | Shows current SSID, BSSID, authentication, and cipher |
| `netsh wlan show profiles` | Lists saved wireless profiles |
| `Get-NetFirewallProfile` | Shows Windows Firewall profile state |
| `Get-MpComputerStatus` | Shows Microsoft Defender status |
| `netstat -ano` | Shows network connections and process IDs |
| `Get-NetTCPConnection` | Shows TCP connection details |
| `whoami /all` | Shows user identity, groups, and privileges |
| `wevtutil qe Security /c:10 /rd:true /f:text` | Reads recent Security log events |

Commands should be interpreted carefully. A listening port is not automatically malicious, and a high process ID does not indicate compromise. The technician must identify the owning process, expected service, remote endpoint, user context, and business purpose.

## 21.28 Linux Security Verification

Linux provides commands for reviewing identities, services, ports, logs, and firewall rules.

Useful Linux Security Commands

| Command | Purpose |
|---|---|
| `id` | Shows current user and group membership |
| `who` | Shows logged-in users |
| `ss -tulpen` | Shows listening TCP/UDP sockets and processes |
| `ps aux` | Shows running processes |
| `journalctl` | Reviews system and service logs |
| `last` | Shows login history |
| `ip addr` and `ip route` | Verifies network configuration |
| `nft list ruleset` | Shows nftables firewall rules |
| `ufw status` | Shows UFW status where used |

Security review should follow organizational authorization. Scanning, packet capture, password testing, or account access must only be performed with permission.

## 21.29 Cisco and Wireless Security Verification

Cisco IOS and wireless platforms provide commands for reviewing access, port state, security events, and authentication.

Useful Cisco Security Checks

| Command | Purpose |
|---|---|
| `show access-lists` | Reviews ACL entries and counters |
| `show port-security` | Reviews port-security status |
| `show port-security interface` | Reviews security on one switchport |
| `show authentication sessions` | Reviews 802.1X/MAB sessions where supported |
| `show logging` | Reviews device logs |
| `show users` | Shows management sessions |
| `show running-config | include username` | Reviews configured local usernames |
| `show ip interface brief` | Finds unexpected active interfaces |
| `show interfaces status` | Reviews switchport state |
| `show mac address-table` | Reviews learned MAC addresses |

On a WLC or cloud wireless platform, administrators should verify SSID security mode, RADIUS reachability, authentication failures, client identity, assigned VLAN, rogue AP alerts, and management-frame protection.

## 21.30 Enterprise Security Case Study

A company has four network groups:

| Group | Network | Security Requirement |
|---|---|---|
| Staff | VLAN 10 and staff SSID | WPA3/WPA2-Enterprise, RADIUS, internal access |
| Guests | VLAN 30 and guest SSID | Internet only, client isolation |
| IoT/CCTV | VLAN 60 | Restricted services, no broad internal access |
| Servers | VLAN 40 | Limited inbound access, monitoring, backups |

An attacker creates an evil twin named `FEMTECT-STAFF` near the office. A user connects and enters enterprise credentials without checking the server certificate. The attacker captures information that may help compromise the account.

Defense-in-depth can reduce the impact:

1. Managed wireless profiles validate the correct RADIUS certificate.
2. MFA protects sensitive applications.
3. RADIUS logs reveal unusual authentication.
4. WLC detects an unauthorized SSID or rogue AP.
5. Network segmentation limits access.
6. SIEM correlates account and wireless events.
7. The user reports the suspicious certificate prompt.
8. Incident response resets credentials and investigates affected systems.

The case demonstrates that wireless encryption, identity, endpoint configuration, monitoring, segmentation, and user awareness must work together.

## 21.31 Packet Tracer Practice

### Practice Lab 1: Secure Staff and Guest Segmentation

Build a topology with:

| Component | Purpose |
|---|---|
| Staff wireless network | Employee access |
| Guest wireless network | Visitor internet access |
| Staff VLAN 10 | Internal staff subnet |
| Guest VLAN 30 | Isolated guest subnet |
| Server VLAN 40 | Internal services |
| Router or Layer 3 switch | Inter-VLAN routing |
| ACL/firewall policy | Restricts guest access |

Configure the guest network so it cannot reach the server VLAN but can reach the simulated internet. Verify that staff users can reach approved servers.

### Practice Lab 2: Security Troubleshooting

Introduce one fault at a time:

| Fault | Expected Symptom |
|---|---|
| Wrong wireless key | Client cannot authenticate |
| Guest mapped to staff VLAN | Security segmentation failure |
| ACL permits guest-to-server traffic | Unauthorized access path |
| RADIUS server unreachable | Enterprise authentication fails |
| Wrong client time/certificate condition | Certificate authentication may fail |

Students should identify the symptom, affected CIA objective, root cause, corrective action, and prevention.

### Practice Lab 3: Defense-in-Depth Design

Create a written security design for a small office. Include:

- Staff and guest wireless security.
- VLAN segmentation.
- Firewall policy.
- MFA for cloud email.
- Endpoint protection and patching.
- Backups.
- Syslog and monitoring.
- UPS for network availability.
- Incident response contacts.

Explain which controls are preventive, detective, corrective, and recovery controls.

## 21.32 Cybersecurity Career Relevance

Networking knowledge is essential in cybersecurity. Security analysts must understand normal traffic before identifying abnormal traffic. They must know VLANs, routing, DNS, DHCP, NAT, ports, protocols, wireless authentication, and packet journeys.

Career connections:

| Role | Networking/Security Responsibility |
|---|---|
| IT Support | Secure endpoints, accounts, Wi-Fi, and user access |
| Network Engineer | Configure segmentation, firewalls, AAA, VPN, and monitoring |
| SOC Analyst | Investigate alerts, logs, IPs, domains, and traffic |
| Security Engineer | Design controls and harden systems |
| Incident Responder | Contain devices, analyze evidence, restore services |
| Cloud Security Engineer | Protect cloud identities, networks, workloads, and logs |

Students should practice explaining security incidents in networking terms: source, destination, protocol, port, identity, VLAN, route, policy, timestamp, and expected behavior.

## 21.33 Cloud Security Relevance

Cloud security uses the same foundational objectives: confidentiality, integrity, and availability. The controls may be implemented through cloud identity systems, security groups, network ACLs, private subnets, encryption services, logging, and managed security tools.

Cloud Security Examples

| Control | Cloud Example |
|---|---|
| Identity | IAM roles and MFA |
| Segmentation | Virtual networks, subnets, security groups |
| Encryption | Data encryption at rest and in transit |
| Monitoring | Cloud audit logs and flow logs |
| Availability | Multiple zones, backups, load balancing |
| Least Privilege | Narrow IAM permissions |
| Incident Response | Isolate workload, revoke keys, preserve snapshots |

Cloud security follows a shared responsibility model. The provider secures parts of the cloud infrastructure, while the customer remains responsible for areas such as identities, data, configurations, applications, and access policies, depending on the service model.

## 21.34 Interview and Exam Relevance

In IT support interviews, security questions may involve phishing, malware symptoms, compromised accounts, Wi-Fi authentication, Windows Firewall, endpoint protection, safe escalation, and user communication.

In network engineering interviews, questions may involve WPA2 vs WPA3, 802.1X roles, RADIUS, segmentation, DoS/DDoS, spoofing, MITM, logging, and defense-in-depth.

For CCNA, students should understand wireless authentication methods, WPA2/WPA3 concepts, AAA/RADIUS relationships, common attacks, segmentation, and secure network management.

For CompTIA Network+ N10-009, students should understand the CIA triad, security controls, common attacks, malware categories, wireless security, authentication, segmentation, and practical troubleshooting.

## 22. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Network Security | Protection of network systems, services, communications, and data. |
| Asset | Valuable system, data, service, device, or identity. |
| Threat | Something capable of causing harm. |
| Vulnerability | Weakness that can be exploited. |
| Exploit | Method or code used to abuse a vulnerability. |
| Risk | Likelihood and impact of harm. |
| Control | Safeguard used to reduce risk. |
| CIA Triad | Confidentiality, integrity, and availability. |
| Confidentiality | Preventing unauthorized disclosure. |
| Integrity | Protecting accuracy and preventing unauthorized modification. |
| Availability | Keeping services accessible to authorized users. |
| Defense-in-Depth | Multiple overlapping security layers. |
| Least Privilege | Giving only the access required. |
| Zero Trust | Explicitly verifying access rather than trusting location alone. |
| WPA2 | Widely used Wi-Fi security generation supporting Personal and Enterprise modes. |
| WPA3 | Newer Wi-Fi security generation using SAE in Personal mode and stronger protections. |
| SAE | Simultaneous Authentication of Equals. |
| PMF | Protected Management Frames. |
| 802.1X | Port-based network access control framework. |
| Supplicant | Client requesting 802.1X access. |
| Authenticator | Network device controlling 802.1X access. |
| RADIUS | Protocol/service used for centralized authentication, authorization, and accounting. |
| EAP | Framework supporting multiple authentication methods. |
| Evil Twin | Fake AP impersonating a trusted wireless network. |
| Rogue AP | Unauthorized access point. |
| DoS | Denial-of-service attack. |
| DDoS | Distributed denial-of-service attack. |
| MITM | Man-in-the-middle attack. |
| Spoofing | Impersonating a trusted identity, address, or service. |
| Social Engineering | Manipulating people to bypass security. |
| Phishing | Fraudulent message designed to steal information or cause unsafe action. |
| Malware | Malicious software. |
| Ransomware | Malware that encrypts or steals data and demands payment. |
| Trojan | Malware disguised as legitimate software. |
| Worm | Self-propagating malware. |
| Virus | Malware that attaches to files and spreads when executed. |
| Spyware | Malware that secretly collects information. |
| Rootkit | Malware designed to hide activity or maintain privileged access. |
| Botnet | Group of compromised devices controlled by an attacker. |
| IOC | Indicator of compromise. |
| Incident Response | Organized process for handling security incidents. |

## 23. COMPARISON TABLES

### 23.1 Confidentiality vs Integrity vs Availability

| Objective | Protects Against | Example Control |
|---|---|---|
| Confidentiality | Unauthorized disclosure | Encryption |
| Integrity | Unauthorized modification | Hashing/digital signatures |
| Availability | Service disruption | Redundancy/backups |

### 23.2 WPA2 vs WPA3

| Feature | WPA2 | WPA3 |
|---|---|---|
| Personal Method | PSK | SAE |
| Management Frame Protection | Often optional | Required |
| Legacy Compatibility | Broad | Newer devices required |
| Enterprise Support | 802.1X/EAP | 802.1X/EAP with stronger options |
| Deployment Direction | Secure compatibility option | Preferred modern option |

### 23.3 Personal vs Enterprise Wi-Fi

| Feature | Personal | Enterprise |
|---|---|---|
| Identity | Shared password | Individual user/device |
| Server | None required | RADIUS |
| Revocation | Change shared key | Disable one identity |
| Accountability | Limited | Stronger |
| Best Fit | Home/small office/simple devices | Enterprise staff networks |

### 23.4 DoS vs DDoS

| Feature | DoS | DDoS |
|---|---|---|
| Sources | Usually one or few | Many distributed sources |
| Scale | Limited to large | Often large |
| Common Infrastructure | One attacking host | Botnet |
| Defense | Filtering, rate limiting | Upstream/cloud mitigation and filtering |

### 23.5 Virus vs Worm vs Trojan

| Feature | Virus | Worm | Trojan |
|---|---|---|---|
| Main Form | Attaches to file | Standalone self-spreading code | Disguised malicious program |
| User Action | Often | Not always | Usually installation/execution |
| Self-Propagation | Limited | Yes | Not its defining feature |
| Common Defense | Endpoint security | Patching and segmentation | Trusted software and endpoint security |

### 23.6 Preventive vs Detective vs Corrective Controls

| Control Function | Purpose | Example |
|---|---|---|
| Preventive | Stop incident | MFA |
| Detective | Find incident | IDS/SIEM alert |
| Corrective | Remove cause or damage | Patch and malware removal |
| Recovery | Restore operations | Backup restoration |

## 24. REAL-WORLD EXAMPLE / ANALOGY

Think of an enterprise network like a secured office building.

The fence and gate represent perimeter controls. The reception desk represents authentication. Access badges represent authorization. Locked rooms represent segmentation. CCTV represents monitoring. Fire alarms represent detection. Backup generators represent availability. Emergency procedures represent incident response.

No serious building relies on one lock at the front door. In the same way, no serious network should rely on one firewall or one password. Security works through multiple coordinated layers.

## 25. QUICK-RECAP CHEAT SHEET

- Network security protects devices, services, communications, identities, and data.
- Risk exists when a threat can exploit a vulnerability and cause impact.
- CIA means confidentiality, integrity, and availability.
- Defense-in-depth uses multiple security layers.
- Least privilege gives only required access.
- WPA2 commonly uses AES-CCMP and supports Personal and Enterprise modes.
- WPA3-Personal uses SAE.
- WPA3 requires Protected Management Frames.
- Personal Wi-Fi commonly uses a shared passphrase.
- Enterprise Wi-Fi uses 802.1X/EAP and RADIUS.
- 802.1X roles are supplicant, authenticator, and authentication server.
- EAP-TLS uses client and server certificates.
- RADIUS commonly uses UDP 1812 and 1813.
- Evil twins imitate trusted SSIDs.
- Rogue APs are unauthorized access points.
- DoS attacks availability; DDoS uses distributed sources.
- MITM attacks place an attacker between communicating parties.
- Spoofing impersonates trusted identities or addresses.
- Social engineering manipulates people.
- Malware categories include viruses, worms, Trojans, ransomware, spyware, rootkits, and bots.
- Logs, NTP, monitoring, segmentation, MFA, patching, backups, and training support defense-in-depth.
- Incident response includes preparation, detection, containment, eradication, recovery, and lessons learned.

## 26. REVIEW QUESTIONS

1. What is network security?
2. What is the difference between a threat and a vulnerability?
3. What are the three parts of the CIA triad?
4. Give one control that supports confidentiality.
5. Give one control that supports integrity.
6. Give one control that supports availability.
7. What is defense-in-depth?
8. What does least privilege mean?
9. Why should WEP and original WPA/TKIP not be used?
10. What is the difference between WPA2-Personal and WPA2-Enterprise?
11. What authentication method does WPA3-Personal use?
12. What are Protected Management Frames?
13. What are the three main 802.1X roles?
14. What is the role of RADIUS?
15. What is EAP-TLS?
16. What is an evil twin?
17. What is the difference between DoS and DDoS?
18. What is a man-in-the-middle attack?
19. What is social engineering?
20. What is the difference between a virus, worm, and Trojan?
21. How can ransomware affect all three CIA objectives?
22. What is an indicator of compromise?
23. Why is NTP important for security logging?
24. What are the major incident response phases?
25. Why is network segmentation important during a malware incident?

## 27. SUGGESTED ANSWER GUIDE

1. The protection of network systems, services, communications, identities, and data from unauthorized access, alteration, disruption, or destruction.
2. A threat can cause harm; a vulnerability is a weakness the threat can exploit.
3. Confidentiality, integrity, and availability.
4. Encryption, authentication, authorization, or access controls.
5. Hashing, digital signatures, file integrity monitoring, or change management.
6. Redundancy, backups, UPS power, monitoring, or DDoS protection.
7. Using multiple overlapping security controls so one failure does not expose everything.
8. Giving users, devices, and applications only the access required.
9. Their security protections are obsolete and inadequate.
10. Personal uses a shared key; Enterprise uses individual 802.1X/EAP authentication through RADIUS.
11. Simultaneous Authentication of Equals, or SAE.
12. Protection for selected wireless management traffic against forgery and certain disconnection attacks.
13. Supplicant, authenticator, and authentication server.
14. It provides centralized authentication, authorization, and accounting communication.
15. An EAP method that uses client and server certificates.
16. A fake access point that impersonates a trusted SSID.
17. DoS commonly uses one or few sources; DDoS uses many distributed sources.
18. An attack where an attacker places themselves between communicating parties to observe or alter traffic.
19. Manipulating people into revealing information or performing unsafe actions.
20. A virus attaches to files, a worm self-propagates, and a Trojan is disguised as legitimate software.
21. It may steal data, alter/encrypt data, and make systems unavailable.
22. Evidence that a system, account, or network may have been compromised.
23. Accurate time allows logs from different systems to be correlated into one incident timeline.
24. Preparation, detection and analysis, containment, eradication, recovery, and lessons learned.
25. Segmentation limits lateral movement and reduces the number of systems malware can reach.
