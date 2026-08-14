# Lab 16 - Static Routes, Default Routes, and Floating Backup Route - Problem

## Assignment Scenario

A branch office must reach headquarters through a primary link and keep a backup route ready. Students configure static routes, default routes, and a floating static route.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

Branch LAN--R1--R2--HQ LAN, with optional backup R1--R3--R2 path.

## Devices Required

3 routers, 2 switches, 2 PCs

## Addressing Requirement

Branch LAN 192.168.160.0/24, R1-R2 10.0.12.0/30, R1-R3 10.0.13.0/30, R3-R2 10.0.23.0/30, HQ LAN 192.168.170.0/24.

## Student Tasks

1. Build the routers and LANs.
2. Configure all router interfaces.
3. Configure PC1 in Branch LAN and PC2 in HQ LAN.
4. Add static routes across the primary path.
5. Add a default route on R1 toward R2 if R2 represents the upstream router.
6. Add a floating static route using a higher administrative distance through R3.
7. Shut the primary interface and observe route change.
8. Restore the primary interface and confirm normal path returns.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.
