# SwiftMart RIP and NAT/PAT - Problem

## Assignment Scenario

A small office has multiple internal networks and one public internet link. Students configure RIP internally and PAT so many users can share one public IP address.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

Inside LANs connect through R1 and R2. R2 connects to an Internet server network.

## Devices Required

2 routers, 2 switches, 2 PCs, 1 server

## Addressing Requirement

LAN1 192.168.180.0/24, LAN2 192.168.181.0/24, R1-R2 10.0.0.0/30, Internet server 203.0.113.10/24 through R2 public side 203.0.113.1.

## Student Tasks

1. Build R1, R2, two LANs, and one outside server.
2. Configure interfaces and PC/server addresses.
3. Enable RIPv2 between R1 and R2 for internal route learning.
4. Configure PAT on R2 using its outside interface.
5. Ping from inside PCs to the outside server.
6. Use show ip nat translations after traffic is generated.
7. Explain why many private hosts can share one outside interface address.

## Required Deliverables

1. A saved Packet Tracer file named after the case-study name.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.




