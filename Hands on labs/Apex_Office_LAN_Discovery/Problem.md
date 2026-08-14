# Apex Office LAN Discovery and Failure Testing - Problem
## Assignment Scenario

Femtect Support has been asked to check a small office where four staff computers should communicate through one switch. Students will build the LAN, assign IP addresses, prove that the network works, then intentionally create simple faults and diagnose them.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PC1, PC2, PC3, and PC4 connect to SW1.

## Devices Required

1 Cisco 2960 switch, 4 PCs

## Addressing Requirement

PC1 192.168.17.10/24, PC2 192.168.17.11/24, PC3 192.168.17.12/24, PC4 192.168.17.13/24. No default gateway is required because this is one LAN.

## Student Tasks

1. Open Packet Tracer and place one 2960 switch in the center of the workspace.
2. Place four PCs below the switch and rename them PC1, PC2, PC3, and PC4.
3. Use copper straight-through cables from each PC FastEthernet0 port to switch ports Fa0/1 through Fa0/4.
4. Click each PC, open Desktop, open IP Configuration, and enter the assigned IP address and subnet mask 255.255.255.0.
5. Open PC1 Desktop, Command Prompt, and run ping tests to PC2, PC3, and PC4.
6. Create Fault 1 by unplugging PC3 cable, then ping PC3 from PC1 and record the failure.
7. Reconnect PC3, then create Fault 2 by changing PC4 IP address to 192.168.18.13 and test again.
8. Restore PC4 to 192.168.17.13 and prove all pings work again.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.

