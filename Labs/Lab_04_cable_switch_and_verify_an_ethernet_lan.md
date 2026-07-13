# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 4

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: CABLE, SWITCH, AND VERIFY AN ETHERNET LAN

## Aligned Lessons

This lab aligns with Lesson 7, Cabling and Physical Media, Lesson 8, Ethernet Fundamentals, and Lesson 9, Enterprise Switching Fundamentals.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will build an Ethernet LAN, observe switch MAC learning, and verify port status.

## Important Why

This lab matters because most network faults still begin at Layer 1 or Layer 2. Students must know how Ethernet cabling, switch ports, MAC learning, forwarding, flooding, and filtering appear during normal operation.

## Important How

Students finish this lab by cabling devices, verifying switch interfaces, generating traffic, checking the MAC address table, and explaining how the switch learned each MAC address.

## Scenario

A small office has four desktop computers connected to one access switch. The technician must verify physical connectivity and switch learning.

## Required Devices

| Device | Quantity |
|---|---:|
| Cisco 2960 switch | 1 |
| PCs | 4 |
| Copper straight-through cables | 4 |

## Addressing Table

| Device | IP Address | Subnet Mask |
|---|---|---|
| PC1 | 192.168.20.11 | 255.255.255.0 |
| PC2 | 192.168.20.12 | 255.255.255.0 |
| PC3 | 192.168.20.13 | 255.255.255.0 |
| PC4 | 192.168.20.14 | 255.255.255.0 |

## Step-by-Step Tasks

1. Place one 2960 switch and four PCs in Packet Tracer.
2. Connect each PC to the switch using copper straight-through cables.
3. Assign the IP addresses from the addressing table.
4. Open the switch CLI.
5. Enter privileged EXEC mode with `enable`.
6. Run `show interfaces status`.
7. Run `show mac address-table`.
8. Ping PC2 from PC1.
9. Run `show mac address-table` again.
10. Identify which MAC addresses were learned on which switch ports.
11. Disconnect PC4 from its cable.
12. Run `show interfaces status` again.
13. Reconnect PC4 and wait for the port to come up.

## Verification

The switch should learn MAC addresses dynamically after traffic is sent. Ports connected to active PCs should show an up or connected state.

## Student Deliverable

Submit the final MAC address table and explain the difference between a switch forwarding, flooding, and filtering a frame.

---

