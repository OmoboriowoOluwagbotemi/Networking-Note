# Northstar Service Port Testing - Problem
## Assignment Scenario

A company server hosts web, DNS, and file-transfer services. Students enable services, test ports, and identify which application uses which traffic type.

You are acting as the network technician or junior network engineer assigned to complete this Packet Tracer task. Your job is to build the required topology, apply the addressing plan, configure the Cisco devices where required, test the network, and prove that the design works.

## Business or Technical Requirement

PC1 and SRV1 connect to SW1.

## Devices Required

1 switch, 1 PC, 1 server

## Addressing Requirement

PC1 192.168.70.10/24 DNS 192.168.70.20. SRV1 192.168.70.20/24.

## Student Tasks

1. Build PC1--SW1--SRV1.
2. Configure SRV1 IP 192.168.70.20/24.
3. On SRV1 Services, enable HTTP, HTTPS if available, DNS, and FTP.
4. Create DNS A records for www.company.local and ftp.company.local pointing to 192.168.70.20.
5. Configure PC1 with IP 192.168.70.10/24 and DNS 192.168.70.20.
6. From PC1 browser, open http://www.company.local.
7. From PC1 Command Prompt, test DNS using nslookup www.company.local.
8. Open Simulation Mode and observe DNS, TCP, HTTP, and FTP traffic.

## Required Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Main Skills Tested

This assignment tests whether the student can read a scenario, build a Packet Tracer topology, apply correct addressing, configure Cisco devices, verify connectivity, troubleshoot common faults, and document the final result clearly.

