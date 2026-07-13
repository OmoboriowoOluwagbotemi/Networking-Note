# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 7

## Lab Title: Scenario - Fix Layer 2 Loops and Inter-VLAN Connectivity

## Aligned Lessons

This lab aligns with Lesson 15, Spanning Tree Protocol, and Lesson 16, Inter-VLAN Routing.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because redundancy can create danger at Layer 2 if loops are not controlled. Spanning Tree Protocol prevents switching loops by blocking one redundant path. The lab also shows that VLANs separate users until a router or Layer 3 switch provides gateways between VLANs.

## Important How

Students will add a redundant switch link, verify STP, configure router-on-a-stick with subinterfaces, assign default gateways, and test inter-VLAN routing.

## Required Starting Point

Use the completed Lab 6 topology.

## Gateway Plan

| VLAN | Gateway IP |
|---:|---|
| 10 | 192.168.10.1 |
| 20 | 192.168.20.1 |
| 30 | 192.168.30.1 |

## Detailed Step-by-Step Procedure

### Part A: Add a Redundant Link

1. Open the Lab 6 topology.
2. Select Copper Straight-Through or Automatic cable.
3. Connect SW1 Fa0/23 to SW2 Fa0/23.
4. Wait for the ports to settle.
5. Click SW1 > CLI.
6. Type `enable` and press Enter.
7. Type `show spanning-tree` and press Enter.
8. Record the root bridge ID and port roles.
9. Click SW2 > CLI.
10. Type `enable` and press Enter.
11. Type `show spanning-tree` and press Enter.
12. Identify which port is forwarding and which port is blocking or alternate.

### Part B: Make SW1 the Preferred Root Bridge

On SW1, type:

```text
enable
configure terminal
spanning-tree vlan 10,20,30 priority 4096
end
show spanning-tree vlan 10
show spanning-tree vlan 20
show spanning-tree vlan 30
```

Confirm SW1 is the root bridge for VLANs 10, 20, and 30.

### Part C: Add the Router

1. Add one router. A 2911 router is suitable in Packet Tracer.
2. Rename it `R1`.
3. Connect R1 GigabitEthernet0/0 to SW1 Fa0/22.
4. On SW1, configure Fa0/22 as a trunk:

```text
enable
configure terminal
interface fa0/22
 description TRUNK_TO_R1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
end
show interfaces trunk
```

### Part D: Configure Router-on-a-Stick

1. Click R1.
2. Click CLI.
3. If prompted for initial configuration dialog, type `no`.
4. Type `enable` and press Enter.
5. Type `configure terminal` and press Enter.
6. Type the following commands:

```text
interface gigabitEthernet0/0
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
end
show ip interface brief
```

7. Confirm G0/0 and the subinterfaces are up/up. If subinterfaces are down, check the trunk and physical link.

### Part E: Configure PC Default Gateways

1. Click PC-ADMIN-1 > Desktop > IP Configuration.
2. Keep IP address `192.168.10.11`.
3. Set Default Gateway to `192.168.10.1`.
4. Repeat for PC-ADMIN-2 using gateway `192.168.10.1`.
5. Configure Sales PCs with gateway `192.168.20.1`.
6. Configure Guest PCs with gateway `192.168.30.1`.

### Part F: Test Inter-VLAN Routing

1. From PC-ADMIN-1, ping `192.168.20.11`.
2. Confirm the ping succeeds.
3. From PC-SALES-1, ping `192.168.30.11`.
4. Confirm the ping succeeds.
5. From PC-GUEST-1, ping `192.168.10.11`.
6. Confirm the ping succeeds unless an ACL has been added. No ACL should exist in this lab.

## Verification Commands

```text
show spanning-tree
show spanning-tree vlan 10
show interfaces trunk
show ip interface brief
show running-config
ping
```

## Troubleshooting Notes

If same-VLAN pings work but different-VLAN pings fail, check PC default gateways, router subinterface IP addresses, trunk allowed VLANs, and whether `no shutdown` was configured on the physical router interface.

## Student Deliverable

Submit STP output, router subinterface configuration, trunk verification, and successful inter-VLAN ping results.
