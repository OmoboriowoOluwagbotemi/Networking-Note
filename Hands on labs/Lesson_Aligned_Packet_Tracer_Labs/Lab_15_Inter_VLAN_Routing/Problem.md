# Lab 15 - Inter-VLAN Routing by Direct Router Interfaces, Router-on-a-Stick, and Layer 3 Switching - Problem

## Assignment Scenario

Management now wants controlled communication between Guests, Parents, Teachers, and Students. Students first learn the direct-cable method, then compare it with router-on-a-stick.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

Method A: four switch access ports connect to four router interfaces, one per VLAN. Method B: one trunk connects switch to router subinterfaces.

Accuracy note for Packet Tracer: the direct-router-interface method requires a router model or added module with enough Ethernet interfaces for the VLANs being tested. If your selected router has only two or three Ethernet interfaces, test two or three VLANs with the direct method first, then complete all four VLANs with the router-on-a-stick method.

## Devices Required

1 router, 1 switch, 4 PCs minimum

## Addressing Requirement

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN30 192.168.30.0/24 gateway .1, VLAN40 192.168.40.0/24 gateway .1.

## Student Tasks

1. Start with the Lab 13 VLAN switch.
2. For the direct-router-interface method, connect one router interface to an access port in VLAN10, another to VLAN20, another to VLAN30, and another to VLAN40.
3. Configure the switch ports connected to the router as access ports in their matching VLANs.
4. Configure each router physical interface with the gateway IP for that VLAN.
5. Set each PC default gateway to its VLAN router interface.
6. Ping between VLANs and confirm success.
7. Then rebuild or duplicate the topology for router-on-a-stick using one trunk link and router subinterfaces.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
