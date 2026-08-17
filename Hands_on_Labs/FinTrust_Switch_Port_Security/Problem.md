# FinTrust Switch Port Security - Problem

## Assignment Scenario

A finance office wants each desk port protected so unknown devices cannot easily connect. Students configure access ports and basic port security.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PC1 and PC2 connect to SW1. Later, replace PC2 with RoguePC on the same port.

## Devices Required

1 switch, 2 authorized PCs, 1 unauthorized PC for testing

## Addressing Requirement

PC1 192.168.100.10/24, PC2 192.168.100.11/24, RoguePC 192.168.100.99/24.

## Student Tasks

1. Build SW1 with PC1 on Fa0/1 and PC2 on Fa0/2.
2. Configure PC IP addresses.
3. Configure Fa0/1 and Fa0/2 as access ports.
4. Enable port security with maximum 1 MAC address on Fa0/2.
5. Ping PC1 to PC2 to learn the secure MAC.
6. Disconnect PC2 and connect RoguePC to Fa0/2.
7. Ping from RoguePC and observe the port-security violation.
8. Recover the port if it becomes err-disabled.

## Required Deliverables

1. A saved Packet Tracer file named after the case-study name.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.



