# Lab 11 - Subnetting a Branch into Three Departments - Problem

## Assignment Scenario

A branch received 192.168.120.0/24 and must divide it into Admin, Sales, and Support networks. Students calculate subnets, assign gateways, and verify routing.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

R1 connects separately to Admin-SW, Sales-SW, and Support-SW.

## Devices Required

1 router, 3 switches, 6 PCs

## Addressing Requirement

Admin 192.168.120.0/26 gateway .1, Sales 192.168.120.64/26 gateway .65, Support 192.168.120.128/26 gateway .129.

## Student Tasks

1. Calculate each /26 network address, first usable address, last usable address, and broadcast address.
2. Build R1 with three switch connections.
3. Place two PCs per department.
4. Configure each router interface as the gateway for one subnet.
5. Assign PC addresses from the correct subnet.
6. Ping from Admin PC to Sales PC and Support PC.
7. Use failed tests to identify wrong masks or gateways.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
