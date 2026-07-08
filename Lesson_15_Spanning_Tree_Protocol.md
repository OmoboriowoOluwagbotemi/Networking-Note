# LESSON 15: SPANNING TREE PROTOCOL

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 15.1 What Is Spanning Tree Protocol?

Spanning Tree Protocol, or STP, is a Layer 2 loop-prevention protocol used in switched Ethernet networks. Its job is to allow physical redundancy while preventing Layer 2 loops. STP does this by creating a loop-free logical topology and placing selected redundant switch ports into a blocking or discarding state.

In Lessons 13 and 14, VLANs and trunks showed how switches can carry multiple Layer 2 networks across physical links. Redundancy is useful because an enterprise does not want one failed cable or one failed switch to bring down a whole department. However, redundant Layer 2 links can create loops if every path forwards frames at the same time. STP solves this problem.

STP exists because Ethernet frames do not have a built-in hop limit like IP packets. At Layer 3, an IP packet has a TTL or hop limit that eventually expires. At Layer 2, an Ethernet frame can loop indefinitely if the switching topology allows it. Broadcasts, unknown unicasts, and multicasts can multiply quickly and overwhelm the LAN.

In a healthy design, STP allows backup paths to exist physically while keeping the active forwarding topology loop-free. If the active path fails, STP can unblock a backup path so traffic can continue.

For CCNA and CompTIA Network+, students must understand why Layer 2 loops occur, what BPDUs are, how the root bridge is elected, and how STP port roles and states prevent loops.

### 15.2 Why STP Matters

STP matters because a Layer 2 loop can bring down an enterprise network very quickly. One wrongly patched cable, one unmanaged switch connected under a desk, or one misconfigured trunk can create a loop. Once a loop forms, broadcast frames may circulate endlessly. Switch CPU usage may rise. MAC address tables may flap. Users may lose access to DHCP, DNS, servers, internet, phones, and wireless services.

STP also matters because redundancy is necessary. A network with no redundant links is simple but fragile. If one uplink fails, users may be disconnected. A network with redundant links but no loop prevention is dangerous. STP provides the balance: physical redundancy with logical loop prevention.

In real enterprise troubleshooting, STP appears in symptoms such as sudden network slowness, switch logs showing topology changes, MAC addresses moving between ports, unstable trunks, high broadcast traffic, and ports blocking unexpectedly. A technician who understands STP can tell the difference between a normal blocked backup path and a dangerous loop.

## 15.3 Why Layer 2 Loops Occur

A Layer 2 loop occurs when there is more than one active switching path between the same Layer 2 devices and frames can circulate endlessly. Loops usually happen when redundant switch links are connected without proper loop prevention.

Example:

```text
SW1 ----- SW2
 |         |
 |         |
 SW3 -----
```

If SW1, SW2, and SW3 are connected in a triangle and all links forward traffic, a broadcast sent by one device may be forwarded around the triangle repeatedly. Each switch floods broadcasts out all ports in the same VLAN except the incoming port. With a loop, those broadcasts can come back again and again.

Layer 2 loops are especially dangerous because switches learn MAC addresses based on the source MAC address of incoming frames. If the same frame loops and arrives on different ports, the switch may keep changing its MAC address table. This is called MAC address table instability or MAC flapping.

Common causes of Layer 2 loops include:

- Redundant switch links without STP.
- A user connecting both ends of a cable into wall ports.
- An unmanaged switch connected with multiple uplinks.
- Misconfigured trunks.
- Incorrectly disabled STP.
- Lab cabling mistakes.
- Bridged wireless or virtualization environments connected incorrectly.

## 15.4 What Happens During a Layer 2 Loop?

When a Layer 2 loop forms, several damaging events can happen.

The first problem is a broadcast storm. A broadcast storm occurs when broadcast frames are repeatedly forwarded and multiplied across the network. ARP Requests, DHCP Discover messages, and other broadcast traffic may loop continuously.

The second problem is MAC address flapping. A switch may learn the same MAC address on one port, then another port, then another port again. This causes unstable forwarding because the switch cannot reliably decide where the device is located.

The third problem is duplicate frames. A host may receive the same frame multiple times because it arrives through different looped paths. This can confuse applications and increase unnecessary traffic.

The fourth problem is control-plane stress. Switch CPU and memory may become overloaded by excessive traffic, constant MAC updates, and topology instability. In severe cases, management access to switches may fail.

Layer 2 Loop Symptoms

| Symptom | What It Suggests |
|---|---|
| Network suddenly becomes very slow | Broadcast storm or loop |
| MAC address moves between ports | MAC flapping |
| Switch CPU becomes high | Excessive Layer 2 control/traffic load |
| DHCP fails across many devices | Broadcast/control-plane congestion |
| Users lose access in multiple VLANs | Trunk or loop problem |
| Switch logs show frequent topology changes | STP instability |

## 15.5 STP Design Goal

The goal of STP is not to remove redundant physical links. The goal is to keep redundancy while preventing loops.

STP builds a loop-free logical topology by selecting one switch as the root bridge. Every non-root switch calculates the best path back to the root bridge. Ports that are needed for the loop-free path are placed into forwarding roles. Ports that would create loops are placed into blocking or discarding roles.

The physical topology may have multiple links:

```text
SW1 ----- SW2
 |         |
 |         |
 SW3 -----
```

The logical STP topology may block one link:

```text
SW1 ----- SW2
 |         
 |         
 SW3 ----- SW2 link blocked logically
```

The link still exists physically, but STP prevents it from forwarding normal data frames while it would create a loop. If an active path fails, STP can reconverge and use the backup path.

## 15.6 BPDUs

BPDU means Bridge Protocol Data Unit. BPDUs are special STP messages that switches use to exchange spanning-tree information.

BPDUs allow switches to answer important questions:

- Which switch should become the root bridge?
- What is the best path to the root bridge?
- Which ports should forward?
- Which ports should block or discard?
- Has the topology changed?

Switches send and receive BPDUs on STP-enabled ports. These messages contain information such as bridge ID, root bridge ID, path cost, sender bridge ID, and port ID.

BPDUs are essential because STP is a distributed protocol. There is no separate controller telling every switch what to do. Switches communicate with each other using BPDUs and independently calculate the loop-free topology.

BPDU Information

| BPDU Field | Purpose |
|---|---|
| Root Bridge ID | Identifies the current root bridge |
| Sender Bridge ID | Identifies the switch sending the BPDU |
| Root Path Cost | Cost from sender toward root bridge |
| Port ID | Helps select ports when other values tie |
| Timers | Control STP convergence behavior |

## 15.7 Bridge ID

The Bridge ID, often called BID, identifies a switch in STP. The Bridge ID is used during root bridge election.

The Bridge ID contains:

```text
Bridge Priority + MAC Address
```

In modern Cisco per-VLAN spanning-tree environments, the bridge priority also includes the VLAN ID as part of the extended system ID. Students do not need to calculate that deeply at this stage, but they should recognize that STP can operate per VLAN on Cisco switches.

The default Cisco STP bridge priority is commonly:

```text
32768
```

Lower Bridge ID wins. Because the Bridge ID contains priority first, the switch with the lowest priority becomes the root bridge. If priorities are tied, the lower MAC address wins.

Bridge ID Decision

| Priority | MAC Address | Result |
|---:|---|---|
| 4096 | 00AA.1111.1111 | Better than default priority |
| 32768 | 0001.2222.2222 | Default priority |
| 32768 | 0001.1111.1111 | Wins over same priority with higher MAC |

In professional networks, engineers should not let the root bridge be chosen accidentally by the lowest MAC address. The root bridge should be planned.

## 15.8 Root Bridge Election

The root bridge is the central reference point for STP calculations. All switches calculate their best path toward the root bridge.

Root bridge election follows this rule:

```text
Lowest Bridge ID becomes the root bridge.
```

Because Bridge ID is based on priority and MAC address, the election process is:

1. Lowest bridge priority wins.
2. If priority ties, lowest MAC address wins.

Example:

| Switch | Priority | MAC Address | Root Election Result |
|---|---:|---|---|
| SW1 | 32768 | 00AA.AAAA.AAAA | Loses |
| SW2 | 4096 | 00BB.BBBB.BBBB | Wins because priority is lowest |
| SW3 | 32768 | 0001.CCCC.CCCC | Loses |

SW2 becomes the root bridge because its priority is 4096, which is lower than 32768.

Root bridge placement matters. A root bridge should usually be placed near the center of the Layer 2 design, often on a distribution switch or collapsed core switch. If an access switch accidentally becomes root, traffic paths may become inefficient and troubleshooting becomes confusing.

Basic Cisco IOS command to influence root bridge:

```text
spanning-tree vlan 10 root primary
```

Alternative manual priority command:

```text
spanning-tree vlan 10 priority 4096
```

The exact design depends on the network, but the principle is clear: choose the root bridge intentionally.

## 15.9 STP Path Cost

STP uses path cost to determine the best path to the root bridge. Faster links usually have lower cost. Lower total cost is preferred.

If a switch has multiple possible paths to the root bridge, it chooses the path with the lowest root path cost.

Example:

```text
SW3 has two paths to root SW1.
Path A uses a 1 Gbps link.
Path B uses a 100 Mbps link.
STP prefers the lower-cost 1 Gbps path.
```

Common Cost Concept

| Link Speed | STP Cost Concept |
|---|---|
| Faster link | Lower cost, more preferred |
| Slower link | Higher cost, less preferred |

Different STP standards and platforms may use different exact cost values, especially for modern high-speed links. For beginner CCNA and Network+ understanding, the important idea is that lower cost is preferred and faster links generally have lower cost.

## 15.10 STP Port Roles

STP assigns port roles to determine which ports forward and which ports prevent loops.

The main STP port roles students should understand are:

- Root port.
- Designated port.
- Non-designated or alternate port.

The root port is the best port on a non-root switch toward the root bridge. Every non-root switch has one root port per spanning-tree instance.

A designated port is the best forwarding port on a network segment. Designated ports forward traffic toward and away from that segment.

A non-designated or alternate port is a port that is not currently forwarding because forwarding would create a loop. In classic STP, this port is blocking. In Rapid STP terminology, an alternate port is in a discarding state.

STP Port Roles

| Port Role | Where It Exists | Purpose |
|---|---|---|
| Root Port | Non-root switches | Best path toward root bridge |
| Designated Port | Each segment | Forwarding port for that segment |
| Alternate/Non-Designated Port | Redundant path | Prevents Layer 2 loop |

On the root bridge, all active STP ports are designated ports because the root bridge is the reference point for the topology.

## 15.11 STP Port States

Classic STP uses port states to control whether a port forwards frames or learns MAC addresses.

The classic 802.1D STP port states are:

- Blocking.
- Listening.
- Learning.
- Forwarding.
- Disabled.

Blocking means the port does not forward normal traffic and does not learn MAC addresses. It listens for BPDUs.

Listening means the port is preparing to participate in the topology but still does not learn MAC addresses or forward normal traffic.

Learning means the port learns MAC addresses but does not forward normal traffic yet.

Forwarding means the port forwards normal traffic and learns MAC addresses.

Disabled means the port is administratively shut down or not participating.

Classic STP Port States

| State | Forwards Data? | Learns MACs? | Receives BPDUs? |
|---|---|---|---|
| Blocking | No | No | Yes |
| Listening | No | No | Yes |
| Learning | No | Yes | Yes |
| Forwarding | Yes | Yes | Yes |
| Disabled | No | No | No normal participation |

Rapid Spanning Tree Protocol, or RSTP, simplifies states into discarding, learning, and forwarding. Many modern networks use Rapid PVST+ or other faster STP variants, but understanding classic states helps students understand the logic.

RSTP State Mapping

| Classic STP State | RSTP Equivalent |
|---|---|
| Blocking | Discarding |
| Listening | Discarding |
| Learning | Learning |
| Forwarding | Forwarding |
| Disabled | Discarding/disabled context |

## 15.12 How STP Prevents Loops Step by Step

Consider three switches connected in a triangle:

```text
SW1 ----- SW2
 |         |
 |         |
 SW3 -----
```

Step 1: Switches exchange BPDUs.

Each switch sends BPDUs containing its bridge information. At the beginning, each switch may believe it is the root bridge until it hears a better BPDU.

Step 2: Root bridge is elected.

The switch with the lowest Bridge ID becomes the root bridge.

Step 3: Non-root switches choose root ports.

Each non-root switch chooses its best path back to the root bridge.

Step 4: Designated ports are selected on each segment.

Each network segment needs one forwarding designated port.

Step 5: Redundant loop-causing ports are blocked or discarded.

Any port that would create a loop is placed into a non-forwarding state.

Step 6: The logical topology becomes loop-free.

Traffic can forward, but not around a loop. If a forwarding link fails, STP can recalculate and use a backup path.

## 15.13 STP Variants

Several STP variants exist. Students should recognize the names and basic differences.

STP, based on IEEE 802.1D, is the original spanning-tree standard. It prevents loops but converges relatively slowly compared with modern options.

RSTP, based on IEEE 802.1w, is Rapid Spanning Tree Protocol. It improves convergence speed and uses port roles such as root, designated, alternate, and backup.

PVST+ is Cisco's Per-VLAN Spanning Tree Plus. It runs a separate STP instance for each VLAN, allowing different VLANs to have different root bridges and paths.

Rapid PVST+ is Cisco's rapid per-VLAN version based on RSTP behavior.

MST, Multiple Spanning Tree, maps multiple VLANs to fewer spanning-tree instances to reduce overhead in larger environments.

STP Variant Summary

| Variant | Main Idea | Common Relevance |
|---|---|---|
| STP / 802.1D | Original loop prevention | Foundational concept |
| RSTP / 802.1w | Faster convergence | Modern standard behavior |
| PVST+ | One STP instance per VLAN | Cisco environments |
| Rapid PVST+ | Per-VLAN rapid STP | Common Cisco campus use |
| MST | Maps VLANs to fewer instances | Larger scalable designs |

For this course stage, the most important point is not memorizing every timer. The key is understanding how STP prevents Layer 2 loops.

## 15.14 PortFast

PortFast is a Cisco feature used on access ports connected to end devices. It allows an access port to move to forwarding quickly instead of waiting through normal STP listening and learning delays.

PortFast exists because end devices such as PCs, printers, and phones do not normally create Layer 2 loops. A user device expects network access quickly after link comes up. Without PortFast, a device may wait before the port forwards traffic, which can delay DHCP and startup connectivity.

Basic PortFast command:

```text
interface fastEthernet 0/10
 spanning-tree portfast
```

Important warning:

```text
Use PortFast only on ports connected to end devices.
```

Do not enable PortFast on switch-to-switch links. If PortFast is incorrectly enabled on a port connected to another switch, a loop can form before STP has time to protect the network.

## 15.15 BPDU Guard

BPDU Guard is a protection feature often used with PortFast. It disables a PortFast-enabled port if the port receives a BPDU.

BPDU Guard exists because an access port should not normally receive BPDUs. If a BPDU appears on a user-facing PortFast port, it may mean someone connected a switch or bridge device where an endpoint should be.

Basic interface command:

```text
interface fastEthernet 0/10
 spanning-tree bpduguard enable
```

Global default for PortFast ports:

```text
spanning-tree portfast bpduguard default
```

If BPDU Guard triggers, the port may enter an err-disabled state. The administrator should investigate before re-enabling the port.

BPDU Guard is a cybersecurity and stability feature. It helps prevent accidental or unauthorized switches from creating Layer 2 problems at the access layer.

## 15.16 STP Troubleshooting

STP troubleshooting begins by identifying whether the issue is normal loop prevention or an actual fault. A blocked port may be healthy if it is blocking a redundant path. A topology change may be normal after a link failure. However, repeated topology changes, MAC flapping, high broadcast traffic, or unexpected root bridge changes require investigation.

Useful Cisco IOS commands:

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show spanning-tree root
show interfaces status
show interfaces trunk
show mac address-table
show logging
```

What to check:

- Which switch is the root bridge?
- Is the expected switch the root bridge?
- Which ports are root ports?
- Which ports are designated ports?
- Which ports are blocking or discarding?
- Are topology changes frequent?
- Are MAC addresses flapping?
- Are trunks carrying the expected VLANs?
- Did BPDU Guard err-disable a port?

Common STP Troubleshooting Table

| Symptom | Possible Cause | What to Check |
|---|---|---|
| Unexpected blocked port | STP preventing a loop | `show spanning-tree` |
| Wrong switch is root | Priority not configured | Root bridge ID, priority |
| Frequent topology changes | Flapping link or loop | Logs, interfaces, STP summary |
| MAC address flapping | Layer 2 loop | MAC table, logs, cabling |
| Access port err-disabled | BPDU Guard triggered | `show logging`, interface status |
| VLAN affected across trunk | Per-VLAN STP or trunk issue | `show spanning-tree vlan`, `show interfaces trunk` |

## 15.17 Windows, Linux, and Cisco IOS Practical Checks

### Windows Checks

```text
ipconfig /all
ping <default-gateway>
arp -a
tracert <destination>
```

Windows does not show STP directly. A Windows user may report symptoms such as intermittent connectivity, DHCP failure, or sudden network slowness. The technician uses Windows to confirm host impact, then checks the switch for STP and loop symptoms.

### Linux Checks

```text
ip addr
ip route
ip neigh
ping <default-gateway>
```

Linux checks confirm whether the endpoint has an address, gateway, and neighbor entries. If multiple endpoints in the same VLAN fail at once, the problem is more likely a switching, trunk, STP, or DHCP issue than a single host issue.

### Cisco IOS Checks

```text
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
show spanning-tree root
show interfaces status
show logging
show mac address-table
```

Cisco IOS is the primary place to verify STP. These commands show root bridge information, port roles, port states, topology changes, and logs.

## 15.18 Cisco Packet Tracer Practice

### Practice Lab: Observe STP Blocking a Redundant Link

Build a topology:

- Three switches connected in a triangle.
- Two PCs in VLAN 10 connected to different switches.
- Trunks between switches.

Tasks:

1. Create VLAN 10 on all switches.
2. Configure switch-to-switch links as trunks.
3. Connect the switches in a triangle.
4. Run `show spanning-tree vlan 10`.
5. Identify the root bridge.
6. Identify root ports and designated ports.
7. Identify which port is blocking.
8. Disconnect one forwarding trunk.
9. Observe STP reconvergence.
10. Test PC connectivity again.

Expected learning outcome:

Students should understand that STP blocks one redundant path to prevent a loop and can use the backup path if the active path fails.

### Practice Lab: Control the Root Bridge

Use the same three-switch topology.

On the switch that should be root:

```text
configure terminal
spanning-tree vlan 10 root primary
end
```

Tasks:

1. Verify the root bridge using `show spanning-tree vlan 10`.
2. Record the root bridge ID.
3. Configure a different switch with a lower priority manually.
4. Observe whether the root bridge changes.
5. Explain why root bridge placement should be planned.

Expected learning outcome:

Students should understand that STP root bridge election should be intentional, not accidental.

## 15.19 Cybersecurity Relevance

STP is also a security topic because Layer 2 instability can be caused accidentally or maliciously. An attacker who connects an unauthorized switch could influence STP, create topology changes, or attempt to become the root bridge if protections are weak.

Security-focused STP practices include:

- Configure the intended root bridge.
- Use BPDU Guard on PortFast access ports.
- Use PortFast only on endpoint ports.
- Disable unused ports.
- Avoid unmanaged switches under desks.
- Monitor topology changes.
- Investigate MAC flapping.
- Protect trunk ports physically and administratively.

Features such as Root Guard and Loop Guard also exist in enterprise designs, but they are beyond the basic scope of this lesson. The important principle is that STP should be controlled, monitored, and documented.

## 15.20 Cloud Networking Relevance

Public cloud networks usually hide physical STP from customers. Cloud providers manage the underlying physical and virtual switching fabric. However, STP remains relevant in private clouds, data centers, virtualization clusters, and campus networks that connect to cloud gateways.

In a data center, redundant switches, hypervisor uplinks, storage networks, and firewall pairs may require loop prevention or alternative redundancy designs. Some modern data centers use Layer 3 links, MLAG/vPC, EVPN, or software-defined fabrics to reduce reliance on classic STP. Even then, understanding STP helps engineers understand why Layer 2 loops are dangerous.

For hybrid cloud, a local switching loop can break access to cloud applications before the traffic ever leaves the building. Cloud troubleshooting still begins with the local network.

## 15.21 Interview and Exam Relevance

In IT support interviews, STP questions may focus on symptoms. An interviewer may ask what could cause the whole office network to suddenly slow down after someone connected a small switch. The answer should include the possibility of a Layer 2 loop and STP behavior.

In network engineering interviews, STP questions may include root bridge election, BPDUs, port roles, port states, PortFast, BPDU Guard, and how to verify STP with show commands.

For CCNA, students should understand root bridge election, bridge priority, BPDUs, root ports, designated ports, blocked or alternate ports, and basic STP verification. For Network+, students should understand why STP exists and how it prevents switching loops.

## 16. KEY TERMS / GLOSSARY

| Term | Meaning |
|---|---|
| STP | Spanning Tree Protocol, a Layer 2 loop-prevention protocol. |
| Layer 2 Loop | Loop where Ethernet frames can circulate endlessly through switches. |
| Broadcast Storm | Excessive broadcast traffic caused by looping or uncontrolled broadcasts. |
| BPDU | Bridge Protocol Data Unit, STP message exchanged between switches. |
| Bridge ID | Identifier used in STP root bridge election. |
| Bridge Priority | Configurable STP value used to influence root election. |
| Root Bridge | Switch selected as the reference point for STP calculations. |
| Root Port | Best port on a non-root switch toward the root bridge. |
| Designated Port | Forwarding port selected for a network segment. |
| Alternate Port | Backup path that does not forward while it would create a loop. |
| Blocking State | Classic STP state where a port does not forward data frames. |
| Forwarding State | State where a port forwards data frames and learns MAC addresses. |
| Topology Change | STP event indicating the Layer 2 topology changed. |
| PortFast | Cisco feature that lets endpoint access ports move to forwarding quickly. |
| BPDU Guard | Feature that disables a protected port if it receives a BPDU. |
| MAC Flapping | Same MAC address repeatedly learned on different ports. |
| RSTP | Rapid Spanning Tree Protocol, faster STP version. |
| PVST+ | Cisco per-VLAN spanning-tree implementation. |
| Rapid PVST+ | Cisco rapid per-VLAN spanning-tree implementation. |

## 17. COMPARISON TABLES

### 17.1 Redundancy Without STP vs Redundancy With STP

| Feature | Without STP | With STP |
|---|---|---|
| Redundant Links | Dangerous | Controlled |
| Loop Prevention | None | Yes |
| Broadcast Storm Risk | High | Reduced |
| Backup Path | Active and loop-prone | Available when needed |
| Enterprise Suitability | Poor | Standard Layer 2 protection |

### 17.2 Root Port vs Designated Port vs Alternate Port

| Port Role | Main Purpose | Forwarding? |
|---|---|---|
| Root Port | Best path to root bridge | Yes |
| Designated Port | Best port for a segment | Yes |
| Alternate Port | Backup loop-prevention path | No, unless topology changes |

### 17.3 Classic STP States

| State | Learns MACs? | Forwards Frames? | Purpose |
|---|---|---|---|
| Blocking | No | No | Prevents loops |
| Listening | No | No | Prepares topology participation |
| Learning | Yes | No | Builds MAC table before forwarding |
| Forwarding | Yes | Yes | Normal data forwarding |
| Disabled | No | No | Administratively or operationally down |

### 17.4 STP Variants

| Variant | Meaning | Main Benefit |
|---|---|---|
| STP | Original 802.1D | Loop prevention |
| RSTP | Rapid STP | Faster convergence |
| PVST+ | Per-VLAN STP | Separate STP per VLAN |
| Rapid PVST+ | Rapid per-VLAN STP | Faster per-VLAN convergence |
| MST | Multiple Spanning Tree | Scalable VLAN-to-instance mapping |

### 17.5 PortFast and BPDU Guard

| Feature | Purpose | Where Used |
|---|---|---|
| PortFast | Moves endpoint port to forwarding quickly | Access ports to end devices |
| BPDU Guard | Shuts protected port if BPDU is received | PortFast access ports |

## 18. REAL-WORLD EXAMPLE / ANALOGY

Think of STP like a traffic controller in a city with multiple roads between the same places. Redundant roads are useful because they provide backup routes. However, if every road is open in every direction without rules, traffic can circle endlessly and cause gridlock.

STP keeps some redundant paths available but logically closed until needed. If the main road fails, STP can open the backup route. The goal is not to remove redundancy; the goal is to control it.

## 19. QUICK-RECAP CHEAT SHEET

- STP prevents Layer 2 loops.
- Ethernet frames do not have a TTL.
- Redundant Layer 2 links can create loops.
- Broadcast storms can occur when broadcasts loop.
- MAC flapping happens when the same MAC is learned on different ports repeatedly.
- BPDUs are STP messages exchanged between switches.
- The root bridge is the reference point for STP.
- Lowest Bridge ID becomes root bridge.
- Bridge ID includes bridge priority and MAC address.
- Lower priority is better.
- If priorities tie, lower MAC address wins.
- Root port is the best port toward the root bridge.
- Designated port forwards for a network segment.
- Alternate or blocking port prevents loops.
- Classic STP states include blocking, listening, learning, forwarding, and disabled.
- RSTP uses discarding, learning, and forwarding.
- PortFast is for endpoint access ports.
- BPDU Guard protects PortFast ports from unexpected BPDUs.
- `show spanning-tree` verifies STP behavior.
- Plan the root bridge intentionally.

## 20. REVIEW QUESTIONS

1. What does STP stand for?
2. What problem does STP solve?
3. Why are Layer 2 loops dangerous?
4. Why can Ethernet frames loop indefinitely?
5. What is a broadcast storm?
6. What is MAC flapping?
7. What does BPDU mean?
8. What information do switches exchange using BPDUs?
9. What is the root bridge?
10. How is the root bridge elected?
11. What two main values are part of the Bridge ID?
12. If bridge priorities tie, what decides the root bridge?
13. What is a root port?
14. What is a designated port?
15. What is an alternate or non-designated port?
16. List the classic STP port states.
17. What is PortFast used for?
18. Why should PortFast not be used on switch-to-switch links?
19. What does BPDU Guard do?
20. Which Cisco command verifies STP information?

## 21. SUGGESTED ANSWER GUIDE

1. Spanning Tree Protocol.
2. STP prevents Layer 2 switching loops while allowing redundant physical links.
3. They can cause broadcast storms, MAC flapping, duplicate frames, high CPU, and network outages.
4. Ethernet frames do not have a TTL or hop limit.
5. A broadcast storm is excessive broadcast traffic, often caused by looping broadcasts.
6. MAC flapping is when the same MAC address is learned on different switch ports repeatedly.
7. Bridge Protocol Data Unit.
8. Root bridge ID, sender bridge ID, path cost, port information, and timers.
9. The root bridge is the central reference switch for STP calculations.
10. The switch with the lowest Bridge ID becomes the root bridge.
11. Bridge priority and MAC address.
12. The lower MAC address wins.
13. The root port is the best port on a non-root switch toward the root bridge.
14. A designated port is the forwarding port selected for a network segment.
15. It is a backup port that does not forward while it would create a loop.
16. Blocking, listening, learning, forwarding, and disabled.
17. PortFast lets endpoint access ports move to forwarding quickly.
18. It can allow a loop to form before STP protects the topology.
19. BPDU Guard disables a protected port if it receives a BPDU.
20. `show spanning-tree`.
