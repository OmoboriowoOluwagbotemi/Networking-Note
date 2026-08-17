# Villa University Network Design Solution

## Purpose of This Solution

This document gives a robust step-by-step solution for the Villa University Cisco Packet Tracer assignment. It explains what to build, why each part is needed, how to configure it, and how to verify that the network is working.

The design follows the assignment requirements:

- 6 university buildings.
- 1 central core switch in the ICT Centre.
- 6 access switches, one per building.
- 1 Cisco router for Router-on-a-Stick inter-VLAN routing.
- 15 VLANs, one per department.
- Minimum 5 PCs per department.
- 75 total PCs.

## Important Design Decision

The assignment requires Router-on-a-Stick. That means the router will use one physical interface connected to the core switch as a trunk. The router will then use subinterfaces, one subinterface per VLAN. Each router subinterface becomes the default gateway for that VLAN.

The core switch and access switches will operate at Layer 2. They will carry VLAN traffic across trunk links. The router will perform Layer 3 routing between VLANs.

## Packet Tracer Accuracy Note

The commands below are written for common Cisco Packet Tracer devices such as a 2911 router and 2960 switches. If your router interface names are different, first run `show ip interface brief` on the router and use the available Ethernet interface name in place of `gigabitEthernet0/0`.

On Cisco 2960 switches in Packet Tracer, do not use `switchport trunk encapsulation dot1q`. The 2960 uses 802.1Q trunking and usually does not accept that command.

## Topology Summary

| Device | Role | Suggested Name |
|---|---|---|
| Router | Inter-VLAN routing gateway | R1 |
| Core Switch | Campus aggregation switch in ICT Centre | CORE-SW |
| Access Switch 1 | Building A - Administration Block | SW-A-ADMIN |
| Access Switch 2 | Building B - Faculty of Science | SW-B-SCIENCE |
| Access Switch 3 | Building C - Faculty of Engineering | SW-C-ENGINEERING |
| Access Switch 4 | Building D - Library | SW-D-LIBRARY |
| Access Switch 5 | Building E - ICT Centre | SW-E-ICT |
| Access Switch 6 | Building F - Student Affairs | SW-F-STUDENT |

## Physical Connection Plan

| Link | From Device | From Port | To Device | To Port | Link Type |
|---|---|---|---|---|---|
| Router trunk | R1 | G0/0 | CORE-SW | Fa0/1 | Trunk |
| Building A uplink | CORE-SW | Fa0/2 | SW-A-ADMIN | Fa0/24 | Trunk |
| Building B uplink | CORE-SW | Fa0/3 | SW-B-SCIENCE | Fa0/24 | Trunk |
| Building C uplink | CORE-SW | Fa0/4 | SW-C-ENGINEERING | Fa0/24 | Trunk |
| Building D uplink | CORE-SW | Fa0/5 | SW-D-LIBRARY | Fa0/24 | Trunk |
| Building E uplink | CORE-SW | Fa0/6 | SW-E-ICT | Fa0/24 | Trunk |
| Building F uplink | CORE-SW | Fa0/7 | SW-F-STUDENT | Fa0/24 | Trunk |

## VLAN and Gateway Plan

Each VLAN uses the `.1` address as its default gateway on the router.

| VLAN | Department | Network | Default Gateway |
|---:|---|---|---|
| 10 | Registry | 192.168.10.0/24 | 192.168.10.1 |
| 20 | Finance | 192.168.20.0/24 | 192.168.20.1 |
| 30 | HR | 192.168.30.0/24 | 192.168.30.1 |
| 40 | Computer Science | 192.168.40.0/24 | 192.168.40.1 |
| 50 | Biology | 192.168.50.0/24 | 192.168.50.1 |
| 60 | Chemistry | 192.168.60.0/24 | 192.168.60.1 |
| 70 | Electrical Engineering | 192.168.70.0/24 | 192.168.70.1 |
| 80 | Mechanical Engineering | 192.168.80.0/24 | 192.168.80.1 |
| 90 | Civil Engineering | 192.168.90.0/24 | 192.168.90.1 |
| 100 | Library Staff | 192.168.100.0/24 | 192.168.100.1 |
| 110 | Library Students | 192.168.110.0/24 | 192.168.110.1 |
| 120 | Network Operations | 192.168.120.0/24 | 192.168.120.1 |
| 130 | Server Room | 192.168.130.0/24 | 192.168.130.1 |
| 140 | Admissions | 192.168.140.0/24 | 192.168.140.1 |
| 150 | Hostel Management | 192.168.150.0/24 | 192.168.150.1 |

## PC Addressing Pattern

Use `.11` to `.15` for the five PCs in each department.

| Department | PC Address Range | Gateway |
|---|---|---|
| Registry | 192.168.10.11 - 192.168.10.15 | 192.168.10.1 |
| Finance | 192.168.20.11 - 192.168.20.15 | 192.168.20.1 |
| HR | 192.168.30.11 - 192.168.30.15 | 192.168.30.1 |
| Computer Science | 192.168.40.11 - 192.168.40.15 | 192.168.40.1 |
| Biology | 192.168.50.11 - 192.168.50.15 | 192.168.50.1 |
| Chemistry | 192.168.60.11 - 192.168.60.15 | 192.168.60.1 |
| Electrical Engineering | 192.168.70.11 - 192.168.70.15 | 192.168.70.1 |
| Mechanical Engineering | 192.168.80.11 - 192.168.80.15 | 192.168.80.1 |
| Civil Engineering | 192.168.90.11 - 192.168.90.15 | 192.168.90.1 |
| Library Staff | 192.168.100.11 - 192.168.100.15 | 192.168.100.1 |
| Library Students | 192.168.110.11 - 192.168.110.15 | 192.168.110.1 |
| Network Operations | 192.168.120.11 - 192.168.120.15 | 192.168.120.1 |
| Server Room | 192.168.130.11 - 192.168.130.15 | 192.168.130.1 |
| Admissions | 192.168.140.11 - 192.168.140.15 | 192.168.140.1 |
| Hostel Management | 192.168.150.11 - 192.168.150.15 | 192.168.150.1 |

## Access Port Allocation Plan

Each department gets five access switch ports.

| Access Switch | Department | VLAN | PC Ports |
|---|---|---:|---|
| SW-A-ADMIN | Registry | 10 | Fa0/1 - Fa0/5 |
| SW-A-ADMIN | Finance | 20 | Fa0/6 - Fa0/10 |
| SW-A-ADMIN | HR | 30 | Fa0/11 - Fa0/15 |
| SW-B-SCIENCE | Computer Science | 40 | Fa0/1 - Fa0/5 |
| SW-B-SCIENCE | Biology | 50 | Fa0/6 - Fa0/10 |
| SW-B-SCIENCE | Chemistry | 60 | Fa0/11 - Fa0/15 |
| SW-C-ENGINEERING | Electrical Engineering | 70 | Fa0/1 - Fa0/5 |
| SW-C-ENGINEERING | Mechanical Engineering | 80 | Fa0/6 - Fa0/10 |
| SW-C-ENGINEERING | Civil Engineering | 90 | Fa0/11 - Fa0/15 |
| SW-D-LIBRARY | Library Staff | 100 | Fa0/1 - Fa0/5 |
| SW-D-LIBRARY | Library Students | 110 | Fa0/6 - Fa0/10 |
| SW-E-ICT | Network Operations | 120 | Fa0/1 - Fa0/5 |
| SW-E-ICT | Server Room | 130 | Fa0/6 - Fa0/10 |
| SW-F-STUDENT | Admissions | 140 | Fa0/1 - Fa0/5 |
| SW-F-STUDENT | Hostel Management | 150 | Fa0/6 - Fa0/10 |

---

# Part 1: Build the Topology in Cisco Packet Tracer

## Step 1: Open Packet Tracer

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file immediately as `Villa_University_Network.pkt`.

## Step 2: Add the Router

1. Click Network Devices.
2. Click Routers.
3. Drag one Cisco router into the workspace.
4. A 2911 router is suitable if available.
5. Click the router name.
6. Rename the router to `R1`.

## Step 3: Add the Core Switch

1. Click Network Devices.
2. Click Switches.
3. Drag one Cisco 2960 switch into the workspace.
4. Rename it `CORE-SW`.
5. Place it near the middle of the workspace because all buildings connect to it.

## Step 4: Add the Six Access Switches

1. Drag six Cisco 2960 switches into the workspace.
2. Rename them:
   - `SW-A-ADMIN`
   - `SW-B-SCIENCE`
   - `SW-C-ENGINEERING`
   - `SW-D-LIBRARY`
   - `SW-E-ICT`
   - `SW-F-STUDENT`
3. Place the switches around the core switch to represent the six buildings.

## Step 5: Add the PCs

1. Click End Devices.
2. Drag 75 PCs into the workspace.
3. Add 15 groups of 5 PCs.
4. Name the PCs clearly by department.

Recommended examples:

| Department | PC Names |
|---|---|
| Registry | REG-PC1 to REG-PC5 |
| Finance | FIN-PC1 to FIN-PC5 |
| HR | HR-PC1 to HR-PC5 |
| Computer Science | CS-PC1 to CS-PC5 |
| Biology | BIO-PC1 to BIO-PC5 |
| Chemistry | CHEM-PC1 to CHEM-PC5 |
| Electrical Engineering | EE-PC1 to EE-PC5 |
| Mechanical Engineering | ME-PC1 to ME-PC5 |
| Civil Engineering | CE-PC1 to CE-PC5 |
| Library Staff | LIBSTAFF-PC1 to LIBSTAFF-PC5 |
| Library Students | LIBSTUD-PC1 to LIBSTUD-PC5 |
| Network Operations | NETOPS-PC1 to NETOPS-PC5 |
| Server Room | SRV-PC1 to SRV-PC5 |
| Admissions | ADM-PC1 to ADM-PC5 |
| Hostel Management | HOSTEL-PC1 to HOSTEL-PC5 |

## Step 6: Cable the Core Links

Use copper straight-through cables unless Packet Tracer automatically selects the cable.

1. Connect R1 G0/0 to CORE-SW Fa0/1.
2. Connect CORE-SW Fa0/2 to SW-A-ADMIN Fa0/24.
3. Connect CORE-SW Fa0/3 to SW-B-SCIENCE Fa0/24.
4. Connect CORE-SW Fa0/4 to SW-C-ENGINEERING Fa0/24.
5. Connect CORE-SW Fa0/5 to SW-D-LIBRARY Fa0/24.
6. Connect CORE-SW Fa0/6 to SW-E-ICT Fa0/24.
7. Connect CORE-SW Fa0/7 to SW-F-STUDENT Fa0/24.

## Step 7: Cable PCs to Access Switches

Connect each department's five PCs to its assigned switch ports using the access port allocation plan.

Example for Building A:

1. Connect REG-PC1 to SW-A-ADMIN Fa0/1.
2. Connect REG-PC2 to SW-A-ADMIN Fa0/2.
3. Connect REG-PC3 to SW-A-ADMIN Fa0/3.
4. Connect REG-PC4 to SW-A-ADMIN Fa0/4.
5. Connect REG-PC5 to SW-A-ADMIN Fa0/5.
6. Connect FIN-PC1 to SW-A-ADMIN Fa0/6.
7. Continue until all Finance and HR PCs are connected.

Repeat the same pattern for all other buildings.

---

# Part 2: Configure VLANs on the Core Switch

## Why This Step Matters

The core switch must know all VLAN IDs because it receives trunk traffic from all access switches and sends trunk traffic to the router. If a VLAN is missing on the core switch, traffic for that VLAN may not pass correctly across the campus.

## How to Configure the Core Switch

1. Click `CORE-SW`.
2. Click CLI.
3. Press Enter.
4. If asked about the initial configuration dialog, type `no` and press Enter.
5. Copy and paste the command block below.

## CORE-SW VLAN Creation Commands

```text
enable
configure terminal
hostname CORE-SW
vlan 10
 name REGISTRY
exit
vlan 20
 name FINANCE
exit
vlan 30
 name HR
exit
vlan 40
 name COMPUTER_SCIENCE
exit
vlan 50
 name BIOLOGY
exit
vlan 60
 name CHEMISTRY
exit
vlan 70
 name ELECTRICAL_ENG
exit
vlan 80
 name MECHANICAL_ENG
exit
vlan 90
 name CIVIL_ENG
exit
vlan 100
 name LIBRARY_STAFF
exit
vlan 110
 name LIBRARY_STUDENTS
exit
vlan 120
 name NETWORK_OPERATIONS
exit
vlan 130
 name SERVER_ROOM
exit
vlan 140
 name ADMISSIONS
exit
vlan 150
 name HOSTEL_MANAGEMENT
exit
end
show vlan brief
```

## Expected Result

The output of `show vlan brief` should display VLANs 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, and 150.

---

# Part 3: Configure Core Switch Trunks

## Why This Step Matters

Trunk ports carry traffic for multiple VLANs over one physical link. The link from the core switch to the router must be a trunk because the router needs to receive traffic from all 15 VLANs. The links from the core switch to access switches must also be trunks because each building switch carries multiple department VLANs.

## CORE-SW Trunk Commands

```text
enable
configure terminal
interface fa0/1
 description TRUNK_TO_R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150
exit
interface fa0/2
 description TRUNK_TO_SW_A_ADMIN
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
exit
interface fa0/3
 description TRUNK_TO_SW_B_SCIENCE
 switchport mode trunk
 switchport trunk allowed vlan 40,50,60
exit
interface fa0/4
 description TRUNK_TO_SW_C_ENGINEERING
 switchport mode trunk
 switchport trunk allowed vlan 70,80,90
exit
interface fa0/5
 description TRUNK_TO_SW_D_LIBRARY
 switchport mode trunk
 switchport trunk allowed vlan 100,110
exit
interface fa0/6
 description TRUNK_TO_SW_E_ICT
 switchport mode trunk
 switchport trunk allowed vlan 120,130
exit
interface fa0/7
 description TRUNK_TO_SW_F_STUDENT
 switchport mode trunk
 switchport trunk allowed vlan 140,150
exit
end
show interfaces trunk
```

## Expected Result

The command `show interfaces trunk` should show Fa0/1 through Fa0/7 as trunk ports. Each trunk should list the allowed VLANs configured for that link.

---

# Part 4: Configure Access Switches

## Why This Step Matters

Access switches connect end-user PCs. A PC port should normally be an access port, not a trunk. An access port belongs to one VLAN, so the switch knows which department network the PC belongs to.

## Building A: SW-A-ADMIN

### What This Switch Carries

| Department | VLAN | Ports |
|---|---:|---|
| Registry | 10 | Fa0/1 - Fa0/5 |
| Finance | 20 | Fa0/6 - Fa0/10 |
| HR | 30 | Fa0/11 - Fa0/15 |
| Uplink to Core | Trunk | Fa0/24 |

### SW-A-ADMIN Commands

```text
enable
configure terminal
hostname SW-A-ADMIN
vlan 10
 name REGISTRY
exit
vlan 20
 name FINANCE
exit
vlan 30
 name HR
exit
interface range fa0/1 - 5
 description REGISTRY_PCS
 switchport mode access
 switchport access vlan 10
exit
interface range fa0/6 - 10
 description FINANCE_PCS
 switchport mode access
 switchport access vlan 20
exit
interface range fa0/11 - 15
 description HR_PCS
 switchport mode access
 switchport access vlan 30
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
end
show vlan brief
show interfaces trunk
```

## Building B: SW-B-SCIENCE

### SW-B-SCIENCE Commands

```text
enable
configure terminal
hostname SW-B-SCIENCE
vlan 40
 name COMPUTER_SCIENCE
exit
vlan 50
 name BIOLOGY
exit
vlan 60
 name CHEMISTRY
exit
interface range fa0/1 - 5
 description COMPUTER_SCIENCE_PCS
 switchport mode access
 switchport access vlan 40
exit
interface range fa0/6 - 10
 description BIOLOGY_PCS
 switchport mode access
 switchport access vlan 50
exit
interface range fa0/11 - 15
 description CHEMISTRY_PCS
 switchport mode access
 switchport access vlan 60
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 40,50,60
end
show vlan brief
show interfaces trunk
```

## Building C: SW-C-ENGINEERING

### SW-C-ENGINEERING Commands

```text
enable
configure terminal
hostname SW-C-ENGINEERING
vlan 70
 name ELECTRICAL_ENG
exit
vlan 80
 name MECHANICAL_ENG
exit
vlan 90
 name CIVIL_ENG
exit
interface range fa0/1 - 5
 description ELECTRICAL_ENG_PCS
 switchport mode access
 switchport access vlan 70
exit
interface range fa0/6 - 10
 description MECHANICAL_ENG_PCS
 switchport mode access
 switchport access vlan 80
exit
interface range fa0/11 - 15
 description CIVIL_ENG_PCS
 switchport mode access
 switchport access vlan 90
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 70,80,90
end
show vlan brief
show interfaces trunk
```

## Building D: SW-D-LIBRARY

### SW-D-LIBRARY Commands

```text
enable
configure terminal
hostname SW-D-LIBRARY
vlan 100
 name LIBRARY_STAFF
exit
vlan 110
 name LIBRARY_STUDENTS
exit
interface range fa0/1 - 5
 description LIBRARY_STAFF_PCS
 switchport mode access
 switchport access vlan 100
exit
interface range fa0/6 - 10
 description LIBRARY_STUDENTS_PCS
 switchport mode access
 switchport access vlan 110
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 100,110
end
show vlan brief
show interfaces trunk
```

## Building E: SW-E-ICT

### SW-E-ICT Commands

```text
enable
configure terminal
hostname SW-E-ICT
vlan 120
 name NETWORK_OPERATIONS
exit
vlan 130
 name SERVER_ROOM
exit
interface range fa0/1 - 5
 description NETWORK_OPERATIONS_PCS
 switchport mode access
 switchport access vlan 120
exit
interface range fa0/6 - 10
 description SERVER_ROOM_PCS
 switchport mode access
 switchport access vlan 130
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 120,130
end
show vlan brief
show interfaces trunk
```

## Building F: SW-F-STUDENT

### SW-F-STUDENT Commands

```text
enable
configure terminal
hostname SW-F-STUDENT
vlan 140
 name ADMISSIONS
exit
vlan 150
 name HOSTEL_MANAGEMENT
exit
interface range fa0/1 - 5
 description ADMISSIONS_PCS
 switchport mode access
 switchport access vlan 140
exit
interface range fa0/6 - 10
 description HOSTEL_MANAGEMENT_PCS
 switchport mode access
 switchport access vlan 150
exit
interface fa0/24
 description TRUNK_TO_CORE
 switchport mode trunk
 switchport trunk allowed vlan 140,150
end
show vlan brief
show interfaces trunk
```

---

# Part 5: Configure Router-on-a-Stick on R1

## Why This Step Matters

Switches separate departments into VLANs, but VLANs cannot communicate with each other without Layer 3 routing. Router-on-a-Stick allows one router interface to route between many VLANs by using 802.1Q subinterfaces.

Each subinterface must have:

- A VLAN tag using `encapsulation dot1Q`.
- An IP address that acts as the default gateway for that VLAN.
- The physical interface enabled with `no shutdown`.

## R1 Router-on-a-Stick Commands

```text
enable
configure terminal
hostname R1
interface gigabitEthernet0/0
 description TRUNK_TO_CORE_SWITCH
 no shutdown
exit
interface gigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit
interface gigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
exit
interface gigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
exit
interface gigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
exit
interface gigabitEthernet0/0.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
exit
interface gigabitEthernet0/0.60
 encapsulation dot1Q 60
 ip address 192.168.60.1 255.255.255.0
exit
interface gigabitEthernet0/0.70
 encapsulation dot1Q 70
 ip address 192.168.70.1 255.255.255.0
exit
interface gigabitEthernet0/0.80
 encapsulation dot1Q 80
 ip address 192.168.80.1 255.255.255.0
exit
interface gigabitEthernet0/0.90
 encapsulation dot1Q 90
 ip address 192.168.90.1 255.255.255.0
exit
interface gigabitEthernet0/0.100
 encapsulation dot1Q 100
 ip address 192.168.100.1 255.255.255.0
exit
interface gigabitEthernet0/0.110
 encapsulation dot1Q 110
 ip address 192.168.110.1 255.255.255.0
exit
interface gigabitEthernet0/0.120
 encapsulation dot1Q 120
 ip address 192.168.120.1 255.255.255.0
exit
interface gigabitEthernet0/0.130
 encapsulation dot1Q 130
 ip address 192.168.130.1 255.255.255.0
exit
interface gigabitEthernet0/0.140
 encapsulation dot1Q 140
 ip address 192.168.140.1 255.255.255.0
exit
interface gigabitEthernet0/0.150
 encapsulation dot1Q 150
 ip address 192.168.150.1 255.255.255.0
exit
end
show ip interface brief
```

## Expected Result

`show ip interface brief` should show subinterfaces such as:

```text
GigabitEthernet0/0.10    192.168.10.1    up    up
GigabitEthernet0/0.20    192.168.20.1    up    up
GigabitEthernet0/0.30    192.168.30.1    up    up
```

All configured subinterfaces should be up/up. If they are down/down, check that the physical router interface is connected and enabled. If they are up/down or traffic fails, check trunking on CORE-SW Fa0/1.

---

# Part 6: Configure PC IP Addresses

## Why This Step Matters

Each PC must be in the correct VLAN subnet and must use that VLAN's router subinterface as its default gateway. Without the correct default gateway, same-VLAN communication may work but inter-VLAN communication will fail.

## How to Configure Each PC

For every PC:

1. Click the PC.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the correct IP address.
5. Enter subnet mask `255.255.255.0`.
6. Enter the correct default gateway for that VLAN.
7. Close the window.
8. Open Command Prompt.
9. Run `ipconfig` to confirm the settings.

## Example PC Configurations

### REG-PC1

```text
IP Address: 192.168.10.11
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.10.1
```

### FIN-PC1

```text
IP Address: 192.168.20.11
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.20.1
```

### CS-PC1

```text
IP Address: 192.168.40.11
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.40.1
```

### NETOPS-PC1

```text
IP Address: 192.168.120.11
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.120.1
```

## Addressing Rule for the Remaining PCs

For each department, assign the five PCs using `.11`, `.12`, `.13`, `.14`, and `.15`.

Example for VLAN 70 Electrical Engineering:

```text
EE-PC1: 192.168.70.11 / 255.255.255.0 / Gateway 192.168.70.1
EE-PC2: 192.168.70.12 / 255.255.255.0 / Gateway 192.168.70.1
EE-PC3: 192.168.70.13 / 255.255.255.0 / Gateway 192.168.70.1
EE-PC4: 192.168.70.14 / 255.255.255.0 / Gateway 192.168.70.1
EE-PC5: 192.168.70.15 / 255.255.255.0 / Gateway 192.168.70.1
```

---

# Part 7: Verification and Testing

## Why This Step Matters

Configuration is not complete until it is verified. A professional network engineer must prove that VLANs exist, trunks are carrying the correct VLANs, router subinterfaces are up, and PCs can communicate as required.

## Verification on Core Switch

### CORE-SW VLAN Check

```text
enable
show vlan brief
```

What to confirm:

- All 15 VLANs exist.
- VLAN names are correct.

### CORE-SW Trunk Check

```text
show interfaces trunk
```

What to confirm:

- Fa0/1 is trunking to the router.
- Fa0/2 to Fa0/7 are trunking to the access switches.
- Allowed VLANs match the VLANs used on each link.

## Verification on Access Switches

Run these commands on every access switch:

```text
enable
show vlan brief
show interfaces trunk
```

What to confirm:

- PC-facing ports are assigned to the correct VLAN.
- Fa0/24 is trunking to the core switch.
- The allowed VLAN list matches that building.

## Verification on Router

Run:

```text
enable
show ip interface brief
```

Then run:

```text
show running-config
```

What to confirm:

- G0/0 is up.
- Every subinterface exists.
- Every subinterface has the correct `encapsulation dot1Q` value.
- Every subinterface has the correct gateway IP address.

---

# Part 8: Required Ping Tests

## Test 1: Same VLAN, Same Building

From REG-PC1:

```text
ping 192.168.10.12
```

Expected result: Success.

Why it should work: Both PCs are in VLAN 10 and the same subnet.

## Test 2: Different VLAN, Same Building

From REG-PC1:

```text
ping 192.168.20.11
```

Expected result: Success.

Why it should work: REG-PC1 sends traffic to its gateway, R1 routes from VLAN 10 to VLAN 20, and the traffic returns through R1.

## Test 3: Different VLAN, Different Building

From REG-PC1:

```text
ping 192.168.40.11
```

Expected result: Success.

Why it should work: The frame travels from Building A access switch to the core switch, reaches R1 for routing, returns to the core, and is forwarded to Building B.

## Test 4: Library to ICT Centre

From LIBSTUD-PC1:

```text
ping 192.168.120.11
```

Expected result: Success.

## Test 5: Student Affairs to Server Room

From ADM-PC1:

```text
ping 192.168.130.11
```

Expected result: Success.

---

# Part 9: Troubleshooting Guide

## If Same-VLAN PCs Cannot Ping

Check the access switch:

```text
show vlan brief
```

Confirm both PC ports are in the correct VLAN.

Check the PC settings:

```text
ipconfig
```

Confirm both PCs are in the same subnet.

## If Different VLANs Cannot Ping

Check the PC gateway:

```text
ipconfig
```

Confirm the default gateway is the `.1` address for that VLAN.

Check the router:

```text
show ip interface brief
```

Confirm subinterfaces are up/up.

Check the core trunk to the router:

```text
show interfaces trunk
```

Confirm the VLAN is allowed on the trunk.

## If One Building Cannot Communicate

Check the trunk between that building switch and the core switch:

```text
show interfaces trunk
```

Check that the building VLANs are allowed on both ends of the trunk.

## Common Mistakes

| Problem | Likely Cause | Fix |
|---|---|---|
| PC cannot ping its gateway | Wrong VLAN, wrong IP, wrong gateway, or trunk issue | Verify PC IP, access VLAN, trunk, and router subinterface |
| VLAN missing from `show vlan brief` | VLAN not created on that switch | Create the VLAN |
| Trunk missing from `show interfaces trunk` | Port not configured as trunk | Configure `switchport mode trunk` |
| Router subinterface down | Physical interface shutdown or trunk problem | Configure `no shutdown` and verify trunk |
| Only some departments fail | VLAN not allowed on a trunk | Fix allowed VLAN list |

---

# Part 10: Final Screenshots to Submit

Take screenshots of the following:

1. `show vlan brief` on CORE-SW.
2. `show interfaces trunk` on CORE-SW.
3. `show vlan brief` on each access switch.
4. `show interfaces trunk` on each access switch.
5. `show ip interface brief` on R1.
6. Successful ping from one PC to another PC in the same VLAN.
7. Successful ping from one PC to another PC in a different VLAN.
8. Successful ping from one building to another building.

---

# Final Copy-Friendly Command Summary

## CORE-SW Complete Configuration

```text
enable
configure terminal
hostname CORE-SW
vlan 10
 name REGISTRY
exit
vlan 20
 name FINANCE
exit
vlan 30
 name HR
exit
vlan 40
 name COMPUTER_SCIENCE
exit
vlan 50
 name BIOLOGY
exit
vlan 60
 name CHEMISTRY
exit
vlan 70
 name ELECTRICAL_ENG
exit
vlan 80
 name MECHANICAL_ENG
exit
vlan 90
 name CIVIL_ENG
exit
vlan 100
 name LIBRARY_STAFF
exit
vlan 110
 name LIBRARY_STUDENTS
exit
vlan 120
 name NETWORK_OPERATIONS
exit
vlan 130
 name SERVER_ROOM
exit
vlan 140
 name ADMISSIONS
exit
vlan 150
 name HOSTEL_MANAGEMENT
exit
interface fa0/1
 description TRUNK_TO_R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150
exit
interface fa0/2
 description TRUNK_TO_SW_A_ADMIN
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
exit
interface fa0/3
 description TRUNK_TO_SW_B_SCIENCE
 switchport mode trunk
 switchport trunk allowed vlan 40,50,60
exit
interface fa0/4
 description TRUNK_TO_SW_C_ENGINEERING
 switchport mode trunk
 switchport trunk allowed vlan 70,80,90
exit
interface fa0/5
 description TRUNK_TO_SW_D_LIBRARY
 switchport mode trunk
 switchport trunk allowed vlan 100,110
exit
interface fa0/6
 description TRUNK_TO_SW_E_ICT
 switchport mode trunk
 switchport trunk allowed vlan 120,130
exit
interface fa0/7
 description TRUNK_TO_SW_F_STUDENT
 switchport mode trunk
 switchport trunk allowed vlan 140,150
exit
end
show vlan brief
show interfaces trunk
```

## R1 Complete Router-on-a-Stick Configuration

```text
enable
configure terminal
hostname R1
interface gigabitEthernet0/0
 description TRUNK_TO_CORE_SWITCH
 no shutdown
exit
interface gigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit
interface gigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
exit
interface gigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
exit
interface gigabitEthernet0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
exit
interface gigabitEthernet0/0.50
 encapsulation dot1Q 50
 ip address 192.168.50.1 255.255.255.0
exit
interface gigabitEthernet0/0.60
 encapsulation dot1Q 60
 ip address 192.168.60.1 255.255.255.0
exit
interface gigabitEthernet0/0.70
 encapsulation dot1Q 70
 ip address 192.168.70.1 255.255.255.0
exit
interface gigabitEthernet0/0.80
 encapsulation dot1Q 80
 ip address 192.168.80.1 255.255.255.0
exit
interface gigabitEthernet0/0.90
 encapsulation dot1Q 90
 ip address 192.168.90.1 255.255.255.0
exit
interface gigabitEthernet0/0.100
 encapsulation dot1Q 100
 ip address 192.168.100.1 255.255.255.0
exit
interface gigabitEthernet0/0.110
 encapsulation dot1Q 110
 ip address 192.168.110.1 255.255.255.0
exit
interface gigabitEthernet0/0.120
 encapsulation dot1Q 120
 ip address 192.168.120.1 255.255.255.0
exit
interface gigabitEthernet0/0.130
 encapsulation dot1Q 130
 ip address 192.168.130.1 255.255.255.0
exit
interface gigabitEthernet0/0.140
 encapsulation dot1Q 140
 ip address 192.168.140.1 255.255.255.0
exit
interface gigabitEthernet0/0.150
 encapsulation dot1Q 150
 ip address 192.168.150.1 255.255.255.0
exit
end
show ip interface brief
```

## Final Save Commands

Run this on each switch and on the router after confirming everything works:

```text
copy running-config startup-config
```

When prompted for the destination filename, press Enter.


