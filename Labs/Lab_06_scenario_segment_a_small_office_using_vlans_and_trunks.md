# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 6

## Lab Title: Scenario - Segment a Small Office Using VLANs and Trunks

## Aligned Lessons

This lab aligns with Lesson 13, VLAN Fundamentals and Design, and Lesson 14, VLAN Configuration and Trunking.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because enterprise networks are not built as one flat LAN. VLANs separate users into different broadcast domains, reduce unnecessary broadcast traffic, and prepare the network for security policies. Guest devices should not sit in the same Layer 2 network as staff computers.

## Important How

Students will create VLANs on two switches, assign access ports, configure a trunk link, assign PC addresses, and test that same-VLAN devices communicate across switches while different VLANs remain separated.

## Scenario

FEMTECT has two rooms. Each room has one switch. Admin, Sales, and Guest users exist in both rooms. VLANs must span both switches through a trunk link.

## VLAN and Addressing Plan

| VLAN | Name | Subnet | SW1 PC | SW2 PC |
|---:|---|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.11 | 192.168.10.12 |
| 20 | SALES | 192.168.20.0/24 | 192.168.20.11 | 192.168.20.12 |
| 30 | GUEST | 192.168.30.0/24 | 192.168.30.11 | 192.168.30.12 |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Open Cisco Packet Tracer.
2. Add two Cisco 2960 switches.
3. Rename them `SW1` and `SW2`.
4. Add six PCs.
5. Rename them `PC-ADMIN-1`, `PC-SALES-1`, `PC-GUEST-1`, `PC-ADMIN-2`, `PC-SALES-2`, and `PC-GUEST-2`.
6. Connect PC-ADMIN-1 to SW1 Fa0/1.
7. Connect PC-SALES-1 to SW1 Fa0/2.
8. Connect PC-GUEST-1 to SW1 Fa0/3.
9. Connect PC-ADMIN-2 to SW2 Fa0/1.
10. Connect PC-SALES-2 to SW2 Fa0/2.
11. Connect PC-GUEST-2 to SW2 Fa0/3.
12. Connect SW1 Fa0/24 to SW2 Fa0/24.

### Part B: Create VLANs on SW1

1. Click SW1.
2. Open CLI.
3. Type `enable` and press Enter.
4. Type `configure terminal` and press Enter.
5. Type `vlan 10` and press Enter.
6. Type `name ADMIN` and press Enter.
7. Type `exit` and press Enter.
8. Type `vlan 20` and press Enter.
9. Type `name SALES` and press Enter.
10. Type `exit` and press Enter.
11. Type `vlan 30` and press Enter.
12. Type `name GUEST` and press Enter.
13. Type `exit` and press Enter.
14. Type `end` and press Enter.
15. Type `show vlan brief` and press Enter.
16. Confirm VLANs 10, 20, and 30 exist.

### Part C: Create VLANs on SW2

Repeat the exact VLAN creation commands on SW2:

```text
enable
configure terminal
vlan 10
 name ADMIN
exit
vlan 20
 name SALES
exit
vlan 30
 name GUEST
exit
end
show vlan brief
```

### Part D: Configure Access Ports on SW1

On SW1, type the following:

```text
enable
configure terminal
interface fa0/1
 switchport mode access
 switchport access vlan 10
 description PC-ADMIN-1
exit
interface fa0/2
 switchport mode access
 switchport access vlan 20
 description PC-SALES-1
exit
interface fa0/3
 switchport mode access
 switchport access vlan 30
 description PC-GUEST-1
exit
end
show vlan brief
```

Confirm Fa0/1 is in VLAN 10, Fa0/2 is in VLAN 20, and Fa0/3 is in VLAN 30.

### Part E: Configure Access Ports on SW2

On SW2, type the following:

```text
enable
configure terminal
interface fa0/1
 switchport mode access
 switchport access vlan 10
 description PC-ADMIN-2
exit
interface fa0/2
 switchport mode access
 switchport access vlan 20
 description PC-SALES-2
exit
interface fa0/3
 switchport mode access
 switchport access vlan 30
 description PC-GUEST-2
exit
end
show vlan brief
```

### Part F: Configure the Trunk Between Switches

On SW1, type:

```text
enable
configure terminal
interface fa0/24
 description TRUNK_TO_SW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
end
show interfaces trunk
```

On SW2, type:

```text
enable
configure terminal
interface fa0/24
 description TRUNK_TO_SW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
end
show interfaces trunk
```

### Part G: Configure PC IP Addresses

1. Click PC-ADMIN-1 > Desktop > IP Configuration.
2. Set IP address `192.168.10.11` and mask `255.255.255.0`.
3. Leave default gateway blank.
4. Configure PC-ADMIN-2 as `192.168.10.12/24`.
5. Configure PC-SALES-1 as `192.168.20.11/24`.
6. Configure PC-SALES-2 as `192.168.20.12/24`.
7. Configure PC-GUEST-1 as `192.168.30.11/24`.
8. Configure PC-GUEST-2 as `192.168.30.12/24`.

### Part H: Test VLAN Communication

1. From PC-ADMIN-1, ping `192.168.10.12`. It should succeed.
2. From PC-SALES-1, ping `192.168.20.12`. It should succeed.
3. From PC-GUEST-1, ping `192.168.30.12`. It should succeed.
4. From PC-ADMIN-1, ping `192.168.20.11`. It should fail.
5. From PC-SALES-1, ping `192.168.30.11`. It should fail.

## Verification Commands

```text
show vlan brief
show interfaces trunk
show interfaces fa0/24 switchport
show mac address-table dynamic
```

## Accuracy Note

Different VLANs should not communicate in this lab because no router or Layer 3 switch gateway has been configured. That failure is the correct result.

## Student Deliverable

Submit `show vlan brief`, `show interfaces trunk`, successful same-VLAN pings, and failed different-VLAN pings.
