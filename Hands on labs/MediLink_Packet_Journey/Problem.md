# MediLink Packet Journey to a Remote Server - Problem
## Assignment Scenario

A clinic workstation must reach a server on a different network. Students trace the packet journey through a router and explain how frames change while IP packets move toward the destination.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PC1--SW1--R1--R2--SW2--WEB1

## Devices Required

2 routers, 2 switches, 1 PC, 1 server

## Addressing Requirement

LAN 192.168.50.0/24, WAN 10.10.10.0/30, Server LAN 172.16.50.0/24.

## Student Tasks

1. Build the topology PC1 to SW1, SW1 to R1, R1 to R2, R2 to SW2, SW2 to WEB1.
2. Configure PC1 as 192.168.50.10/24 gateway 192.168.50.1.
3. Configure WEB1 as 172.16.50.10/24 gateway 172.16.50.1 and enable HTTP.
4. Configure R1 and R2 using the commands below.
5. Use Simulation Mode to send a ping from PC1 to WEB1.
6. Inspect the PDU at each hop and record source and destination MAC changes.
7. Confirm Layer 3 source and destination IP addresses stay focused on PC1 and WEB1.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.

