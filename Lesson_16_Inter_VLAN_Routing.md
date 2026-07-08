# LESSON 16: INTER-VLAN ROUTING

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 16.1 What Is Inter-VLAN Routing?

Inter-VLAN routing is the process of allowing devices in different VLANs to communicate through a Layer 3 device. VLANs separate traffic at Layer 2. Routing connects different Layer 3 networks. Since each VLAN normally maps to a different IP subnet, devices in different VLANs need routing to communicate.

In Lessons 13 and 14, VLANs were explained as separate broadcast domains. A staff PC in VLAN 10 and a server in VLAN 30 are separated at Layer 2. Their Ethernet broadcasts do not cross VLAN boundaries. This is good for segmentation, but it also means communication between the VLANs requires a router, Layer 3 switch, or firewall.

Inter-VLAN routing exists because enterprises need both separation and controlled communication. Guest Wi-Fi should be separated from staff systems, but staff PCs may need to reach servers. IP phones may need to reach call-control systems. CCTV cameras may need to reach an NVR. Management laptops may need to reach switch management IP addresses. VLANs create boundaries; routing and policy decide which boundaries can be crossed.

There are two common ways to perform inter-VLAN routing:

- Router-on-a-stick.
- Layer 3 switching using Switch Virtual Interfaces.

For CCNA and CompTIA Network+, students must understand why inter-VLAN routing is needed, how router-on-a-stick works, how SVIs work, how default gateways relate to VLANs, and how to troubleshoot inter-VLAN connectivity.

### 16.2 Why Inter-VLAN Routing Matters

Inter-VLAN routing matters because most real enterprise networks use multiple VLANs. A network with VLANs but no routing between required VLANs is segmented, but isolated. Users may be able to communicate with devices inside their own VLAN, but not with servers, printers, management systems, or internet gateways in other VLANs.

Inter-VLAN routing also matters for security. The goal is not to allow every VLAN to reach every other VLAN freely. The goal is to route where business communication is required and apply policy where traffic should be restricted. In some networks, a Layer 3 switch routes between trusted internal VLANs, while a firewall controls traffic between user VLANs, server VLANs, guest VLANs, and the internet.

In troubleshooting, inter-VLAN routing is a common failure point. A user may have the correct IP address and VLAN assignment but still fail to reach another subnet because the default gateway is wrong, the SVI is down, a router subinterface is missing, a trunk is not carrying the VLAN, routing is disabled, or an access control rule blocks the traffic.

## 16.3 Why Devices in Different VLANs Need Routing

A VLAN is a Layer 2 broadcast domain. An IP subnet is a Layer 3 network. In good design, each VLAN usually maps to one IP subnet.

Example:

| VLAN | Name | Subnet | Gateway |
|---:|---|---|---|
| 10 | STAFF | 192.168.10.0/24 | 192.168.10.1 |
| 20 | VOICE | 192.168.20.0/24 | 192.168.20.1 |
| 30 | SERVERS | 192.168.30.0/24 | 192.168.30.1 |
| 50 | GUEST | 192.168.50.0/24 | 192.168.50.1 |

If a staff PC `192.168.10.25/24` wants to reach a server `192.168.30.10/24`, it first checks its subnet mask. The server is not in the local `192.168.10.0/24` network, so the PC sends the packet to its default gateway, `192.168.10.1`.

The default gateway is the Layer 3 interface for that VLAN. It may be a router subinterface, a firewall interface, or a Layer 3 switch SVI. That Layer 3 device then routes the packet toward VLAN 30.

Important rule:

```text
Devices in different VLANs need Layer 3 routing to communicate.
```

VLANs do not route by themselves. Switches operating only at Layer 2 do not move traffic between VLANs.

## 16.4 Default Gateway Per VLAN

Each VLAN/subnet needs a default gateway if devices in that VLAN must reach other networks. The gateway IP address must be in the same subnet as the hosts.

Example:

```text
VLAN 10 subnet: 192.168.10.0/24
Gateway:        192.168.10.1
Host:           192.168.10.25
```

The host can send remote traffic to `192.168.10.1` because the gateway is local to the host's subnet.

Wrong gateway example:

```text
Host:           192.168.10.25/24
Wrong Gateway:  192.168.20.1
```

This is incorrect because `192.168.20.1` is not local to `192.168.10.25/24`. The host may not be able to reach its gateway at Layer 2.

Default Gateway Design Table

| VLAN | Subnet | Correct Gateway | Incorrect Gateway Example |
|---:|---|---|---|
| 10 | 192.168.10.0/24 | 192.168.10.1 | 192.168.20.1 |
| 20 | 192.168.20.0/24 | 192.168.20.1 | 192.168.10.1 |
| 30 | 192.168.30.0/24 | 192.168.30.1 | 192.168.50.1 |

The gateway is usually configured manually on servers and network devices, and delivered through DHCP to client devices.

## 16.5 Router-on-a-Stick

Router-on-a-stick is an inter-VLAN routing design where one physical router interface connects to a switch trunk and uses subinterfaces to route between multiple VLANs.

The router has one physical link to the switch. That link is configured as an 802.1Q trunk. On the router, each VLAN uses a logical subinterface. Each subinterface has an IP address that acts as the default gateway for that VLAN.

Example topology:

```text
PC VLAN 10 ---- Access Switch ---- trunk ---- Router G0/0
PC VLAN 20 ---- Access Switch ---- trunk ---- Router G0/0
```

Router subinterfaces:

```text
G0/0.10 -> VLAN 10 gateway -> 192.168.10.1/24
G0/0.20 -> VLAN 20 gateway -> 192.168.20.1/24
G0/0.30 -> VLAN 30 gateway -> 192.168.30.1/24
```

Router-on-a-stick is common in labs, small networks, branch offices, and CCNA training because it clearly shows the relationship between trunks, VLAN tags, and Layer 3 gateways.

### Router-on-a-Stick Configuration

Switch trunk toward router:

```text
interface gigabitEthernet 0/1
 description Trunk to Router
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

Router configuration:

```text
interface gigabitEthernet 0/0
 no shutdown

interface gigabitEthernet 0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface gigabitEthernet 0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0

interface gigabitEthernet 0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
```

The `encapsulation dot1Q <vlan-id>` command tells the router which VLAN tag belongs to that subinterface. The IP address on the subinterface becomes the gateway for that VLAN.

Router-on-a-Stick Summary

| Component | Purpose |
|---|---|
| Switch trunk | Carries multiple VLANs to router |
| Router physical interface | Parent interface for subinterfaces |
| Router subinterface | Gateway for one VLAN |
| `encapsulation dot1Q` | Maps subinterface to VLAN tag |
| Host default gateway | Points to router subinterface IP |

## 16.6 Router-on-a-Stick Packet Journey

Assume PC1 in VLAN 10 wants to reach Server1 in VLAN 30.

PC1:

```text
IP Address: 192.168.10.25/24
Gateway:    192.168.10.1
```

Server1:

```text
IP Address: 192.168.30.10/24
Gateway:    192.168.30.1
```

Step 1: PC1 sees that Server1 is remote because `192.168.30.10` is not in `192.168.10.0/24`.

Step 2: PC1 sends the packet to its default gateway `192.168.10.1`.

Step 3: The switch receives the frame on an access port in VLAN 10.

Step 4: The switch forwards the frame across the trunk to the router, tagged for VLAN 10.

Step 5: The router receives the frame on subinterface `G0/0.10`.

Step 6: The router removes the Layer 2 header, examines the destination IP address, and routes the packet toward VLAN 30.

Step 7: The router sends the packet out subinterface `G0/0.30`, tagged for VLAN 30.

Step 8: The switch receives the tagged frame, places it in VLAN 30, and forwards it to Server1.

This process shows why router-on-a-stick depends on correct VLANs, trunking, dot1Q encapsulation, IP addressing, and default gateways.

## 16.7 Router-on-a-Stick Advantages and Limitations

Router-on-a-stick is simple and useful, especially in small environments and labs. It requires only one router interface and one switch trunk to route multiple VLANs.

However, it can become a bottleneck. All inter-VLAN traffic must cross the same physical router link. If many VLANs send heavy traffic through that one link, performance may suffer. It also depends on the router's interface speed and processing capacity.

Router-on-a-Stick Comparison

| Advantage | Limitation |
|---|---|
| Simple to understand | One trunk can become a bottleneck |
| Useful in small networks | Router interface failure affects all VLANs |
| Good for labs and CCNA practice | Less scalable than Layer 3 switching |
| Requires fewer physical router ports | All inter-VLAN traffic hairpins through router |

In larger enterprise LANs, Layer 3 switching is often preferred for internal inter-VLAN routing.

## 16.8 Switch Virtual Interfaces

A Switch Virtual Interface, or SVI, is a logical Layer 3 interface on a Layer 3 switch. An SVI provides a gateway IP address for a VLAN directly on the switch.

Instead of sending inter-VLAN traffic to an external router, the Layer 3 switch routes between VLANs internally.

Example:

```text
interface vlan 10
 ip address 192.168.10.1 255.255.255.0

interface vlan 20
 ip address 192.168.20.1 255.255.255.0

interface vlan 30
 ip address 192.168.30.1 255.255.255.0
```

Each SVI acts as the default gateway for its VLAN.

SVIs are common in enterprise networks because they are fast and scalable. A Layer 3 switch can route traffic between VLANs at high speed, often using hardware forwarding.

### Layer 3 Switching Requirements

For SVI-based inter-VLAN routing to work:

1. The VLAN must exist.
2. The SVI must have the correct IP address and subnet mask.
3. The SVI must be up/up.
4. At least one active port in the VLAN must usually be up, or the VLAN must be active through a trunk.
5. IP routing must be enabled on the Layer 3 switch.
6. Hosts must use the SVI IP address as their default gateway.

Cisco IOS command to enable routing on a Layer 3 switch:

```text
ip routing
```

SVI configuration example:

```text
configure terminal
ip routing
vlan 10
 name STAFF
vlan 20
 name SERVERS

interface vlan 10
 description Gateway for STAFF VLAN
 ip address 192.168.10.1 255.255.255.0
 no shutdown

interface vlan 20
 description Gateway for SERVERS VLAN
 ip address 192.168.20.1 255.255.255.0
 no shutdown
end
```

## 16.9 Router-on-a-Stick vs Layer 3 Switching

Router-on-a-stick and Layer 3 switching both provide inter-VLAN routing, but they are used in different situations.

| Feature | Router-on-a-Stick | Layer 3 Switching with SVIs |
|---|---|---|
| Routing Device | External router | Layer 3 switch |
| VLAN Gateway | Router subinterface | SVI |
| Link to Switch | 802.1Q trunk to router | Internal switch fabric |
| Performance | Limited by router link/interface | Usually faster for LAN routing |
| Common Use | Labs, small branches | Enterprise distribution/collapsed core |
| Scalability | Lower | Higher |
| Configuration Focus | Subinterfaces and dot1Q | SVIs and `ip routing` |

For CCNA, students should be comfortable with both designs. In real enterprise networks, Layer 3 switching is very common for internal VLAN routing, while firewalls may route or filter traffic between security zones.

## 16.10 Inter-VLAN Routing and Firewalls

Not all inter-VLAN routing should happen freely on a Layer 3 switch. Some VLANs require security policy between them. In those cases, a firewall may route between VLANs or sit between major security zones.

Example:

| Source VLAN | Destination VLAN | Policy |
|---|---|---|
| Staff | Servers | Allow required business ports |
| Guest | Internal LAN | Deny |
| CCTV | NVR | Allow only camera/NVR traffic |
| Management | Network Devices | Allow admin protocols |
| Voice | Call Manager | Allow voice control/media |

A Layer 3 switch may route trusted internal VLANs, while a firewall controls guest, server, DMZ, internet, and sensitive traffic. The design depends on business risk and performance needs.

Security principle:

```text
Routing enables communication. Policy controls communication.
```

## 16.11 IPv6 Inter-VLAN Routing

IPv6 also needs inter-VLAN routing. Each VLAN may have an IPv6 `/64` prefix and a gateway address on a router subinterface or SVI.

Example SVI:

```text
interface vlan 10
 ipv6 address 2001:db8:100:10::1/64
```

Hosts in VLAN 10 may use SLAAC, DHCPv6, or manual configuration. The router or Layer 3 switch sends Router Advertisements, and hosts learn default gateway information through IPv6 neighbor discovery behavior.

IPv6 routing must be enabled on Cisco devices:

```text
ipv6 unicast-routing
```

At this course level, the core idea is simple: VLAN segmentation applies to IPv6 too, and a Layer 3 device is required to route between IPv6 prefixes.

## 16.12 Inter-VLAN Routing Troubleshooting

Inter-VLAN troubleshooting should be systematic. Because inter-VLAN routing depends on both Layer 2 and Layer 3, the technician must check VLANs, trunks, IP addressing, gateways, and routing.

Troubleshooting sequence:

1. Confirm the source host IP address, subnet mask, and default gateway.
2. Confirm the destination host IP address and subnet.
3. Verify the source switch port VLAN.
4. Verify the destination switch port VLAN.
5. Confirm the VLANs exist on the switches.
6. If trunks are involved, confirm the VLANs are allowed on trunks.
7. Confirm the default gateway interface exists.
8. Confirm the router subinterface or SVI is up.
9. Confirm IP routing is enabled where needed.
10. Check ACLs or firewall policy.
11. Test gateway reachability from each VLAN.
12. Test end-to-end connectivity.

Common Inter-VLAN Routing Problems

| Symptom | Likely Cause | What to Check |
|---|---|---|
| Host cannot ping gateway | Wrong VLAN, wrong gateway, SVI down | VLAN, gateway IP, SVI status |
| Same-VLAN works, different-VLAN fails | Missing routing or gateway issue | Router/SVI, `ip routing` |
| One VLAN cannot cross trunk | VLAN missing from allowed list | `show interfaces trunk` |
| Router-on-a-stick VLAN fails | Missing dot1Q subinterface | Router subinterface config |
| SVI is down/down | VLAN inactive or no active ports | VLAN existence, active port/trunk |
| Guest reaches internal network | Policy missing or wrong | Firewall/ACL rules |
| IPv6 works locally but not across VLANs | IPv6 routing or RA issue | `ipv6 unicast-routing`, SVI IPv6 |

## 16.13 Verification Commands

### Cisco IOS Router-on-a-Stick Commands

```text
show ip interface brief
show running-config interface gigabitEthernet 0/0.10
show interfaces trunk
show ip route connected
show arp
ping <destination>
traceroute <destination>
```

On the switch, use:

```text
show vlan brief
show interfaces trunk
show interfaces switchport
show mac address-table vlan 10
```

### Cisco IOS Layer 3 Switch Commands

```text
show ip interface brief
show running-config interface vlan 10
show vlan brief
show ip route connected
show interfaces trunk
show mac address-table vlan 10
ping <destination>
traceroute <destination>
```

For IPv6:

```text
show ipv6 interface brief
show ipv6 route
show ipv6 neighbors
ping ipv6 <destination>
```

## 16.14 Windows, Linux, and Cisco IOS Practical Checks

### Windows Checks

```text
ipconfig /all
ping <default-gateway>
ping <remote-vlan-host>
arp -a
tracert <remote-vlan-host>
```

Windows helps confirm whether the device has the correct IP address, subnet mask, gateway, and DNS settings. If the host cannot ping its own default gateway, fix local VLAN/gateway issues before testing remote VLANs.

### Linux Checks

```text
ip addr
ip route
ip neigh
ping <default-gateway>
ping <remote-vlan-host>
traceroute <remote-vlan-host>
```

Linux shows the prefix length and default route clearly. If `ip route` has no default route, the host may communicate locally but fail to reach other VLANs.

### Cisco IOS Checks

```text
show vlan brief
show interfaces trunk
show ip interface brief
show ip route
show arp
show running-config interface <interface-id>
```

Cisco IOS verifies the switch and routing side of the path. Use these commands to prove whether the issue is VLAN membership, trunking, gateway configuration, routing, or policy.

## 16.15 Cisco Packet Tracer Practice

### Practice Lab: Router-on-a-Stick

Build a topology:

- One router.
- One switch.
- Two PCs in VLAN 10.
- Two PCs in VLAN 20.
- Router connected to switch using one trunk.

Addressing:

| VLAN | Subnet | Gateway |
|---:|---|---|
| 10 | 192.168.10.0/24 | 192.168.10.1 |
| 20 | 192.168.20.0/24 | 192.168.20.1 |

Tasks:

1. Create VLAN 10 and VLAN 20 on the switch.
2. Assign PC ports to the correct VLANs.
3. Configure the switch port to the router as a trunk.
4. Configure router subinterfaces with `encapsulation dot1Q`.
5. Configure PC IP addresses and default gateways.
6. Ping within the same VLAN.
7. Ping between VLANs.
8. Remove one `encapsulation dot1Q` command or block one VLAN on the trunk.
9. Observe the failure.
10. Restore the configuration and verify connectivity.

Expected learning outcome:

Students should understand how router subinterfaces act as VLAN gateways and why trunks must carry the required VLANs.

### Practice Lab: Layer 3 Switch SVIs

Build a topology:

- One Layer 3 switch.
- Two VLANs.
- Two PCs in each VLAN.

Addressing:

| VLAN | Subnet | SVI Gateway |
|---:|---|---|
| 10 | 10.10.10.0/24 | 10.10.10.1 |
| 20 | 10.10.20.0/24 | 10.10.20.1 |

Configuration concept:

```text
ip routing
vlan 10
vlan 20
interface vlan 10
 ip address 10.10.10.1 255.255.255.0
 no shutdown
interface vlan 20
 ip address 10.10.20.1 255.255.255.0
 no shutdown
```

Tasks:

1. Create VLANs.
2. Assign access ports.
3. Configure SVIs.
4. Enable `ip routing`.
5. Configure PCs with correct gateways.
6. Test inter-VLAN connectivity.
7. Disable `ip routing`.
8. Observe what breaks.

Expected learning outcome:

Students should understand that SVIs provide gateways on a Layer 3 switch and that `ip routing` is required for routing between VLANs.

## 16.16 Cybersecurity Relevance

Inter-VLAN routing is a security control point. Once routing exists, VLAN boundaries can be crossed. This is useful for business communication, but dangerous if unrestricted.

A poor design may allow guest users to reach internal servers, CCTV cameras, printers, or management interfaces. A better design routes traffic through a firewall or applies ACLs so only approved communication is allowed.

Examples:

| Traffic | Recommended Policy |
|---|---|
| Guest to internal LAN | Deny |
| Staff to file server | Allow required ports |
| CCTV to NVR | Allow only camera/NVR traffic |
| User VLAN to switch management | Deny |
| Admin VLAN to network devices | Allow SSH/HTTPS/SNMP as required |

Inter-VLAN routing should be paired with least privilege. Do not route everything everywhere simply because it is technically possible.

## 16.17 Cloud Networking Relevance

Cloud networks use the same principle: subnets are separated, and routing connects them. In a public cloud, a route table may decide whether a subnet can reach another subnet, an internet gateway, a NAT gateway, a firewall, or a VPN.

In private cloud and virtualization environments, VLANs may still exist underneath virtual networks. A hypervisor may trunk multiple VLANs to virtual switches. A virtual firewall may route between VLAN-backed port groups.

Understanding inter-VLAN routing helps students understand cloud route tables, subnet gateways, network security groups, firewall appliances, and hybrid VPN routing.

## 16.18 Interview and Exam Relevance

In IT support interviews, inter-VLAN routing questions often sound like troubleshooting scenarios. A user can ping someone in the same department but cannot reach the server VLAN. The technician should check the gateway, VLAN assignment, trunk, SVI or router subinterface, and policy.

In network engineering interviews, questions may include router-on-a-stick, dot1Q subinterfaces, SVIs, `ip routing`, default gateways, trunk allowed VLANs, and inter-VLAN troubleshooting.

For CCNA, students should know both router-on-a-stick and SVI-based inter-VLAN routing. For Network+, students should understand that VLANs segment traffic and routing is required for communication between VLANs.

## 17. KEY TERMS / GLOSSARY

| Term | Meaning |
|---|---|
| Inter-VLAN Routing | Routing traffic between different VLANs/subnets. |
| Router-on-a-Stick | Inter-VLAN routing design using router subinterfaces over one trunk. |
| Subinterface | Logical interface created under a physical router interface. |
| `encapsulation dot1Q` | Cisco command that maps a router subinterface to a VLAN tag. |
| SVI | Switch Virtual Interface; logical Layer 3 VLAN interface on a switch. |
| Layer 3 Switch | Switch that can route between IP networks as well as switch frames. |
| Default Gateway | Local Layer 3 address hosts use to reach remote networks. |
| `ip routing` | Cisco command enabling IPv4 routing on a Layer 3 switch. |
| Connected Route | Route automatically created when an interface with an IP address is up. |
| Gateway VLAN | VLAN whose SVI or router subinterface acts as host gateway. |
| Policy Control | Rules that permit or deny traffic between VLANs or networks. |

## 18. COMPARISON TABLES

### 18.1 Router-on-a-Stick vs Layer 3 Switching

| Feature | Router-on-a-Stick | Layer 3 Switching |
|---|---|---|
| Gateway Type | Router subinterface | SVI |
| Link Type | Trunk to router | Internal switch routing |
| Key Command | `encapsulation dot1Q` | `interface vlan`, `ip routing` |
| Performance | Lower for large LANs | Higher for LAN routing |
| Common Use | Labs, small sites | Enterprise campus/distribution |

### 18.2 Layer 2 VLAN vs Layer 3 Gateway

| Feature | VLAN | Gateway/SVI/Subinterface |
|---|---|---|
| OSI Layer | Layer 2 | Layer 3 |
| Purpose | Separates broadcast domain | Routes to other networks |
| Example | VLAN 10 | 192.168.10.1 |
| Device Function | Switching | Routing |
| Failure Symptom | Wrong subnet/DHCP | Cannot reach remote VLANs |

### 18.3 Common Inter-VLAN Faults

| Fault | Result |
|---|---|
| Wrong access VLAN | Host may get wrong IP subnet |
| Missing trunk VLAN | VLAN fails across switches |
| Missing router subinterface | Router-on-a-stick VLAN cannot route |
| SVI down | Hosts cannot reach gateway |
| `ip routing` disabled | Layer 3 switch does not route |
| ACL/firewall block | Routing exists but traffic denied |

## 19. REAL-WORLD EXAMPLE / ANALOGY

Think of VLANs as separate departments in a building. Each department has its own internal room space. Inter-VLAN routing is the controlled hallway or security desk that allows approved movement between departments.

Without the hallway, departments are isolated. With an uncontrolled hallway, everyone can go everywhere. A good network uses routing for required movement and policy to control who is allowed through.

## 20. QUICK-RECAP CHEAT SHEET

- VLANs separate Layer 2 broadcast domains.
- Devices in different VLANs usually belong to different IP subnets.
- Different VLANs need Layer 3 routing to communicate.
- Each VLAN/subnet needs a default gateway.
- Router-on-a-stick uses one router physical interface with subinterfaces.
- Router-on-a-stick requires a trunk between switch and router.
- `encapsulation dot1Q <vlan-id>` maps a subinterface to a VLAN.
- An SVI is a Layer 3 interface for a VLAN on a Layer 3 switch.
- SVIs commonly act as default gateways.
- Layer 3 switches need `ip routing` for IPv4 routing.
- IPv6 inter-VLAN routing needs `ipv6 unicast-routing`.
- Same-VLAN communication can work even when inter-VLAN routing is broken.
- Missing allowed VLANs on trunks can break inter-VLAN paths.
- Wrong default gateway breaks remote network access.
- Firewalls and ACLs should control inter-VLAN traffic where security matters.

## 21. REVIEW QUESTIONS

1. What is inter-VLAN routing?
2. Why do devices in different VLANs need routing?
3. What is the default gateway used for?
4. Why must a host's gateway be in the same subnet as the host?
5. What is router-on-a-stick?
6. What is a router subinterface?
7. What does `encapsulation dot1Q` do?
8. What switch port type is needed between a switch and router in router-on-a-stick?
9. What is an SVI?
10. What command enables IPv4 routing on a Cisco Layer 3 switch?
11. What is a Layer 3 switch?
12. Name two requirements for an SVI to route successfully.
13. Why is router-on-a-stick less scalable than Layer 3 switching?
14. What should you check if same-VLAN traffic works but different-VLAN traffic fails?
15. What command shows router or Layer 3 switch interface IP status?
16. What command shows connected routes?
17. Why might a firewall be used for inter-VLAN routing?
18. What can happen if guest VLAN traffic is routed freely to internal VLANs?
19. Does IPv6 also require routing between VLAN prefixes?
20. What command enables IPv6 routing on Cisco devices?

## 22. SUGGESTED ANSWER GUIDE

1. Inter-VLAN routing is routing traffic between different VLANs and subnets.
2. VLANs are separate Layer 2 broadcast domains and usually separate IP subnets.
3. The default gateway sends traffic from a host to remote networks.
4. The host must reach the gateway locally before the gateway can route traffic.
5. Router-on-a-stick uses one router physical interface with subinterfaces over a trunk.
6. A subinterface is a logical interface under a physical router interface.
7. It maps a router subinterface to an 802.1Q VLAN tag.
8. A trunk port.
9. An SVI is a Switch Virtual Interface, a Layer 3 interface for a VLAN.
10. `ip routing`.
11. A Layer 3 switch can switch frames and route IP packets.
12. The VLAN must exist, the SVI must have the right IP, it must be up/up, active ports/trunks must exist, and `ip routing` must be enabled.
13. All inter-VLAN traffic must cross one router link, which can become a bottleneck.
14. Check gateway, SVI/router subinterface, trunk allowed VLANs, VLAN assignment, routing, and policy.
15. `show ip interface brief`.
16. `show ip route connected`.
17. To enforce security policy between VLANs.
18. Guests may access internal business systems, creating a major security risk.
19. Yes.
20. `ipv6 unicast-routing`.
