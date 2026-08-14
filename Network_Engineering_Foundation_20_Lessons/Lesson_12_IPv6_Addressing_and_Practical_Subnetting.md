# LESSON 12: IPV6 ADDRESSING AND PRACTICAL SUBNETTING

## TRAINING FOCUS

This lesson is part of the FEMTECT Network Engineering Foundation course. It is written to help students build strong networking fundamentals through clear explanations, real enterprise context, practical troubleshooting logic, and certification-aware technical depth.


## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 12.1 IPv6

IPv6 means Internet Protocol version 6. It is the modern IP addressing system designed to replace IPv4 and provide a much larger address space. IPv6 operates at Layer 3 of the OSI model, the Network layer, just like IPv4. It provides logical addressing so packets can be delivered across local networks, enterprise networks, cloud networks, service provider networks, and the internet.

In Lesson 10, IPv4 was introduced as a 32-bit addressing system. In Lesson 11, students learned how to subnet IPv4 networks using CIDR, network addresses, broadcast addresses, host ranges, and VLSM. IPv6 continues the Layer 3 addressing story, but it is not simply IPv4 with more digits. IPv6 has a different address format, different address types, different auto-configuration behavior, and no broadcast.

An IPv6 address is 128 bits long. Humans write IPv6 addresses in hexadecimal, divided into eight groups called hextets. Each hextet contains 16 bits and is separated by colons.

Example:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

Because full IPv6 addresses can be long, IPv6 includes abbreviation rules. The same address can be shortened to:

```text
2001:db8::1
```

IPv6 exists because IPv4 address space is limited. Private IPv4 addressing and NAT helped extend IPv4 life, but they did not solve the underlying shortage of globally unique addresses. IPv6 provides a much larger address space and was designed for scalable addressing, efficient routing, auto-configuration, and modern network growth.

For CCNA and CompTIA Network+, students must understand IPv6 structure, abbreviation, address types, link-local addressing, global unicast addressing, multicast, anycast, SLAAC, DHCPv6, and basic IPv6 troubleshooting.

### 12.2 Technical and Business Importance of IPv6

IPv6 matters because modern networks are increasingly dual-stack, cloud-connected, mobile, and internet-facing. Even if an organization still uses IPv4 heavily inside the LAN, IPv6 may already exist on Windows, Linux, macOS, mobile devices, cloud platforms, ISP networks, VPN services, and security tools.

Many technicians ignore IPv6 because they believe their company "does not use it." This is risky. Devices may automatically configure IPv6 link-local addresses. Applications may prefer IPv6 when available. Security tools may log IPv6 traffic. Attackers may abuse unmanaged IPv6 behavior if administrators monitor only IPv4.

IPv6 also matters because it changes troubleshooting thinking. There is no ARP in IPv6. IPv6 uses Neighbor Discovery Protocol through ICMPv6. There is no traditional IPv4 broadcast. IPv6 uses multicast for many discovery functions. Hosts commonly have multiple IPv6 addresses on one interface, including link-local and global unicast addresses.

In enterprise and cloud environments, IPv6 supports internet-facing services, mobile provider networks, large-scale routing, and cloud workloads. A network engineer does not need to memorize every IPv6 detail at this stage, but must understand the basic address structure and behavior well enough to configure, verify, and troubleshoot it.

## 12.3 IPv6 ADDRESS STRUCTURE

An IPv6 address is 128 bits long. It is written as eight hextets separated by colons. Each hextet represents 16 bits and is written in hexadecimal.

Full IPv6 address example:

```text
2001:0db8:0000:0000:0000:ff00:0042:8329
```

This address has eight hextets:

| Hextet Position | Value |
|---:|---|
| 1 | `2001` |
| 2 | `0db8` |
| 3 | `0000` |
| 4 | `0000` |
| 5 | `0000` |
| 6 | `ff00` |
| 7 | `0042` |
| 8 | `8329` |

Each hextet contains four hexadecimal characters. Because each hexadecimal character represents four bits, each hextet represents 16 bits.

```text
4 hex characters x 4 bits each = 16 bits
8 hextets x 16 bits each = 128 bits
```

IPv6 addresses are usually written with a prefix length, such as:

```text
2001:db8:10:20::25/64
```

The `/64` means the first 64 bits identify the network prefix, and the remaining 64 bits are used for the interface ID. In most normal LAN IPv6 designs, `/64` is the standard subnet size.

## 12.4 HEXADECIMAL REVIEW FOR IPv6

IPv6 uses hexadecimal because 128-bit addresses would be too long if written in binary or decimal. Hexadecimal is compact and maps neatly to binary.

Hexadecimal uses sixteen symbols:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

The letters represent values 10 through 15.

| Hex | Decimal | Binary |
|---|---:|---|
| A | 10 | 1010 |
| B | 11 | 1011 |
| C | 12 | 1100 |
| D | 13 | 1101 |
| E | 14 | 1110 |
| F | 15 | 1111 |

IPv6 is not case-sensitive. The letters may be uppercase or lowercase. These two addresses mean the same thing:

```text
2001:DB8::1
2001:db8::1
```

Most documentation and commands use lowercase for readability.

## 12.5 IPv6 ABBREVIATION RULES

IPv6 addresses can be shortened using two main abbreviation rules.

Rule 1: Leading zeros inside a hextet can be removed.

Example:

```text
Full:       2001:0db8:0000:0000:0000:ff00:0042:8329
Shortened:  2001:db8:0:0:0:ff00:42:8329
```

The hextet `0db8` becomes `db8`. The hextet `0042` becomes `42`. A hextet of `0000` becomes `0`.

Rule 2: One continuous sequence of all-zero hextets can be replaced with double colon `::`.

Example:

```text
Before double-colon: 2001:db8:0:0:0:ff00:42:8329
After double-colon:  2001:db8::ff00:42:8329
```

The double colon can be used only once in an address. If it were used more than once, the address would become ambiguous because the device would not know how many zero hextets belong in each location.

Example of valid abbreviation:

```text
2001:db8::1
```

Example of invalid abbreviation:

```text
2001::db8::1
```

That invalid address has two double-colon sections, so it is not clear how many zero hextets each `::` represents.

IPv6 Abbreviation Examples

| Full Address | Correct Short Form |
|---|---|
| `2001:0db8:0000:0000:0000:0000:0000:0001` | `2001:db8::1` |
| `fe80:0000:0000:0000:0202:b3ff:fe1e:8329` | `fe80::202:b3ff:fe1e:8329` |
| `2001:0db8:0001:0002:0000:0000:0000:0005` | `2001:db8:1:2::5` |
| `0000:0000:0000:0000:0000:0000:0000:0001` | `::1` |

## 12.6 EXPANDING AN IPv6 ADDRESS

Technicians must also be able to expand shortened IPv6 addresses.

Example:

```text
Short: 2001:db8::1
```

Step 1: Count the visible hextets.

Visible hextets:

```text
2001
db8
1
```

There are 3 visible hextets. IPv6 requires 8 hextets, so the double colon represents 5 hextets of zeros.

Expanded address:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

Another example:

```text
Short: fe80::202:b3ff:fe1e:8329
```

Visible hextets:

```text
fe80
202
b3ff
fe1e
8329
```

There are 5 visible hextets, so `::` represents 3 hextets of zeros.

Expanded:

```text
fe80:0000:0000:0000:0202:b3ff:fe1e:8329
```

Expansion matters in troubleshooting because logs, firewalls, packet captures, operating systems, and network devices may display IPv6 addresses in different shortened forms.

## 12.7 IPv6 PREFIX LENGTH AND BASIC SUBNETTING

IPv6 uses prefix length notation, similar to CIDR in IPv4. A prefix length tells how many bits identify the network.

Example:

```text
2001:db8:10:20::/64
```

This means the first 64 bits are the network prefix. In hextet form, the first four hextets are the network portion:

```text
Network prefix: 2001:db8:10:20
Interface ID:   remaining 64 bits
```

In most enterprise LANs, IPv6 subnets are `/64`. This is important because SLAAC expects a `/64` prefix. Unlike IPv4, engineers do not usually try to conserve every host address inside a LAN subnet. IPv6 has a very large address space, so the design focus is clean routing, consistent allocation, and operational simplicity.

Basic IPv6 Subnet Example

| Department | IPv6 Subnet |
|---|---|
| Staff | `2001:db8:100:10::/64` |
| Voice | `2001:db8:100:20::/64` |
| Servers | `2001:db8:100:30::/64` |
| Management | `2001:db8:100:40::/64` |
| Guest Wi-Fi | `2001:db8:100:50::/64` |

Each subnet uses a different fourth hextet. This makes the design readable.

IPv6 practical subnetting at this level means assigning clean `/64` subnets to VLANs, departments, cloud networks, or site segments. Advanced IPv6 route planning and provider allocation are beyond this basic lesson.

## 12.8 GLOBAL UNICAST ADDRESSES

A global unicast address is an IPv6 address that is globally routable on the IPv6 internet. It is similar in purpose to a public IPv4 address, but IPv6 global unicast addressing is much larger and is designed for end-to-end reachability.

Global unicast addresses commonly begin with `2000::/3`, which means many global addresses start with `2` or `3`.

Example:

```text
2001:db8:100:10::25
```

The range `2001:db8::/32` is reserved for documentation examples. It should be used in lessons, books, labs, and examples, but not as a real production internet-routed prefix.

In an enterprise, global unicast addresses may be assigned by an ISP or cloud provider. A company may receive a prefix and then divide it into `/64` subnets for internal VLANs, server networks, VPNs, and internet-facing services.

Global unicast addresses matter because IPv6 was designed to reduce the need for NAT. However, not using NAT does not mean no security. Firewalls, security groups, ACLs, endpoint protection, monitoring, and segmentation still matter.

## 12.9 LINK-LOCAL ADDRESSES

A link-local address is an IPv6 address used only on the local network link. Link-local addresses are not routed beyond the local segment.

IPv6 link-local addresses begin with:

```text
fe80::/10
```

Most commonly, students will see addresses that start with:

```text
fe80::
```

Every IPv6-enabled interface normally has a link-local address. This address is used for local communication, Neighbor Discovery, router discovery, and many routing protocol neighbor relationships.

Example:

```text
fe80::1
fe80::a1b2:ccff:fe33:4455
```

Link-local addresses matter because IPv6 devices can communicate locally even without a global unicast address. Routers also use link-local addresses as next-hop addresses in many IPv6 routing situations.

On Windows, a link-local address may appear with a zone index:

```text
fe80::a1b2:ccff:fe33:4455%12
```

The `%12` identifies the local interface. This is necessary because the same link-local range exists on every interface, so the operating system must know which interface to use.

## 12.10 MULTICAST ADDRESSES

IPv6 does not use broadcast. Instead, IPv6 uses multicast for many functions that IPv4 often handled with broadcast.

IPv6 multicast addresses begin with:

```text
ff00::/8
```

Multicast sends traffic to a group of interested devices rather than every device on the local network. This is more efficient than broadcast because only devices listening to that multicast group need to process the traffic.

Important IPv6 multicast examples:

| Multicast Address | Meaning |
|---|---|
| `ff02::1` | All nodes on the local link |
| `ff02::2` | All routers on the local link |
| `ff02::1:ffXX:XXXX` | Solicited-node multicast address |

Solicited-node multicast is used by Neighbor Discovery to find devices without broadcasting to every host. This replaces the role ARP played in IPv4, but it uses ICMPv6 and multicast instead of ARP broadcast.

For CCNA and Network+, remember: IPv6 has no broadcast. IPv6 uses multicast and Neighbor Discovery.

## 12.11 ANYCAST ADDRESSES

An anycast address is an IPv6 address assigned to multiple devices, where traffic is delivered to the nearest or best destination according to routing.

Anycast is useful for services that should be reachable from multiple locations using the same address. DNS is a common real-world example. Multiple DNS servers may share the same anycast address, and users are routed to the nearest available server based on network routing.

Anycast is not written with a special visible prefix like multicast. An anycast address looks like a unicast address, but it is assigned to multiple devices.

In enterprise and internet networks, anycast can improve performance, redundancy, and service availability. If one anycast location fails, routing can direct users to another location.

Students should understand the concept at this stage: unicast is one-to-one, multicast is one-to-many selected group, and anycast is one-to-nearest.

## 12.12 IPv6 ADDRESS TYPES SUMMARY

IPv6 address types are not optional trivia. They affect how devices communicate and troubleshoot.

| Address Type | Common Prefix | Purpose | Routed Beyond Local Link? |
|---|---|---|---|
| Global Unicast | `2000::/3` | Publicly routable IPv6 communication | Yes |
| Link-Local | `fe80::/10` | Local-link communication and discovery | No |
| Multicast | `ff00::/8` | Group communication | Depends on scope |
| Anycast | Looks like unicast | Nearest/best destination by routing | Yes |
| Loopback | `::1` | Local host testing | No |
| Unspecified | `::` | No address or source before assignment | No |

The loopback address `::1` is similar to IPv4 `127.0.0.1`. It tests the local IPv6 stack.

The unspecified address `::` is similar in concept to IPv4 `0.0.0.0` in certain contexts. It can mean no address assigned or an address not yet specified.

## 12.13 SLAAC

SLAAC means Stateless Address Autoconfiguration. It allows an IPv6 host to configure its own IPv6 address using information advertised by a router.

SLAAC exists because IPv6 was designed to support automatic address configuration without requiring a DHCP server for every basic address assignment. A router sends Router Advertisement messages that announce the IPv6 prefix and configuration flags. The host uses the prefix and creates an interface ID to form its IPv6 address.

The process works like this:

1. The host enables IPv6 on an interface.
2. The host creates a link-local address.
3. The host listens for Router Advertisement messages or sends a Router Solicitation.
4. The router advertises the network prefix, commonly `/64`.
5. The host combines the prefix with an interface ID.
6. The host performs Duplicate Address Detection to make sure the address is not already in use.
7. The host can then use the IPv6 address.

SLAAC is useful because it reduces manual configuration. However, SLAAC by itself may not provide all information that an enterprise wants, such as DNS server settings, depending on host support and network design.

## 12.14 DHCPv6

DHCPv6 is Dynamic Host Configuration Protocol for IPv6. It provides IPv6 configuration information to hosts.

DHCPv6 can be used in two major ways: stateless DHCPv6 and stateful DHCPv6.

Stateless DHCPv6 means the host uses SLAAC for its IPv6 address but contacts DHCPv6 for additional information such as DNS servers or domain search list.

Stateful DHCPv6 means the DHCPv6 server assigns the IPv6 address and may also provide other settings. This is closer to traditional IPv4 DHCP behavior, although IPv6 still uses Router Advertisements for default gateway information.

SLAAC vs DHCPv6

| Feature | SLAAC | Stateless DHCPv6 | Stateful DHCPv6 |
|---|---|---|---|
| Address Assignment | Host creates address from router prefix | Host uses SLAAC | DHCPv6 server assigns address |
| DNS Information | May come from RA depending on support | DHCPv6 provides DNS | DHCPv6 provides DNS |
| Address Tracking | Limited centrally | Limited centrally | Better central lease tracking |
| Default Gateway | Router Advertisement | Router Advertisement | Router Advertisement |
| Common Use | Simple auto-addressing | SLAAC plus options | More controlled environments |

For CCNA and Network+, remember that IPv6 hosts learn default gateway information from Router Advertisements, not from DHCPv6 in the same way IPv4 hosts learn a default gateway from DHCP.

## 12.15 NEIGHBOR DISCOVERY AND ICMPv6

IPv6 does not use ARP. It uses Neighbor Discovery Protocol, often called NDP. NDP uses ICMPv6 messages to discover neighbors, resolve Layer 2 addresses, find routers, and detect duplicate addresses.

Important NDP functions include:

- Router Solicitation.
- Router Advertisement.
- Neighbor Solicitation.
- Neighbor Advertisement.
- Duplicate Address Detection.

A Router Solicitation is sent by a host to request router information. A Router Advertisement is sent by a router to announce IPv6 prefix and gateway information. A Neighbor Solicitation asks for the Layer 2 address of another IPv6 device. A Neighbor Advertisement provides the answer. Duplicate Address Detection checks whether an address is already in use.

NDP is critical to IPv6. Blocking all ICMPv6 can break IPv6 communication. This is an important cybersecurity and firewall lesson: ICMPv6 is not optional noise. It is part of normal IPv6 operation.

IPv4 ARP vs IPv6 Neighbor Discovery

| Feature | IPv4 ARP | IPv6 NDP |
|---|---|---|
| Purpose | Resolve IP to MAC | Resolve IPv6 to MAC and support discovery |
| Protocol Used | ARP | ICMPv6 |
| Broadcast Used | Yes | No |
| Multicast Used | No | Yes |
| Router Discovery | Not ARP's role | Built into NDP |
| Duplicate Address Detection | Not ARP's main role | Built into NDP |

## 12.16 BASIC IPv6 CONFIGURATION

IPv6 can be configured manually, through SLAAC, through DHCPv6, or through a combination of methods.

Basic Cisco IOS interface configuration:

```text
configure terminal
ipv6 unicast-routing
interface gigabitEthernet 0/0
 ipv6 address 2001:db8:100:10::1/64
 ipv6 address fe80::1 link-local
 no shutdown
end
```

The command `ipv6 unicast-routing` enables IPv6 routing on a Cisco router or Layer 3 switch. Without it, the device may have IPv6 addresses on interfaces but may not route IPv6 traffic between interfaces.

The global unicast address `2001:db8:100:10::1/64` belongs to the subnet. The link-local address `fe80::1` is used for local-link functions and may be manually set for readability.

On hosts, IPv6 may be configured automatically. Windows and Linux commonly generate link-local addresses automatically when IPv6 is enabled.

## 12.17 BASIC IPv6 TROUBLESHOOTING

IPv6 troubleshooting starts with identifying which IPv6 addresses exist on the interface. A host may have a link-local address but no global unicast address. That means local IPv6 functions may work, but routed IPv6 communication may fail.

A practical troubleshooting sequence is:

1. Check whether IPv6 is enabled.
2. Identify link-local and global unicast addresses.
3. Confirm the prefix length.
4. Verify the default gateway or router advertisement.
5. Check neighbor entries.
6. Test loopback with `ping ::1`.
7. Test link-local communication when appropriate.
8. Test global IPv6 gateway reachability.
9. Test DNS name resolution.
10. Check firewall rules and ICMPv6 filtering.

Common IPv6 Troubleshooting Symptoms

| Symptom | Possible Cause | What to Check |
|---|---|---|
| Only `fe80::` address exists | No global prefix learned or assigned | Router Advertisements, DHCPv6, manual config |
| Cannot reach gateway | RA issue, wrong VLAN, firewall, link problem | Router, prefix, switch port, NDP |
| IPv6 works locally but not remotely | Missing route or routing disabled | `ipv6 unicast-routing`, routes |
| DNS name fails but IPv6 ping works | DNS issue | DNS settings, DHCPv6, RA DNS options |
| Neighbor entries missing | NDP or ICMPv6 blocked | Firewall, ACL, local link |
| Duplicate address warning | Address conflict | DAD, manual duplicate, interface ID |

## 12.18 WINDOWS, LINUX, AND CISCO IOS PRACTICAL COMMANDS

### Windows Commands

```text
ipconfig /all
ping ::1
ping <IPv6-address>
netsh interface ipv6 show neighbors
tracert -6 <destination>
```

`ipconfig /all` shows IPv6 addresses, link-local addresses, DNS servers, and interface details. `ping ::1` tests the local IPv6 stack. `tracert -6` forces IPv6 traceroute behavior on Windows.

### Linux Commands

```text
ip -6 addr
ip -6 route
ip -6 neigh
ping -6 ::1
ping -6 <IPv6-address>
traceroute6 <destination>
```

`ip -6 addr` shows IPv6 interface addresses. `ip -6 route` shows IPv6 routes. `ip -6 neigh` shows IPv6 neighbor entries learned through NDP.

### Cisco IOS Commands

```text
show ipv6 interface brief
show ipv6 interface gigabitEthernet 0/0
show ipv6 neighbors
show ipv6 route
ping ipv6 <destination>
traceroute ipv6 <destination>
show running-config interface gigabitEthernet 0/0
```

`show ipv6 interface brief` is the fastest Cisco IOS command for checking IPv6 interface addresses and status. `show ipv6 neighbors` is similar in troubleshooting value to checking ARP in IPv4, but it uses IPv6 Neighbor Discovery.

## 12.20 CYBERSECURITY RELEVANCE

IPv6 security matters because unmanaged IPv6 can create blind spots. A company may believe it only uses IPv4, while endpoints still generate IPv6 link-local traffic. Attackers may exploit weak monitoring, rogue router advertisements, or firewall rules that ignore IPv6.

Security teams must understand that IPv6 has no ARP but uses NDP. Attacks against neighbor discovery and rogue router advertisements can affect local traffic. Enterprises may use RA Guard, DHCPv6 Guard, IPv6 ACLs, firewall policy, endpoint protection, and monitoring to reduce risk.

Blocking ICMPv6 completely is not a safe security strategy because IPv6 depends on ICMPv6 for essential functions. Security controls should be specific and informed rather than blindly disabling required protocol behavior.

Global unicast IPv6 addressing can make devices reachable without NAT, depending on firewall policy. This does not mean every device is exposed automatically, but it does mean firewall and host security policy must be correct.

## 12.21 CLOUD NETWORKING RELEVANCE

Cloud providers increasingly support IPv6 for virtual networks, load balancers, public services, and container platforms. A cloud subnet may have both IPv4 and IPv6 prefixes in a dual-stack design.

Example cloud design:

| Cloud Segment | IPv6 Prefix |
|---|---|
| Public web subnet | `2001:db8:500:10::/64` |
| Private app subnet | `2001:db8:500:20::/64` |
| Database subnet | `2001:db8:500:30::/64` |
| Management subnet | `2001:db8:500:40::/64` |

In cloud networking, IPv6 security groups, route tables, internet gateways, firewall rules, DNS records, and monitoring must be configured intentionally. An engineer should not assume that IPv4 security automatically covers IPv6.

IPv6 also reduces some NAT pressure, but it does not remove the need for segmentation, least privilege, logging, and access control.

## 13. KEY TERMS / GLOSSARY

| Term | Meaning |
|---|---|
| IPv6 | Internet Protocol version 6, a 128-bit Layer 3 addressing system. |
| Hextet | A 16-bit section of an IPv6 address written with four hexadecimal characters. |
| Prefix Length | Slash notation showing how many bits identify the network prefix. |
| Interface ID | Host/interface portion of an IPv6 address, commonly the last 64 bits in a `/64`. |
| Global Unicast Address | Globally routable IPv6 address. |
| Link-Local Address | IPv6 address used only on the local link, commonly beginning with `fe80::`. |
| Multicast Address | IPv6 address used to reach a group of receivers. |
| Anycast Address | Address assigned to multiple devices where routing delivers to the nearest/best one. |
| Loopback Address | `::1`, used to test the local IPv6 stack. |
| Unspecified Address | `::`, used when no IPv6 address is specified. |
| SLAAC | Stateless Address Autoconfiguration, where a host forms its own IPv6 address using router advertisements. |
| DHCPv6 | DHCP for IPv6, used to provide IPv6 addresses or configuration options. |
| Stateful DHCPv6 | DHCPv6 mode where the server assigns IPv6 addresses. |
| Stateless DHCPv6 | DHCPv6 mode where SLAAC provides the address and DHCPv6 provides extra options. |
| Neighbor Discovery | IPv6 discovery system using ICMPv6 instead of ARP. |
| Router Advertisement | ICMPv6 message used by routers to advertise prefix and gateway information. |
| Router Solicitation | ICMPv6 message used by hosts to request router advertisements. |
| Neighbor Solicitation | ICMPv6 message used to discover a neighbor's Layer 2 address. |
| Neighbor Advertisement | ICMPv6 message used to answer neighbor solicitations. |
| Duplicate Address Detection | IPv6 process that checks whether an address is already in use. |

## 14. COMPARISON TABLES

### 14.1 IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address Length | 32 bits | 128 bits |
| Common Format | Dotted decimal | Hexadecimal hextets |
| Example | `192.168.10.25` | `2001:db8::25` |
| Broadcast | Yes | No |
| Local Discovery | ARP | Neighbor Discovery |
| Auto-Configuration | DHCP/manual/APIPA | SLAAC, DHCPv6, manual |
| Loopback | `127.0.0.1` | `::1` |

### 14.2 IPv6 Address Types

| Address Type | Prefix/Example | Main Purpose |
|---|---|---|
| Global Unicast | `2000::/3` | Routable IPv6 communication |
| Link-Local | `fe80::/10` | Local-link communication |
| Multicast | `ff00::/8` | Group communication |
| Anycast | Looks like unicast | Nearest/best destination |
| Loopback | `::1` | Local host testing |
| Unspecified | `::` | No address specified |

### 14.3 SLAAC vs DHCPv6

| Feature | SLAAC | DHCPv6 |
|---|---|---|
| Address Creation | Host creates address from advertised prefix | Server may assign address in stateful mode |
| Default Gateway | Learned from Router Advertisement | Learned from Router Advertisement |
| DNS Options | May come from RA depending on support | Commonly provided by DHCPv6 |
| Central Tracking | Limited | Stronger with stateful DHCPv6 |
| Common Role | Automatic addressing | Address/options management |

### 14.4 IPv4 ARP vs IPv6 NDP

| Feature | ARP | NDP |
|---|---|---|
| Used By | IPv4 | IPv6 |
| Protocol | ARP | ICMPv6 |
| Broadcast | Yes | No |
| Multicast | No | Yes |
| Finds MAC Address | Yes | Yes |
| Router Discovery | No | Yes |

## 15. REAL-WORLD EXAMPLE / ANALOGY

IPv6 addressing is like expanding from a small local street-numbering system to a global addressing system with enough space to organize every building, department, room, and device cleanly. IPv4 often required address sharing through NAT because the address space was limited. IPv6 provides enough space for cleaner addressing, but the organization still needs good planning.

The important lesson is not that IPv6 addresses are long. The important lesson is that IPv6 uses structure: prefixes, hextets, address types, link-local communication, multicast discovery, and automatic configuration.

## 16. QUICK-RECAP CHEAT SHEET

- IPv6 is a 128-bit Layer 3 addressing system.
- IPv6 uses hexadecimal.
- An IPv6 address has eight hextets.
- Each hextet is 16 bits.
- Leading zeros inside a hextet can be removed.
- One continuous run of zero hextets can be replaced with `::`.
- `::` can be used only once in an IPv6 address.
- `/64` is the standard IPv6 LAN subnet size.
- Global unicast addresses are globally routable and commonly fall within `2000::/3`.
- `2001:db8::/32` is reserved for documentation examples.
- Link-local addresses begin with `fe80::/10`.
- IPv6 has no broadcast.
- IPv6 multicast begins with `ff00::/8`.
- `ff02::1` means all nodes on the local link.
- `ff02::2` means all routers on the local link.
- Anycast sends traffic to the nearest or best destination using routing.
- SLAAC lets hosts create IPv6 addresses from router advertisements.
- DHCPv6 provides IPv6 addressing or additional options depending on mode.
- IPv6 uses Neighbor Discovery instead of ARP.
- Neighbor Discovery uses ICMPv6.
- `::1` is the IPv6 loopback address.
- `::` is the unspecified address.

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
