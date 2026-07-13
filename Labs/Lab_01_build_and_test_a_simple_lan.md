# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 1

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: BUILD AND TEST A SIMPLE LAN

## Aligned Lessons

This lab aligns with Lesson 1, How Networks Work and Why They Fail, and Lesson 2, Network Devices and Appliances.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will build a small LAN using end devices, a switch, and correct IP addressing. They will verify basic connectivity using `ping` and understand the role of each device.

## Important Why

This lab matters because every advanced network begins with the same foundation: end devices must be cabled correctly, addressed correctly, and tested correctly. Before students configure VLANs, routers, NAT, or security, they must understand what a working local network looks like.

## Important How

Students finish this lab by building the topology, assigning IP settings, testing with ping, and explaining why same-subnet devices can communicate without a default gateway.

## Scenario

A small training room has three computers that need to communicate with one another through a switch. There is no router yet because all devices are on the same local network.

## Required Devices

| Device | Quantity |
|---|---:|
| Cisco 2960 switch | 1 |
| PCs | 3 |
| Copper straight-through cables | 3 |

## Addressing Table

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| PC1 | FastEthernet0 | 192.168.10.11 | 255.255.255.0 | Not required |
| PC2 | FastEthernet0 | 192.168.10.12 | 255.255.255.0 | Not required |
| PC3 | FastEthernet0 | 192.168.10.13 | 255.255.255.0 | Not required |

## Step-by-Step Tasks

1. Open Cisco Packet Tracer.
2. Drag one 2960 switch into the workspace.
3. Drag three PCs into the workspace.
4. Rename the PCs as PC1, PC2, and PC3.
5. Use copper straight-through cables to connect PC1 to switch port Fa0/1, PC2 to Fa0/2, and PC3 to Fa0/3.
6. Click PC1, open Desktop, then IP Configuration.
7. Enter IP address `192.168.10.11` and subnet mask `255.255.255.0`.
8. Repeat the same process for PC2 and PC3 using the addressing table.
9. Open PC1 Command Prompt.
10. Run `ping 192.168.10.12`.
11. Run `ping 192.168.10.13`.
12. Open PC2 Command Prompt and run `ping 192.168.10.13`.
13. Wait for switch port lights to turn green if the first ping fails.

## Verification

| Test | Expected Result |
|---|---|
| PC1 pings PC2 | Success |
| PC1 pings PC3 | Success |
| PC2 pings PC3 | Success |
| All switch links | Green/up |

## Troubleshooting Checklist

If the ping fails, confirm the cable type, port status, IP address, subnet mask, and whether all PCs are in the same subnet.

## Student Deliverable

Submit a screenshot of the topology and a short note explaining why a default gateway is not required when all devices are in the same LAN.

---

