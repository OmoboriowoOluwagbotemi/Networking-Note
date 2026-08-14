# Lab 13 - School VLAN Segmentation for Guests, Parents, Teachers, and Students - Problem

## Assignment Scenario

A school has one switch but four user groups must be separated: Guests, Parents, Teachers, and Students. Students build the topology shown in the supplied VLAN screenshots and prove that VLANs isolate broadcasts.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

One central switch connects to eight PCs grouped into four colored departments, two PCs per department.

## Devices Required

1 switch, 8 PCs

## Addressing Requirement

Guests VLAN10 192.168.10.10-11/24, Parents VLAN20 192.168.20.12-13/24, Teachers VLAN30 192.168.30.14-15/24, Students VLAN40 192.168.40.16-17/24.

## Student Tasks

1. Place one 2960 switch and eight PCs.
2. Use drawing rectangles or notes to group PCs into Guests, Parents, Teachers, and Students.
3. Connect PC1-PC8 to switch ports Fa0/1 through Fa0/8.
4. Create VLANs 10, 20, 30, and 40.
5. Assign two ports to each VLAN.
6. Configure each PC with the correct IP address from its VLAN subnet.
7. Ping between two PCs in the same VLAN and confirm success.
8. Ping from a Guest PC to a Teacher PC and confirm failure because no inter-VLAN routing exists yet.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
