# CarePoint IPv4 Addressing Repair - Problem
## Assignment Scenario

A support technician must configure PCs correctly and identify when a host is in the wrong network or has an APIPA-style address.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PCs connect to SW1. SW1 connects to R1.

## Devices Required

1 router, 1 switch, 3 PCs

## Addressing Requirement

LAN 192.168.110.0/24 gateway 192.168.110.1. PC1 .10, PC2 .11, PC3 intentionally wrong first.

## Student Tasks

1. Build R1--SW1--three PCs.
2. Configure R1 LAN gateway.
3. Configure PC1 and PC2 correctly.
4. Configure PC3 first as 169.254.10.5/16 and test failure.
5. Change PC3 to 192.168.111.12/24 and test failure due to wrong subnet.
6. Correct PC3 to 192.168.110.12/24 gateway 192.168.110.1.
7. Record how IP address, subnet mask, and default gateway affect connectivity.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.

