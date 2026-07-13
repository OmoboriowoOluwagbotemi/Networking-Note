# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 7

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - FIX LAYER 2 LOOPS AND INTER-VLAN CONNECTIVITY

## Aligned Lessons

This lab aligns with Lesson 15, Spanning Tree Protocol, and Lesson 16, Inter-VLAN Routing.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will observe STP behavior, configure router-on-a-stick, and troubleshoot inter-VLAN connectivity.

## Important Why

This lab matters because redundant Layer 2 links can protect a network or break it badly if loops are not controlled. Students also learn that VLAN separation requires Layer 3 gateways when different VLANs must communicate.

## Important How

Students finish this lab by identifying STP behavior, adding router subinterfaces, configuring 802.1Q encapsulation, setting PC gateways, and verifying inter-VLAN routing.

## Scenario

The office added a second link between switches for redundancy. The network also needs Admin, Sales, and Guest VLANs to reach their default gateways. Students must verify that STP prevents loops and then enable inter-VLAN routing.

## Required Devices

Use the Lab 6 topology and add one router.

## Router-on-a-Stick Gateway Plan

| VLAN | Gateway |
|---:|---|
| 10 | 192.168.10.1 |
| 20 | 192.168.20.1 |
| 30 | 192.168.30.1 |

## Step-by-Step Tasks

1. Open the Lab 6 topology.
2. Add a second link between SW1 and SW2 using Fa0/23 on both switches.
3. Run `show spanning-tree` on SW1.
4. Run `show spanning-tree` on SW2.
5. Identify the root bridge and blocked or alternate port.
6. Add one router and connect router G0/0 to SW1 Fa0/22.
7. Configure SW1 Fa0/22 as a trunk.
8. On the router, enter interface G0/0 and run `no shutdown`.
9. Create subinterface G0/0.10.
10. Configure `encapsulation dot1Q 10`.
11. Configure IP address `192.168.10.1 255.255.255.0`.
12. Create subinterface G0/0.20.
13. Configure `encapsulation dot1Q 20`.
14. Configure IP address `192.168.20.1 255.255.255.0`.
15. Create subinterface G0/0.30.
16. Configure `encapsulation dot1Q 30`.
17. Configure IP address `192.168.30.1 255.255.255.0`.
18. Configure each PC default gateway based on its VLAN.
19. Ping from an Admin PC to a Sales PC.
20. Ping from a Sales PC to a Guest PC.

## Cisco IOS Configuration Example

```text
interface g0/0
 no shutdown

interface g0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface g0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0

interface g0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
```

## Verification Commands

```text
show spanning-tree
show interfaces trunk
show ip interface brief
show running-config
```

## Student Deliverable

Submit STP root bridge evidence, router subinterface configuration, and successful inter-VLAN ping results.

---

