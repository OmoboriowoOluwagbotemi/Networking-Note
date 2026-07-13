# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 6

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - SEGMENT A SMALL OFFICE USING VLANS AND TRUNKS

## Aligned Lessons

This lab aligns with Lesson 13, VLAN Fundamentals and Design, and Lesson 14, VLAN Configuration and Trunking.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will create VLANs, assign access ports, configure a trunk between switches, and verify VLAN separation.

## Important Why

This lab matters because enterprise networks are not built as one flat LAN. VLANs allow an organization to separate departments, reduce broadcast scope, and apply security policies in a controlled way.

## Important How

Students finish this lab by creating VLANs on both switches, assigning access ports, configuring trunks, testing same-VLAN communication across switches, and proving different VLANs are separated.

## Scenario

FEMTECT has opened a small office with three groups: Admin, Sales, and Guest. The company does not want guest users sharing the same broadcast domain with staff devices. Two access switches are installed in different rooms, and VLANs must work across both switches.

## Required Devices

| Device | Quantity |
|---|---:|
| Cisco 2960 switches | 2 |
| PCs | 6 |
| Copper straight-through cables | 6 |
| Copper crossover or automatic cable | 1 |

## VLAN Plan

| VLAN | Name | Subnet |
|---:|---|---|
| 10 | ADMIN | 192.168.10.0/24 |
| 20 | SALES | 192.168.20.0/24 |
| 30 | GUEST | 192.168.30.0/24 |

## Step-by-Step Tasks

1. Place two switches named SW1 and SW2.
2. Place three PCs near SW1 and three PCs near SW2.
3. Connect SW1 Fa0/24 to SW2 Fa0/24.
4. Connect PCs to access ports Fa0/1 to Fa0/3 on each switch.
5. On SW1, enter configuration mode.
6. Create VLAN 10 with `vlan 10` and `name ADMIN`.
7. Create VLAN 20 with `vlan 20` and `name SALES`.
8. Create VLAN 30 with `vlan 30` and `name GUEST`.
9. Repeat the same VLAN creation on SW2.
10. On SW1, assign Fa0/1 to VLAN 10 using `switchport mode access` and `switchport access vlan 10`.
11. Assign Fa0/2 to VLAN 20.
12. Assign Fa0/3 to VLAN 30.
13. Repeat the same access-port assignments on SW2.
14. Configure SW1 Fa0/24 as a trunk using `switchport mode trunk`.
15. Configure SW2 Fa0/24 as a trunk using `switchport mode trunk`.
16. Configure IP addresses on PCs based on their VLAN subnet.
17. Ping between Admin PCs on different switches.
18. Ping between Sales PCs on different switches.
19. Ping between Guest PCs on different switches.
20. Ping from Admin to Sales and observe the failure.

## Verification Commands

```text
show vlan brief
show interfaces trunk
show mac address-table
```

## Expected Result

Devices in the same VLAN should communicate across the trunk. Devices in different VLANs should not communicate because inter-VLAN routing has not been configured yet.

## Student Deliverable

Submit the VLAN table, trunk verification, and one paragraph explaining why VLANs improve security and broadcast control.

---

