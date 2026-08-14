# LESSON 20: SECURE OPERATIONS, VPNS, RESILIENCE, AND PROFESSIONAL TROUBLESHOOTING

## TRAINING FOCUS

This lesson is part of the FEMTECT Network Engineering Foundation course. It is written to help students build strong networking fundamentals through clear explanations, real enterprise context, practical troubleshooting logic, and certification-aware technical depth.

---

## Access Control, Hardening, and Essential Services

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### Access Control, Hardening, and Essential Services

Access control is the process of deciding who or what may use a network resource and which actions are permitted. It can filter traffic, restrict administrative access, authenticate users, and prevent unauthorized devices from communicating.

Device hardening is the process of reducing a device's attack surface: the interfaces, services, accounts, protocols, and weaknesses that could be attacked. Hardening removes unnecessary exposure and strengthens required functions.

Essential services make network administration secure and dependable:

| Service | Purpose |
|---|---|
| SSH | Encrypts remote command-line management |
| NTP | Synchronizes device clocks |
| Syslog | Sends event messages to a central collector |
| SNMP | Monitors device status and performance |
| AAA | Controls and records administrative access |

These controls work together. An ACL limits which management station can reach a router. AAA verifies the administrator. SSH protects the session. NTP supplies accurate time. Syslog records events. SNMP reports device health. This is defense-in-depth applied to network operations.

### Technical Importance: and Where These Controls Matter

A device may forward traffic correctly and still be insecure. Telnet could expose credentials, an unused wall port could provide internal access, a rogue DHCP server could redirect users, or inaccurate clocks could make incident investigation difficult.

The controls protect three operational areas:

| Plane | Purpose | Examples of Protection |
|---|---|---|
| Data plane | Forwards user traffic | ACLs, DHCP snooping, DAI |
| Control plane | Builds forwarding information | Protocol filtering, authentication |
| Management plane | Configures and monitors devices | AAA, SSH, management ACLs, SNMPv3 |

## 22.3 Access Control List Fundamentals

An access control list, or ACL, is an ordered set of permit and deny statements. Each rule is an access control entry, or ACE. Cisco IOS ACLs can classify packets by fields such as source address, destination address, protocol, and transport-layer port.

ACLs process entries from top to bottom and stop at the first match:

```text
Packet arrives
  |
  v
First ACE -- match --> permit or deny; stop
  |
 no match
  v
Next ACE --> continue until matched
  |
 no entries match
  v
Implicit deny
```

Every ACL has an invisible `deny any` at the end. Traffic that must pass therefore requires an explicit permit. Traditional router ACLs are normally stateless: they classify individual packets rather than remembering the full state of a conversation as a stateful firewall does.

An ACL can be applied in either direction:

- **Inbound:** Examines a packet as it enters an interface, before the normal routing decision.
- **Outbound:** Examines a packet after the routing decision, before it leaves the selected interface.

Direction is always described from the device's perspective. In general, one IPv4 ACL can be applied per interface, per direction, per protocol.

## 22.4 Standard IPv4 ACLs

A standard IPv4 ACL matches only the source IPv4 address. It cannot directly distinguish destinations, TCP from UDP, or application ports.

Standard numbered ranges are `1-99` and `1300-1999`. Because the matching criteria are limited, a standard ACL is generally placed close to the destination. Placing it near the source could block that source from every destination beyond the interface.

Example: block host `192.168.10.50` from a destination network while permitting other sources.

```cisco
access-list 10 deny host 192.168.10.50
access-list 10 permit any

interface GigabitEthernet0/1
 ip access-group 10 out
```

Without `permit any`, all remaining traffic reaches the implicit deny.

A named ACL is easier to interpret and edit:

```cisco
ip access-list standard BLOCK-FINANCE-SOURCE
 10 deny host 192.168.10.50
 20 permit any
```

Sequence numbers allow controlled insertion and removal of entries.

## 22.5 Extended IPv4 ACLs

An extended IPv4 ACL can match the IP protocol, source address, destination address, and source or destination TCP/UDP port. Extended numbered ranges are `100-199` and `2000-2699`.

Extended ACLs are generally placed close to the source. Their precision allows unwanted traffic to be blocked before it consumes bandwidth across the network.

Requirement: users in `192.168.10.0/24` may use HTTPS to reach `10.20.30.10`, but may not send other IP traffic to that server.

```cisco
ip access-list extended STAFF-TO-APP
 10 permit tcp 192.168.10.0 0.0.0.255 host 10.20.30.10 eq 443
 20 deny ip 192.168.10.0 0.0.0.255 host 10.20.30.10
 30 permit ip any any

interface GigabitEthernet0/0
 ip access-group STAFF-TO-APP in
```

Line 30 allows unrelated traffic. Rule order is critical: if `permit ip any any` appeared first, every IP packet would match it and the later deny would never be evaluated.

Extended ACL examples:

```cisco
permit tcp 192.168.10.0 0.0.0.255 host 10.20.30.10 eq 443
permit udp any host 10.20.40.53 eq 53
permit icmp 192.168.10.0 0.0.0.255 host 10.20.30.10 echo
```

The operators `eq`, `gt`, `lt`, `neq`, and `range` can classify transport ports. ACLs should implement documented business requirements rather than relying on broad permits.

## 22.6 Wildcard Masks

A wildcard mask tells Cisco IOS which address bits must match:

```text
Wildcard bit 0 = corresponding address bit must match
Wildcard bit 1 = corresponding address bit may vary
```

For a contiguous network, subtract the subnet mask from `255.255.255.255`.

```text
255.255.255.255
-255.255.255.0
=  0.  0.  0.255
```

Thus, `192.168.10.0/24` is written as:

```cisco
192.168.10.0 0.0.0.255
```

| Prefix | Subnet Mask | Wildcard Mask |
|---|---|---|
| /32 | 255.255.255.255 | 0.0.0.0 |
| /30 | 255.255.255.252 | 0.0.0.3 |
| /28 | 255.255.255.240 | 0.0.0.15 |
| /27 | 255.255.255.224 | 0.0.0.31 |
| /26 | 255.255.255.192 | 0.0.0.63 |
| /25 | 255.255.255.128 | 0.0.0.127 |
| /24 | 255.255.255.0 | 0.0.0.255 |
| /16 | 255.255.0.0 | 0.0.255.255 |

`host 192.168.10.50` is equivalent to `192.168.10.50 0.0.0.0`. The keyword `any` is equivalent to `0.0.0.0 255.255.255.255`.

A wildcard mask is not a subnet mask. A subnet mask separates network and host portions; a wildcard mask defines matching behavior.

## 22.7 ACL Placement, Safety, and Verification

Correct ACL design answers:

1. What traffic should be permitted or denied?
2. What are the source and destination?
3. Which protocol and application port are involved?
4. Which interfaces are in the packet path?
5. In which direction will the ACL encounter the packet?

| ACL Type | General Placement | Reason |
|---|---|---|
| Standard | Close to destination | Source-only matching can overblock |
| Extended | Close to source | Precise unwanted traffic can be blocked early |

These are guidelines. The ACL must be placed where the packet actually travels. Return traffic, DNS, DHCP, routing protocols, and management access must also be considered.

Before a production ACL change, back up the configuration, review rule order, use an approved change window, prepare rollback, and verify immediately. A remote ACL mistake can disconnect the administrator. The `log` keyword can record matches, but excessive logging can consume CPU, bandwidth, and storage.

Useful commands:

```cisco
show access-lists
show ip access-lists
show ip interface
show running-config | section access-list
show running-config interface GigabitEthernet0/0
```

| Symptom | Likely Cause |
|---|---|
| All traffic stops | Required permit missing |
| Deny never matches | Broader permit appears earlier |
| ACL has no effect | Wrong interface or direction |
| Application partly works | Return traffic, DNS, or additional ports blocked |
| Wrong hosts are affected | Incorrect wildcard mask |
| SSH fails | Administrator subnet or TCP 22 not permitted |

Troubleshoot by identifying the source, destination, protocol, port, path, applied ACL, sequence, direction, and match counters.

## 22.8 IPv6 ACL Overview

IPv6 ACLs use IPv6 prefixes rather than wildcard masks and are normally named:

```cisco
ipv6 access-list USERS-V6
 permit tcp 2001:db8:10::/64 host 2001:db8:30::10 eq 443
 deny ipv6 2001:db8:10::/64 host 2001:db8:30::10
 permit ipv6 any any

interface GigabitEthernet0/0
 ipv6 traffic-filter USERS-V6 in
```

IPv6 depends on ICMPv6 for Neighbor Discovery and Path MTU Discovery. Blocking all ICMPv6 can break normal operation, so policy must permit required control messages.

## 22.9 AAA Concepts

AAA stands for authentication, authorization, and accounting.

- **Authentication asks, "Who are you?"** It verifies an identity through a password, certificate, token, or other credential.
- **Authorization asks, "What may you do?"** It controls commands, resources, or privilege levels after authentication.
- **Accounting asks, "What did you do, and when?"** It records logins, commands, sessions, or resource usage.

AAA may use local accounts or a centralized server. Local accounts are useful for emergency fallback. Centralized AAA provides consistent policy, immediate account control, and better accountability.

| Feature | RADIUS | TACACS+ |
|---|---|---|
| Common transport | UDP 1812 authentication; UDP 1813 accounting | TCP 49 |
| Typical use | 802.1X, VPN, network access | Device administration |
| Protection | Protects password field; not the entire packet | Encrypts packet body |
| AAA separation | Less granular | Separates AAA functions; granular command control |

The wireless security lesson introduced RADIUS for 802.1X. TACACS+ is especially common for controlling administrators on routers and switches.

## 22.10 Switch Port Security

Port security restricts which source MAC addresses may use a Layer 2 access port. Secure addresses can be static, dynamically learned, or sticky. Sticky addresses are learned dynamically and added to the running configuration.

```cisco
interface GigabitEthernet0/10
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
 spanning-tree portfast
```

Two addresses may be needed when an IP phone and workstation share the port.

| Violation Mode | Unauthorized Frames | Port State | Notification |
|---|---|---|---|
| Protect | Dropped | Up | Minimal |
| Restrict | Dropped | Up | Counter and log/SNMP |
| Shutdown | Dropped | Err-disabled | Log/SNMP; default mode |

```cisco
show port-security
show port-security interface GigabitEthernet0/10
show port-security address
show interfaces status err-disabled
```

Port security is normally used on static access ports. Virtualization, docks, phones, and legitimate device changes may produce multiple MAC addresses. Port security is not an identity system and does not replace 802.1X or Network Access Control.

## 22.11 DHCP Snooping

DHCP snooping monitors DHCP messages and distinguishes trusted from untrusted switch ports. A rogue DHCP server could supply a malicious default gateway or DNS server. DHCP snooping blocks server messages arriving on untrusted ports.

Client ports remain untrusted. Only ports toward legitimate DHCP servers or valid relay paths should be trusted.

DHCP snooping builds bindings containing the client MAC address, assigned IPv4 address, VLAN, switch port, and lease time.

```cisco
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

interface GigabitEthernet0/1
 description Uplink toward legitimate DHCP service
 ip dhcp snooping trust

interface range GigabitEthernet0/2-24
 ip dhcp snooping limit rate 15
```

```cisco
show ip dhcp snooping
show ip dhcp snooping binding
show ip dhcp snooping statistics
```

Trusting every access port defeats the protection. An incorrect rate limit can disable a port carrying legitimate bursts, so the threshold must reflect the port's purpose.

## 22.12 Dynamic ARP Inspection

Dynamic ARP Inspection, or DAI, validates ARP messages on untrusted ports. It helps prevent ARP spoofing, in which false ARP information redirects traffic through an attacker.

DAI commonly compares an ARP sender's MAC address, IPv4 address, VLAN, and port with the DHCP snooping binding table. Invalid ARP messages are dropped.

```cisco
ip arp inspection vlan 10,20,30

interface GigabitEthernet0/1
 description Trusted infrastructure uplink
 ip arp inspection trust
```

```cisco
show ip arp inspection
show ip arp inspection interfaces
show ip arp inspection statistics
```

Static-IP servers, printers, and gateways may not appear in DHCP bindings. They can require ARP ACLs or supported static bindings. Enabling DAI without planning for them can interrupt valid communication.

DHCP snooping and DAI operate as a sequence:

```text
Legitimate DHCP exchange
          |
          v
DHCP snooping creates binding
          |
          v
DAI validates later ARP claims
```

## 22.13 Device Hardening

Hardening reduces unnecessary exposure while preserving required business functions.

Unused access ports should be shut down and assigned to an unused parking VLAN:

```cisco
interface range GigabitEthernet0/15-24
 description UNUSED
 switchport mode access
 switchport access vlan 999
 shutdown
```

The parking VLAN should have no usable Layer 3 gateway. The shutdown command is the primary control.

Use unique named accounts, strong secrets, least privilege, centralized AAA where available, and a protected local emergency account. Remove unused accounts. Shared administrator accounts weaken accountability. Use `enable secret` rather than the legacy `enable password`.

Disable services that are not required:

```cisco
no ip http server
no ip http secure-server
no service pad
```

The decision depends on the environment. Do not disable secure HTTPS management if it is an approved requirement. Hardening is a documented risk decision, not blind removal.

Protect management through a dedicated VLAN or out-of-band network where possible. Restrict SSH, SNMP, and web management to approved subnets. Do not expose management directly to the public Internet.

Additional controls include software updates, configuration backups, legal banners, session timeouts, login controls, NTP authentication where supported, centralized logging, and SNMPv3.

## 22.14 Secure Shell

SSH uses TCP 22 and encrypts remote command-line access. Telnet uses TCP 23 and transmits credentials and session content without encryption.

```cisco
hostname SW1
ip domain-name femtect.local
username netadmin privilege 15 secret <strong-secret>
enable secret <strong-enable-secret>

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4
 login local
 transport input ssh
 exec-timeout 10 0
```

The hostname and domain name support RSA key generation. `login local` uses the local user database, and `transport input ssh` rejects Telnet.

```cisco
show ip ssh
show ssh
show users
```

In an enterprise, centralized AAA may replace normal local login, while a securely managed local account remains for emergency recovery.

## 22.15 Network Time Protocol

NTP synchronizes device clocks and commonly uses UDP 123. Accurate time allows logs from routers, switches, firewalls, servers, and applications to be correlated.

NTP uses a hierarchy. Stratum 1 systems synchronize closely with authoritative sources; higher numbers are farther away. A low stratum does not itself prove trustworthiness, so organizations use approved sources and authentication where supported.

```cisco
clock timezone WAT 1 0
ntp server 10.20.50.10 prefer
```

```cisco
show clock
show ntp associations
show ntp status
```

Enterprises commonly operate internal NTP servers that synchronize with approved external sources. Infrastructure devices then synchronize internally.

## 22.16 Syslog

Syslog carries device event messages to a central collector. Traditional Syslog commonly uses UDP 514, although TCP and protected transport options also exist.

Central logging preserves events when a device restarts or is compromised and allows many systems to be searched together.

| Level | Name | Meaning |
|---:|---|---|
| 0 | Emergencies | System unusable |
| 1 | Alerts | Immediate action required |
| 2 | Critical | Critical condition |
| 3 | Errors | Error condition |
| 4 | Warnings | Warning condition |
| 5 | Notifications | Normal but significant |
| 6 | Informational | Informational message |
| 7 | Debugging | Detailed debugging |

Lower numbers are more severe. Selecting level 4 normally includes levels 0 through 4.

```cisco
service timestamps log datetime msec
logging host 10.20.50.20
logging trap warnings
logging source-interface Vlan50
```

Use `show logging` to verify. Debug-level logging may create excessive load, bandwidth usage, and storage consumption.

## 22.17 Simple Network Management Protocol

SNMP allows a network management system to monitor and, where permitted, manage devices.

| Component | Function |
|---|---|
| Manager/NMS | Polls devices, stores data, displays status, receives alerts |
| Agent | Software on the managed device |
| MIB | Structured collection of managed objects |
| OID | Identifier for a managed object |
| Trap/Inform | Device-generated notification |

SNMP commonly uses UDP 161 for queries and UDP 162 for traps or informs.

| Version | Security |
|---|---|
| SNMPv1 | Legacy community strings; no modern protection |
| SNMPv2c | Better operation; community strings; no encryption |
| SNMPv3 | User authentication, integrity, and privacy encryption |

Prefer SNMPv3. Avoid read-write access unless required and strongly protected. Restrict SNMP to approved monitoring systems.

```cisco
show snmp
show snmp user
show snmp group
```

An NMS can poll utilization, errors, CPU, memory, temperature, uptime, and availability. Traps provide event-driven notification, but polling remains important because traps can be lost.

## 22.18 Essential Services Working Together

During an unauthorized login attempt:

1. NTP gives the switch accurate time.
2. AAA rejects the identity and records the attempt.
3. Syslog sends the event to a central collector.
4. Monitoring may alert the operations team.
5. An ACL ensures only the management subnet can initiate SSH.
6. SSH protects valid administrator sessions.

Prevention, detection, accountability, and investigation become connected.

## 22.19 Windows and Linux Verification

Windows:

```powershell
Test-NetConnection 10.20.50.2 -Port 22
w32tm /query /status
Get-NetTCPConnection
arp -a
ssh netadmin@10.20.50.2
```

Linux:

```bash
ssh netadmin@10.20.50.2
timedatectl status
chronyc sources
ip neigh
ss -tulpen
journalctl -p warning
```

`Test-NetConnection` tests a specific TCP port. Windows Time or Linux time-service commands verify synchronization. `arp -a` and `ip neigh` display local address mappings useful when investigating spoofing or connectivity.

## 22.20 Enterprise Case Study

A growing office has staff, Finance, server, guest, voice, and management VLANs. Every user can reach Finance, Telnet is enabled, unused ports remain active, a test router offers unauthorized DHCP settings, and logs have inconsistent time.

The network team applies an extended ACL near user sources to permit only approved HTTPS traffic to Finance. Management traffic is restricted to the management VLAN.

Administrators configure AAA and SSH, disable Telnet and unused services, and shut inactive ports into a parking VLAN. DHCP snooping trusts only the legitimate server path; DAI validates ARP against learned bindings.

Finally, all devices use internal NTP, central Syslog, and SNMPv3 monitoring. The result is enforced policy, reduced exposure, trustworthy address assignment, monitored health, and usable audit evidence.

## 22.22 TROUBLESHOOTING METHOD

When security causes unexpected loss of connectivity, do not remove every control. Use this process:

1. Define expected communication.
2. Identify source, destination, protocol, and port.
3. Verify Layer 1, VLAN, addressing, gateway, and routing.
4. Identify ingress and egress interfaces.
5. Inspect ACL sequence, direction, and counters.
6. Check port-security state and learned addresses.
7. Check DHCP snooping bindings and trusted ports.
8. Check DAI statistics and static-IP exceptions.
9. Compare logs using synchronized timestamps.
10. Make one controlled correction and retest.

A feature may be working exactly as configured but not as intended. Compare configuration with documented policy.

## 22.23 CYBERSECURITY, CLOUD, CAREER, AND EXAM RELEVANCE

ACLs support least privilege and segmentation. AAA improves identity control and accountability. Port security reduces casual unauthorized connection. DHCP snooping and DAI reduce local spoofing opportunities. SSH protects management traffic. NTP and Syslog improve investigation, while SNMPv3 supports protected monitoring.

Cloud security groups and cloud network ACLs use related filtering concepts, but behavior differs by provider. Some security groups are stateful, while traditional router ACLs are commonly stateless. Always verify direction, defaults, scope, and return-traffic behavior.

IT support technicians may encounter locked ports, failed SSH, incorrect time, or DHCP security issues. Network engineers design policy and operate management services. Security analysts use the resulting logs and controls during detection and response.

### CCNA 200-301 and Network+ N10-009 Reminders

- Standard ACLs match source IPv4 only.
- Extended ACLs match protocol, source, destination, and ports.
- Processing is top-down, first-match, with an implicit deny.
- Generally place standard ACLs near the destination and extended ACLs near the source.
- Wildcard `0` means match; `1` means ignore.
- Authentication verifies identity, authorization controls actions, and accounting records activity.
- DHCP snooping blocks unauthorized DHCP server messages and creates bindings.
- DAI validates ARP using trusted information.
- SSH is encrypted; Telnet is not.
- Syslog 0 is most severe and 7 is debugging.
- Prefer SNMPv3.

## 23. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| ACL | Ordered list of permit and deny statements |
| ACE | One rule in an ACL |
| Implicit Deny | Unwritten deny at the end of an ACL |
| Standard ACL | IPv4 ACL matching source address only |
| Extended ACL | IPv4 ACL matching protocol, source, destination, and ports |
| Wildcard Mask | Mask where 0 means match and 1 means ignore |
| AAA | Authentication, authorization, and accounting |
| Authentication | Verification of identity |
| Authorization | Determination of allowed actions |
| Accounting | Recording of access and activity |
| RADIUS | AAA protocol commonly used for network access |
| TACACS+ | AAA protocol commonly used for device administration |
| Port Security | Switch restriction on permitted source MAC addresses |
| Sticky MAC | Dynamically learned secure MAC saved in running configuration |
| Err-disabled | Switch state disabling a port after specified violations |
| DHCP Snooping | DHCP filtering and binding-table security feature |
| Trusted Port | Port permitted to receive authoritative messages |
| DAI | Dynamic ARP Inspection; validates ARP |
| ARP Spoofing | False ARP information used to redirect traffic |
| Device Hardening | Reduction of unnecessary exposure |
| Attack Surface | Collection of points through which a system can be attacked |
| Management Plane | Functions used to administer a device |
| SSH | Encrypted remote CLI protocol using TCP 22 |
| NTP | Time protocol commonly using UDP 123 |
| Stratum | NTP distance level from an authoritative source |
| Syslog | Event-message transport and collection method |
| SNMP | Network monitoring and management protocol |
| NMS | Network management system |
| MIB | Structured collection of managed objects |
| OID | Identifier for an SNMP object |
| Trap | Unsolicited SNMP notification |
| SNMPv3 | SNMP version supporting authentication and encryption |
| Parking VLAN | Unused VLAN assigned to inactive ports |

## 24. COMPARISON TABLES

### 24.1 Standard vs Extended ACL

| Feature | Standard | Extended |
|---|---|---|
| Matches | Source IPv4 | Protocol, source, destination, ports |
| Ranges | 1-99, 1300-1999 | 100-199, 2000-2699 |
| General placement | Near destination | Near source |
| Precision | Lower | Higher |

### 24.2 Port Security vs 802.1X

| Feature | Port Security | 802.1X |
|---|---|---|
| Identity | MAC address | Credentials or certificate |
| Central policy | Limited | Common through RADIUS |
| Best fit | Fixed, simple ports | Enterprise identity-based access |

### 24.3 DHCP Snooping vs DAI

| Feature | DHCP Snooping | DAI |
|---|---|---|
| Protects | DHCP | ARP |
| Threat | Rogue DHCP service | ARP spoofing |
| Relationship | Builds bindings | Uses bindings |

### 24.4 SSH vs Telnet

| Feature | SSH | Telnet |
|---|---|---|
| Port | TCP 22 | TCP 23 |
| Encryption | Yes | No |
| Production use | Recommended | Avoid |

### 24.5 Essential Services

| Service | Purpose | Common Port |
|---|---|---|
| NTP | Time synchronization | UDP 123 |
| Syslog | Event collection | UDP 514 traditionally |
| SNMP | Monitoring | UDP 161; traps UDP 162 |

## 25. REAL-WORLD ANALOGY

In a secure office, an ACL is the visitor policy. AAA checks identity, assigns permitted access, and records the visit. Port security controls registered equipment at each desk. DHCP snooping rejects false office directions, while DAI validates identity-to-location claims. SSH is a private conversation with the manager, NTP keeps every clock aligned, Syslog is the incident book, and SNMP is the building-monitoring console.

## 26. QUICK-RECAP CHEAT SHEET

```text
ACL: top-down, first match, implicit deny
Standard: source only; near destination
Extended: protocol/source/destination/ports; near source
Wildcard: 0 match, 1 ignore
AAA: authenticate, authorize, account
Port security: protect, restrict, shutdown
DHCP snooping: trusted server path + binding table
DAI: validates ARP using bindings
SSH TCP 22; never prefer Telnet
NTP UDP 123; accurate time
Syslog: 0 emergencies through 7 debugging
SNMP: UDP 161; traps 162; prefer v3
```

---

## VPNs and Remote Access Security

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### Virtual Private Network

A Virtual Private Network, or VPN, creates a protected logical connection across a network that is not fully trusted. The untrusted network is commonly the public Internet, but it may also be a service-provider network, shared cloud infrastructure, or another organization's network.

The word **virtual** means the connection is created logically rather than through a dedicated physical cable between the endpoints. **Private** means approved traffic is protected and access is controlled. **Network** means the connection carries communication between devices, users, applications, or entire IP networks.

A VPN does not make the Internet private. It creates a protected tunnel through it.

```text
Private network A
      |
VPN gateway A
      |
====== Encrypted tunnel across untrusted network ======
      |
VPN gateway B
      |
Private network B
```

### Technical Importance: VPNs Exist

Organizations need secure communication beyond the physical office. A company may connect a Lagos headquarters to an Abuja branch, allow an engineer to work from home, connect an on-premises data center to a cloud virtual network, or provide a contractor with controlled application access.

Sending sensitive traffic directly across the Internet creates risks:

- Attackers may capture traffic.
- Data may be altered in transit.
- An unauthorized system may impersonate a trusted endpoint.
- Internal services may be exposed unnecessarily.
- Users may connect from infected or unmanaged devices.

A properly designed VPN can provide confidentiality, integrity, peer authentication, and controlled access. These security properties support the CIA triad introduced in Lesson 19.

### Operation and Deployment Context: VPNs Operate

A VPN normally performs four broad functions:

1. It identifies the traffic that should use the tunnel.
2. It authenticates the VPN peer, user, or both.
3. It encapsulates and protects the original traffic.
4. It sends the protected packet across the untrusted network.

VPN components may exist on routers, firewalls, dedicated VPN concentrators, cloud gateways, or endpoint software.

| Component | Purpose |
|---|---|
| VPN gateway | Terminates tunnels and enforces VPN policy |
| VPN client | Software that establishes remote-user connectivity |
| Identity service | Authenticates users or devices |
| PKI/certificate authority | Issues and validates digital certificates |
| Firewall/ACL | Restricts traffic before and after tunnel termination |
| Routing system | Directs protected networks toward the tunnel |
| Logging/monitoring | Records tunnel status, authentication, and security events |

## 23.4 The Security Services of a VPN

### 23.4.1 Confidentiality

Encryption transforms readable plaintext into ciphertext. A party without the correct key should not be able to understand captured traffic.

Encryption protects data in transit, but it does not repair an infected endpoint or prevent an authorized user from mishandling data after decryption.

### 23.4.2 Integrity

Integrity protection allows a recipient to detect unauthorized modification. If an attacker changes a protected packet in transit, the integrity check should fail and the packet should be rejected.

### 23.4.3 Authentication

Peer authentication verifies the identity of VPN gateways. User authentication verifies the person or account requesting remote access. Authentication methods include:

- Pre-shared keys
- Digital certificates
- Passwords
- One-time codes
- Hardware or software tokens
- Multifactor authentication

Pre-shared keys can be practical in small deployments, but unique certificates scale more effectively and avoid distributing the same secret to many peers.

### 23.4.4 Anti-Replay Protection

An attacker may capture a valid protected packet and transmit it again. Anti-replay mechanisms use sequence information and a sliding window to detect and reject duplicated or excessively old packets.

### 23.4.5 Authorization

A successful VPN login should not provide unrestricted access. Authorization determines which networks, applications, and ports the identity may reach. The AAA and ACL concepts in this lesson therefore remain important after the tunnel forms.

## 23.5 Tunneling, Encapsulation, and Encryption

Tunneling places an original packet inside another packet so that it can cross an intermediate network.

```text
Original private packet
[Original IP header][TCP/UDP header][Data]

After VPN protection
[New outer IP header][VPN security information][Protected original packet]
```

The outer header is used to route the packet across the public network. The original packet is carried inside the protected payload.

Tunneling and encryption are related but not identical:

- **Tunneling** creates the logical path through encapsulation.
- **Encryption** protects confidentiality.
- **Integrity checking** detects modification.
- **Authentication** verifies an identity.

Some tunneling protocols do not encrypt data by themselves. For example, GRE provides flexible encapsulation but does not provide confidentiality. It must be combined with a security protocol such as IPsec when encryption is required.

## 23.6 Site-to-Site VPN

A site-to-site VPN connects entire networks through VPN gateways. End devices usually do not run VPN software or know that encryption is occurring.

```text
Headquarters LAN        Branch LAN
192.168.10.0/24         192.168.20.0/24
       |                      |
   HQ gateway ========== Branch gateway
             IPsec tunnel
```

When a headquarters host sends traffic to the branch subnet, the headquarters gateway identifies it as protected traffic, encrypts it, and sends it to the branch gateway. The branch gateway verifies, decrypts, and forwards the original packet.

### Deployment Context: Site-to-Site VPNs Are Used

- Headquarters-to-branch connectivity
- Data-center interconnection
- Business-to-business partner connections
- On-premises-to-cloud hybrid networking
- Backup paths across a secondary ISP
- Temporary secure connection during a migration

### 23.6.2 Benefits and Limitations

| Benefit | Explanation |
|---|---|
| Transparent to users | Gateways protect traffic automatically |
| Network-to-network reachability | Many hosts can communicate through one tunnel |
| Uses available Internet links | Dedicated private circuits may not be required |
| Central policy | Gateways enforce encryption and filtering |

Site-to-site VPN performance depends on Internet quality, gateway capacity, cryptographic processing, packet size, and routing. A VPN does not guarantee the bandwidth or latency of a private leased circuit.

## 23.7 Client-to-Site VPN

A client-to-site VPN, also called a remote-access VPN, connects one endpoint to an organization's VPN gateway.

```text
Remote laptop
     |
VPN client
     |
Internet
     |
Remote-access VPN gateway
     |
Approved internal resources
```

The user starts a VPN client or uses an operating-system VPN function. The gateway authenticates the user and possibly the device. If access is approved, the endpoint receives tunnel parameters, routes, DNS settings, and an address from a VPN pool.

### 23.7.1 Common Uses

- Employees working from home
- Engineers providing approved after-hours support
- Traveling staff using public Wi-Fi
- Contractors reaching a limited project environment
- Administrators managing systems through a controlled path

Remote access creates higher endpoint risk than a gateway-to-gateway tunnel because the remote computer may be outside the organization's physical control. Strong authentication, endpoint security, posture assessment, least privilege, and monitoring are essential.

## 23.8 Remote-Access Connection Process

A typical connection proceeds as follows:

1. The client discovers and contacts the VPN gateway.
2. The client and gateway negotiate supported security settings.
3. The gateway presents its identity, commonly through a certificate.
4. The user and possibly the device authenticate.
5. Authorization policy determines permitted access.
6. Session keys are created.
7. The gateway supplies an address, routes, and DNS settings.
8. Protected traffic begins.
9. The gateway logs session events and enforces timeouts.
10. Keys and security associations are renewed or removed when the session ends.

The exact process varies by VPN technology, but the security goals remain similar.

## 23.9 Full-Tunnel and Split-Tunnel VPN

Routing policy determines which client traffic enters the VPN.

### 23.9.1 Full Tunnel

In a full-tunnel design, most or all endpoint traffic is sent through the organization's VPN gateway, including general Internet traffic.

```text
Remote user --> encrypted tunnel --> company gateway --> Internet/internal systems
```

This allows company security controls to inspect and log Internet access. It increases VPN bandwidth demand and may add latency.

### 23.9.2 Split Tunnel

In a split-tunnel design, traffic for protected company networks enters the VPN while other Internet traffic exits through the user's local connection.

```text
Company traffic --> VPN tunnel
Public Internet traffic --> local Internet gateway
```

Split tunneling reduces gateway load and often improves cloud-application performance. However, the endpoint simultaneously communicates with trusted and untrusted networks, so endpoint controls and policy become especially important.

| Feature | Full Tunnel | Split Tunnel |
|---|---|---|
| Internet traffic path | Through organization | Through local Internet |
| Central inspection | Greater | Reduced for local traffic |
| VPN bandwidth use | Higher | Lower |
| Typical latency | May be higher | Often lower for public cloud/SaaS |
| Endpoint security importance | High | Especially high |

The correct choice depends on risk, bandwidth, regulatory requirements, and application architecture.

## 23.10 IPsec Fundamentals

Internet Protocol Security, or IPsec, is a suite of standards used to protect IP communication. It is widely used for site-to-site VPNs and can also support remote access.

IPsec is not one encryption algorithm or one protocol. It is a framework that combines:

- Peer authentication
- Security parameter negotiation
- Key establishment
- Confidentiality
- Integrity
- Anti-replay protection

### 23.10.1 Security Association

A Security Association, or SA, is a set of agreed security parameters used to protect traffic in one direction. Because an SA is unidirectional, normal two-way communication requires separate inbound and outbound SAs.

An SA can define algorithms, keys, lifetime, mode, and protected traffic. Security associations are replaced periodically so that one key is not used indefinitely.

### 23.10.2 IPsec Protocol Numbers and Supporting Ports

| Function | Protocol/Port |
|---|---|
| ESP | IP protocol 50 |
| AH | IP protocol 51 |
| IKE | UDP 500 |
| NAT Traversal | UDP 4500 |

ESP and AH are IP protocols, not TCP or UDP ports. This distinction is frequently tested.

## 23.11 Encapsulating Security Payload

Encapsulating Security Payload, or ESP, is the primary IPsec protocol used in modern VPNs. ESP can provide:

- Confidentiality through encryption
- Integrity
- Data-origin authentication
- Anti-replay protection

ESP does not encrypt the new outer IP header in tunnel mode because routers need that header to forward the packet across the Internet.

## 23.12 Authentication Header

Authentication Header, or AH, provides integrity, data-origin authentication, and anti-replay protection, but it does not encrypt the payload.

AH also protects selected IP-header fields. NAT changes IP header information, which makes AH incompatible with normal NAT operation. ESP is therefore much more common in practical VPN deployments.

## 23.13 Transport Mode and Tunnel Mode

### 23.13.1 Transport Mode

Transport mode protects the upper-layer payload of the original IP packet while retaining the original IP header. It is commonly associated with host-to-host protection.

```text
[Original IP header][Protected transport data]
```

### 23.13.2 Tunnel Mode

Tunnel mode protects the entire original IP packet and adds a new outer IP header. It is commonly used between VPN gateways.

```text
[New IP header][IPsec information][Protected original IP packet]
```

| Feature | Transport Mode | Tunnel Mode |
|---|---|---|
| Original IP header | Remains outer header | Protected inside tunnel |
| New outer IP header | No | Yes |
| Common use | Host-to-host | Gateway-to-gateway, remote access |
| Overhead | Lower | Higher |

## 23.14 Internet Key Exchange

Internet Key Exchange, or IKE, negotiates IPsec security parameters and establishes keys. Rather than manually configuring every short-lived encryption key, peers use IKE to authenticate and derive shared session keys securely.

### 23.14.1 IKEv1 and IKEv2

IKEv2 is newer, more efficient, and generally preferred where supported. It uses fewer exchanges, handles mobility and address changes more effectively, and simplifies negotiation compared with IKEv1.

At a conceptual level:

1. The peers agree on cryptographic algorithms.
2. They perform a key exchange.
3. They authenticate one another.
4. They create an IKE SA.
5. They negotiate child SAs used to protect application traffic.

Students should understand the process and verification logic before memorizing vendor-specific syntax.

## 23.15 Cryptographic Building Blocks

### 23.15.1 Symmetric Encryption

Symmetric encryption uses a shared secret key for encryption and decryption. It is efficient for protecting large amounts of VPN data. AES is a widely used example.

### 23.15.2 Asymmetric Cryptography

Asymmetric cryptography uses a public key and a private key. It supports digital signatures, certificates, and secure identity verification. It is computationally heavier than symmetric encryption, so VPNs commonly use asymmetric methods during establishment and symmetric keys for the data session.

### 23.15.3 Hashing and Integrity

A cryptographic hash produces a fixed-length digest from input data. Integrity mechanisms such as HMAC combine a hash function with a secret key to detect modification and authenticate the source of protected data.

### 23.15.4 Diffie-Hellman Key Exchange

Diffie-Hellman allows two peers to derive shared key material across an untrusted network without transmitting the resulting shared secret directly. Strong, supported groups should be selected according to current organizational policy.

### 23.15.5 Perfect Forward Secrecy

Perfect Forward Secrecy, or PFS, generates fresh key material for new security associations. Compromise of one long-term key should not automatically reveal previously protected sessions.

## 23.16 NAT Traversal

Traditional IPsec can experience problems when a NAT device changes packet addressing. NAT Traversal, or NAT-T, encapsulates IPsec ESP traffic inside UDP, commonly using port 4500.

```text
Original ESP packet
        |
NAT is detected
        |
ESP is carried inside UDP 4500
        |
NAT device can maintain the translation
```

Firewalls along the path may need to allow UDP 500 for IKE and UDP 4500 for NAT-T. Opening only TCP 443 does not automatically permit a traditional IPsec tunnel.

## 23.17 Interesting Traffic and VPN Policy

In policy-based IPsec designs, "interesting traffic" means traffic selected for VPN protection. ACL-like rules may identify the local and remote protected subnets.

For example:

```text
Local protected subnet:  192.168.10.0/24
Remote protected subnet: 192.168.20.0/24
```

The peer configurations must agree. If one side defines `/24` and the other defines only one host, the tunnel may establish partially or fail to pass expected traffic.

Interesting-traffic classification is not necessarily the same as a firewall permission. A crypto policy identifies what should be encrypted; a security policy determines what is allowed. Both must be correct.

## 23.18 Policy-Based and Route-Based VPNs

### Policy-Based VPN

A policy-based VPN selects protected traffic through policy entries or crypto ACLs. It is straightforward for a small number of subnet pairs but becomes difficult to manage as networks grow.

### Route-Based VPN

A route-based VPN uses a logical tunnel interface. Normal routing sends destination networks toward that interface. It can simplify dynamic routing, redundancy, and many-network designs.

| Feature | Policy-Based | Route-Based |
|---|---|---|
| Traffic selection | Crypto policy/ACL | Routing table |
| Logical tunnel interface | Usually no | Yes |
| Scalability | Best for simpler pairs | Better for complex topology |
| Dynamic routing | More difficult | Commonly supported |
| Troubleshooting focus | Selectors and policy | Routes, interface, and SAs |

Platform terminology and implementation vary, so engineers must consult the applicable vendor design.

## 23.19 VPN Routing, NAT, DNS, and MTU

A tunnel can be established while applications still fail. The protected data path also depends on routing, NAT, DNS, and packet size.

### Routing

Each side needs a route to the remote protected network. Remote-access clients need routes for full or split tunneling. Overlapping subnets create ambiguity: if a home user's LAN and the company both use `192.168.1.0/24`, the endpoint may send traffic to the wrong interface.

### NAT

Site-to-site protected traffic is often exempted from normal Internet PAT. If the source is translated before VPN selection, the traffic may no longer match the expected protected subnet.

### DNS

Remote clients may require internal DNS servers and search suffixes. A tunnel can pass IP traffic while users report failure because internal names do not resolve.

### MTU and Fragmentation

VPN encapsulation adds headers and increases packet size. A packet that fit the physical interface MTU before encryption may become too large afterward. Symptoms can include small pings working while large transfers, web pages, or applications fail. Path MTU Discovery, TCP MSS adjustment, and correct ICMP handling may be relevant.

## 23.20 Remote Access Authentication and Authorization

Passwords alone are weak protection for Internet-facing remote access. Multifactor authentication, or MFA, requires evidence from more than one factor category:

| Factor | Example |
|---|---|
| Something you know | Password or PIN |
| Something you have | Token, phone, smart card |
| Something you are | Fingerprint or other biometric |

Two passwords are not two factors because both are knowledge factors.

Remote access can integrate with RADIUS, directory services, certificates, identity providers, and conditional-access systems. Authorization should map users to only the resources required by their role.

Examples:

- Finance users may reach the finance application.
- Help desk may reach approved support tools.
- Contractors may reach one project subnet during defined hours.
- Network administrators may reach management systems through a separate privileged policy.

## 23.21 Network Access Control

Network Access Control, or NAC, is a framework for deciding whether a user or device may connect and what level of network access it should receive.

VPN authentication answers, "Is this identity allowed to establish a session?" NAC expands the decision:

```text
Who is the user?
What device is being used?
Is the device managed?
Does it meet security policy?
Where and how is it connecting?
What access should it receive?
```

### 23.21.1 NAC Components

| Component | Role |
|---|---|
| Endpoint/supplicant | Requests access and may report posture |
| Enforcement point | Switch, WLAN controller, or VPN gateway |
| Policy server | Evaluates identity, device, posture, and policy |
| Identity store | Directory or identity provider |
| Posture service | Checks endpoint compliance |
| Remediation service | Helps noncompliant devices become compliant |

### 23.21.2 Pre-Admission and Post-Admission Control

Pre-admission control evaluates the endpoint before normal access is granted. Post-admission control continues monitoring after connection and can change access if risk or compliance changes.

### 23.21.3 Endpoint Posture

Posture checks may assess:

- Supported operating-system version
- Required security updates
- Active endpoint protection
- Host firewall status
- Disk encryption
- Device certificate
- Mobile-device-management enrollment
- Indicators that the device is rooted or jailbroken

Posture data must be collected with clear privacy, legal, and operational policy.

### 23.21.4 Enforcement Outcomes

NAC does not only allow or deny. It may:

- Grant normal role-based access
- Assign a VLAN or downloadable ACL
- Place the device in a restricted network
- Redirect it to remediation
- Allow guest Internet access only
- Quarantine a risky endpoint
- Terminate an existing session

## 23.22 VPN Security Risks and Controls

| Risk | Control |
|---|---|
| Stolen password | MFA, risk-based login, account monitoring |
| Rogue gateway | Certificate validation and trusted configuration |
| Infected remote endpoint | EDR, posture checks, least privilege |
| Excessive remote access | Role-based authorization and ACLs |
| Weak cryptography | Approved algorithms and lifecycle management |
| Shared pre-shared key | Unique certificates or carefully managed secrets |
| Unpatched VPN gateway | Vulnerability management and timely updates |
| Brute-force attempts | MFA, rate limits, lockout policy, monitoring |
| Split-tunnel exposure | Endpoint firewall, DNS/web protection, EDR |
| Forgotten contractor account | Expiration, sponsorship, access review |

VPN gateways are Internet-facing security devices and attractive attack targets. They require hardening, patching, restricted administration, configuration backup, central logging, and continuous monitoring.

## 23.23 Site-to-Site Enterprise Design Example

A company has:

```text
Lagos HQ:   10.10.0.0/16
Abuja site: 10.20.0.0/16
```

Each site has an Internet connection and an edge firewall. The design process is:

1. Confirm that private address spaces do not overlap.
2. Define approved subnet and application flows.
3. Select compatible IKE/IPsec settings.
4. Choose certificates or strong unique peer credentials.
5. Configure protected-network selectors or tunnel routing.
6. Exempt protected traffic from Internet PAT where required.
7. Permit IKE, NAT-T, and ESP as needed.
8. Apply firewall policy inside the tunnel.
9. Configure redundant monitoring and logging.
10. Test failover, performance, rekeying, and recovery.

The tunnel should not automatically allow every HQ device to reach every branch device. Segmentation and least privilege remain necessary.

## 23.24 Remote-Worker Enterprise Design Example

A company supports staff using managed Windows laptops. The remote-access design requires:

- Company-issued device certificate
- User credentials and MFA
- Endpoint protection and disk encryption
- Automatic VPN profile
- Internal DNS and approved routes
- Role-based access
- Session timeout and reauthentication
- Central authentication and VPN logs
- Help-desk recovery procedure

A Finance employee receives access to finance services. A contractor receives only a project application. A failed posture check places the device into remediation rather than unrestricted production access.

This design verifies identity, device trust, and business need instead of treating possession of a password as sufficient.

## 23.25 Windows VPN and Route Verification

Windows includes built-in VPN support, and organizations may deploy vendor clients.

Useful PowerShell commands:

```powershell
Get-VpnConnection
Get-NetIPConfiguration
Get-NetRoute
Get-DnsClientServerAddress
Test-NetConnection 10.20.30.10 -Port 443
Resolve-DnsName intranet.example.local
tracert 10.20.30.10
```

`Get-VpnConnection` shows configured Windows VPN profiles. `Get-NetRoute` reveals whether a protected destination uses the VPN interface. `Test-NetConnection` tests a specific application port. Name-resolution tests determine whether the problem is DNS rather than the tunnel.

## 23.26 Linux VPN and Route Verification

Linux clients may use NetworkManager, strongSwan, OpenVPN, WireGuard, or vendor software depending on organizational design.

Useful commands:

```bash
ip address
ip route
ip route get 10.20.30.10
resolvectl status
ping -c 4 10.20.30.10
tracepath 10.20.30.10
ss -tulpen
journalctl -u NetworkManager
```

For an IPsec implementation, platform-specific commands may display IKE and child SAs. Engineers must avoid exposing keys or sensitive configuration in tickets and screenshots.

## 23.27 Cisco IOS Conceptual Verification

Exact commands depend on platform and configuration style. Common IOS/IKEv2 and IPsec verification commands include:

```cisco
show crypto ikev2 sa
show crypto ipsec sa
show crypto session
show access-lists
show ip route
show ip nat translations
show logging
```

Important evidence includes:

- Peer address
- IKE SA state
- IPsec SA state
- Encapsulation and decapsulation counters
- Authentication or negotiation errors
- Selected protected networks
- Routes to the destination
- NAT behavior

Rising encapsulation but zero decapsulation may indicate that packets leave but no protected return traffic arrives. Counters are evidence, not a complete diagnosis.

## 23.28 VPN Troubleshooting Method

Troubleshoot in layers.

### Stage 1: Underlay Reachability

Can each VPN endpoint reach the other's public address? Check interfaces, public addressing, ISP service, routing, and upstream filtering.

### Stage 2: IKE Negotiation

Do the peers agree on version, algorithms, authentication, identity, and credentials? Check clock accuracy and certificate validity.

### Stage 3: IPsec Security Associations

Do protected-traffic selectors, transforms, and lifetimes agree? Is NAT-T required? Are ESP or UDP 4500 permitted?

### Stage 4: Protected Data Path

Check routes, NAT exemption, firewall policy, ACLs, encryption/decryption counters, and return routes.

### Stage 5: Application Services

Check DNS, required ports, server policy, endpoint firewall, MTU, and application authentication.

| Symptom | Likely Investigation |
|---|---|
| Gateway unreachable | Internet, route, DNS, upstream firewall |
| Authentication fails | Credentials, MFA, certificate, AAA |
| IKE up but no IPsec SA | Selectors, transforms, policy mismatch |
| Tunnel up but no traffic | Routes, NAT, ACL, firewall, return path |
| One subnet works | Missing route or selector for other subnet |
| IP works but name fails | VPN DNS settings or DNS reachability |
| Small traffic works, large fails | MTU, fragmentation, blocked ICMP |
| Disconnects regularly | Rekey/lifetime mismatch, unstable link |
| Remote user reaches too much | Authorization or split-tunnel policy |

## 23.29 PRACTICAL LABS

### Lab 1: Site-to-Site VPN Design Worksheet

Given two sites, document:

- Public peer addresses
- Local and remote protected subnets
- IKE version
- Authentication method
- Encryption and integrity policy
- NAT exemption requirement
- Firewall requirements
- Verification commands
- Rollback and escalation plan

Draw both the outer public packet path and the inner protected packet path.

### Lab 3: Remote-Access Policy Design

Create three user roles: employee, contractor, and administrator. For each role, define authentication, MFA, posture, permitted resources, split/full-tunnel policy, session timeout, and logging.

The goal is to show that successful authentication does not mean unrestricted authorization.

### Lab 4: Client Troubleshooting

Using Windows or Linux route and DNS commands:

1. Record routes before connection.
2. Connect to an available lab VPN or use a supplied sample output.
3. Record the new interface, address, routes, and DNS servers.
4. Test a protected IP and hostname.
5. Determine whether the design uses full or split tunneling.
6. Diagnose a provided route, DNS, or MTU fault.

## 23.30 Cybersecurity Relevance

VPNs reduce exposure of data in transit, but they can also create an authenticated path around perimeter controls. A compromised remote endpoint may use that path to reach internal systems. Therefore, modern remote access combines encryption with identity, MFA, endpoint detection, posture, segmentation, least privilege, and monitoring.

Security teams monitor unusual countries, impossible travel, repeated MFA failures, new devices, excessive session duration, abnormal data transfer, and access outside a user's role.

Zero Trust does not mean that VPNs disappear. It means network location or tunnel establishment alone should not create unlimited trust. Access decisions should consider identity, device, resource, and context.

## 23.31 Cloud Networking Relevance

Cloud providers commonly offer managed site-to-site VPN gateways and remote-access services. A hybrid design may connect an office firewall to a cloud virtual network.

Cloud VPN design still requires:

- Non-overlapping address plans
- Customer and cloud gateway configuration
- Static or dynamic routing
- Redundant tunnels
- Security groups and network filtering
- Route-table updates
- Monitoring and logs
- Bandwidth and availability planning

Route-based VPNs and BGP are common in resilient hybrid designs. Encryption does not replace cloud security groups, IAM, or workload hardening.


IT support staff frequently diagnose failed authentication, missing routes, wrong DNS, expired certificates, MFA problems, and endpoint posture failures. Network engineers troubleshoot peer negotiation, routing, NAT, SAs, and performance. Cybersecurity teams review remote access policy and logs.

Common interview questions include:

- Site-to-site versus client-to-site VPN
- Full tunnel versus split tunnel
- Tunneling versus encryption
- ESP versus AH
- Tunnel mode versus transport mode
- IKE, SAs, NAT-T, and PFS
- Why a tunnel can be up while applications fail
- How NAC evaluates identity and posture

### CCNA 200-301 and Network+ N10-009 Reminders

- A VPN is a protected logical connection across an untrusted network.
- Site-to-site connects networks; client-to-site connects an endpoint.
- ESP commonly provides confidentiality, integrity, authentication, and anti-replay.
- AH does not encrypt and is not NAT-friendly.
- Tunnel mode protects the original IP packet and adds a new outer header.
- IKE negotiates parameters, authenticates peers, and establishes keys.
- IKE commonly uses UDP 500; NAT-T commonly uses UDP 4500.
- ESP is IP protocol 50, not TCP or UDP port 50.
- Full tunnel sends general traffic through the organization; split tunnel separates protected and local Internet traffic.
- NAC considers identity, device, posture, context, and required access.
- MFA must use different factor categories.

## 24. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| VPN | Protected logical connection across an untrusted network |
| Tunnel | Logical path created by encapsulating traffic |
| Encapsulation | Placing one packet inside another |
| Encryption | Transformation of plaintext into protected ciphertext |
| Ciphertext | Encrypted, unreadable form of data |
| Peer Authentication | Verification of the remote VPN endpoint |
| Anti-Replay | Protection against retransmission of captured valid packets |
| Site-to-Site VPN | VPN connecting two or more networks through gateways |
| Client-to-Site VPN | VPN connecting one endpoint to an organization |
| Remote Access | Connectivity for users or devices outside the local site |
| VPN Concentrator | Device or service terminating many VPN sessions |
| Full Tunnel | Policy sending most or all client traffic through the VPN |
| Split Tunnel | Policy sending only selected traffic through the VPN |
| IPsec | Standards framework for protecting IP communication |
| SA | Security Association containing negotiated protection parameters |
| ESP | IPsec protocol providing encryption and optional integrity/authentication |
| AH | IPsec protocol providing integrity/authentication without encryption |
| Tunnel Mode | IPsec mode protecting the entire original IP packet |
| Transport Mode | IPsec mode protecting the upper-layer payload |
| IKE | Protocol for negotiating IPsec security and keys |
| IKEv2 | Modern version of Internet Key Exchange |
| Symmetric Encryption | Encryption using the same secret key for encryption and decryption |
| Asymmetric Cryptography | Cryptography using related public and private keys |
| Digital Certificate | Signed electronic credential binding identity to a public key |
| PKI | System for issuing, validating, and revoking certificates |
| HMAC | Keyed integrity and authentication mechanism based on hashing |
| Diffie-Hellman | Method for deriving shared key material across an untrusted network |
| PFS | Perfect Forward Secrecy; fresh key material for new sessions |
| NAT-T | NAT Traversal; carries IPsec ESP inside UDP 4500 |
| Interesting Traffic | Traffic selected for VPN protection |
| Policy-Based VPN | VPN selecting traffic through crypto policy |
| Route-Based VPN | VPN using a logical tunnel interface and routing |
| MFA | Authentication using more than one factor category |
| NAC | Network Access Control framework |
| Posture Assessment | Evaluation of endpoint compliance and security state |
| Remediation Network | Restricted access used to correct compliance problems |
| Quarantine | Isolation of a risky or noncompliant endpoint |

## 25. COMPARISON TABLES

### 25.1 Site-to-Site vs Client-to-Site

| Feature | Site-to-Site | Client-to-Site |
|---|---|---|
| Connects | Networks | Individual endpoint |
| Tunnel endpoints | VPN gateways | Client and gateway |
| User action | Usually none | Client/user normally connects |
| Main identity | Peer gateway | User and often device |
| Typical use | Branch or cloud link | Remote worker |

### 25.2 ESP vs AH

| Feature | ESP | AH |
|---|---|---|
| Encryption | Yes, when configured | No |
| Integrity/authentication | Supported | Supported |
| NAT compatibility | Supported through NAT-T | Poor |
| Practical use | Common | Rare |

### 25.3 Tunnel vs Transport Mode

| Feature | Tunnel | Transport |
|---|---|---|
| Protects original IP header | Yes, encapsulated inside | No |
| Adds new IP header | Yes | No |
| Common use | Gateway VPN | Host-to-host |

### 25.4 Full vs Split Tunnel

| Feature | Full | Split |
|---|---|---|
| Public Internet path | Company gateway | Local gateway |
| Central inspection | Greater | Lower |
| VPN bandwidth | Higher | Lower |
| Endpoint dependency | High | Especially high |

### 25.5 VPN vs NAC

| Feature | VPN | NAC |
|---|---|---|
| Primary purpose | Protected connectivity | Access decision and enforcement |
| Core question | How is traffic protected? | Who/what should receive which access? |
| Typical inputs | Peer/user identity, crypto policy | Identity, device, posture, context |
| Relationship | Carries authorized remote traffic | May decide remote-access permission |

## 26. REAL-WORLD ANALOGY

A VPN tunnel is like an armored delivery vehicle traveling on public roads. The public road remains shared, but the contents are protected. The outer address tells the road system where the vehicle must go; the protected package inside contains the original destination information.

Authentication checks the driver and receiving facility. Encryption locks the cargo. Integrity seals reveal tampering. Anti-replay rejects a copied delivery ticket. NAC is the security checkpoint that also inspects the driver, vehicle condition, authorization, and destination before deciding whether entry should be normal, restricted, or denied.

## 27. QUICK-RECAP CHEAT SHEET

```text
VPN = protected logical connection across an untrusted network

SITE-TO-SITE
- Gateway to gateway
- Connects entire networks
- Transparent to end devices

CLIENT-TO-SITE
- Endpoint to gateway
- Remote user/device authentication
- Requires strong endpoint controls

IPSEC
- ESP: protocol 50; encryption + security services
- AH: protocol 51; no encryption; NAT problems
- IKE: UDP 500
- NAT-T: UDP 4500
- SA: one-way negotiated protection parameters
- Tunnel mode: protects complete original packet
- Transport mode: protects upper-layer payload

REMOTE ACCESS
- Full tunnel: most/all traffic through company
- Split tunnel: company traffic through VPN, Internet local
- Use MFA, certificates, least privilege, logging

NAC
- Evaluates user, device, posture, location, and context
- Outcomes: permit, restrict, remediate, quarantine, deny

TROUBLESHOOT
1. Underlay/public reachability
2. IKE negotiation
3. IPsec SAs
4. Routes, NAT, ACLs, counters
5. DNS, ports, MTU, application
```

---

## Power and Resilience

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### Network Power Resilience

Network power resilience is the ability of network infrastructure to continue operating, fail safely, and recover predictably when utility power is interrupted or unstable.

Routers, switches, wireless access points, firewalls, servers, storage systems, optical-network terminals, wireless ISP radios, and monitoring systems all depend on electrical power. A perfectly configured network becomes unavailable when its critical devices lose power.

Resilience is broader than buying a UPS. It requires:

- Understanding the electrical load
- Protecting equipment from poor power quality
- Providing short-term and long-term backup power
- Eliminating single points of failure where justified
- Monitoring power systems
- Maintaining batteries and generators
- Documenting shutdown and recovery procedures
- Testing disaster recovery and business continuity plans

### Technical Importance: Power and Resilience Matter

Availability is one objective of the CIA triad introduced in Lesson 19. Users cannot access protected data or services if the network, identity system, DNS server, firewall, or Internet edge is offline.

Power instability can create more than a temporary outage. Repeated abrupt shutdowns may corrupt storage, interrupt software updates, damage power supplies, reset configurations that were not saved, and shorten battery life. Voltage disturbances can destroy multiple devices simultaneously.

In environments with unreliable utility supply, including many offices, schools, clinics, shops, and small data rooms in Nigeria, backup power is part of network design rather than an optional accessory.

### Deployment Context: Resilience Must Be Applied

Power planning should follow the complete service path:

```text
Utility / generator / solar
           |
Protection and transfer equipment
           |
UPS / inverter / battery system
           |
Network rack power distribution
           |
Router - firewall - switch - server - AP
           |
ISP or service-provider equipment
```

Keeping the core switch alive does not preserve Internet service if the ISP modem, optical-network terminal, wireless radio, firewall, or DNS service loses power. The protected load must include every critical dependency.

## 24.4 Electrical Fundamentals for Network Professionals

Network engineers are not automatically qualified electricians. Permanent wiring, earthing, breakers, transfer switches, battery banks, high-voltage DC systems, solar arrays, and generator integration must be designed and installed by qualified professionals according to applicable codes and manufacturer requirements.

Network staff still need enough electrical knowledge to specify loads, identify risks, monitor systems, and communicate requirements.

### 24.4.1 Voltage, Current, Power, and Energy

| Quantity | Symbol | Unit | Meaning |
|---|---|---|---|
| Voltage | V | Volt | Electrical potential difference |
| Current | I | Ampere | Rate of electric charge flow |
| Real power | P | Watt | Power consumed to perform useful work |
| Apparent power | S | Volt-ampere | Product of RMS voltage and current |
| Energy | E | Watt-hour | Power consumed over time |

For a simple DC load:

```text
Power (W) = Voltage (V) x Current (A)
```

Energy over time:

```text
Energy (Wh) = Power (W) x Time (hours)
```

A 200 W network load operating for four hours ideally requires:

```text
200 W x 4 h = 800 Wh
```

The real system needs more than 800 Wh because inverters, batteries, cabling, and power supplies are not 100 percent efficient.

### 24.4.2 Watts and Volt-Amperes

UPS devices are commonly rated in both watts and volt-amperes. Watts represent real power. VA represents apparent power.

```text
Power factor = Watts / Volt-amperes
```

A `1500 VA / 900 W` UPS must stay below both limits. A load of 950 W is too large even if its apparent power remains below 1500 VA.

Do not assume that a 1000 VA UPS can deliver 1000 W. Always read the manufacturer's watt rating and runtime data.

### 24.4.3 AC and DC

Utility and generator output is alternating current, or AC. Batteries and many electronics internally use direct current, or DC. An inverter converts DC from a battery into AC. A charger or rectifier converts AC into controlled DC for charging or powering DC equipment.

Every conversion introduces loss. Reducing unnecessary conversion stages can improve efficiency, but any direct-DC design must use correct voltage regulation, connectors, polarity protection, fusing, and qualified installation.

## 24.5 Power Quality Problems

Power failure is only one electrical threat.

| Problem | Description | Possible Effect |
|---|---|---|
| Blackout | Complete loss of utility power | Immediate shutdown |
| Brownout | Sustained low voltage | Instability, overheating, UPS transfer |
| Sag | Short reduction in voltage | Device reset or malfunction |
| Surge | Longer increase above normal voltage | Stress or damage |
| Spike/transient | Very brief high-voltage event | Component damage |
| Noise | Unwanted electrical interference | Errors, instability |
| Frequency variation | AC frequency outside expected range | UPS/generator incompatibility |

A UPS does not provide identical protection in every design. The topology, input range, filtering, surge protection, grounding, and connected load all matter.

### 24.5.1 Earthing and Surge Protection

Protective earthing provides a controlled path for fault current and supports safety devices. Surge protective devices help divert transient energy. Neither function should be improvised.

Poor earthing can endanger people and equipment. It may also increase problems on copper links between buildings. Fiber-optic cabling provides electrical isolation between buildings and is often preferred for both distance and lightning-risk reasons.

Network cables entering from outdoors, rooftop radios, CCTV systems, and antennas need coordinated lightning and surge protection designed by qualified installers.

## 24.6 Measuring and Classifying the Load

Do not size backup power using guesses alone.

Build an inventory:

| Device | Quantity | Rated/Measured W Each | Total W | Critical? |
|---|---:|---:|---:|---|
| Edge router | 1 | 25 | 25 | Yes |
| Firewall | 1 | 40 | 40 | Yes |
| PoE switch | 1 | 80 base + PoE | Varies | Yes |
| ISP ONT | 1 | 12 | 12 | Yes |
| Server | 1 | 250 | 250 | Depends |
| Monitor | 1 | 30 | 30 | No |

Manufacturer ratings provide a safe planning reference but may represent maximum consumption. A calibrated power meter, managed PDU, UPS telemetry, or device power report can provide measured values.

Loads should be classified:

- **Critical:** Must remain operational.
- **Essential:** May be shed after a defined period.
- **Nonessential:** Should not consume backup capacity.

Desktop printers, kettles, heaters, air conditioners, and unrelated sockets should not be connected to a network UPS unless the system was explicitly engineered for them.

## 24.7 Power over Ethernet and Hidden Load

Power over Ethernet, or PoE, allows a switch to deliver power and data through Ethernet cabling. The switch therefore supplies not only its own electronics but also APs, IP phones, cameras, and other powered devices.

```text
Total switch input load
= switch base consumption
+ delivered PoE power
+ conversion losses
```

A switch drawing 60 W by itself may draw several hundred watts when serving many PoE devices. The configured PoE budget is a maximum capability, not necessarily the present load.

Useful Cisco IOS commands vary by platform but may include:

```cisco
show power inline
show environment
show environment power
show processes cpu
```

When power is limited, critical PoE devices can be prioritized. For example, the reception phone, security camera, and primary AP may have higher priority than a meeting-room phone.

## 24.8 Capacity, Headroom, and Growth

Backup equipment should not be operated continuously at its absolute maximum. Headroom supports startup behavior, battery aging, normal variation, future growth, and safer operation.

A planning process is:

1. Inventory and measure the critical load.
2. Include PoE endpoint demand.
3. Identify startup or peak load.
4. Add documented design headroom.
5. Check both watt and VA ratings.
6. Verify required runtime from manufacturer data.
7. Confirm environmental and expansion requirements.

The exact headroom is an engineering and organizational decision. A common preliminary design may reserve 20 to 30 percent, but manufacturer guidance and professional calculations take priority.

## 24.9 Uninterruptible Power Supply

An Uninterruptible Power Supply, or UPS, supplies temporary power when the input fails and may improve power quality.

A UPS commonly contains:

- Charger/rectifier
- Battery
- Inverter
- Transfer or bypass components
- Monitoring and control electronics

The UPS performs three important jobs:

1. Bridges short outages without service interruption.
2. Provides time for a generator or larger backup system to start.
3. Allows controlled shutdown if power will not return.

### 24.9.1 Standby UPS

A standby, or offline, UPS normally supplies the load from utility power and transfers to the inverter during failure. It is affordable and may suit low-risk endpoints, but it has a transfer time and provides less conditioning.

### 24.9.2 Line-Interactive UPS

A line-interactive UPS can correct some voltage variation without using the battery and transfers to battery during an outage. It is common for network closets and small server rooms.

### 24.9.3 Online Double-Conversion UPS

An online UPS continuously converts input AC to DC and then DC back to AC for the load. This isolates the load from many input disturbances and normally provides no transfer interruption when utility power fails.

It offers strong protection but costs more, produces heat, and has conversion losses.

| Feature | Standby | Line-Interactive | Online Double-Conversion |
|---|---|---|---|
| Normal power path | Utility | Utility with regulation | Through rectifier/inverter |
| Transfer time | Present | Present but short | Effectively none |
| Conditioning | Basic | Moderate | Strong |
| Cost | Lower | Medium | Higher |
| Typical use | Individual low-risk device | Network closet/small server room | Critical infrastructure |

## 24.10 UPS Runtime

UPS VA capacity does not tell the runtime. Runtime depends on the connected watts, battery capacity, battery condition, temperature, inverter efficiency, UPS design, and discharge rate.

Manufacturer runtime charts or calculators are the preferred source for a specific UPS. A simple energy calculation is useful only for preliminary estimation.

Example: critical load is 300 W and required runtime is 30 minutes.

```text
Ideal energy = 300 W x 0.5 h
             = 150 Wh
```

The battery system must provide more than 150 Wh because of losses, discharge characteristics, aging, and reserve. A UPS advertised as 1500 VA may still provide only a short runtime at 300 W if its battery is small.

### 24.10.1 Runtime Objectives

Specify the purpose:

- Bridge a 30-second generator start
- Survive common 10-minute outages
- Keep the Internet edge alive for two hours
- Provide 15 minutes for server shutdown

Without a runtime objective, capacity selection has no clear success criterion.

## 24.11 Battery Fundamentals

### 24.11.1 Battery Capacity

Battery capacity is often stated in ampere-hours:

```text
Nominal watt-hours = Battery voltage x Ampere-hours
```

A nominal `12 V, 100 Ah` battery stores:

```text
12 V x 100 Ah = 1200 Wh nominal
```

This does not mean all 1200 Wh should or can be delivered as usable AC energy. Usable energy depends on battery chemistry, permitted depth of discharge, discharge rate, age, temperature, inverter efficiency, cabling, and low-voltage cut-off.

### 24.11.2 Depth of Discharge

Depth of discharge, or DoD, is the percentage of battery capacity removed during a cycle. Repeated deep discharge can significantly shorten the life of some battery chemistries.

### 24.11.3 State of Charge and State of Health

State of charge estimates how full the battery is now. State of health estimates how its present capability compares with a new battery. A battery can report fully charged but have poor capacity due to age or damage.

### 24.11.4 Common Battery Types

| Type | Characteristics |
|---|---|
| Flooded lead-acid | Lower cost; ventilation and maintenance requirements |
| Sealed lead-acid/VRLA | Common in UPS systems; limited maintenance; heat-sensitive |
| AGM | Sealed lead-acid design with good power delivery |
| Gel | Sealed design requiring compatible charging |
| Lithium iron phosphate | Higher cycle life and usable DoD; higher initial cost; requires BMS |

Battery chemistry must match the charger/inverter profile. Mixing old and new batteries or different capacities and chemistries in one bank creates imbalance and risk.

### 24.11.5 Battery Safety

Battery banks can deliver extremely high fault current. Hazards include fire, electric shock, chemical exposure, toxic gas, burns, and explosion.

Requirements include correctly rated cables, overcurrent protection, disconnects, ventilation where required, physical protection, temperature control, polarity control, battery-management systems, and qualified installation. Never short a battery or place tools across terminals.

## 24.12 Inverter Systems

An inverter converts battery DC into AC for connected equipment. A complete inverter/charger may also charge batteries and transfer between utility, generator, solar, and battery sources.

### 24.12.1 Waveform

Sensitive IT equipment generally operates best with a true or pure sine-wave output. Modified sine-wave products may cause noise, heat, malfunction, or incompatibility in some power supplies.

### 24.12.2 Inverter Rating

Check:

- Continuous watt rating
- Surge rating and duration
- DC input voltage
- AC output voltage and frequency
- Efficiency curve
- Charger capacity and supported chemistry
- Transfer time
- Communications and monitoring
- Environmental limits

Do not size an inverter using only its marketing VA number.

### 24.12.3 Preliminary Battery Runtime Calculation

Suppose the critical network load is 400 W and the goal is four hours. Assume, for preliminary planning only:

- 90 percent inverter efficiency
- 80 percent usable battery fraction

Required nominal battery energy:

```text
Required Wh
= (Load W x Hours) / (Efficiency x Usable fraction)

= (400 x 4) / (0.90 x 0.80)
= 1600 / 0.72
= approximately 2222 Wh
```

At a nominal 24 V:

```text
Required Ah = 2222 Wh / 24 V
            = approximately 92.6 Ah
```

This is not a final installation specification. Battery aging, peak load, temperature, cable loss, actual discharge curves, reserve, manufacturer limits, and growth must be included by a qualified designer.

## 24.13 Solar Integration

A solar power system can extend runtime and reduce dependence on utility supply or fuel.

```text
Solar panels
     |
Charge controller / hybrid inverter
     |
Battery bank
     |
Inverter output
     |
Critical network loads
```

The panels generate DC energy. A charge controller manages battery charging. A hybrid inverter may coordinate solar, batteries, utility, and generator power.

### 24.13.1 Solar Energy Estimation

Daily load energy:

```text
Daily Wh = Average load W x operating hours
```

For a 300 W load operating continuously:

```text
300 W x 24 h = 7200 Wh/day = 7.2 kWh/day
```

If preliminary planning assumes five effective peak-sun-hours:

```text
Ideal panel power = 7200 Wh / 5 h
                  = 1440 W
```

The actual array must be larger to account for temperature, dust, wiring, controller and inverter loss, battery charging, weather, panel orientation, aging, and required reserve. Local site survey and solar-resource data are necessary.

### 24.13.2 Solar Is Not Automatically Backup Power

A grid-tied solar system may shut down during a utility outage for anti-islanding safety. Backup operation requires an architecture specifically designed to form and control an isolated power system, usually with a compatible inverter and storage.

Students must not assume that visible solar panels mean the network remains powered during blackout.

### 24.13.3 Nigerian Operational Considerations

Practical considerations may include:

- Long utility outages
- Generator fuel availability and quality
- High ambient temperature
- Dust reducing solar output and blocking ventilation
- Lightning and surge exposure
- Physical security of panels and batteries
- Access to trained maintenance personnel
- Replacement battery availability
- Harmonic or frequency quality from generators

Design should match local operating reality, not only laboratory conditions.

## 24.14 Generator Integration

A generator provides longer-duration power when fuel and maintenance are available. A UPS bridges the starting and transfer interval and protects critical loads from interruption.

```text
Utility fails
     |
UPS immediately supports load
     |
Generator starts and stabilizes
     |
Transfer system connects generator
     |
UPS accepts input and recharges
```

Generator integration requires correctly designed transfer switching so that generator output cannot back-feed the utility supply. Generator voltage, frequency, waveform quality, grounding arrangement, capacity, and load steps must be compatible with the UPS and facility.

An oversized UPS charger may place a large load on the generator while batteries recharge. Capacity planning must include both the live equipment and charging demand.

Fuel storage, exhaust, ventilation, noise, emissions, fire safety, test schedules, and refueling during prolonged incidents are business continuity issues.

## 24.15 Automatic Transfer Switch and Bypass

An Automatic Transfer Switch, or ATS, transfers a load between approved power sources. Transfer behavior, interlocking, switching time, neutral treatment, and source compatibility must be engineered.

A maintenance bypass can allow qualified staff to service a UPS without shutting down the protected load. Incorrect bypass operation can remove power protection or create dangerous conditions, so procedures and labeling are essential.

## 24.16 Power Distribution in the Network Rack

A Power Distribution Unit, or PDU, distributes power within a rack. PDUs may be:

- Basic
- Metered
- Monitored over the network
- Switched for controlled outlet operation

Dual-power-supply equipment should use separate power paths where the resilience design justifies it:

```text
Device PSU A --> UPS/PDU path A
Device PSU B --> UPS/PDU path B
```

Connecting both supplies to the same PDU and same UPS protects against one power-supply failure but not against PDU or UPS failure.

Do not overload sockets, extension cords, PDUs, breakers, UPS outlets, or phases. Cable management must not block airflow or create trip and fire hazards.

## 24.17 Cooling and Environmental Resilience

Network equipment converts electrical power into heat. A room can retain power and still fail because cooling stops.

Monitor:

- Room and rack inlet temperature
- Humidity
- Device temperature
- Fan state
- Airflow obstruction
- Water leakage
- Smoke/fire alarms
- Door access

Common environmental threats include failed air conditioning, dust, blocked filters, leaking roofs, flooding, rodents, construction debris, and unauthorized access.

High temperature accelerates battery aging. Battery and UPS runtime claims are usually based on specified environmental conditions, not a hot unventilated cupboard.

## 24.18 Monitoring Power Systems

Managed UPS, PDU, inverter, environmental sensor, and generator systems may report:

- Input and output voltage
- Frequency
- Load percentage and watts
- Battery state of charge
- Estimated runtime
- Battery replacement warning
- Temperature
- Source status
- Transfer events
- Overload and fault alarms

Monitoring may use SNMPv3, Syslog, APIs, vendor platforms, dry contacts, or building-management systems. This lesson establishes why NTP and central logging are essential: power events from different devices must share accurate timestamps.

Alerts should be actionable. Examples include:

- Utility power lost
- UPS on battery
- Runtime below threshold
- Battery fault
- UPS overload
- Generator failed to start
- Rack temperature high
- Critical PDU outlet offline

## 24.19 Graceful Shutdown and Startup

When runtime becomes insufficient, systems should shut down in a controlled order.

Example shutdown sequence:

1. Stop nonessential applications.
2. Shut down application servers.
3. Shut down databases and storage according to vendor procedure.
4. Shut down noncritical network services.
5. Preserve the management, monitoring, firewall, and Internet edge as long as useful.
6. Shut down remaining equipment before battery exhaustion.

Startup is usually performed in dependency order:

1. Power and cooling stable
2. Core network and storage fabric
3. Firewalls, routing, DNS, DHCP, identity, and time
4. Databases and storage
5. Application services
6. User access

The correct order depends on documented service dependencies. Randomly powering every device at once may cause high inrush current and application failures.

## 24.20 Availability, Reliability, and Resilience

| Term | Meaning |
|---|---|
| Availability | Proportion of time a service is usable |
| Reliability | Ability to operate without failure for a period |
| Resilience | Ability to withstand disruption and recover |
| Redundancy | Duplicate components or paths used to reduce failure impact |
| Fault tolerance | Ability to continue operating after a component failure |

Availability can be expressed as:

```text
Availability = Uptime / (Uptime + Downtime)
```

Approximate annual downtime:

| Availability | Annual Downtime |
|---:|---:|
| 99% | About 3 days 15 hours 39 minutes |
| 99.9% | About 8 hours 46 minutes |
| 99.99% | About 52 minutes 34 seconds |
| 99.999% | About 5 minutes 15 seconds |

High availability becomes progressively more expensive. The target must reflect business impact rather than prestige.

## 24.21 Single Points of Failure

A single point of failure, or SPOF, is a component whose failure can stop a required service.

Examples include:

- One utility feed
- One UPS
- One firewall
- One core switch
- One ISP
- One DNS server
- One physical cable path
- One administrator who knows the recovery process

Redundancy must remove the actual failure domain. Two ISP links using the same provider, pole, fiber duct, building entrance, and edge router may fail together.

Ask:

```text
What can fail?
What depends on it?
Will the backup survive the same event?
How is failover detected and tested?
```

## 24.22 High-Availability Design

High availability may use:

- Redundant power supplies
- Separate UPS/PDU paths
- Device pairs
- Switch stacking or chassis redundancy
- First-hop redundancy
- Dynamic routing
- Multiple ISPs
- Diverse physical cable paths
- Server clustering
- Replicated storage
- Multiple cloud zones or regions

Redundancy introduces complexity. Split-brain behavior, inconsistent configuration, failed state synchronization, and untested failover can make a redundant design less dependable than expected.

## 24.23 Disaster Recovery and Business Continuity

Disaster Recovery, or DR, is the organized restoration of technology services after serious disruption.

Business Continuity, or BC, is the broader ability of the organization to continue its critical functions during and after disruption.

```text
Business continuity asks:
How does the organization keep operating?

Disaster recovery asks:
How are technology and data restored?
```

BC may include alternative workplaces, manual procedures, emergency communications, suppliers, staff welfare, finance, and legal obligations. DR supports BC but does not replace it.

## 24.24 Threats and Disaster Scenarios

Plans should consider realistic scenarios:

- Prolonged utility outage
- UPS or battery-bank failure
- Generator failure or fuel shortage
- Fire, flood, or severe weather
- Internet-provider outage
- Hardware failure
- Ransomware
- Accidental deletion or misconfiguration
- Theft or vandalism
- Cloud-region or SaaS outage
- Loss of key personnel
- Building inaccessible

A risk assessment considers likelihood, impact, existing controls, and residual risk.

## 24.25 Business Impact Analysis

A Business Impact Analysis, or BIA, identifies critical business processes, their technology dependencies, and the consequences of interruption.

A BIA asks:

- Which service is critical?
- Who uses it?
- What systems, networks, power, people, and suppliers support it?
- How long can it be unavailable?
- How much data loss is acceptable?
- What financial, safety, legal, and reputational impacts arise?
- Which service must be restored first?

| Service | Dependency | Maximum Tolerable Downtime | Priority |
|---|---|---:|---:|
| Emergency communications | Network, voice, power | 15 minutes | 1 |
| Payment processing | Internet, DNS, application | 1 hour | 2 |
| Internal file archive | Storage, identity | 24 hours | 4 |

The BIA drives technical recovery priorities. Technology teams should not decide business criticality alone.

## 24.26 RTO, RPO, and MTD

### Recovery Time Objective

RTO is the target maximum time to restore a service after disruption.

### Recovery Point Objective

RPO is the maximum acceptable amount of data loss measured in time.

If a system backs up every four hours, a failure just before the next backup could lose nearly four hours of changes. An RPO of 15 minutes requires more frequent replication or backup than daily copying.

### Maximum Tolerable Downtime

Maximum Tolerable Downtime, or MTD, is the longest the business process can remain unavailable before unacceptable harm occurs. The planned RTO should be shorter than the MTD.

```text
Incident occurs
      |
      |---- acceptable data-loss window ----|  RPO looks backward
      |
      |---- target restoration time --------|  RTO looks forward
      |
      |---- maximum tolerable downtime -----|  business limit
```

| Metric | Main Question |
|---|---|
| RTO | How quickly must service return? |
| RPO | How much recent data may be lost? |
| MTD | How long before impact becomes unacceptable? |

## 24.27 Backup Fundamentals

A backup is a recoverable copy of data or configuration stored separately from the working system.

### 24.27.1 Backup Types

| Type | Contents | Backup Speed | Restore Consideration |
|---|---|---|---|
| Full | All selected data | Slowest/largest | Simplest base restore |
| Incremental | Changes since last backup of any type | Fast/small | Requires full plus incrementals |
| Differential | Changes since last full backup | Grows over time | Requires full plus latest differential |

### 24.27.2 The 3-2-1 Principle

A common principle is:

```text
3 copies of important data
2 different storage media or systems
1 copy off-site
```

Modern ransomware resilience may add an offline, immutable, or logically isolated copy. The design must prevent compromised administrator credentials from deleting every backup.

A synchronized replica is not automatically a backup. Corruption, deletion, or ransomware may replicate to it.

### 24.27.3 Network Configuration Backups

Back up:

- Router, switch, firewall, WLC, and VPN configurations
- Device software images where licensing permits
- Certificates and keys using protected procedures
- Network diagrams and IP address plans
- ISP and support contacts
- License information
- Automation scripts and templates

Secrets must be encrypted and access-controlled. A configuration backup is sensitive security information.

## 24.28 Recovery Sites

| Site Type | Characteristics | Recovery Speed | Cost |
|---|---|---|---|
| Cold site | Space and basic facilities; little active equipment | Slow | Lower |
| Warm site | Some equipment, connectivity, and recent data | Medium | Medium |
| Hot site | Operational systems and replicated data | Fast | Higher |

Cloud services can support recovery, but cloud DR still requires architecture, security, data transfer, testing, cost control, and staff capability.

## 24.29 Recovery Documentation

A recovery runbook should contain:

- Scope and activation criteria
- Roles and authority
- Emergency contacts
- Service dependencies
- Current diagrams and inventories
- Backup locations and credentials procedure
- Shutdown and startup order
- Recovery steps
- Validation tests
- Communication plan
- Vendor escalation paths
- Manual workarounds
- Return-to-normal procedure
- Evidence and incident-record requirements

The plan must be available during the incident. A runbook stored only on the failed server is not useful.

## 24.30 Testing and Maintenance

An untested recovery plan is an assumption.

Testing methods include:

| Test | Description |
|---|---|
| Checklist review | Staff review procedures and contacts |
| Tabletop exercise | Team discusses response to a scenario |
| Walkthrough | Staff step through responsibilities and systems |
| Simulation | Controlled scenario tests coordination |
| Parallel test | Recovery systems run without replacing production |
| Full interruption | Production fails over; highest risk and realism |

Tests should have objectives, approvals, safety controls, rollback, observers, evidence, and an after-action review.

Plans change when staff, suppliers, applications, addresses, passwords, circuits, or equipment change. Review them on a defined schedule and after major changes or incidents.

## 24.31 Incident Response, DR, and BC Relationship

Incident response contains and manages the immediate event. Disaster recovery restores technology. Business continuity sustains critical operations.

Example ransomware sequence:

1. Incident response isolates affected systems.
2. Business continuity activates manual or alternate processes.
3. Disaster recovery rebuilds clean infrastructure and restores validated data.
4. Security teams verify that the threat is removed.
5. Business owners validate service.
6. The organization returns to normal operation and reviews lessons.

Restoring too quickly without containment can reintroduce the threat.

## 24.32 Enterprise Power Case Study

A 20-person office has:

- ISP ONT: 12 W
- Edge router: 25 W
- Firewall: 45 W
- 24-port PoE switch including active PoE load: 210 W
- Small server: 180 W
- Monitoring appliance: 30 W

Total measured critical load:

```text
12 + 25 + 45 + 210 + 180 + 30 = 502 W
```

With preliminary 25 percent headroom:

```text
502 W x 1.25 = 627.5 W
```

The team must choose equipment whose continuous watt and VA limits exceed the engineered requirement. The UPS bridges transfer and controlled shutdown; a hybrid inverter and battery bank provide longer runtime; a generator covers prolonged low-solar periods and major outages.

The network team also identifies that the rack air conditioner and ISP rooftop radio are dependencies. The power design would fail its service objective if either were omitted.

Loads are prioritized. The server shuts down after a sustained outage, while the firewall, router, switch, critical AP, phones, and ISP equipment remain available longer.

## 24.33 Business Continuity Case Study

A retail company depends on Internet-based payment processing. Its BIA establishes:

```text
MTD: 4 hours
RTO: 1 hour
RPO: 15 minutes for transaction records
```

Controls include dual Internet providers using diverse paths, UPS and generator power, a cellular payment fallback, replicated transaction data, offline backups, paper-based emergency procedures, and a tested communication plan.

During an area-wide fiber cut, routing fails over to the second provider. If both wired providers fail, essential payment devices use controlled cellular service. The company continues limited operation while the network team works with carriers.

The lesson is that business continuity combines technology, people, suppliers, procedures, and communication.

## 24.34 Practical Labs

### Lab 1: Network Power Audit

Inspect a real or simulated network rack.

1. List every device and power supply.
2. Record rated and measured watts where available.
3. Include PoE endpoint demand.
4. Classify each load as critical, essential, or nonessential.
5. Identify all power-path single points of failure.
6. Record UPS watt/VA rating, load, battery age, and runtime estimate.
7. Recommend monitoring and maintenance improvements.

Do not open electrical panels or battery enclosures.

### Lab 2: Runtime Calculation

Use this example:

```text
Critical load: 350 W
Required runtime: 3 hours
Inverter efficiency: 90%
Usable battery fraction: 80%
Nominal battery voltage: 24 V
```

Calculate preliminary nominal watt-hours and ampere-hours. Then list at least five reasons the final professional design must be larger or differently specified.

### Lab 4: BIA and Recovery Runbook

Choose a school, clinic, shop, or office. Identify three critical services. Define dependencies, MTD, RTO, RPO, backup method, recovery order, responsible role, and validation test.

Conduct a tabletop exercise involving a 12-hour utility outage followed by a failed generator start.

## 24.35 Troubleshooting Power and Resilience

Use a safety-first process:

1. Protect people and follow site electrical procedures.
2. Determine the scope: one device, rack, room, building, or area.
3. Identify the active source: utility, UPS, inverter, solar, or generator.
4. Check alarms and monitoring without bypassing safety controls.
5. Verify load percentage, estimated runtime, temperature, and battery status.
6. Check which dependencies lost power.
7. Shed approved nonessential loads if the procedure allows.
8. Begin controlled shutdown before reserve is exhausted.
9. Escalate electrical faults to qualified personnel.
10. Record the timeline and preserve logs.

| Symptom | Possible Cause |
|---|---|
| UPS overload alarm | Excess load, PoE growth, failed redundant PSU |
| Runtime much shorter | Aged battery, heat, added load, poor charge |
| UPS rejects generator | Voltage/frequency instability or incompatibility |
| Devices restart during transfer | Transfer time, weak battery, overloaded inverter |
| Battery never fully charges | Charger fault, undersized source, damaged battery |
| Network survives but Internet fails | ISP equipment omitted from backup |
| UPS healthy but rack off | PDU, breaker, outlet, cable, or bypass issue |
| Repeated temperature alarms | Cooling failure, blocked airflow, excess load |

## 24.36 Cybersecurity and Cloud Relevance

Power and physical resilience are cybersecurity concerns. An attacker may target power, cooling, UPS management interfaces, building systems, or recovery backups. Management interfaces should use strong authentication, segmentation, updates, secure protocols, and logging.

Availability attacks include DDoS, ransomware, destructive configuration changes, and physical disruption. Backups must be protected from unauthorized deletion.

Cloud services reduce some local power responsibilities but do not remove resilience planning. Customers still design for availability zones, regions, Internet paths, identity dependencies, backups, quotas, and provider outages. The shared-responsibility model means the provider protects facility infrastructure while the customer remains responsible for appropriate architecture and data protection.


IT support staff may check UPS alarms, coordinate shutdown, verify service recovery, document incidents, and escalate electrical faults. Network engineers calculate network loads, identify service dependencies, design redundancy, monitor power systems, and participate in DR tests.

Interview questions often include:

- Watt versus VA
- UPS topology and runtime
- PoE load effects
- Battery capacity and usable energy
- RTO versus RPO
- Backup versus replication
- Redundancy and common failure domains
- Cold, warm, and hot sites
- Why recovery plans must be tested

### CCNA 200-301 and Network+ N10-009 Reminders

- Availability depends on power, cooling, connectivity, hardware, software, and people.
- A UPS supplies temporary power; its VA rating does not equal runtime.
- Check both watt and VA limits.
- PoE endpoint power contributes to switch and UPS load.
- Redundancy must avoid shared failure domains.
- RTO is target restoration time; RPO is acceptable data-loss time.
- A backup must be recoverable and protected separately.
- DR restores technology; BC sustains business operations.
- Cold sites recover slowly; hot sites recover quickly at higher cost.
- Monitoring, documentation, maintenance, and testing are part of resilience.

## 25. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Power Resilience | Ability to continue, fail safely, and recover during power disruption |
| Voltage | Electrical potential difference measured in volts |
| Current | Flow of electric charge measured in amperes |
| Watt | Unit of real power |
| Volt-Ampere | Unit of apparent power |
| Watt-Hour | Unit of energy |
| Power Factor | Ratio of real power in watts to apparent power in VA |
| Blackout | Complete loss of electrical supply |
| Brownout | Sustained reduction in voltage |
| Sag | Short-duration voltage reduction |
| Surge | Voltage increase lasting longer than a transient |
| Transient | Very short voltage disturbance |
| UPS | Uninterruptible Power Supply |
| Standby UPS | UPS that transfers from utility to battery during failure |
| Line-Interactive UPS | UPS providing voltage regulation and battery backup |
| Online UPS | Double-conversion UPS continuously supplying through inverter |
| Runtime | Time backup power can support a specified load |
| Battery Capacity | Amount of charge or energy a battery can store |
| Depth of Discharge | Percentage of battery capacity removed |
| State of Charge | Estimate of current battery fullness |
| State of Health | Estimate of present battery capability versus new |
| Inverter | Device converting DC into AC |
| Pure Sine Wave | AC output closely resembling utility waveform |
| Charge Controller | Device regulating energy used to charge batteries |
| Peak Sun Hours | Equivalent hours of full rated solar irradiance |
| ATS | Automatic Transfer Switch |
| Maintenance Bypass | Path allowing service around a UPS |
| PDU | Power Distribution Unit |
| Availability | Proportion of time a service is usable |
| Reliability | Ability to operate without failure |
| Resilience | Ability to withstand and recover from disruption |
| Redundancy | Duplication used to reduce failure impact |
| Fault Tolerance | Continued operation after a failure |
| SPOF | Single Point of Failure |
| Disaster Recovery | Restoration of technology after disruption |
| Business Continuity | Continuation of critical business functions |
| BIA | Business Impact Analysis |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| MTD | Maximum Tolerable Downtime |
| Full Backup | Copy of all selected data |
| Incremental Backup | Changes since the most recent backup |
| Differential Backup | Changes since the most recent full backup |
| Immutable Backup | Backup protected against alteration or deletion |
| Cold Site | Basic alternate location with little active equipment |
| Warm Site | Partially prepared recovery location |
| Hot Site | Operational recovery location with current systems/data |
| Runbook | Documented operational or recovery procedure |
| Tabletop Exercise | Discussion-based test of an incident scenario |

## 26. COMPARISON TABLES

### 26.1 Watts vs VA vs Watt-Hours

| Measure | Meaning | Used For |
|---|---|---|
| Watts | Real power | Load and equipment watt limit |
| VA | Apparent power | UPS/inverter electrical capacity |
| Wh | Energy | Runtime and battery planning |

### 26.2 UPS Topologies

| Feature | Standby | Line-Interactive | Online |
|---|---|---|---|
| Transfer | Yes | Yes | Effectively none |
| Conditioning | Basic | Moderate | Strong |
| Efficiency/cost | Efficient/lower cost | Balanced | More loss/higher cost |
| Use | Low-risk endpoint | Closet/small room | Critical systems |

### 26.3 UPS vs Inverter vs Generator vs Solar

| Technology | Primary Role | Typical Duration | Key Limitation |
|---|---|---|---|
| UPS | Immediate backup and conditioning | Minutes to hours | Battery runtime |
| Inverter/battery | Extended stored-energy supply | Hours | Battery capacity/recharge |
| Generator | Long-duration generated power | Fuel-dependent | Start, fuel, maintenance |
| Solar | Generates energy from sunlight | Resource-dependent | Weather/time/storage |

### 26.4 RTO vs RPO vs MTD

| Metric | Measures | Question |
|---|---|---|
| RTO | Restoration time | How quickly must it return? |
| RPO | Acceptable data-loss period | How much recent data may be lost? |
| MTD | Business tolerance limit | How long before harm is unacceptable? |

### 26.5 DR vs Business Continuity

| Feature | Disaster Recovery | Business Continuity |
|---|---|---|
| Scope | Technology restoration | Whole critical business operation |
| Focus | Systems, data, infrastructure | People, process, facilities, suppliers, technology |
| Relationship | Supports continuity | Includes and depends on DR |

### 26.6 Cold vs Warm vs Hot Sites

| Site | Readiness | Recovery | Cost |
|---|---|---|---|
| Cold | Low | Slow | Lower |
| Warm | Partial | Medium | Medium |
| Hot | High | Fast | Higher |

### 26.7 Full vs Incremental vs Differential Backup

| Type | Copies | Backup Requirement | Restore Requirement |
|---|---|---|---|
| Full | All selected data | More time/storage | Full backup |
| Incremental | Since last backup | Less time/storage | Full plus all required incrementals |
| Differential | Since last full | Grows until next full | Full plus latest differential |

## 27. REAL-WORLD ANALOGY

Think of a hospital emergency power plan. A UPS is the immediate bridge that prevents critical equipment from stopping. A generator supplies longer-duration power. Solar and batteries can reduce fuel dependence. Load classification ensures life-safety systems receive power before nonessential equipment.

Disaster recovery is the technical procedure for restoring failed systems. Business continuity is the larger plan that keeps patient care functioning through alternate rooms, communications, staff roles, suppliers, and manual procedures. Resilience comes from the complete system, not one battery.

## 28. QUICK-RECAP CHEAT SHEET

```text
POWER
W = V x A
Wh = W x hours
Power factor = W / VA
Check both UPS watts and VA
UPS rating does not equal runtime

LOAD
Inventory every dependency
Include PoE devices and ISP equipment
Critical, essential, nonessential
Add engineered headroom

BACKUP POWER
Standby: basic, transfer time
Line-interactive: voltage regulation
Online: double conversion, strongest conditioning
UPS bridges; inverter/battery extends; generator sustains
Solar generates energy but needs correct backup architecture

BATTERY
Nominal Wh = V x Ah
Usable energy depends on DoD, efficiency, age, temperature
Battery work requires qualified installation and protection

RESILIENCE
Find SPOFs and shared failure domains
Power, cooling, ISP, DNS, identity, people all matter
Monitor and test failover

RECOVERY
RTO = target restoration time
RPO = acceptable data loss in time
MTD = maximum business outage tolerance
DR restores technology
BC keeps critical business operating
Backups must be separate, protected, and tested
```

---

## Diagnose, Document, Decide

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### Meaning of Diagnose, Document, Decide

This final lesson converts the knowledge from Lessons 1 through 24 into professional practice.

**Diagnose** means identifying the actual cause of a problem through evidence, structured testing, and technical reasoning. It is not random command entry or changing several settings until the symptom disappears.

**Document** means creating an accurate record of the network, incident, change, decision, and operational state so that another qualified person can understand and support it.

**Decide** means selecting the next technical action and career direction based on evidence, risk, business need, and personal capability.

These three activities are connected:

```text
Good diagnosis produces reliable evidence.
Reliable evidence produces useful documentation.
Useful documentation supports better decisions.
```

### Technical and Business Importance of This Lesson

Employers do not only need people who can define VLAN, DHCP, OSPF, or VPN. They need people who can enter an unfamiliar environment, understand the service, collect evidence, communicate clearly, restore operation safely, and prevent recurrence.

A technically correct fix can still be unprofessional if it:

- Creates an undocumented security weakness
- Breaks another service
- Cannot be reproduced
- Has no rollback plan
- Hides the root cause
- Leaves no record for the next shift
- Exposes passwords or customer information

Professional networking combines technical skill, process discipline, communication, and judgment.

### Operation and Process: the Course Fits Together

| Course Foundation | Capstone Use |
|---|---|
| Physical media and Ethernet | Check power, links, errors, speed, duplex, frames |
| VLANs and STP | Verify access/trunk state, VLAN path, and loop prevention |
| IPv4/IPv6 and subnetting | Validate addressing, masks, gateways, and routes |
| Routing and NAT | Trace remote paths and Internet translation |
| DHCP and DNS | Separate configuration and name-resolution failures |
| Wireless | Distinguish RF, association, authentication, and IP problems |
| Security | Preserve least privilege while troubleshooting |
| Monitoring and logging | Compare behavior with baselines and timelines |
| Power and resilience | Identify environmental dependencies and recovery needs |

## 25.4 Troubleshooting as a Controlled Process

A troubleshooting methodology prevents guesswork and reduces the chance of creating a second problem.

A practical process is:

1. Identify and define the problem.
2. Establish a theory of probable cause.
3. Test the theory.
4. Create a plan of action.
5. Implement the approved solution or escalate.
6. Verify full functionality and apply preventive measures.
7. Document findings, actions, results, and lessons.

The process is iterative. If evidence disproves the theory, return to the evidence and form a better theory.

### 25.4.1 Identify the Problem

Ask precise questions:

- What exactly fails?
- Who is affected?
- Which locations, VLANs, applications, and times are involved?
- Did it ever work?
- What changed?
- Is the problem constant or intermittent?
- What error does the user see?
- What still works?
- What is the business impact?

"The network is down" is not a diagnosis. "Four Finance PCs on access switch SW2 cannot reach their default gateway after yesterday's desk move, while other VLANs remain operational" is a usable problem statement.

### 25.4.2 Establish Scope

Start with the smallest confirmed facts:

```text
One application or all applications?
One host or many hosts?
One port, VLAN, switch, site, or entire organization?
Local network, remote network, Internet, or DNS only?
Wired, wireless, or both?
```

The scope helps locate the likely failure domain.

### 25.4.3 Gather Evidence Before Changing Anything

Evidence may include:

- User report and screenshot
- Time the failure began
- Interface status and counters
- Client IP configuration
- VLAN and trunk state
- MAC and ARP tables
- Routing table
- DHCP lease and DNS results
- Logs and monitoring alerts
- Recent change records
- Physical labels and cable tests
- Packet capture

Capture the current state before commands such as clearing counters, rebooting, renewing addresses, or replacing equipment erase evidence.

## 25.5 Troubleshooting Approaches

### 25.5.1 Bottom-Up

Begin at OSI Layer 1 and move upward. This is effective when link lights are absent, cabling was disturbed, or physical failure is likely.

### 25.5.2 Top-Down

Begin with the application and move downward. This is useful when only one service fails but basic connectivity works.

### 25.5.3 Divide-and-Conquer

Begin at a middle layer, commonly Layer 3. If the host can reach its gateway, investigate upward or farther along the path. If it cannot, investigate downward and locally.

### 25.5.4 Follow-the-Path

Trace the actual packet path from source to destination, checking every interface, VLAN, route, policy, and return path. This is especially useful for multi-device enterprise networks.

### 25.5.5 Compare-to-Baseline

Compare current behavior with a known healthy state. An interface at 70 percent utilization may be normal or abnormal depending on its baseline.

| Approach | Best Starting Condition |
|---|---|
| Bottom-up | Link or physical fault suspected |
| Top-down | One application/service fails |
| Divide-and-conquer | Layer is not yet known |
| Follow-the-path | Multi-hop or asymmetric problem |
| Compare-to-baseline | Performance degradation or intermittent issue |

## 25.6 The Troubleshooting Toolkit

### 25.6.1 Windows Commands

```powershell
ipconfig /all
Get-NetIPConfiguration
Get-NetAdapter
ping <destination>
tracert <destination>
pathping <destination>
arp -a
route print
nslookup <name>
Resolve-DnsName <name>
Test-NetConnection <host> -Port <port>
netstat -ano
```

### 25.6.2 Linux Commands

```bash
ip address
ip link
ip route
ip neigh
ping -c 4 <destination>
tracepath <destination>
traceroute <destination>
dig <name>
resolvectl status
ss -tulpen
ethtool <interface>
tcpdump -ni <interface>
```

### 25.6.3 Cisco IOS Commands

```cisco
show interfaces
show interfaces status
show interfaces counters errors
show ip interface brief
show vlan brief
show interfaces trunk
show mac address-table
show spanning-tree
show etherchannel summary
show ip arp
show ip route
show access-lists
show cdp neighbors detail
show lldp neighbors detail
show logging
show processes cpu
show memory statistics
```

Commands must be interpreted in context. `up/up` confirms interface protocol state but does not prove that DHCP, DNS, routing, policy, or the application works.

### 25.6.4 Physical and Analysis Tools

| Tool | Purpose |
|---|---|
| Cable tester | Continuity, wire map, opens, shorts, split pairs |
| Certifier | Standards-based cable performance certification |
| Tone generator/probe | Identify an unlabeled copper cable |
| Optical power meter | Measure received optical power |
| Visual fault locator | Locate some fiber breaks or faults |
| Wi-Fi analyzer | Observe channels, signal, noise, and neighboring WLANs |
| Packet analyzer | Capture and decode frames and packets |
| Loopback plug | Test transmit/receive operation on supported interfaces |
| Console cable | Out-of-band device administration |

## 25.7 Forming and Testing a Hypothesis

A useful hypothesis is specific and testable:

```text
Weak: "The switch is bad."

Strong: "The Finance PC cannot reach its gateway because SW2
GigabitEthernet0/18 is assigned to VLAN 30 instead of VLAN 20."
```

Test the least disruptive theory first. Do not restart a core switch to test whether one access port has the wrong VLAN.

Change one relevant variable at a time. If several changes are made simultaneously, the team may restore service without knowing which action worked or what new risk was introduced.

## 25.8 FULL END-TO-END TROUBLESHOOTING CASE STUDY

### 25.8.1 Environment

FEMTECT Services has a headquarters office with:

```text
VLAN 10 - Staff       192.168.10.0/24
VLAN 20 - Finance     192.168.20.0/24
VLAN 30 - Voice       192.168.30.0/24
VLAN 40 - Guest       192.168.40.0/24
VLAN 50 - Management  192.168.50.0/24
```

A multilayer switch, DSW1, performs inter-VLAN routing. Access switch SW2 connects Finance workstations and IP phones. A firewall provides Internet access. DHCP and DNS run on server `192.168.60.10`.

```text
Internet
   |
Firewall
   |
DSW1 (Layer 3 switch)
   |
802.1Q trunk
   |
SW2
   |
Finance PCs and phones
```

### 25.8.2 Incident Report

At 09:10, Finance reports:

- PC-FIN1 shows no network connection.
- PC-FIN2 receives an address but cannot reach the Finance application.
- IP phones on the same desks work.
- Staff users elsewhere are operational.
- The problem began after desks were moved and a switch change was completed the previous evening.

This is a combined Layer 1, Layer 2, and Layer 3 incident. There is more than one fault.

### 25.8.3 Initial Problem Statement

```text
Finance connectivity through SW2 is partially unavailable after a desk
move and switch change. At least two endpoints show different symptoms.
Voice and other office services remain available. Business impact is
high because Finance cannot process transactions.
```

### 25.8.4 Preserve Evidence

Before making changes:

- Record incident and change-ticket numbers.
- Save current SW2 and DSW1 configurations.
- Capture interface, VLAN, trunk, route, DHCP, and log output.
- Photograph cable labels without exposing sensitive information.
- Record times using synchronized clocks.
- Ask the previous engineer exactly what was changed.

### 25.8.5 Layer 1 Investigation: PC-FIN1

PC-FIN1 reports no link.

Windows:

```powershell
Get-NetAdapter
```

Expected observation:

```text
Ethernet: Media disconnected
```

SW2:

```cisco
show interfaces status
show interfaces GigabitEthernet0/18
```

Observation:

```text
Gi0/18  notconnect  20  auto  auto
```

The technician checks:

1. NIC enabled and cable seated.
2. Patch lead at the desk.
3. Patch-panel mapping.
4. Switch port and link light.
5. Cable with a tester.

The tester reports an open conductor in the desk patch lead. A certified replacement cable restores link.

Verification:

```text
Get-NetAdapter now reports Up.
SW2 Gi0/18 reports connected.
```

This repairs PC-FIN1's Layer 1 fault, but the overall incident is not closed because PC-FIN2 still fails.

### 25.8.6 Layer 2 Investigation: PC-FIN2

PC-FIN2 has:

```text
IPv4 address: 192.168.40.87
Mask:         255.255.255.0
Gateway:      192.168.40.1
```

The PC is physically in Finance but received a Guest VLAN address.

Commands:

```cisco
show vlan brief
show interfaces GigabitEthernet0/19 switchport
show mac address-table interface GigabitEthernet0/19
```

Observation:

```text
Gi0/19 access VLAN: 40
Expected access VLAN: 20
```

The previous change assigned the port to the wrong VLAN.

Approved correction:

```cisco
interface GigabitEthernet0/19
 description FINANCE-PC-FIN2
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
```

After changing VLAN membership, the client renews DHCP:

```powershell
ipconfig /release
ipconfig /renew
ipconfig /all
```

PC-FIN2 now receives:

```text
IPv4 address: 192.168.20.87
Gateway:      192.168.20.1
DNS:          192.168.60.10
```

The client can reach its gateway but still cannot reach the application server. The Layer 2 fault is fixed, but a Layer 3 problem remains.

### 25.8.7 Validate the Trunk

Before moving to routing, verify VLAN 20 crosses the SW2-DSW1 trunk:

```cisco
show interfaces trunk
show spanning-tree vlan 20
show mac address-table vlan 20
```

Confirm:

- Correct trunk mode
- VLAN 20 exists on both switches
- VLAN 20 is allowed and forwarding
- Native VLAN matches
- MAC addresses are learned on expected ports

In this case, VLAN 20 is allowed and STP is forwarding. The trunk is not the remaining fault.

### 25.8.8 Layer 3 Investigation

PC-FIN2 tests:

```powershell
ping 192.168.20.1
ping 192.168.60.10
tracert 192.168.60.10
Test-NetConnection 192.168.60.10 -Port 443
```

Results:

```text
Gateway ping succeeds.
Server ping and TCP 443 fail.
Trace stops at 192.168.20.1.
```

This proves local VLAN communication reaches DSW1. Investigate routing and policy on DSW1.

```cisco
show ip interface brief
show ip route
show access-lists
show ip interface Vlan20
```

Observation:

```text
Vlan20 is up/up with 192.168.20.1/24.
Route to 192.168.60.0/24 points to 10.255.0.6.
The correct next hop is 10.255.0.2.
```

A static route was entered incorrectly during the previous change:

```cisco
ip route 192.168.60.0 255.255.255.0 10.255.0.6
```

The team checks the approved implementation and rollback plan before correcting:

```cisco
no ip route 192.168.60.0 255.255.255.0 10.255.0.6
ip route 192.168.60.0 255.255.255.0 10.255.0.2
```

### 25.8.9 End-to-End Verification

Do not stop after one successful ping.

Verify:

- PC-FIN1 and PC-FIN2 have correct link, VLAN, IP, gateway, and DNS.
- Both reach their gateway.
- Finance application TCP 443 works.
- DNS resolves the application hostname.
- Internet access follows policy.
- Guest VLAN remains isolated.
- IP phones still register.
- Monitoring reports healthy interfaces and routes.
- Logs contain no new errors.
- Configuration is saved and backed up.

Example:

```powershell
Resolve-DnsName finance-app.femtect.local
Test-NetConnection finance-app.femtect.local -Port 443
tracert 192.168.60.10
```

### 25.8.10 Root Causes

The incident had three independent causes:

| Layer | Root Cause | Symptom |
|---|---|---|
| Layer 1 | Open conductor in patch cable | PC-FIN1 had no link |
| Layer 2 | Access port assigned to Guest VLAN | PC-FIN2 received wrong DHCP scope |
| Layer 3 | Static route used wrong next hop | Finance could not reach server subnet |

The presence of multiple faults explains why one correction did not restore the entire service.

### 25.8.11 Contributing Process Failures

- Desk-move cables were not tested.
- Port description and floor plan were outdated.
- Switch change lacked peer review.
- Validation tested only link and not application reachability.
- The static route was manually entered without a comparison check.

### 25.8.12 Preventive Actions

- Test and label moved cabling.
- Use standard access-port templates.
- Require peer review for route and VLAN changes.
- Automate configuration backup and difference reporting.
- Add post-change tests for DHCP, gateway, DNS, application, and isolation.
- Update the physical and logical diagrams.
- Monitor critical routes and application reachability.

## 25.9 Packet Capture as Evidence

A packet capture shows what was transmitted and received at the capture point. It can reveal:

- Repeated ARP requests without replies
- DHCP DORA failure
- DNS errors or delays
- TCP SYN retransmissions
- TCP resets
- ICMP unreachable messages
- Duplicate acknowledgments and retransmissions
- TLS negotiation failures at a high level

Capture only with authorization. Packets may contain personal data, authentication material, internal addresses, and sensitive application content. Limit scope, protect files, and follow retention policy.

A capture point matters. A packet absent on one interface may still exist elsewhere. Interpret the packet path, SPAN configuration, VLAN tags, offloading behavior, and encryption boundaries.

## 25.10 Escalation and Communication

Escalate when:

- Safety is at risk.
- Required access or authority is unavailable.
- The issue is outside support scope.
- A change could affect many users.
- A vendor or service provider owns the failing component.
- The recovery exceeds the agreed time target.
- Evidence suggests a security incident.

A useful escalation contains:

```text
Business impact
Affected users/services
Start time and current status
What works and what fails
Evidence collected
Tests completed and results
Changes already made
Current hypothesis
Specific assistance required
Relevant ticket, device, circuit, and contact information
```

Avoid sending "Internet down, please check." Give the receiving team enough evidence to act.

## 25.11 Network Documentation Standards

Network documentation is controlled operational information, not decorative paperwork.

Good documentation is:

- Accurate
- Current
- Consistent
- Version-controlled
- Dated and owned
- Accessible to authorized staff
- Protected according to sensitivity
- Detailed enough to operate and recover the network

### 25.11.1 Documentation Set

| Document | Purpose |
|---|---|
| Physical diagram | Devices, racks, ports, media, and physical links |
| Logical diagram | VLANs, subnets, routing, security zones, services |
| Rack elevation | Device location and rack-unit position |
| IP address plan/IPAM | Addresses, prefixes, gateways, reservations, owners |
| VLAN register | VLAN ID, name, subnet, gateway, purpose |
| Circuit register | Provider, circuit ID, bandwidth, demarcation, support |
| Device inventory | Model, serial, role, location, support status |
| Configuration backup | Recoverable device configuration |
| Dependency map | Relationships between services and infrastructure |
| Runbook | Repeatable operational procedure |
| Change record | Planned and completed change evidence |
| Incident record | Timeline, impact, diagnosis, resolution, lessons |

### 25.11.2 Naming Standards

Names should convey useful information without becoming unmanageably long.

Example:

```text
LAG-HQ-DSW01
LAG-HQ-ASW02
ABJ-BR-FW01
LAG-HQ-AP-F2-03
```

A standard may encode site, building/floor, role, and sequence. Use the organization's approved convention consistently.

### 25.11.3 Interface Descriptions

An interface description should identify the connected device or service:

```cisco
interface GigabitEthernet1/0/24
 description UPLINK_TO_LAG-HQ-DSW01_Gi1/0/12
```

For a provider link:

```text
ISP: Provider name
Circuit ID: NG-LAG-004812
Bandwidth: 100 Mbps
Demarcation: Rack A, RU 38
Support contact: service desk record reference
```

Do not place passwords or secret keys in interface descriptions.

## 25.12 Physical and Logical Diagrams

A physical diagram answers:

```text
What equipment exists?
Where is it?
Which physical port and cable connect it?
Which media and speed are used?
```

A logical diagram answers:

```text
Which VLANs and subnets exist?
Where are Layer 3 boundaries?
How is traffic routed?
Where are firewalls, VPNs, NAT, and services?
```

Example logical diagram:

```text
                    Internet
                       |
                  [Firewall]
                       |
             10.255.0.0/30 transit
                       |
                    [DSW1]
          _____________|_____________
         |             |             |
    VLAN 10        VLAN 20       VLAN 40
    Staff          Finance       Guest
192.168.10/24  192.168.20/24  192.168.40/24
         |
      [SW2]
```

### 25.12.1 Diagram Quality Rules

- Include title, scope, owner, revision, and date.
- Use consistent symbols and line styles.
- Label device names and important interfaces.
- Show prefixes, VLAN IDs, and security boundaries where relevant.
- Distinguish primary and backup paths.
- Avoid crossing lines where possible.
- Include a legend for non-obvious symbols.
- Keep secrets out of diagrams.
- Create separate views when one diagram becomes unreadable.

Diagrams should be understandable when printed or viewed without the author's explanation.

## 25.13 IP Address Management

IP Address Management, or IPAM, tracks addressing and subnet assignments.

Recommended fields include:

| Field | Example |
|---|---|
| Prefix | 192.168.20.0/24 |
| Purpose | Finance user VLAN |
| VLAN | 20 |
| Gateway | 192.168.20.1 |
| DHCP range | 192.168.20.50-199 |
| Exclusions | 192.168.20.1-49 |
| DNS domain | femtect.local |
| Site | Lagos HQ |
| Owner | Network Operations |
| Status | Active |

An unmanaged spreadsheet may work for a very small environment, but a shared IPAM system improves validation, history, automation, and duplicate-address prevention.

## 25.14 Configuration Documentation and Source of Truth

A source of truth is the authoritative record of intended state. It may be an IPAM/DCIM platform, configuration repository, automation inventory, or controlled document system.

Running device configuration is evidence of actual state, but it is not always the intended state. Differences between intended and actual state are configuration drift.

Configuration-management practices include:

- Automated scheduled backups
- Encryption and access control
- Version history
- Difference comparison
- Standard templates
- Peer review
- Validation and compliance checks
- Tested restoration

Never store plaintext passwords, private keys, or community strings in an unprotected public repository.

## 25.15 Baselines

A baseline is a recorded picture of normal performance and behavior under defined conditions. It gives meaning to future measurements.

Baseline dimensions include:

- Time of day and day of week
- Normal and peak utilization
- User or transaction volume
- Application response time
- Interface errors and drops
- CPU and memory
- Wireless channel use and client count
- WAN latency, jitter, and packet loss
- Power load and temperature

One measurement is not a baseline. Collect data across representative business cycles and record major changes.

## 25.16 Performance Metrics

### 25.16.1 Bandwidth, Throughput, and Goodput

- **Bandwidth:** Theoretical or configured link capacity.
- **Throughput:** Actual rate of data transferred.
- **Goodput:** Useful application data delivered, excluding overhead and retransmissions.

A 1 Gbps interface does not guarantee 1 Gbps application goodput.

### 25.16.2 Latency

Latency is the time required for data to travel from source to destination. Round-trip time measures travel to the destination and back.

Latency is affected by distance, propagation, serialization, processing, queueing, congestion, and path selection.

### 25.16.3 Jitter

Jitter is variation in packet delay. Voice and video are especially sensitive because packets must arrive at a steady rate.

### 25.16.4 Packet Loss

Packet loss is the percentage of packets that do not arrive. Congestion, physical errors, wireless interference, overloaded devices, faulty links, and policy can cause loss.

```text
Packet loss % = Lost packets / Sent packets x 100
```

### 25.16.5 Utilization

```text
Utilization % = Used bandwidth / Available bandwidth x 100
```

High average utilization may indicate insufficient capacity. Short peaks may be normal. Baselines and application impact determine significance.

### 25.16.6 Interface Errors and Discards

Useful counters include:

- CRC/FCS errors
- Input errors
- Output errors
- Runts and giants
- Collisions or late collisions on relevant legacy/duplex cases
- Input/output discards
- Queue drops

Counters are cumulative. Record time and calculate the rate of increase. A historical counter that no longer rises may not represent a current fault.

## 25.17 Monitoring Architecture

Monitoring answers:

```text
Is the service available?
Is performance normal?
What changed?
Where is the failure?
Who must respond?
```

Monitoring methods include:

| Method | Use |
|---|---|
| ICMP probe | Basic reachability and latency |
| SNMPv3 polling | Interface, CPU, memory, environment, counters |
| Syslog | Event and fault messages |
| Flow telemetry | Traffic conversations and volume |
| Packet capture | Detailed packet-level evidence |
| API/streaming telemetry | Structured high-frequency metrics |
| Synthetic transaction | Tests application from a user's perspective |
| Agent monitoring | Host/application health |

Monitoring only device reachability is insufficient. A server may answer ping while its application is unavailable.

## 25.18 Thresholds, Alerts, and Alert Fatigue

A threshold defines when a metric requires attention. Static thresholds are simple but may not fit every device or time. Dynamic thresholds compare current behavior with historical patterns.

An actionable alert should contain:

- Affected object and service
- Condition and measured value
- Start time and duration
- Severity and business impact
- Relevant dependency
- Link to dashboard or runbook
- Escalation owner

Too many low-value alerts create alert fatigue. Staff begin ignoring notifications, including important ones. Tune duplicate, flapping, and non-actionable alerts.

## 25.19 Logs and Time Correlation

This lesson introduced NTP and Syslog. In a complete monitoring system:

1. Devices synchronize time.
2. Logs are sent centrally.
3. Metrics and changes use consistent timestamps.
4. Events are correlated across network, server, identity, security, and power systems.

Log retention must match legal, security, operational, and storage requirements. Protect logs from unauthorized alteration and restrict access to sensitive records.

## 25.20 Capacity Planning

Capacity planning predicts when resources will become insufficient.

Consider:

- User and device growth
- New applications
- WAN and Internet demand
- PoE power
- Wireless client density
- CPU, memory, and session limits
- Address-pool consumption
- VPN throughput
- Storage and log growth
- UPS and cooling load

Capacity should be added before sustained demand causes failure. Procurement lead time, budget cycles, licensing, installation, and change windows must be included.

## 25.21 Change Management

A change is an authorized modification to infrastructure, configuration, software, policy, or documentation.

Change management reduces risk by ensuring the work is understood, reviewed, scheduled, tested, reversible, and recorded.

### 25.21.1 Change Types

| Type | Description |
|---|---|
| Standard | Low-risk, repeatable, pre-approved procedure |
| Normal | Assessed, reviewed, and approved before implementation |
| Emergency | Urgent change needed to restore service or reduce immediate risk |

Emergency does not mean undocumented. The review may be expedited, but actions and approvals must still be recorded and reviewed afterward.

### 25.21.2 Change Request Contents

A professional change request contains:

- Title and change owner
- Business reason
- Scope and affected systems
- Risk and impact assessment
- Dependencies
- Implementation steps
- Pre-change validation
- Test plan and success criteria
- Backout/rollback plan
- Maintenance window
- Required approvals
- Communication plan
- Post-change validation
- Documentation updates

### 25.21.3 Maintenance Window

A maintenance window is an approved period for planned work. It does not remove the need for careful design. Some changes can continue affecting users after the window, so the plan must reserve time for testing and rollback.

## 25.22 Implementation and Rollback

The implementation plan should be precise enough that another qualified engineer can follow it.

Weak:

```text
Configure the VLAN and test.
```

Professional:

```text
1. Confirm current config backup completed.
2. Verify VLAN 20 exists on DSW1 and SW2.
3. Confirm Gi0/19 endpoint and approved port mapping.
4. Configure Gi0/19 as static access VLAN 20.
5. Verify switchport mode, VLAN, STP, and MAC learning.
6. Renew client DHCP.
7. Test gateway, DNS, Finance HTTPS, and Guest isolation.
8. Save configuration and archive post-change state.
```

A rollback plan restores the previous known state. "Reboot if it fails" is not a rollback plan.

Rollback must specify:

- Trigger or decision point
- Exact restoration commands or backup
- Responsible person
- Time required
- Validation after rollback
- Communication and escalation

## 25.23 Configuration Management

Configuration management maintains device state throughout its lifecycle.

Core practices:

- Standard approved templates
- Unique device identity
- Version-controlled intended configuration
- Automated backups
- Secure secret handling
- Configuration-drift detection
- Software and firmware inventory
- License and support tracking
- End-of-life planning
- Tested restore procedure

### 25.23.1 Golden Configuration

A golden configuration is an approved secure baseline for a device role. It may define AAA, SSH, NTP, Syslog, SNMPv3, management ACLs, banners, interface defaults, and required security controls.

It must be maintained as technology and policy change. A stale golden configuration can reproduce old vulnerabilities at scale.

### 25.23.2 Backup Before and After Change

Preserve:

```text
Pre-change configuration
Approved intended change
Command/output evidence
Post-change configuration
Difference report
Validation results
```

Never assume that `copy running-config startup-config` replaces an external backup.

## 25.24 Root Cause Analysis

Root Cause Analysis, or RCA, asks why the incident occurred and how recurrence can be reduced.

The immediate technical cause is not always the complete root cause.

```text
Symptom: Finance application unavailable.
Technical causes: wrong VLAN, route, and failed cable.
Process causes: outdated diagram, inadequate review, incomplete testing.
Organizational cause: change process did not require application validation.
```

### 25.24.1 Five Whys

The Five Whys technique repeatedly asks why, but it must be evidence-based.

```text
Why could Finance not reach the server?
Because the route used the wrong next hop.

Why was the wrong route installed?
Because the next hop was entered manually from an outdated note.

Why was the outdated note used?
Because the source-of-truth record was not updated.

Why was it not updated?
Because documentation was not included in change closure.

Why was change closure incomplete?
Because the process lacked a required documentation check.
```

Do not use RCA to blame an individual. Improve systems, controls, training, and verification.

## 25.25 Incident Report Structure

A professional incident report contains:

1. Executive summary
2. Business impact
3. Detection method
4. Timeline
5. Technical evidence
6. Root and contributing causes
7. Resolution
8. Validation
9. Preventive actions
10. Owners and due dates

Separate facts from assumptions. Record times consistently. Do not expose secrets or unnecessary personal information.

### 25.25.1 Example Timeline

| Time | Event |
|---|---|
| 09:10 | Finance reports connectivity failure |
| 09:15 | Incident acknowledged and scope confirmed |
| 09:23 | Failed PC-FIN1 patch cable identified |
| 09:31 | Cable replaced and link restored |
| 09:39 | Wrong access VLAN found on Gi0/19 |
| 09:46 | VLAN corrected; gateway reachable |
| 09:55 | Incorrect server-subnet route identified |
| 10:05 | Approved route correction completed |
| 10:15 | Application, DNS, voice, and isolation validated |
| 10:30 | Incident monitoring period completed |

## 25.26 Handover Documentation

A handover transfers responsibility without losing context.

A shift or project handover should state:

- Current service status
- Work completed
- Outstanding issues
- Risks and temporary workarounds
- Monitoring or alerts to watch
- Pending changes and approvals
- Vendor cases
- Next actions, owners, and deadlines
- Location of evidence and documentation

### 25.26.1 Example Handover

```text
Subject: Finance Network Incident Handover - INC-2026-0142

Status:
Service restored at 10:15 WAT. Monitoring remains normal.

Impact:
Two Finance workstations could not access transaction services.

Resolved:
- Replaced failed patch cable for PC-FIN1.
- Corrected SW2 Gi0/19 from VLAN 40 to VLAN 20.
- Corrected DSW1 route to 192.168.60.0/24 via 10.255.0.2.

Validated:
DHCP, gateway, DNS, HTTPS application, voice registration,
Internet policy, and Guest isolation.

Outstanding:
Update floor-port map and complete peer review of previous change.

Next owner:
Network Operations, due 17:00 WAT.

Evidence:
Incident folder INC-2026-0142 in the controlled operations repository.
```

## 25.27 Building a Portfolio Case Study

A portfolio piece demonstrates thinking, not only a screenshot of commands.

Recommended structure:

1. **Problem:** Describe the business and technical challenge.
2. **Constraints:** State available devices, simulation limits, time, and policy.
3. **Design:** Provide physical/logical diagrams and addressing.
4. **Implementation:** Show key configurations with secrets removed.
5. **Testing:** Show expected and actual results.
6. **Troubleshooting:** Explain one deliberate or real fault and evidence.
7. **Security:** Explain segmentation and management controls.
8. **Resilience:** Explain backup, monitoring, and recovery.
9. **Outcome:** State what worked and what was learned.
10. **Artifacts:** Include sanitized files, diagrams, and runbook.

### 25.27.1 Portfolio Project: Secure Resilient Branch Network

Build as a separate practical assignment if the instructor wants a portfolio exercise:

- Staff, Finance, Voice, Guest, and Management VLANs
- Trunks and STP protections
- Inter-VLAN routing
- DHCP and DNS
- Static/default or dynamic routing
- NAT/PAT
- ACL segmentation
- SSH management
- NTP, Syslog, and SNMP concepts
- Wireless staff and guest design
- Site-to-site VPN design
- Redundant path or documented resilience plan

Introduce three faults, diagnose them, and include the incident report.

### 25.27.2 Protect Confidential Information

Never publish:

- Real public IP addresses without authorization
- Passwords, secrets, hashes, tokens, or private keys
- Customer names or personal information
- Internal hostnames or diagrams from an employer
- Proprietary configuration
- Vulnerability details that create risk

Use lab data, documentation ranges, fictional names, and sanitized screenshots.

## 25.28 Evidence That Employers Value

Useful evidence includes:

- Clear topology diagram
- Address and VLAN plan
- Configuration excerpts
- Verification matrix
- Before/after evidence
- Troubleshooting decision log
- Change request and rollback
- Incident report and RCA
- Handover note
- README explaining how to reproduce the lab

Quality matters more than the number of screenshots.

## 25.29 Guided Career Branch Point

The course foundation supports several paths. The branches overlap; professionals often move between them.

### 25.29.1 Network Engineering

Network engineers design, implement, automate, secure, and troubleshoot connectivity.

Core interests:

- Routing and switching
- Wireless design
- WAN, VPN, and Internet connectivity
- High availability
- Automation and monitoring
- Performance analysis

Next steps:

- Deepen CCNA-level skills
- Build multi-site labs
- Learn Python, APIs, Git, and automation
- Study enterprise wireless and firewalls
- Practice packet analysis and design documentation

### 25.29.2 Cybersecurity

Cybersecurity professionals protect identities, systems, networks, and data.

Core interests:

- Security monitoring
- Vulnerability management
- Incident response
- Network defense
- Identity and access
- Governance and risk

Next steps:

- Strengthen Linux, Windows, and networking
- Study logs, SIEM, endpoint protection, and threat analysis
- Build defensive labs ethically
- Learn secure configuration and incident handling
- Practice explaining risk and evidence

Networking remains foundational because attacks and controls operate across protocols, identities, devices, and traffic paths.

### 25.29.3 IT Support

IT support professionals restore user productivity and operate endpoints, accounts, applications, and local networks.

Core interests:

- User communication
- Windows and productivity systems
- Hardware and peripherals
- Identity and permissions
- Basic networking
- Ticketing and escalation

Next steps:

- Practice structured troubleshooting
- Learn Microsoft administration and endpoint management
- Build home-office and small-business labs
- Improve ticket notes and customer communication
- Study backup, security, and remote support

IT support is not a lesser path. It develops broad operational judgment and can lead into networking, security, cloud, systems, or management.

### 25.29.4 Cloud

Cloud professionals design and operate services in provider environments.

Core interests:

- Virtual networks, subnets, and routing
- Security groups and identity
- Load balancing and DNS
- Hybrid connectivity and VPN
- Infrastructure as code
- Monitoring, cost, and resilience

Next steps:

- Choose one cloud platform for structured study
- Build virtual-network and hybrid labs
- Learn Linux, scripting, Git, and infrastructure as code
- Study IAM and shared responsibility
- Practice high-availability and cost-aware design

Cloud networking still uses the principles from this course. The interfaces are virtual, but packets still require addressing, routes, policy, DNS, and reachable return paths.

## 25.30 Choosing a Direction

Use evidence rather than pressure or trend alone.

Rate each area from 1 to 5:

| Question | Network | Security | IT Support | Cloud |
|---|---:|---:|---:|---:|
| I enjoy this work |  |  |  |  |
| I persist when it becomes difficult |  |  |  |  |
| I have access to learning resources |  |  |  |  |
| Local/remote job demand is visible |  |  |  |  |
| My current skills transfer well |  |  |  |  |
| I can build portfolio evidence |  |  |  |  |

The score is a discussion tool, not destiny. Choose one primary direction for the next three to six months and maintain foundational networking practice.

### 25.30.1 A 90-Day Development Plan

**Days 1-30: Foundation and repetition**

- Review weak course topics.
- Rebuild one complete network without notes.
- Practice subnetting and command interpretation.
- Improve CV and professional profile.

**Days 31-60: Specialization**

- Follow one structured certification or role path.
- Build one deeper role-specific lab.
- Read job descriptions and identify recurring requirements.
- Conduct weekly troubleshooting drills.

**Days 61-90: Evidence and applications**

- Publish a sanitized capstone.
- Practice interview explanations aloud.
- Apply for appropriate internships, support roles, junior roles, or volunteer projects.
- Track applications and skill gaps.
- Request specific feedback and revise.

## 25.31 Interview Communication

Use the STAR structure where appropriate:

- **Situation:** Context and impact
- **Task:** Your responsibility
- **Action:** Evidence, reasoning, and steps
- **Result:** Verified outcome and lesson

Example:

```text
Situation:
Finance users lost application access after a switch change.

Task:
Restore service while protecting other VLANs and preserving evidence.

Action:
I scoped affected hosts, checked Layer 1 first, corrected a failed cable,
identified a wrong access VLAN, traced the route, corrected the approved
next hop, and tested DHCP, DNS, HTTPS, voice, and Guest isolation.

Result:
Service was restored and monitored. I documented three root causes,
updated diagrams, and added peer review and post-change validation.
```

Do not claim production experience you do not have. A well-explained lab demonstrates honest skill.

## 25.33 Verification Matrix

A verification matrix proves that requirements work after a change.

| Test | Source | Destination | Expected | Result |
|---|---|---|---|---|
| DHCP | Finance PC | DHCP service | Receives VLAN 20 scope | Pass/Fail |
| Gateway | Finance PC | 192.168.20.1 | Reachable | Pass/Fail |
| DNS | Finance PC | Internal DNS | Resolves finance app | Pass/Fail |
| HTTPS | Finance PC | Finance server TCP 443 | Permitted | Pass/Fail |
| Guest isolation | Guest client | Finance server | Denied | Pass/Fail |
| Voice | IP phone | Call service | Registered | Pass/Fail |
| Management | Staff PC | Switch SSH | Denied | Pass/Fail |
| Monitoring | NMS | SW2 | Metrics/logs received | Pass/Fail |

Both positive and negative tests matter. A firewall rule is not fully tested until required traffic passes and prohibited traffic remains blocked.

## 25.34 Common Professional Mistakes

| Mistake | Better Practice |
|---|---|
| Reboot first | Preserve evidence and scope the problem |
| Change many settings | Test one evidence-based theory |
| Stop after ping works | Test DNS, application, return path, and security |
| Work without ticket | Record ownership, impact, and actions |
| Skip backup | Capture recoverable pre-change state |
| No rollback | Define trigger and restoration steps |
| Blame user or colleague | Focus on facts and system improvement |
| Publish real configuration | Sanitize all sensitive data |
| Monitor devices only | Monitor end-to-end services |
| Let documentation age | Make updates part of change closure |

## 25.35 Cybersecurity Relevance

Troubleshooting access can expose sensitive systems. Use least privilege, approved accounts, secure protocols, and auditable changes.

Unexpected symptoms may indicate an attack rather than a fault:

- New unauthorized route
- MAC or ARP instability
- Unknown DHCP server
- Repeated authentication failures
- Configuration changed outside a window
- Unusual outbound traffic
- Disabled logging

If evidence suggests compromise, preserve logs, follow incident-response procedures, and avoid destroying evidence through unnecessary resets.

Documentation itself is sensitive. Network diagrams, backups, inventories, and runbooks reveal valuable information to attackers. Classify, encrypt, back up, and restrict them.

## 25.36 Cloud Relevance

Cloud troubleshooting follows the same logic:

```text
Application
Security group / network ACL
Route table
Subnet and address
Load balancer
DNS
VPN or direct connection
Identity and platform service
```

Cloud environments add APIs, IAM, regions, availability zones, managed services, quotas, and provider control planes. Infrastructure as code improves repeatability and review, but a flawed template can reproduce a fault at scale.

Monitor application transactions, not only virtual-machine state. Maintain diagrams, tags, source-controlled configuration, change review, and recovery tests.

## 25.37 Final CCNA 200-301 and Network+ N10-009 Reminders

- Troubleshoot systematically and document every significant action.
- Verify physical link, VLAN, IP configuration, gateway, routing, policy, DNS, and application in a logical order.
- A successful ping does not prove full service.
- Establish a baseline before declaring a measurement abnormal.
- Interface errors must be interpreted as rates and trends.
- Use NTP, Syslog, SNMP, flow data, captures, and synthetic tests appropriately.
- Change plans require risk, testing, rollback, approval, and documentation.
- Positive and negative verification tests are both necessary.
- RTO, RPO, backups, power, and redundancy influence recovery.
- Escalate with evidence and business impact.
- Protect credentials, packet captures, diagrams, and configurations.
- Networking skills remain foundational across IT support, cybersecurity, cloud, and network engineering.

## 26. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Troubleshooting | Structured process of identifying and resolving faults |
| Problem Statement | Precise description of symptom, scope, time, and impact |
| Scope | Boundary of users, systems, locations, and services affected |
| Hypothesis | Testable explanation for observed evidence |
| Bottom-Up | Troubleshooting approach beginning at the physical layer |
| Top-Down | Approach beginning at the application layer |
| Divide-and-Conquer | Approach starting at a middle layer and moving based on results |
| Follow-the-Path | Inspection of every stage in a packet's route |
| Baseline | Recorded normal behavior under defined conditions |
| Root Cause | Underlying reason an incident occurred |
| Contributing Cause | Condition that increased likelihood or impact |
| RCA | Root Cause Analysis |
| Five Whys | Repeated evidence-based questioning to uncover process causes |
| Escalation | Transfer or request for higher/specialized assistance |
| Physical Diagram | Representation of devices, ports, media, and physical links |
| Logical Diagram | Representation of addressing, VLANs, routes, and security boundaries |
| Rack Elevation | Diagram showing rack-unit placement |
| IPAM | IP Address Management |
| Source of Truth | Authoritative record of intended state |
| Configuration Drift | Difference between intended and actual configuration |
| Bandwidth | Theoretical or configured link capacity |
| Throughput | Actual data-transfer rate |
| Goodput | Useful application data delivered per unit time |
| Latency | Time required for data to travel |
| Jitter | Variation in packet delay |
| Packet Loss | Percentage of packets not delivered |
| Utilization | Percentage of available capacity in use |
| Synthetic Transaction | Automated test that imitates user activity |
| Alert Fatigue | Reduced responsiveness caused by excessive low-value alerts |
| Capacity Planning | Forecasting and preparing for future resource demand |
| Change Management | Controlled process for modifying systems |
| Standard Change | Repeatable low-risk pre-approved change |
| Normal Change | Change assessed and approved before implementation |
| Emergency Change | Urgent, expedited change with retained accountability |
| Maintenance Window | Approved period for planned technical work |
| Rollback | Restoration of the prior known state |
| Golden Configuration | Approved secure baseline for a device role |
| Incident Report | Formal record of impact, timeline, cause, and resolution |
| Handover | Transfer of current operational responsibility and context |
| Verification Matrix | Table of required tests, expected results, and outcomes |
| Portfolio | Curated evidence of skills, reasoning, and completed work |
| STAR | Situation, Task, Action, Result interview framework |

## 27. COMPARISON TABLES

### 27.1 Troubleshooting Approaches

| Approach | Starting Point | Best Use |
|---|---|---|
| Bottom-up | Physical layer | Link/media fault |
| Top-down | Application | One service failure |
| Divide-and-conquer | Middle layer | Unknown fault domain |
| Follow-the-path | Source-to-destination path | Multi-hop failure |
| Baseline comparison | Historical normal | Performance issue |

### 27.2 Physical vs Logical Diagram

| Feature | Physical | Logical |
|---|---|---|
| Shows | Ports, cables, racks, media | VLANs, subnets, routes, zones |
| Main question | How is it physically connected? | How does traffic logically flow? |
| Audience | Install/support/operations | Engineering/security/operations |

### 27.3 Bandwidth vs Throughput vs Goodput

| Metric | Meaning |
|---|---|
| Bandwidth | Maximum/configured capacity |
| Throughput | Actual transferred data rate |
| Goodput | Useful application payload rate |

### 27.4 Standard vs Normal vs Emergency Change

| Type | Approval | Risk/Urgency |
|---|---|---|
| Standard | Pre-approved procedure | Low and repeatable |
| Normal | Reviewed before work | Assessed planned change |
| Emergency | Expedited | Urgent service or risk need |

### 27.5 Incident vs Problem vs Change

| Record | Purpose |
|---|---|
| Incident | Restore service and record impact/timeline |
| Problem/RCA | Identify underlying causes and prevention |
| Change | Control modification to systems |

### 27.6 Monitoring Methods

| Method | Strength | Limitation |
|---|---|---|
| ICMP | Simple reachability/latency | Does not prove application |
| SNMPv3 | Broad device metrics | Poll interval may miss short events |
| Syslog | Event detail | Depends on message quality/retention |
| Flow | Conversation visibility | Not complete packet content |
| Packet capture | Deep evidence | Storage, privacy, capture-point limits |
| Synthetic test | User-view service check | Tests only scripted path |

### 27.7 Career Branches

| Path | Primary Focus | Strong Next Skill |
|---|---|---|
| Network Engineering | Connectivity and infrastructure | Routing, automation, design |
| Cybersecurity | Risk, defense, detection, response | Logs, systems, network defense |
| IT Support | User and endpoint operations | Windows, identity, communication |
| Cloud | Virtual infrastructure and services | IAM, automation, cloud networking |

## 28. REAL-WORLD ANALOGY

A professional troubleshooter is like an investigator and an engineer working together. The investigator preserves the scene, collects evidence, forms a testable explanation, and separates fact from assumption. The engineer understands how the system should operate, repairs it safely, verifies every requirement, and strengthens the design.

Documentation is the case file and operating manual. Change management is the controlled authorization to alter the system. Monitoring is the ongoing observation that reveals whether the repair remains healthy.

## 29. QUICK-RECAP CHEAT SHEET

```text
DIAGNOSE
1. Define symptom, scope, time, and impact
2. Gather evidence before changing state
3. Form a specific, testable hypothesis
4. Test the least disruptive theory
5. Plan, approve, implement, and rollback if required
6. Verify complete service and security
7. Document and prevent recurrence

LAYER PATH
Physical -> Link/VLAN -> IP/Gateway -> Route/ACL/NAT
-> DNS/Transport -> Application

DOCUMENT
Physical + logical diagrams
VLAN/IPAM + device/circuit inventory
Config backups + source of truth
Incident + RCA + change + runbook + handover

BASELINE
Bandwidth, throughput, goodput
Latency, jitter, loss
Utilization, errors, discards
CPU, memory, wireless, power, application response

CHANGE
Reason, scope, risk, commands, approvals
Test plan, success criteria, rollback, communication
Pre/post backup and documentation update

VERIFY
Test allowed behavior AND denied behavior
Ping alone is not full validation

PORTFOLIO
Problem, constraints, design, implementation
Testing, troubleshooting, security, resilience, outcome
Sanitize every artifact

CAREER
Choose one primary 90-day direction
Network | Security | IT Support | Cloud
Keep networking fundamentals active
```

## 7. LESSON ASSESSMENT

This assessment is intentionally focused. Students should answer clearly, use correct networking terminology, and show practical troubleshooting thinking.

### 7.1 Theory Questions

1. Explain the main networking concept covered in this lesson and describe its role in a real enterprise network.
2. Describe two technical problems that can occur when this lesson's concept is poorly designed or incorrectly configured.
3. Explain how a network technician or junior network engineer would verify that this part of the network is working correctly.
4. Describe one security, reliability, or performance concern related to this topic.
5. Explain how this topic connects to CCNA, Network+, IT support, or junior network engineering work.

### 7.2 Multiple-Choice Questions

1. What is the best reason for studying this lesson's topic?
   A. It helps students understand and support real network operation.
   B. It replaces the need for troubleshooting.
   C. It removes the need for IP addressing.
   D. It is only useful for memorizing definitions.

2. When troubleshooting a problem related to this lesson, what should be done first?
   A. Gather evidence and identify the exact scope of the problem.
   B. Replace every network device immediately.
   C. Delete the running configuration without backup.
   D. Assume the Internet service provider is always responsible.

3. Which habit best reflects professional network engineering practice?
   A. Verify changes with commands, tests, and documented results.
   B. Make random changes until something works.
   C. Ignore diagrams and rely only on memory.
   D. Avoid documenting successful fixes.

4. Which item is most useful when proving that a network feature is working?
   A. A successful test result compared with the expected result.
   B. A guess from another user.
   C. A device name with no configuration evidence.
   D. A screenshot unrelated to the problem.

5. What should students connect this lesson to during hands-on practice?
   A. Addressing, device roles, commands, verification, and troubleshooting.
   B. Only typing speed.
   C. Only cable color.
   D. Only memorizing vendor logos.

6. In an enterprise environment, why is documentation important for this topic?
   A. It helps future troubleshooting, audits, handover, and change control.
   B. It makes testing unnecessary.
   C. It disables security risks automatically.
   D. It replaces the need for correct configuration.

7. Which approach gives the strongest learning outcome?
   A. Combining technical explanation with lab practice and verification.
   B. Reading commands without understanding them.
   C. Skipping troubleshooting steps.
   D. Memorizing answers without using the network.

8. If a configuration change causes a new outage, what should the technician use?
   A. A rollback plan and saved baseline information.
   B. A random new subnet.
   C. A different monitor.
   D. A guess without evidence.

9. Which result shows that a student understands the lesson at a practical level?
   A. The student can explain the concept, configure or identify it, test it, and troubleshoot failure.
   B. The student can only repeat the title.
   C. The student avoids using commands.
   D. The student ignores enterprise examples.

10. Why are scenario questions included in this course?
   A. They train students to apply concepts to real network problems.
   B. They remove the need for labs.
   C. They focus only on spelling.
   D. They are unrelated to IT jobs.

### 7.3 Scenario-Based Questions

1. A user or department reports a connectivity problem related to this lesson's topic. Write the first five checks you would perform, the commands or tools you would use, and the evidence you expect to collect.
2. You are asked to explain this topic to a new IT support intern before a hands-on lab. Write a short technical explanation that connects the concept to real devices, real traffic flow, and troubleshooting.

### 7.4 Answer Guide

Theory answers should be marked for technical accuracy, clear explanation, correct terminology, and practical relevance to enterprise networking. Scenario answers should show a logical troubleshooting sequence, evidence gathering, likely causes, verification steps, and a professional final recommendation.

Multiple-choice answers: 1. A; 2. A; 3. A; 4. A; 5. A; 6. A; 7. A; 8. A; 9. A; 10. A
