# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 14

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - DESIGN A SECURE AND RESILIENT BRANCH NETWORK

## Aligned Lessons

This lab aligns with Lesson 23, VPNs and Remote Access Security, and Lesson 24, Power and Resilience.

## Main Tool

Cisco Packet Tracer, with a written resilience worksheet.

## Lab Goal

Students will design a branch network with secure remote connectivity concepts, redundancy awareness, and power-resilience planning.

## Important Why

This lab matters because real branches need both secure communication and operational resilience. A branch router, switch, AP, and WAN link are only useful if they remain secure and powered during business disruption.

## Important How

Students finish this lab by building the HQ and branch topology, documenting VPN requirements, testing branch-to-HQ reachability, and completing a branch power-resilience worksheet.

## Scenario

FEMTECT has a branch office that must connect securely to headquarters. The branch also experiences unstable power, so the network design must include backup power planning and business continuity thinking.

## Step-by-Step Packet Tracer Tasks

1. Build a headquarters LAN with one router, one switch, one server, and one PC.
2. Build a branch LAN with one router, one switch, and two PCs.
3. Connect the HQ router and branch router through an ISP router or WAN cloud.
4. Configure IP addressing on both LANs.
5. Configure routing so HQ and branch can communicate.
6. Label the WAN path as an untrusted network.
7. Add notes in Packet Tracer showing that VPN encryption would protect branch-to-HQ traffic.
8. If Packet Tracer VPN support is available in the selected devices, configure a basic site-to-site VPN.
9. If VPN configuration is not available, document the VPN parameters that would be required: peer IP, interesting traffic, encryption, authentication, and tunnel endpoints.
10. Test branch PC connectivity to the HQ server.

## Step-by-Step Resilience Worksheet

1. List all network devices in the branch.
2. Estimate the wattage for each device.
3. Add the total wattage.
4. Add 25 percent headroom.
5. Decide which devices are critical during power failure.
6. Choose a UPS runtime target, such as 30 minutes or 1 hour.
7. Document what should stay on during outage: router, switch, AP, modem, and one admin workstation if needed.
8. Write a startup and shutdown order.
9. Write one business continuity risk and one mitigation.

## Student Deliverable

Submit the branch topology, VPN design notes, power worksheet, and one paragraph explaining why network security and power resilience must be planned together.

---

