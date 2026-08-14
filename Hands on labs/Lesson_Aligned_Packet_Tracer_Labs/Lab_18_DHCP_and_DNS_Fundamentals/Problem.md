# Lab 18 - DHCP, DNS, and IP Helper for Two VLANs - Problem

## Assignment Scenario

A company wants automatic addressing and name resolution for two departments. The DHCP/DNS server is in the server VLAN, so router relay is required.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

Router-on-a-stick connects VLAN10 Users, VLAN20 Admin, and VLAN99 Servers.

## Devices Required

1 router, 1 switch, 1 server, 4 PCs

## Addressing Requirement

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN99 192.168.99.0/24 gateway .1, Server 192.168.99.10.

## Student Tasks

1. Build router, switch, server, and four PCs.
2. Create VLANs 10, 20, and 99 on the switch.
3. Configure access ports and one trunk to the router.
4. Configure router subinterfaces and add ip helper-address 192.168.99.10 under VLAN10 and VLAN20 subinterfaces.
5. Configure DHCP pools on the server for VLAN10 and VLAN20.
6. Configure DNS service on the server with intranet.local pointing to 192.168.99.10.
7. Set PCs to DHCP and verify they receive correct addresses.
8. Browse or ping intranet.local from a client.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
