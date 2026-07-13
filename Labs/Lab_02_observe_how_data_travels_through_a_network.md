# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 2

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: OBSERVE HOW DATA TRAVELS THROUGH A NETWORK

## Aligned Lessons

This lab aligns with Lesson 3, How Data Travels Through a Network, Lesson 4, OSI Model Deep Dive, and Lesson 5, TCP/IP Protocol Suite.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will observe ARP, ICMP, source and destination addressing, and packet movement using Packet Tracer simulation mode.

## Important Why

This lab matters because students must see that network communication is not magic. ARP, ICMP, MAC addresses, IP addresses, encapsulation, and decapsulation all work together each time a simple ping succeeds.

## Important How

Students finish this lab by switching to Simulation mode, filtering ARP and ICMP, stepping through packets, and recording what changes at Layer 2 and Layer 3.

## Scenario

The training-room LAN is working, but students must now prove what happens when one PC communicates with another PC.

## Required Devices

Use the completed topology from Lab 1.

## Step-by-Step Tasks

1. Open the Lab 1 topology.
2. Confirm PC1, PC2, and PC3 can ping each other.
3. Switch Packet Tracer from Real-Time mode to Simulation mode.
4. Click Edit Filters.
5. Clear all filters.
6. Select only ARP and ICMP.
7. Open PC1 Command Prompt.
8. Run `arp -a` to check the ARP table.
9. Run `ping 192.168.10.12`.
10. Click Capture/Forward one step at a time.
11. Observe the ARP request leaving PC1.
12. Observe the ARP reply returning from PC2.
13. Observe the ICMP echo request and echo reply.
14. Click the packet envelope and inspect Layer 2 and Layer 3 information.
15. Repeat the test from PC1 to PC3.

## Verification

Students should observe that ARP discovers the MAC address first, then ICMP carries the ping test. They should also observe that the IP address identifies the host logically, while the MAC address is used for local Ethernet delivery.

## Troubleshooting Checklist

If no ARP appears, clear the ARP cache by powering the PC off and on in Packet Tracer, or ping a host that has not recently communicated with the source PC.

## Student Deliverable

Submit a table showing the source MAC, destination MAC, source IP, and destination IP for one ICMP packet.

---

