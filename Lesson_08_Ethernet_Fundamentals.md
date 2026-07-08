# LESSON 8: ETHERNET FUNDAMENTALS

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 8.1 What Is Ethernet?

Ethernet is the most widely used wired LAN technology in modern networks. It defines how devices format, address, transmit, and receive frames on a local network. Ethernet operates mainly at Layer 2, the Data Link layer, and depends on Layer 1 physical media such as copper cables, fiber optic cables, transceivers, and switch ports.

In Lesson 7, cabling and physical media were explained as the pathways that carry signals. Ethernet builds on those pathways by defining the frame format, MAC addressing, local delivery behavior, speed negotiation, duplex behavior, and switching foundation used in LANs.

Ethernet exists because devices on a local network need a standard way to communicate. A laptop, printer, server, IP phone, switch, and router interface must agree on how frames are structured and how local addresses are used. Ethernet provides that standard.

In real enterprise networks, Ethernet is used to connect end devices to access switches, switches to distribution switches, servers to data center switches, access points to wired networks, routers to LAN segments, and firewalls to internal and external networks. Even when users connect wirelessly, wireless access points often connect back to the wired network using Ethernet.

For CCNA and CompTIA Network+, students must understand Ethernet frame structure, MAC addressing, collision domains, broadcast domains, duplex, speed, and auto-negotiation. These concepts prepare students for enterprise switching, VLANs, trunking, Spanning Tree Protocol, and troubleshooting.

### 8.2 Why Ethernet Matters

Ethernet matters because most LAN communication begins with an Ethernet frame. When a device sends traffic on a wired LAN, the data is encapsulated into an Ethernet frame. That frame contains local delivery information, including source and destination MAC addresses. Switches use this information to move traffic inside the LAN.

If Ethernet behavior fails, the network may appear broken even when IP addressing is correct. A PC may have a valid IP address but fail to communicate because the switch port is in the wrong VLAN. A server may have the correct gateway but experience poor performance because of duplex mismatch or physical errors. A broadcast storm may overload a LAN. A wrong MAC address table entry may send traffic in the wrong direction. A damaged cable may cause frame errors.

Ethernet is also important because it introduces two major ideas that will appear repeatedly in the course: local delivery and segmentation. MAC addresses handle local delivery. Collision domains and broadcast domains help explain how network traffic is contained, separated, and controlled. VLANs, which will be covered later, are built on broadcast-domain control.

## 8.3 ETHERNET STANDARDS AND LAN OPERATION

Ethernet is standardized by IEEE 802.3. The standard has evolved over time from older shared-media networks to modern switched full-duplex networks. Early Ethernet networks used hubs and shared media, where devices competed to transmit. Modern Ethernet networks use switches, where each device typically has a dedicated switch port.

Ethernet can run over different physical media and speeds. Common examples include Fast Ethernet at 100 Mbps, Gigabit Ethernet at 1 Gbps, 10 Gigabit Ethernet, 40 Gigabit Ethernet, 100 Gigabit Ethernet, and faster standards in data centers and service provider networks.

Ethernet does not replace IP. Ethernet handles local frame delivery inside a LAN or VLAN. IP handles logical addressing and routing between networks. In a typical packet journey, an IP packet is carried inside an Ethernet frame on each local Ethernet segment.

Ethernet Characteristics

- Common wired LAN technology.
- Standardized by IEEE 802.3.
- Uses frames at Layer 2.
- Uses MAC addresses for local delivery.
- Commonly uses switches in modern LANs.
- Supports many speeds, including 100 Mbps, 1 Gbps, 10 Gbps, and higher.
- Works over copper and fiber media.

Enterprise Example

In an office, a user's PC connects to an access switch using Ethernet over CAT6 cable. The PC sends Ethernet frames to the switch. If the destination is local, the switch forwards the frame toward the destination device. If the destination is remote, the PC sends the frame to the default gateway's MAC address, and the router or Layer 3 switch routes the packet onward.

## 8.4 ETHERNET FRAME STRUCTURE

An Ethernet frame is the Layer 2 data unit used by Ethernet. It carries network-layer data, such as an IP packet, across a local Ethernet link. The frame includes addressing and control information that switches and network interfaces use to deliver and verify the data.

Ethernet frame structure matters because switches forward frames based on MAC addresses. If students understand the frame, they can understand why switches learn MAC addresses, why VLAN tags exist, why frame errors matter, and why Layer 2 troubleshooting is different from Layer 3 troubleshooting.

### Main Ethernet Frame Fields

The common Ethernet frame includes these important fields:

- Preamble and Start Frame Delimiter.
- Destination MAC Address.
- Source MAC Address.
- EtherType or Length.
- Payload/Data.
- Frame Check Sequence.

### Preamble and Start Frame Delimiter

The preamble and Start Frame Delimiter help receiving devices synchronize and identify the beginning of a frame. This is part of how Ethernet prepares the receiver to read the incoming bits correctly.

In normal troubleshooting, technicians rarely inspect the preamble directly, but it is important conceptually because it shows that Ethernet frames are carefully structured, not random signals.

### Destination MAC Address

The destination MAC address identifies the local Layer 2 recipient of the frame. If the destination is on the same local network, the destination MAC may belong to the final receiving device. If the destination IP is remote, the destination MAC is usually the MAC address of the default gateway.

Switches examine the destination MAC address to decide where to forward the frame.

### Source MAC Address

The source MAC address identifies the network interface that sent the frame on the local link. Switches learn MAC addresses by reading the source MAC address of incoming frames. This learning process allows switches to build MAC address tables. Lesson 9 will explain MAC address tables in more depth.

### EtherType or Length

The EtherType field identifies the type of payload carried inside the frame. For example, EtherType `0x0800` indicates IPv4, and `0x86DD` indicates IPv6. This tells the receiving device what protocol should process the payload after the Ethernet header is removed.

### Payload/Data

The payload is the data being carried by the Ethernet frame. In many modern networks, this payload is an IP packet. The payload may contain TCP, UDP, ICMP, or other upper-layer information inside the IP packet.

### Frame Check Sequence

The Frame Check Sequence, or FCS, is used for error detection. It allows the receiving device to check whether the frame was corrupted during transmission. If the frame fails the FCS check, it is discarded.

FCS is important because physical media problems, electrical noise, bad cables, faulty transceivers, or duplex issues can cause corrupted frames. Switch interface counters may show CRC or FCS errors when Layer 1 or Layer 2 problems exist.

Ethernet Frame Structure Table

| Field | Purpose |
|---|---|
| Preamble / SFD | Synchronizes receiver and marks frame start |
| Destination MAC | Identifies local Layer 2 destination |
| Source MAC | Identifies local Layer 2 sender |
| EtherType/Length | Identifies payload type or length |
| Payload/Data | Carries upper-layer data, commonly an IP packet |
| FCS | Detects frame corruption |

Important Exam Note

For CCNA and Network+, remember that Ethernet frames use MAC addresses, while IP packets use IP addresses. Switches forward frames. Routers forward packets.

## 8.5 MAC ADDRESSING

A MAC address is a Layer 2 hardware address used to identify a network interface on a local network. MAC stands for Media Access Control. Ethernet devices use MAC addresses for local frame delivery.

A MAC address is 48 bits long and is commonly written as 12 hexadecimal digits. It may appear in formats such as:

```text
00:1A:2B:3C:4D:5E
00-1A-2B-3C-4D-5E
001A.2B3C.4D5E
```

The first 24 bits are often associated with the vendor or manufacturer and are called the Organizationally Unique Identifier, or OUI. The remaining bits identify the specific interface, although modern devices and virtualization can sometimes use locally administered or randomized MAC addresses.

### Why MAC Addresses Exist

MAC addresses exist because devices on the same local network need local identifiers. IP addresses identify logical network location, but Ethernet needs a Layer 2 address to deliver frames across the local segment.

For example, if a PC wants to send traffic to its default gateway, it places the gateway's MAC address in the destination MAC field of the Ethernet frame. The switch forwards the frame based on that MAC address. The IP packet inside the frame may be destined for a remote server, but the Ethernet frame is only concerned with the next local Layer 2 destination.

### Types of MAC Addresses

Unicast MAC Address

A unicast MAC address identifies one specific network interface. Most normal Ethernet traffic uses unicast MAC addresses.

Broadcast MAC Address

The broadcast MAC address is:

```text
FF:FF:FF:FF:FF:FF
```

It means all devices in the local broadcast domain should receive the frame. ARP Requests use broadcast at Layer 2.

Multicast MAC Address

A multicast MAC address identifies a group of receivers. It is used when frames should be delivered to selected devices that are interested in a multicast group.

### MAC Address Troubleshooting

MAC addresses are useful in troubleshooting because they help engineers identify where a device is connected. On a switch, the MAC address table can show which port learned a device's MAC address. This helps locate devices, investigate loops, troubleshoot wrong VLANs, and detect unexpected devices.

Windows command:

```powershell
getmac
ipconfig /all
```

Linux command:

```bash
ip link
```

Cisco IOS command:

```text
show mac address-table
```

## 8.6 LOCAL DELIVERY: MAC ADDRESS VS IP ADDRESS

MAC addresses and IP addresses work together, but they do different jobs.

An IP address identifies the logical source and destination across networks. A MAC address identifies the local Layer 2 sender and local Layer 2 next destination. In a remote communication, the destination IP address may be the final server, but the destination MAC address is usually the default gateway's MAC address.

This distinction is one of the most important Ethernet concepts.

Example: Same LAN

PC1 at `192.168.10.10` sends traffic to PC2 at `192.168.10.20` in the same VLAN. PC1 uses ARP to learn PC2's MAC address. The Ethernet frame destination MAC is PC2's MAC address.

Example: Remote Network

PC1 at `192.168.10.10` sends traffic to a server at `10.20.5.50`. The server is not in the local network. PC1 uses ARP to learn the default gateway's MAC address. The Ethernet frame destination MAC is the gateway's MAC address, while the IP packet destination remains `10.20.5.50`.

MAC vs IP Comparison

| Feature | MAC Address | IP Address |
|---|---|---|
| OSI Layer | Layer 2 | Layer 3 |
| Main Purpose | Local delivery | Logical addressing and routing |
| Used By | Switches and NICs | Routers, hosts, Layer 3 devices |
| Changes Across Routed Hops | Yes | Usually no, unless NAT is used |
| Example | `00:1A:2B:3C:4D:5E` | `192.168.10.10` |

## 8.7 COLLISION DOMAINS

A collision domain is a network segment where devices share the same transmission space and where collisions can occur if two devices transmit at the same time. Collisions were common in older Ethernet networks that used hubs or shared media.

A collision happens when two devices transmit on a shared medium at the same time and the signals interfere with each other. Older Ethernet used CSMA/CD, which means Carrier Sense Multiple Access with Collision Detection. Devices listened before transmitting, detected collisions, waited a random time, and tried again.

Modern switched Ethernet greatly reduces collision problems. Each switch port is its own collision domain. In full-duplex switched Ethernet, collisions should not occur because the device and switch can send and receive simultaneously over separate signaling paths.

### Hub vs Switch Collision Behavior

A hub is a Layer 1 device that repeats signals to all ports. All devices connected to a hub share one collision domain. If two devices transmit at the same time, a collision can occur.

A switch is a Layer 2 device that makes forwarding decisions. Each switch port is a separate collision domain. This is one reason switches replaced hubs in modern LANs.

Collision Domain Examples

| Device/Design | Collision Domain Behavior |
|---|---|
| Hub with 10 connected PCs | One shared collision domain |
| Switch with 10 connected PCs | 10 separate collision domains |
| Full-duplex switch port | Collisions should not occur |

Collision Domain Troubleshooting Clues

- Collisions are mostly historical in modern full-duplex switched networks.
- Late collisions usually indicate duplex mismatch or physical-layer issues.
- If collisions appear on a modern switch port, check duplex settings and cabling.
- Hubs should not be used in modern enterprise LANs.

## 8.8 BROADCAST DOMAINS

A broadcast domain is a network area where broadcast frames are forwarded. If one device sends a Layer 2 broadcast, all devices in the same broadcast domain receive it.

Broadcast domains matter because broadcast traffic consumes network resources. Broadcasts are useful for discovery protocols such as ARP and DHCP, but excessive broadcasts can reduce performance. Large flat networks with too many devices in one broadcast domain are harder to manage and less secure.

Switches forward broadcasts out all ports in the same VLAN, except the port where the broadcast was received. Routers do not forward Layer 2 broadcasts by default. VLANs create separate broadcast domains inside a switched network.

Broadcast Domain Examples

| Design | Broadcast Domain Behavior |
|---|---|
| One switch, one VLAN | One broadcast domain |
| One switch, three VLANs | Three broadcast domains |
| Two switches connected by trunk carrying one VLAN | One broadcast domain for that VLAN across both switches |
| Router separating two LANs | Two broadcast domains |

Broadcast Domain Troubleshooting Clues

- Excessive broadcast traffic can slow a network.
- ARP and DHCP use broadcast behavior in IPv4 networks.
- VLANs control broadcast scope.
- If DHCP does not cross a router, DHCP relay/IP helper may be required.
- If a device is in the wrong VLAN, it may be in the wrong broadcast domain.

Enterprise Example

A company places staff, voice, CCTV, and guest Wi-Fi in separate VLANs. Each VLAN is a separate broadcast domain. Guest users' broadcasts do not reach staff computers, and CCTV device broadcasts do not flood the voice VLAN. This improves performance, segmentation, and troubleshooting.

## 8.9 COLLISION DOMAINS VS BROADCAST DOMAINS

Collision domains and broadcast domains are different concepts.

A collision domain is about where collisions can occur on shared media. It is mostly related to older Ethernet behavior and hub-based networks. A broadcast domain is about where broadcast frames are delivered. Broadcast domains are still very important in modern switched networks.

Collision vs Broadcast Domain Comparison

| Feature | Collision Domain | Broadcast Domain |
|---|---|---|
| Main Concern | Simultaneous transmissions causing collisions | Broadcast traffic reach |
| Commonly Controlled By | Switch ports and full-duplex links | Routers and VLANs |
| Still Important Today | Less common, mostly for troubleshooting duplex issues | Very important |
| Hub Behavior | One shared collision domain | One broadcast domain unless routed |
| Switch Behavior | Each port is separate collision domain | VLAN defines broadcast domain |
| Router Behavior | Separates collision domains by interface | Separates broadcast domains by interface |

Exam Reminder

For CCNA and Network+, remember: each switch port is a collision domain, and each VLAN is a broadcast domain. Routers separate broadcast domains.

## 8.10 DUPLEX

Duplex describes whether a network interface can send and receive at the same time.

Half-duplex means a device cannot send and receive simultaneously. It must take turns. Half-duplex was common with older hub-based Ethernet. Collisions can occur in half-duplex environments.

Full-duplex means a device can send and receive at the same time. Modern switched Ethernet normally uses full-duplex. In full-duplex communication, collisions should not occur.

Duplex matters because mismatched duplex settings can cause serious performance problems. A duplex mismatch may occur when one side is forced to full-duplex and the other side auto-negotiates or uses half-duplex. The link may come up, but performance may be poor, with errors, retransmissions, and late collisions.

Duplex Comparison

| Duplex Mode | Behavior | Collision Risk | Modern Use |
|---|---|---|---|
| Half-duplex | Send or receive, not both at the same time | Yes | Mostly legacy |
| Full-duplex | Send and receive simultaneously | No expected collisions | Standard modern Ethernet |

Duplex Troubleshooting Clues

- Slow performance with link up may indicate duplex mismatch.
- Late collisions suggest duplex or physical-layer problems.
- CRC errors may indicate cabling, physical media, or duplex issues.
- Modern devices should usually use auto-negotiation unless design requires otherwise.

## 8.11 SPEED AND AUTO-NEGOTIATION

Ethernet speed describes the data rate supported by the link. Common Ethernet speeds include 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, 40 Gbps, 100 Gbps, and higher in modern data centers.

Auto-negotiation is the process where two connected Ethernet devices exchange capabilities and agree on speed and duplex. For example, a PC and switch may negotiate 1 Gbps full-duplex if both support it and the cable is suitable.

Auto-negotiation exists because devices may support different speeds and duplex modes. It allows them to choose the best common setting automatically. In modern networks, auto-negotiation usually works well when cabling and hardware are correct.

However, problems can occur. A bad cable may cause a device to negotiate at 100 Mbps instead of 1 Gbps. A manually forced speed or duplex on one side can create mismatch. An older device may not support the desired speed. A transceiver may not match the port speed.

Common Speed and Negotiation Symptoms

- Link comes up at 100 Mbps instead of 1 Gbps.
- Link flaps between up and down.
- Interface shows high errors.
- One side shows full-duplex and the other shows half-duplex.
- Fiber link does not come up due to optic mismatch.

Cisco IOS Speed/Duplex Checks

```text
show interfaces status
show interfaces
```

Windows Checks

```powershell
Get-NetAdapter
```

Linux Checks

```bash
ethtool <interface>
```

Best Practice

Use auto-negotiation in most modern Ethernet environments unless there is a specific engineering requirement to hard-code speed and duplex. If hard-coding is required, configure both sides consistently and document the reason.

## 8.12 ETHERNET TROUBLESHOOTING

Ethernet troubleshooting combines Layer 1 and Layer 2 thinking. The technician must check the physical link, negotiated speed, duplex, MAC learning, VLAN placement, broadcast behavior, and interface errors.

Common Ethernet Troubleshooting Flow

1. Check link light and cable.
2. Check interface status.
3. Check speed and duplex.
4. Check error counters such as CRC, input errors, output errors, and late collisions.
5. Check MAC address learning.
6. Check VLAN assignment.
7. Check whether broadcasts are excessive.
8. Check whether the issue affects one device, one switch port, one VLAN, or many users.

Cisco IOS Ethernet Troubleshooting Commands

```text
show interfaces status
show interfaces
show mac address-table
show vlan brief
show interfaces counters errors
```

Windows and Linux Checks

```powershell
Get-NetAdapter
ipconfig /all
```

```bash
ip link
ethtool <interface>
```

Important Troubleshooting Reminder

If a link is up but performance is poor, do not assume the network is healthy. Check speed, duplex, errors, cable quality, and interface counters.

## 8.13 CYBERSECURITY RELEVANCE

Ethernet security matters because Layer 2 is the first point of access in many wired networks. If an attacker can plug into an Ethernet port, they may attempt to join the LAN, capture traffic, spoof MAC addresses, send rogue DHCP messages, perform ARP spoofing, or attack local services.

MAC addresses are not strong identity by themselves. They can be spoofed. This means security should not depend only on trusting a MAC address. Enterprise networks use additional controls such as port security, 802.1X authentication, DHCP Snooping, Dynamic ARP Inspection, VLAN segmentation, disabled unused ports, and monitoring.

Broadcast domains also matter for security. A flat network with one large broadcast domain allows more devices to see discovery traffic and may allow attacks to spread more easily. Segmentation using VLANs reduces unnecessary exposure.

Security Reminder

Ethernet is local, but local does not mean safe. Physical access plus weak Layer 2 controls can become a serious security risk.

## 8.14 CLOUD NETWORKING RELEVANCE

Cloud customers usually do not manage physical Ethernet switches inside the cloud provider's data center, but Ethernet concepts still matter. Cloud providers use high-speed Ethernet fabrics inside their infrastructure. Virtual NICs, virtual switches, overlays, and software-defined networks still depend on Layer 2 and Layer 3 principles.

In cloud environments, customers often see virtual MAC addresses, virtual NICs, virtual subnets, and security policies instead of physical switch ports. The customer may not troubleshoot a physical Ethernet cable, but they still troubleshoot interface attachment, IP assignment, security groups, virtual routing, and traffic flow.

Hybrid networks also depend on Ethernet locally. A company may access cloud services through an office LAN, switch, firewall, ISP handoff, and router. If the local Ethernet link to the firewall is negotiating incorrectly or dropping frames, cloud applications may appear slow even though the cloud platform is healthy.

Cloud Reminder

Cloud abstracts many Layer 2 details, but Ethernet concepts remain important for hybrid networks, virtualization, data centers, and troubleshooting local access to cloud services.

## 9. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Ethernet | Common wired LAN technology standardized by IEEE 802.3. |
| Ethernet Frame | Layer 2 data unit used by Ethernet. |
| MAC Address | 48-bit Layer 2 address used for local Ethernet delivery. |
| OUI | Organizationally Unique Identifier, vendor-related part of a MAC address. |
| Preamble | Frame field used to help synchronize the receiver. |
| Start Frame Delimiter | Field marking the start of an Ethernet frame. |
| EtherType | Field identifying the protocol carried in the Ethernet payload. |
| Payload | Data carried inside an Ethernet frame, commonly an IP packet. |
| FCS | Frame Check Sequence used for error detection. |
| Collision Domain | Network area where collisions can occur. |
| Broadcast Domain | Network area where broadcast frames are forwarded. |
| Hub | Layer 1 device that repeats signals to all ports. |
| Switch | Layer 2 device that forwards frames using MAC addresses. |
| CSMA/CD | Older Ethernet collision detection method. |
| Half-Duplex | Communication mode where a device cannot send and receive at the same time. |
| Full-Duplex | Communication mode where a device can send and receive simultaneously. |
| Auto-Negotiation | Process where devices agree on speed and duplex. |
| CRC Error | Error indicating possible frame corruption, often related to physical issues. |
| Late Collision | Collision detected late, often related to duplex mismatch or legacy problems. |
| Broadcast MAC | `FF:FF:FF:FF:FF:FF`, used to send to all local devices in a broadcast domain. |

## 10. COMPARISON TABLES

### 10.1 Ethernet Frame Fields

| Field | Main Purpose |
|---|---|
| Preamble / SFD | Synchronization and frame start |
| Destination MAC | Local Layer 2 destination |
| Source MAC | Local Layer 2 sender |
| EtherType/Length | Identifies payload type or length |
| Payload | Carries upper-layer data |
| FCS | Detects frame corruption |

### 10.2 MAC Address vs IP Address

| Feature | MAC Address | IP Address |
|---|---|---|
| Layer | Layer 2 | Layer 3 |
| Used For | Local frame delivery | Logical addressing and routing |
| Device Mainly Using It | Switch | Router |
| Changes Across Routed Hops | Yes | Usually no, unless NAT |
| Example Format | `001A.2B3C.4D5E` | `192.168.10.10` |

### 10.3 Collision Domain vs Broadcast Domain

| Feature | Collision Domain | Broadcast Domain |
|---|---|---|
| Concern | Collisions on shared media | Broadcast traffic reach |
| Controlled By | Switch ports/full duplex | VLANs and routers |
| Modern Importance | Lower, mostly troubleshooting | High |
| Hub Effect | One shared collision domain | One broadcast domain |
| Switch Effect | Each port is separate collision domain | VLAN defines broadcast domain |

### 10.4 Half-Duplex vs Full-Duplex

| Feature | Half-Duplex | Full-Duplex |
|---|---|---|
| Send and Receive | One direction at a time | Both directions at once |
| Collisions | Possible | Not expected |
| Common Today | Rare/legacy | Standard |
| Common Problem | Collisions | Mismatch if configured badly |

### 10.5 Common Ethernet Symptoms

| Symptom | Possible Cause |
|---|---|
| No link | Cable, port, NIC, transceiver, shutdown port |
| Link at wrong speed | Bad cable, old device, negotiation issue |
| High CRC errors | Cable, interference, transceiver, physical problem |
| Late collisions | Duplex mismatch or legacy shared media |
| Broadcast storm | Loop or excessive broadcast traffic |
| Device unreachable in same VLAN | MAC learning, VLAN, cable, NIC, local firewall |

## 11. REAL-WORLD EXAMPLE / ANALOGY

Think of Ethernet like an office mailroom inside one building.

The IP address is like the full company address used to reach a building or branch. The MAC address is like the desk or room label used inside the local office. The Ethernet frame is like the internal envelope used by the mailroom to deliver the package locally. If the package must go to another branch, the local mailroom first sends it to the outgoing mail desk, which is like the default gateway.

Collision domains are like shared walkways where people can bump into each other if everyone moves at once. Modern switches create separate paths, reducing collisions. Broadcast domains are like announcement zones. If an announcement is made in one department, everyone in that department hears it. VLANs create separate announcement zones so every message does not disturb the whole building.

## 12. CISCO PACKET TRACER PRACTICE

### Practice Lab: Observe Ethernet Behavior

Build a topology:

- PC1.
- PC2.
- One switch.
- One router or Layer 3 gateway.

Suggested addressing:

| Device | IP Address | Gateway |
|---|---|---|
| PC1 | 192.168.10.10/24 | 192.168.10.1 |
| PC2 | 192.168.10.20/24 | 192.168.10.1 |
| Gateway | 192.168.10.1/24 | Not applicable |

Student tasks:

1. Ping PC2 from PC1.
2. Use Simulation Mode to observe ARP and Ethernet frames.
3. Identify source and destination MAC addresses.
4. Ping the gateway and observe the destination MAC.
5. Add a second VLAN if available and observe broadcast separation.
6. Check the switch MAC address table.
7. Disconnect a cable and observe link behavior.

Expected learning outcome:

Students should understand that Ethernet uses frames and MAC addresses for local delivery, while broadcast domains define where local broadcasts are heard.

## 13. WINDOWS, LINUX, AND CISCO IOS PRACTICAL COMMANDS

### Windows Commands

```powershell
getmac
ipconfig /all
Get-NetAdapter
arp -a
```

### Linux Commands

```bash
ip link
ip addr
ip neigh
ethtool <interface>
```

### Cisco IOS Commands

```text
show mac address-table
show interfaces status
show interfaces
show vlan brief
show interfaces counters errors
```

## 14. QUICK-RECAP CHEAT SHEET

- Ethernet is the most common wired LAN technology.
- Ethernet is standardized by IEEE 802.3.
- Ethernet uses frames at Layer 2.
- Ethernet uses MAC addresses for local delivery.
- A MAC address is 48 bits long.
- The broadcast MAC address is `FF:FF:FF:FF:FF:FF`.
- Switches forward frames based on MAC addresses.
- Routers forward packets based on IP addresses.
- An Ethernet frame includes destination MAC, source MAC, EtherType, payload, and FCS.
- FCS helps detect frame corruption.
- A collision domain is where collisions can occur.
- Each switch port is its own collision domain.
- A broadcast domain is where broadcast frames are forwarded.
- Each VLAN is a broadcast domain.
- Routers separate broadcast domains.
- Half-duplex cannot send and receive at the same time.
- Full-duplex can send and receive at the same time.
- Modern switched Ethernet normally uses full-duplex.
- Auto-negotiation allows devices to agree on speed and duplex.
- Duplex mismatch can cause poor performance and errors.

## 15. REVIEW QUESTIONS

1. What is Ethernet?
2. What IEEE standard defines Ethernet?
3. What OSI layer mainly uses Ethernet frames?
4. What is an Ethernet frame?
5. What are the main fields in an Ethernet frame?
6. What is the purpose of the destination MAC address?
7. What is the purpose of the source MAC address?
8. What does EtherType identify?
9. What does FCS do?
10. What is a MAC address?
11. What is the broadcast MAC address?
12. What is the difference between a MAC address and an IP address?
13. What is a collision domain?
14. Why are collisions rare in modern switched Ethernet?
15. What is a broadcast domain?
16. How do VLANs affect broadcast domains?
17. What is the difference between half-duplex and full-duplex?
18. What is auto-negotiation?
19. What can cause a link to negotiate at a lower speed than expected?
20. Why does successful link status not always mean Ethernet performance is healthy?

## 16. SUGGESTED ANSWER GUIDE

1. Ethernet is the most common wired LAN technology for local network communication.
2. IEEE 802.3.
3. Layer 2, the Data Link layer.
4. An Ethernet frame is the Layer 2 data unit used by Ethernet.
5. Preamble/SFD, destination MAC, source MAC, EtherType/Length, payload, and FCS.
6. It identifies the local Layer 2 recipient of the frame.
7. It identifies the local Layer 2 sender of the frame.
8. EtherType identifies the protocol carried in the payload, such as IPv4 or IPv6.
9. FCS detects frame corruption.
10. A MAC address is a 48-bit Layer 2 address used for local delivery.
11. `FF:FF:FF:FF:FF:FF`.
12. A MAC address is used for local Layer 2 delivery, while an IP address is used for logical Layer 3 addressing and routing.
13. A collision domain is a network segment where collisions can occur.
14. Modern switches give each port its own collision domain and usually use full-duplex.
15. A broadcast domain is the area where broadcast frames are forwarded.
16. Each VLAN creates a separate broadcast domain.
17. Half-duplex cannot send and receive at the same time; full-duplex can.
18. Auto-negotiation is the process where Ethernet devices agree on speed and duplex.
19. Bad cable, old hardware, unsupported speed, transceiver mismatch, or negotiation problems.
20. The link may be up but still have errors, duplex mismatch, poor cable quality, or excessive broadcasts.
