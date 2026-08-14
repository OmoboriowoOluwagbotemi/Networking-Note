# Villa University Network Design Problem

## Source

This problem is based on the uploaded PDF titled `Villa University.pdf`.

## Assignment Title

Designing a University Network Using LANs, VLANs, Inter-VLAN Routing, Router-on-a-Stick, and Campus Area Network.

## Scenario

Villa University is expanding its campus and requires a secure and scalable network infrastructure connecting six buildings through a Campus Area Network, also called a CAN.

The university management wants each department to have its own VLAN for security and traffic isolation. Departments must still be able to communicate with one another through inter-VLAN routing implemented using Router-on-a-Stick.

You are acting as the Network Engineer. Your task is to design and configure the network in Cisco Packet Tracer.

## University Buildings

| Building | Building Name | Departments |
|---|---|---|
| Building A | Administration Block | Registry, Finance, Human Resources |
| Building B | Faculty of Science | Computer Science, Biology, Chemistry |
| Building C | Faculty of Engineering | Electrical Engineering, Mechanical Engineering, Civil Engineering |
| Building D | Library | Staff, Students |
| Building E | ICT Centre | Network Operations, Server Room |
| Building F | Student Affairs | Admissions, Hostel Management |

## Network Requirement 1: Campus Area Network

All six buildings must be connected together through a central Core Switch located inside the ICT Centre.

## Network Requirement 2: VLANs

Create the following VLANs:

| VLAN ID | Department | Network Address |
|---:|---|---|
| 10 | Registry | 192.168.10.0/24 |
| 20 | Finance | 192.168.20.0/24 |
| 30 | HR | 192.168.30.0/24 |
| 40 | Computer Science | 192.168.40.0/24 |
| 50 | Biology | 192.168.50.0/24 |
| 60 | Chemistry | 192.168.60.0/24 |
| 70 | Electrical Engineering | 192.168.70.0/24 |
| 80 | Mechanical Engineering | 192.168.80.0/24 |
| 90 | Civil Engineering | 192.168.90.0/24 |
| 100 | Library Staff | 192.168.100.0/24 |
| 110 | Library Students | 192.168.110.0/24 |
| 120 | Network Operations | 192.168.120.0/24 |
| 130 | Server Room | 192.168.130.0/24 |
| 140 | Admissions | 192.168.140.0/24 |
| 150 | Hostel Management | 192.168.150.0/24 |

## Network Requirement 3: Devices

### Router

| Device Type | Quantity |
|---|---:|
| Cisco Router | 1 |

### Switches

| Device Type | Quantity |
|---|---:|
| Core Switch | 1 |
| Access Switches | 6 |

### End Devices

Each department must have a minimum of 5 PCs.

| Department Count | PCs Per Department | Total PCs |
|---:|---:|---:|
| 15 | 5 | 75 |

## Required Deliverables

Students should submit:

1. Cisco Packet Tracer file named `Villa_University_Network.pkt`.
2. Proper physical and logical labeling.
3. Screenshots of VLAN configuration using `show vlan brief`.
4. Screenshots of trunk configuration using `show interfaces trunk`.
5. Screenshots of router subinterfaces using `show ip interface brief`.
6. Screenshots of successful ping tests.

## Main Technical Topics Tested

This assignment tests campus network design, VLAN creation, access-port assignment, trunking, Router-on-a-Stick, inter-VLAN routing, IP addressing, network labeling, verification commands, and basic end-to-end testing.
