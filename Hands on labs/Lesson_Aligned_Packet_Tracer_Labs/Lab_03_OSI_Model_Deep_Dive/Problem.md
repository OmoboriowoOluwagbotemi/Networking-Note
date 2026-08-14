# Lab 03 - OSI Layer Evidence in Packet Tracer Simulation Mode - Problem

## Assignment Scenario

A helpdesk trainee must prove which OSI layers are involved when a PC opens a web page from a local server. Students build a small network, generate HTTP traffic, and inspect PDUs in Simulation Mode.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PC1 and WEB1 connect to SW1.

## Devices Required

1 switch, 1 PC, 1 server

## Addressing Requirement

PC1 192.168.40.10/24, WEB1 192.168.40.20/24. No gateway required.

## Student Tasks

1. Place one 2960 switch, one PC, and one server.
2. Connect PC1 and WEB1 to SW1 using straight-through cables.
3. Configure PC1 IP address 192.168.40.10 mask 255.255.255.0.
4. Configure WEB1 IP address 192.168.40.20 mask 255.255.255.0.
5. Click WEB1, open Services, open HTTP, and turn HTTP On.
6. Switch Packet Tracer from Realtime to Simulation.
7. On PC1, open Web Browser and browse to http://192.168.40.20.
8. Click the captured PDU and observe Layer 7 HTTP, Layer 4 TCP, Layer 3 IP, Layer 2 Ethernet, and Layer 1 movement.
9. Record one example of evidence for each OSI layer from Layer 7 down to Layer 1.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
