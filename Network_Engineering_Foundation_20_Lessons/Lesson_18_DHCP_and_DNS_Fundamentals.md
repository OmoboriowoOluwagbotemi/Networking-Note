# LESSON 18: DHCP AND DNS FUNDAMENTALS

## TRAINING FOCUS

This lesson is part of the FEMTECT Network Engineering Foundation course. It is written to help students build strong networking fundamentals through clear explanations, real enterprise context, practical troubleshooting logic, and certification-aware technical depth.


## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 19.1 DHCP and DNS

DHCP means Dynamic Host Configuration Protocol. It is the network service that automatically gives IP configuration to devices. A device does not only need an IP address. It also needs a subnet mask or prefix length, default gateway, DNS server, lease information, and sometimes extra options such as domain name, TFTP server, voice VLAN information, or boot server details.

DNS means Domain Name System. It is the network service that translates human-readable names into IP addresses and provides other name-related information. Users prefer names such as `www.example.com`, `mail.company.com`, or `fileserver01.company.local`. Computers communicate using IP addresses. DNS connects those two worlds.

DHCP answers this question:

```text
What IP settings should this device use?
```

DNS answers this question:

```text
What IP address or service information belongs to this name?
```

In earlier lessons, students learned IPv4 addressing, subnetting, VLANs, inter-VLAN routing, static/default routing, dynamic routing, and NAT/PAT. DHCP and DNS now explain how real devices receive their addresses and how users reach services by name instead of memorizing IP addresses.

### 19.2 Technical Importance: DHCP and DNS Matter

DHCP matters because manual IP configuration does not scale. In a small lab with three computers, an administrator can manually type IP addresses. In a school, hotel, bank branch, hospital, factory floor, office, or wireless guest network with hundreds of devices, manual addressing becomes slow, error-prone, and difficult to audit.

Without DHCP, users may configure duplicate IP addresses, wrong subnet masks, wrong gateways, or wrong DNS servers. Any one of those mistakes can break communication. A laptop may connect to Wi-Fi but fail to reach the internet because it has no default gateway. A desktop may ping the gateway but fail to browse websites because it has the wrong DNS server.

DNS matters because modern networking depends on names. Applications, websites, email systems, cloud services, authentication platforms, file shares, monitoring tools, and security tools all rely on DNS. If DNS fails, the network may look broken even when routing, switching, NAT, and internet connectivity are working.

In real enterprise troubleshooting, DHCP and DNS are among the first services to verify. A user complaint such as "the internet is not working" may really mean the device has an APIPA address because DHCP failed, or it may mean the device has internet connectivity but cannot resolve names because DNS failed.

### 19.3 Deployment Context: DHCP and DNS Operate in the Network

DHCP operates mainly at the application layer but directly supports Layer 3 addressing. It uses UDP ports 67 and 68. The DHCP server listens on UDP port 67. The DHCP client uses UDP port 68. DHCP for IPv4 depends heavily on broadcast traffic at the beginning of the process because a new client may not yet have an IP address.

DNS also operates at the application layer. DNS commonly uses UDP port 53 for normal queries and TCP port 53 for zone transfers and larger responses. Modern DNS can also use encrypted methods such as DNS over HTTPS and DNS over TLS, but traditional enterprise troubleshooting still begins with understanding standard DNS over port 53.

DHCP and DNS are often hosted on Windows Server in many enterprise networks. They may also be hosted on Linux servers, network appliances, routers, firewalls, cloud services, or managed service platforms.

Common DHCP and DNS placement:

| Environment | Common DHCP Location | Common DNS Location |
|---|---|---|
| Small office | Router or firewall | ISP DNS, router, or public DNS |
| Windows enterprise | Windows Server DHCP | Active Directory-integrated DNS |
| Linux environment | `dhcpd`, `dnsmasq`, or similar | BIND, Unbound, or PowerDNS |
| Cisco lab | Router DHCP pool | External DNS server or simulated server |
| Cloud network | Cloud DHCP service | Cloud private DNS and public DNS |
| Guest Wi-Fi | Firewall, router, or controller-integrated DHCP | Public DNS or filtered DNS |

## 19.4 DHCP Operation: Discover, Offer, Request, Acknowledge

DHCP uses a four-step process commonly called DORA:

```text
Discover
Offer
Request
Acknowledge
```

The process begins when a client joins a network and does not have a valid IPv4 address. Because the client does not yet know its own address or the DHCP server address, it sends a broadcast message.

DHCP DORA Process

| Step | Message | Direction | Purpose |
|---|---|---|---|
| 1 | DHCP Discover | Client to broadcast | Client asks whether any DHCP server is available |
| 2 | DHCP Offer | Server to client | Server offers an available IP configuration |
| 3 | DHCP Request | Client to server/broadcast | Client requests the offered configuration |
| 4 | DHCP Acknowledge | Server to client | Server confirms the lease and settings |

### 19.4.1 DHCP Discover

The DHCP Discover message is sent by a client that needs configuration. The client may use source IP address `0.0.0.0` because it does not yet have a usable IP address. The destination is usually the limited broadcast address `255.255.255.255`.

At this stage, the client is saying:

```text
I am on this network. Is there any DHCP server that can give me IP settings?
```

Because the message is broadcast, it normally stays inside the local broadcast domain. This is why VLAN design matters. If a client is in VLAN 20, its DHCP Discover message does not automatically cross into VLAN 10 or VLAN 30. If the DHCP server is not in the same VLAN, a DHCP relay is required.

### 19.4.2 DHCP Offer

The DHCP server replies with a DHCP Offer. The offer contains proposed IP configuration, such as IP address, subnet mask, lease time, default gateway, DNS server, and other options.

At this stage, the server is saying:

```text
You may use this address and these network settings.
```

There may be more than one DHCP server on a network. A client can receive multiple offers, but it normally chooses one.

### 19.4.3 DHCP Request

The DHCP client sends a DHCP Request to accept an offer. This message tells the selected DHCP server that the client wants to use the offered address. It also informs other DHCP servers that their offers were not selected.

At this stage, the client is saying:

```text
I accept this offered configuration.
```

### 19.4.4 DHCP Acknowledge

The DHCP server sends a DHCP Acknowledge, often called DHCP ACK. This confirms the lease. After the ACK, the client can use the assigned IP address and communicate normally.

At this stage, the server is saying:

```text
The lease is approved. You may use these settings.
```

If the server cannot approve the address, it may send a DHCP NAK, or negative acknowledgment. A DHCP NAK tells the client that the requested address is not valid and that the client should restart the DHCP process.

## 19.5 DHCP Scope Design

A DHCP scope is a range of IP addresses and configuration options that a DHCP server can assign to clients on a specific subnet. A scope must match the subnet where clients live.

For example, if VLAN 10 uses subnet `192.168.10.0/24`, the DHCP scope for VLAN 10 may assign addresses from `192.168.10.50` to `192.168.10.200`. The default gateway may be `192.168.10.1`, and DNS may point to `192.168.10.10`.

DHCP scope design should follow the IP addressing and VLAN design already created for the network. DHCP should not be designed randomly. It must match the subnet plan, gateway addresses, reserved infrastructure addresses, security policy, and documentation.

Example Scope Design

| VLAN | Purpose | Subnet | Gateway | DHCP Range | DNS Server |
|---|---|---|---|---|---|
| 10 | Staff | 192.168.10.0/24 | 192.168.10.1 | 192.168.10.50-192.168.10.220 | 192.168.100.10 |
| 20 | Voice | 192.168.20.0/24 | 192.168.20.1 | 192.168.20.50-192.168.20.200 | 192.168.100.10 |
| 30 | Guest Wi-Fi | 192.168.30.0/24 | 192.168.30.1 | 192.168.30.50-192.168.30.250 | 8.8.8.8 |
| 40 | Servers | 192.168.40.0/24 | 192.168.40.1 | No general client DHCP | 192.168.100.10 |

The server VLAN often does not need a broad DHCP range because servers are usually configured with static IP addresses or DHCP reservations. Guest networks usually need larger pools because mobile devices join and leave frequently.

## 19.6 DHCP Reservations

A DHCP reservation gives the same IP address to the same device every time, based on the device's MAC address or client identifier. The device still uses DHCP, but the server always reserves a specific address for it.

Reservations are useful when a device should keep a consistent address but administrators still want centralized DHCP management. Examples include printers, IP phones, access points, scanners, CCTV devices, time attendance machines, and some network appliances.

Reservation Example

| Device | MAC Address | Reserved IP | Reason |
|---|---|---|---|
| Printer-Admin | 00:11:22:AA:BB:CC | 192.168.10.25 | Users need stable printer mapping |
| AP-Lobby | 00:11:22:DD:EE:FF | 192.168.50.10 | Controller and monitoring need stable AP address |
| CCTV-NVR | 00:11:22:44:55:66 | 192.168.60.20 | Security team needs consistent access |

A reservation is not the same as a manually configured static IP address. With a static IP address, the device itself is configured manually. With a reservation, the DHCP server manages the address assignment.

## 19.7 DHCP Lease Time

A DHCP lease is temporary permission to use an IP address. Lease time controls how long a client may use the address before renewal is required.

Lease time matters because different networks have different device behavior. A corporate desktop network may use longer leases because devices stay in the same place for a long time. A guest Wi-Fi network may use shorter leases because users arrive and leave frequently.

Lease Time Design

| Network Type | Suggested Lease Behavior | Reason |
|---|---|---|
| Office desktops | Longer lease | Stable devices, less DHCP traffic |
| Guest Wi-Fi | Shorter lease | Many temporary users |
| Conference/event network | Very short lease | High turnover |
| Voice VLAN | Medium to long lease | Phones are stable but may reboot |
| Lab network | Short to medium lease | Frequent topology changes |

If the lease is too short, clients renew too often and DHCP traffic increases. If the lease is too long, addresses may remain unavailable after users leave, especially on guest networks.

## 19.8 DHCP Exclusions

An exclusion is an address or range inside a subnet that the DHCP server must not assign dynamically. Exclusions protect addresses used by gateways, servers, printers, network devices, or reserved future use.

For example, in subnet `192.168.10.0/24`, administrators may exclude:

```text
192.168.10.1-192.168.10.49
192.168.10.221-192.168.10.254
```

Then DHCP can assign:

```text
192.168.10.50-192.168.10.220
```

This design keeps important infrastructure addresses outside the general client pool.

Exclusion Planning

| Address Range | Use |
|---|---|
| .1-.9 | Gateways and network infrastructure |
| .10-.29 | Servers and appliances |
| .30-.49 | Printers, CCTV, access points, reserved devices |
| .50-.220 | DHCP client pool |
| .221-.254 | Future growth, testing, or special assignments |

Good DHCP design prevents duplicate IP addresses and keeps troubleshooting predictable.

## 19.9 DHCP Options

DHCP options are additional settings delivered to clients. The IP address is only one part of the configuration. A useful DHCP lease usually includes several options.

Common DHCP Options

| Option | Purpose |
|---|---|
| Subnet Mask | Tells the client which addresses are local |
| Default Gateway / Router | Tells the client where to send remote traffic |
| DNS Server | Tells the client which resolver to query |
| Domain Name | Provides local DNS search suffix |
| Lease Time | Defines how long the lease is valid |
| NTP Server | Provides time synchronization |
| TFTP Server | Used by some phones, PXE boot systems, and network devices |

In a voice network, DHCP may provide options needed by IP phones to locate call managers or TFTP servers. In a PXE boot environment, DHCP may provide boot server details. In normal user networks, the most important options are gateway and DNS.

## 19.10 DHCP Relay and IP Helper

DHCP clients often use broadcast messages, but routers do not forward broadcasts by default. This creates a practical issue in VLAN-based networks.

Imagine this design:

```text
VLAN 10 users: 192.168.10.0/24
VLAN 20 users: 192.168.20.0/24
DHCP server:   192.168.100.10
```

The DHCP server is in a server VLAN, not inside every user VLAN. A laptop in VLAN 10 sends a DHCP Discover broadcast, but the router or Layer 3 switch will not forward that broadcast automatically. A DHCP relay solves this problem.

On Cisco devices, DHCP relay is commonly configured with the `ip helper-address` command on the Layer 3 interface that acts as the gateway for the client VLAN.

Example Cisco IOS DHCP Relay

```text
interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 ip helper-address 192.168.100.10

interface vlan 20
 ip address 192.168.20.1 255.255.255.0
 ip helper-address 192.168.100.10
```

The relay agent receives the client's DHCP broadcast, converts it into a unicast message toward the DHCP server, and includes information about the client subnet. The DHCP server uses that relay information to choose the correct scope.

DHCP Relay Process

| Step | Action |
|---|---|
| 1 | Client sends DHCP Discover broadcast in its VLAN |
| 2 | Gateway interface receives the broadcast |
| 3 | Relay agent forwards the request to DHCP server as unicast |
| 4 | DHCP server selects the correct scope |
| 5 | DHCP server replies to relay agent |
| 6 | Relay agent forwards response to client |

If the helper address is missing, wrong, blocked by ACL, or placed on the wrong interface, clients may fail to receive IP addresses.

## 19.11 Cisco IOS DHCP Server Basics

Cisco routers and Layer 3 switches can provide DHCP service in small networks and labs. In larger enterprises, DHCP is often centralized on Windows or Linux servers, but understanding Cisco DHCP configuration is useful for CCNA and practical router/switch administration.

Example Cisco IOS DHCP Configuration

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.49
ip dhcp excluded-address 192.168.10.221 192.168.10.254

ip dhcp pool STAFF-VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.100.10
 domain-name femtect.local
 lease 7
```

This configuration tells the Cisco device to avoid specific excluded addresses, create a DHCP pool for VLAN 10, assign addresses from the `192.168.10.0/24` subnet, provide gateway `192.168.10.1`, provide DNS server `192.168.100.10`, and set a lease.

Useful Cisco DHCP verification commands:

```text
show ip dhcp binding
show ip dhcp pool
show ip dhcp server statistics
show running-config | section dhcp
debug ip dhcp server events
```

Use `debug` commands carefully in production because they can create heavy CPU and console output.

## 19.12 Windows DHCP and Client Verification

In Windows networks, DHCP is commonly deployed through Windows Server. DHCP scopes are created in the DHCP management console, and DHCP may integrate with Active Directory authorization. Windows clients receive configuration automatically when their adapter is set to obtain an IP address automatically.

On a Windows client, the most important first command is:

```text
ipconfig /all
```

This shows the IP address, subnet mask, default gateway, DNS servers, DHCP enabled status, DHCP server, lease obtained time, and lease expiration time.

Useful Windows commands:

| Command | Purpose |
|---|---|
| `ipconfig /all` | Show full IP, DHCP, DNS, and adapter details |
| `ipconfig /release` | Release the current IPv4 DHCP lease |
| `ipconfig /renew` | Request a new IPv4 DHCP lease |
| `ipconfig /flushdns` | Clear DNS resolver cache |
| `ipconfig /displaydns` | Display local DNS resolver cache |
| `nslookup name` | Test DNS name resolution |
| `ping gateway` | Test local gateway reachability |
| `tracert destination` | Trace Layer 3 path |

If a Windows device shows an address beginning with `169.254`, it is using APIPA. APIPA usually means the device did not receive a valid DHCP lease. The cause may be a disconnected cable, wrong VLAN, missing helper address, DHCP server outage, exhausted scope, firewall block, or Wi-Fi authentication problem.

## 19.13 Linux DHCP and DNS Verification

Linux systems can be DHCP clients, DHCP servers, DNS clients, or DNS servers. The exact commands depend on the distribution and network manager, but the troubleshooting ideas remain consistent.

Useful Linux commands:

| Command | Purpose |
|---|---|
| `ip addr` | Show interface addresses |
| `ip route` | Show routing table and default gateway |
| `resolvectl status` | Show DNS resolver information on systemd-based systems |
| `cat /etc/resolv.conf` | Show resolver configuration on many systems |
| `dig name` | Query DNS and inspect detailed response |
| `nslookup name` | Basic DNS lookup |
| `ping gateway` | Test local gateway |
| `traceroute destination` | Trace path, if installed |
| `journalctl -u NetworkManager` | Review NetworkManager logs on some systems |

Linux servers may use BIND for DNS, ISC DHCP, Kea DHCP, `dnsmasq`, or other services. In enterprise support roles, students do not need to memorize every Linux service immediately, but they should understand how to verify the assigned address, default route, and DNS resolver.

## 19.14 Name Resolution Process

Name resolution is the process of converting a name into the information needed to reach a service. Most beginner explanations say "DNS converts names to IP addresses." That is true, but DNS does more than that. DNS can also identify mail servers, name servers, aliases, text records, reverse mappings, and service-related records.

When a user opens a website such as `www.company.com`, the device must discover the IP address for that name. The process usually begins locally and then moves outward.

Basic DNS Resolution Flow

| Step | Action |
|---|---|
| 1 | User or application requests a name |
| 2 | Device checks local cache |
| 3 | Device may check local hosts file |
| 4 | Device queries configured DNS resolver |
| 5 | Resolver checks its cache |
| 6 | Resolver performs recursive lookup if needed |
| 7 | Resolver returns an answer |
| 8 | Client connects to the returned IP address |

DNS troubleshooting should separate name resolution from connectivity. If `ping 8.8.8.8` works but `ping google.com` fails, routing and internet access may be working while DNS is failing. If both fail, the issue may be addressing, gateway, routing, NAT, firewall, or ISP connectivity.

## 19.15 DNS Hierarchy

DNS is hierarchical. Names are organized from the root of DNS down to top-level domains, domains, and host records.

For example:

```text
www.branch.company.com
```

This name can be read from right to left:

| Part | Meaning |
|---|---|
| `.` | DNS root |
| `com` | Top-level domain |
| `company` | Registered domain |
| `branch` | Subdomain |
| `www` | Host or service name |

The DNS hierarchy allows the internet to scale. No single server stores every DNS record for the entire world. Instead, authority is delegated.

## 19.16 DNS Record Types

DNS records store specific information about names and services. Different record types answer different questions.

Common DNS Record Types

| Record Type | Purpose | Example |
|---|---|---|
| A | Maps a name to an IPv4 address | `server1.company.local -> 192.168.10.20` |
| AAAA | Maps a name to an IPv6 address | `server1.company.local -> 2001:db8::20` |
| CNAME | Creates an alias to another name | `www -> webserver01.company.local` |
| MX | Identifies mail servers for a domain | `company.com mail handled by mail.company.com` |
| TXT | Stores text information | SPF, DKIM, verification records |
| NS | Identifies authoritative name servers | `ns1.company.com` |
| PTR | Maps an IP address back to a name | `192.168.10.20 -> server1.company.local` |

### 19.16.1 A Records

An A record maps a hostname to an IPv4 address. It is one of the most common DNS records.

Example:

```text
fileserver01.femtect.local -> 192.168.40.20
```

When a user accesses `\\fileserver01\femshare`, the device may use DNS to resolve the server name to its IP address before connecting using SMB.

### 19.16.2 AAAA Records

An AAAA record maps a hostname to an IPv6 address.

Example:

```text
web01.femtect.local -> 2001:db8:10:40::20
```

The name "AAAA" is used because IPv6 addresses are four times the length of IPv4 addresses in bits: 128 bits instead of 32 bits.

### 19.16.3 CNAME Records

A CNAME record creates an alias. It points one name to another name, not directly to an IP address.

Example:

```text
intranet.femtect.local -> webserver01.femtect.local
```

CNAME records are useful when users need a friendly name while the real server name may change.

### 19.16.4 MX Records

MX records identify mail servers for a domain. When another mail server wants to send mail to `user@company.com`, it checks the MX records for `company.com`.

Example:

```text
company.com MX 10 mail1.company.com
company.com MX 20 mail2.company.com
```

The lower preference number is tried first. If the first mail server is unavailable, the sender may try the next one.

### 19.16.5 TXT Records

TXT records store text information. They are commonly used for domain verification and email security records such as SPF, DKIM, and DMARC.

In cybersecurity, TXT records matter because email authentication helps reduce spoofing and phishing.

### 19.16.6 NS Records

NS records identify which name servers are authoritative for a zone. They help delegate responsibility in the DNS hierarchy.

### 19.16.7 PTR Records

PTR records provide reverse lookup. Instead of resolving name to IP, PTR resolves IP to name.

Example:

```text
192.168.40.20 -> fileserver01.femtect.local
```

PTR records are useful for logging, troubleshooting, email systems, and security investigations.

## 19.17 Forward Zones and Reverse Zones

A DNS zone is an administrative portion of DNS. A zone contains records for a domain or part of a domain.

A forward lookup zone resolves names to IP addresses.

```text
fileserver01.femtect.local -> 192.168.40.20
```

A reverse lookup zone resolves IP addresses to names.

```text
192.168.40.20 -> fileserver01.femtect.local
```

Forward vs Reverse Zones

| Zone Type | Direction | Common Record Type | Example Use |
|---|---|---|---|
| Forward Zone | Name to IP | A, AAAA, CNAME, MX, TXT, NS | User enters server name |
| Reverse Zone | IP to name | PTR | Admin investigates logs or verifies mail server identity |

Forward zones are usually more visible to users. Reverse zones are especially useful in administration, monitoring, and security.

## 19.18 Authoritative vs Recursive DNS

An authoritative DNS server holds the official records for a DNS zone. If a server is authoritative for `company.com`, it can provide official answers for names in that zone.

A recursive DNS resolver performs lookups on behalf of clients. A client asks the recursive resolver a question. If the resolver does not already know the answer, it queries other DNS servers through the DNS hierarchy until it finds the answer or fails.

Authoritative vs Recursive DNS

| Feature | Authoritative DNS | Recursive DNS |
|---|---|---|
| Main Role | Stores official records | Finds answers for clients |
| Used By | Other DNS servers and resolvers | End-user devices and applications |
| Example | Public DNS hosting for `company.com` | ISP DNS, corporate resolver, public resolver |
| Stores Zone Data | Yes | Usually cache, not official zone authority |
| Enterprise Example | AD DNS zone for internal domain | DNS server resolving internet names for clients |

In many organizations, the same DNS server may host internal authoritative zones and also perform recursive resolution for internal clients. Security design must control who is allowed to use recursion. Open recursive DNS servers exposed to the internet can be abused in attacks.

## 19.19 DNS Caching and TTL

DNS caching stores previous answers temporarily. Caching improves performance and reduces repeated DNS queries. TTL means Time To Live. It tells DNS clients and resolvers how long a record may be cached.

If a DNS record has a TTL of 3600 seconds, it may be cached for one hour. If the IP address changes before the TTL expires, some clients may continue using the old answer until the cache expires or is cleared.

TTL matters during migrations. If a company is moving a website to a new public IP address, administrators may lower the TTL before the change. This helps clients receive the new answer faster after the migration.

DNS Cache Troubleshooting

| Symptom | Possible Cause | Action |
|---|---|---|
| Some users reach old server | Cached old DNS answer | Flush cache or wait for TTL |
| Admin changed DNS but users see old IP | TTL has not expired | Verify record from authoritative server |
| One computer fails but others work | Local DNS cache issue | Run `ipconfig /flushdns` on Windows |
| Public users see mixed results | Global DNS propagation and caching | Check multiple resolvers |

## 19.20 DHCP and DNS Working Together

DHCP and DNS often work together. DHCP gives clients their DNS server address. In Windows Active Directory environments, DHCP can also update DNS records dynamically when clients receive addresses.

For example, a laptop named `HR-LAPTOP-17` receives `192.168.10.87` from DHCP. The DNS server may register:

```text
HR-LAPTOP-17.femtect.local -> 192.168.10.87
```

This allows administrators and services to find the device by name.

DHCP and DNS Relationship

| DHCP Provides | DNS Provides |
|---|---|
| IP address | Name-to-address resolution |
| Subnet mask/prefix | Address-to-name resolution through PTR |
| Default gateway | Service discovery through records |
| DNS server address | Central naming database |
| Lease information | Cached and authoritative answers |

If DHCP gives the wrong DNS server, users may have correct IP addresses but fail to access internal resources by name. If DNS has stale records, users may connect to the wrong device or fail to reach a moved service.

## 19.21 Enterprise Example: Multi-VLAN Office

Consider a company with staff, voice, guest Wi-Fi, and server VLANs:

| VLAN | Name | Subnet | Gateway | DHCP/DNS Design |
|---|---|---|---|---|
| 10 | Staff | 192.168.10.0/24 | 192.168.10.1 | DHCP scope with internal DNS |
| 20 | Voice | 192.168.20.0/24 | 192.168.20.1 | DHCP scope with voice options |
| 30 | Guest | 192.168.30.0/24 | 192.168.30.1 | DHCP scope with public or filtered DNS |
| 40 | Servers | 192.168.40.0/24 | 192.168.40.1 | Mostly static/reserved addresses |
| 100 | Infrastructure | 192.168.100.0/24 | 192.168.100.1 | DHCP/DNS servers and management tools |

The DHCP server is `192.168.100.10`. The internal DNS server is also `192.168.100.10`. Because clients are in different VLANs, each client VLAN gateway needs an `ip helper-address 192.168.100.10`.

Staff devices should receive internal DNS so they can resolve internal names such as `fileserver01.femtect.local`. Guest devices should not receive internal DNS if guests should not access internal resources. They may receive public DNS or security-filtered DNS.

This design connects DHCP, DNS, VLANs, routing, and security policy. DHCP provides correct settings. DNS provides names. Inter-VLAN routing carries traffic between networks. ACLs or firewalls decide what communication is allowed.

## 19.22 DHCP Troubleshooting Method

DHCP troubleshooting should be systematic. Do not assume the DHCP server is the problem immediately. A client can fail DHCP because of Layer 1, Layer 2, VLAN, relay, server, scope, firewall, or exhaustion issues.

DHCP Troubleshooting Flow

| Step | Question | Example Test |
|---|---|---|
| 1 | Is the device physically/wirelessly connected? | Check link light or Wi-Fi association |
| 2 | Is the device in the correct VLAN/SSID? | Check switchport or WLAN mapping |
| 3 | Did the client receive an APIPA address? | `ipconfig /all` |
| 4 | Is the DHCP scope active and not exhausted? | Check DHCP server scope |
| 5 | Is DHCP relay configured? | Check `ip helper-address` |
| 6 | Can relay reach DHCP server? | Ping server from gateway |
| 7 | Are UDP 67/68 allowed? | Check ACL/firewall |
| 8 | Are there duplicate or rogue DHCP servers? | Inspect DHCP logs and leases |

Common DHCP Problems

| Symptom | Likely Cause |
|---|---|
| Client has `169.254.x.x` | DHCP process failed |
| Client gets wrong subnet | Wrong VLAN or wrong DHCP scope |
| Client gets IP but no internet | Missing/wrong gateway, NAT, route, or firewall issue |
| Client gets IP but names fail | Wrong DNS server option |
| Some clients fail, others work | Scope exhaustion or lease issue |
| New VLAN clients fail | Missing `ip helper-address` |
| Guest users reach internal DNS | Wrong DHCP option or policy design |

## 19.23 DNS Troubleshooting Method

DNS troubleshooting should separate IP connectivity from name resolution. First prove whether the network path works using an IP address. Then test name resolution.

DNS Troubleshooting Flow

| Step | Question | Example Test |
|---|---|---|
| 1 | Does the client have a valid IP address? | `ipconfig /all` or `ip addr` |
| 2 | Can the client reach the gateway? | `ping 192.168.10.1` |
| 3 | Can the client reach a known IP? | `ping 8.8.8.8` or internal server IP |
| 4 | Which DNS server is configured? | `ipconfig /all`, `resolvectl status` |
| 5 | Can the client query DNS? | `nslookup www.example.com` |
| 6 | Is the DNS record correct? | `nslookup fileserver01.femtect.local` |
| 7 | Is the issue cache-related? | Flush DNS cache or test authoritative server |
| 8 | Is firewall/security blocking DNS? | Check UDP/TCP 53 policy |

Common DNS Problems

| Symptom | Likely Cause |
|---|---|
| IP ping works, name ping fails | DNS resolution failure |
| Internal names fail, internet names work | Wrong DNS server or missing internal zone |
| Internet names fail, internal names work | Forwarder/recursive resolution issue |
| One hostname resolves to old IP | Stale DNS record or cache |
| Reverse lookup fails | Missing PTR or reverse zone |
| Email delivery issues | Wrong MX, SPF, DKIM, DMARC, or PTR |
| Random DNS failures | Resolver outage, packet loss, filtering, or overloaded DNS |

## 19.25 Cybersecurity Relevance

DHCP and DNS are important security targets. If an attacker can control DHCP, the attacker can give victims a wrong gateway or DNS server. If an attacker can control DNS, the attacker can redirect users to malicious services.

Common DHCP-related threats:

| Threat | Explanation |
|---|---|
| Rogue DHCP Server | Unauthorized server gives wrong IP settings |
| DHCP Starvation | Attacker consumes all available leases |
| Wrong Gateway Option | Clients are redirected through attacker-controlled path |
| Wrong DNS Option | Clients use malicious DNS resolver |

Common DNS-related threats:

| Threat | Explanation |
|---|---|
| DNS Spoofing | False DNS answers redirect users |
| DNS Cache Poisoning | Resolver cache is polluted with wrong records |
| DNS Tunneling | Malware hides traffic inside DNS queries |
| Domain Spoofing | Attackers use similar-looking domains for phishing |
| Open Resolver Abuse | Publicly exposed resolver is abused for attacks |

Security controls include DHCP snooping, Dynamic ARP Inspection, trusted DHCP ports, DNS filtering, secure DNS server configuration, DNS logging, split DNS design, least-privilege administration, and monitoring for unusual DNS queries.

CCNA students should connect this lesson to DHCP snooping and Dynamic ARP Inspection from later access-layer security topics. Network+ students should remember that DNS and DHCP are both core infrastructure services and common troubleshooting/security focus areas.

## 19.26 Cloud Networking Relevance

Cloud platforms also use DHCP and DNS concepts, even if administrators do not always manage them the same way as on-premises networks.

In a cloud virtual network, instances often receive private IP addresses automatically from the cloud platform. The cloud provider manages the DHCP-like address assignment service. Administrators define subnets, route tables, DNS settings, private zones, and sometimes custom DNS resolvers.

Cloud DNS examples:

| Cloud Concept | DNS/DHCP Relationship |
|---|---|
| Virtual Network/Subnet | Defines address space where instances receive IPs |
| Private DNS Zone | Resolves internal cloud service names |
| Public DNS Zone | Resolves internet-facing applications |
| Custom DNS Resolver | Allows cloud resources to query enterprise DNS |
| Hybrid DNS | Connects on-premises and cloud name resolution |
| NAT Gateway | Allows private instances to reach internet after they receive private IPs |

In hybrid networks, DNS design is critical. An on-premises user may need to resolve a cloud server name. A cloud workload may need to resolve an on-premises Active Directory domain controller. If DNS forwarding or private zones are wrong, the VPN may be up and routing may work, but applications still fail because names do not resolve.

## 19.27 Interview and Exam Relevance

In IT support interviews, DHCP and DNS questions are extremely common because they appear in daily troubleshooting. A support technician must know how to check IP configuration, identify APIPA, renew a DHCP lease, verify DNS servers, flush DNS cache, and test name resolution.

In network engineering interviews, questions may focus on DHCP relay, multiple VLAN scopes, rogue DHCP, DNS zones, authoritative vs recursive DNS, split DNS, and troubleshooting name resolution across routed networks.

For CCNA, students should remember DHCP operation, DHCP relay using `ip helper-address`, DHCP server configuration basics, DNS purpose, record types, and troubleshooting commands.

For CompTIA Network+ N10-009, students should remember DHCP, DNS, common ports, record types, name resolution, lease behavior, reservations, scope configuration, and service troubleshooting.

## 20. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| DHCP | Dynamic Host Configuration Protocol, used to automatically assign IP configuration to clients. |
| DNS | Domain Name System, used to resolve names and provide name-related records. |
| DORA | DHCP Discover, Offer, Request, Acknowledge process. |
| Scope | A DHCP address range and options for a subnet. |
| Reservation | A DHCP configuration that gives a specific device the same IP address. |
| Lease | Temporary permission for a DHCP client to use an IP address. |
| Exclusion | Address or range that DHCP must not dynamically assign. |
| DHCP Relay | Device function that forwards DHCP requests between client VLANs and DHCP servers. |
| IP Helper | Cisco `ip helper-address` feature used for DHCP relay. |
| Resolver | DNS client or server component that looks up DNS information. |
| Authoritative DNS | DNS server that holds official records for a zone. |
| Recursive DNS | DNS server that performs lookups on behalf of clients. |
| Forward Lookup Zone | DNS zone used to resolve names to IP addresses. |
| Reverse Lookup Zone | DNS zone used to resolve IP addresses to names. |
| A Record | DNS record that maps a name to an IPv4 address. |
| AAAA Record | DNS record that maps a name to an IPv6 address. |
| CNAME Record | DNS alias record. |
| MX Record | DNS mail exchanger record. |
| TXT Record | DNS text record. |
| NS Record | DNS name server record. |
| PTR Record | DNS pointer record used for reverse lookup. |
| TTL | Time To Live, the amount of time a DNS record may be cached. |
| APIPA | Automatic Private IP Addressing, commonly `169.254.0.0/16`, used when DHCP fails. |

## 21. COMPARISON TABLES

### 21.1 DHCP vs DNS

| Feature | DHCP | DNS |
|---|---|---|
| Main Purpose | Assign IP configuration | Resolve names and records |
| Common Ports | UDP 67/68 | UDP/TCP 53 |
| Client Need | IP settings | Name resolution |
| Failure Symptom | APIPA, wrong gateway, wrong DNS | Names fail, IP access may still work |
| Enterprise Role | Address automation | Service discovery and naming |

### 21.2 DHCP Scope vs Reservation vs Exclusion

| Feature | Scope | Reservation | Exclusion |
|---|---|---|
| Meaning | Assignable range and options | Fixed assignment for one device | Address range DHCP must not assign |
| Based On | Subnet design | MAC/client identifier | Infrastructure address planning |
| Example | `192.168.10.50-192.168.10.220` | Printer gets `192.168.10.25` | Gateway `192.168.10.1` excluded |

### 21.3 Authoritative vs Recursive DNS

| Feature | Authoritative DNS | Recursive DNS |
|---|---|---|
| Holds Official Zone Records | Yes | No, except cache |
| Answers For | Its own zones | Client lookups |
| Example | DNS host for `company.com` | Corporate DNS resolver |
| Security Concern | Zone integrity | Recursion abuse and cache poisoning |

### 21.4 Forward vs Reverse Lookup

| Feature | Forward Lookup | Reverse Lookup |
|---|---|---|
| Direction | Name to IP | IP to name |
| Common Record | A, AAAA | PTR |
| Example | `server1 -> 192.168.10.20` | `192.168.10.20 -> server1` |
| Common Use | Application access | Logs, monitoring, email, investigation |

### 21.5 DHCP and DNS Troubleshooting Commands

| Platform | DHCP Commands | DNS Commands |
|---|---|---|
| Windows | `ipconfig /all`, `ipconfig /release`, `ipconfig /renew` | `nslookup`, `ipconfig /flushdns`, `ipconfig /displaydns` |
| Linux | `ip addr`, `ip route`, NetworkManager logs | `dig`, `nslookup`, `resolvectl status` |
| Cisco IOS | `show ip dhcp binding`, `show ip dhcp pool` | Check configured DNS server, test reachability, verify DHCP option |

## 22. REAL-WORLD EXAMPLE / ANALOGY

Think of DHCP as the reception desk in an office building. When a visitor arrives, reception gives the visitor a badge, tells them which floor to go to, and gives basic instructions. In networking, DHCP gives a device an IP address, subnet mask, gateway, DNS server, and lease time.

Think of DNS as the company directory. A person may know "Accounts Department" but not the exact room number. The directory tells them where to go. In networking, a user knows `portal.company.com`, but the computer needs an IP address. DNS provides the mapping.

If reception fails, the visitor may never enter the building properly. If the directory fails, the visitor may enter the building but not find the correct office. This is why DHCP and DNS failures can look similar to users but require different troubleshooting steps.

## 23. QUICK-RECAP CHEAT SHEET

- DHCP automatically assigns IP configuration to clients.
- DNS resolves names and other DNS records.
- DHCP uses UDP ports 67 and 68.
- DNS commonly uses UDP/TCP port 53.
- DHCP DORA means Discover, Offer, Request, Acknowledge.
- A DHCP scope must match the client subnet.
- A DHCP reservation gives the same device the same IP through DHCP.
- An exclusion prevents DHCP from assigning protected addresses.
- A lease is temporary permission to use an IP address.
- DHCP relay is required when clients and DHCP server are in different routed networks.
- Cisco uses `ip helper-address` for DHCP relay.
- APIPA usually means the client failed to receive DHCP.
- A records map names to IPv4 addresses.
- AAAA records map names to IPv6 addresses.
- CNAME records create aliases.
- MX records identify mail servers.
- TXT records store text such as verification and email security data.
- NS records identify authoritative DNS servers.
- PTR records support reverse lookup.
- Forward zones resolve names to IP addresses.
- Reverse zones resolve IP addresses to names.
- Authoritative DNS stores official zone records.
- Recursive DNS performs lookups for clients.
- Always separate IP connectivity troubleshooting from DNS troubleshooting.

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
