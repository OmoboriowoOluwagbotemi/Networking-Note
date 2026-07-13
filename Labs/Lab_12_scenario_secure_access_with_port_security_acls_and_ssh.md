# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 12

## Lab Title: Scenario - Secure Access With Port Security, ACLs, and SSH

## Aligned Lessons

This lab aligns with Lesson 21, Wireless and Network Security Foundations, and Lesson 22, Access Control, Hardening, and Essential Services.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because a network that works but is easy to abuse is not professionally ready. Access ports should be controlled, management access should use SSH instead of Telnet, and routers should be able to enforce basic traffic policy with ACLs.

## Important How

Students will configure a management IP on a switch, enable SSH, configure port security on an access port, apply an extended ACL on a router interface, and verify both permitted and denied traffic.

## Topology

Use one router, one switch, two trusted PCs, one guest PC, and one server.

## Addressing Plan

| Device/Network | Addressing |
|---|---|
| Staff LAN | 192.168.80.0/24 |
| Guest LAN | 192.168.90.0/24 |
| Server LAN | 192.168.100.0/24 |
| R1 Staff Gateway | 192.168.80.1 |
| R1 Guest Gateway | 192.168.90.1 |
| R1 Server Gateway | 192.168.100.1 |
| SW1 Management IP | 192.168.80.2 |
| Server | 192.168.100.10 |

## Detailed Step-by-Step Procedure

### Part A: Build a Basic Routed Topology

1. Add one router named `R1`.
2. Add one 2960 switch named `SW1`.
3. Add three PCs named `PC-STAFF1`, `PC-STAFF2`, and `PC-GUEST`.
4. Add one server named `SRV1`.
5. Connect PC-STAFF1 to SW1 Fa0/1.
6. Connect PC-STAFF2 to SW1 Fa0/2.
7. Connect SW1 Fa0/24 to R1 G0/0.
8. Connect PC-GUEST directly to R1 G0/1 or through a second switch if available.
9. Connect SRV1 to R1 G0/2 if the router model has G0/2. If not, use another available Ethernet interface or add a switch and router subinterfaces.

### Part B: Configure R1 Interfaces

Use available interface names shown by `show ip interface brief`. The example below uses G0/0, G0/1, and G0/2.

```text
enable
configure terminal
hostname R1
interface gigabitEthernet0/0
 description STAFF_LAN
 ip address 192.168.80.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description GUEST_LAN
 ip address 192.168.90.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/2
 description SERVER_LAN
 ip address 192.168.100.1 255.255.255.0
 no shutdown
exit
end
show ip interface brief
```

### Part C: Configure End Devices

1. Configure PC-STAFF1 as `192.168.80.11/24`, gateway `192.168.80.1`.
2. Configure PC-STAFF2 as `192.168.80.12/24`, gateway `192.168.80.1`.
3. Configure PC-GUEST as `192.168.90.11/24`, gateway `192.168.90.1`.
4. Configure SRV1 as `192.168.100.10/24`, gateway `192.168.100.1`.
5. From PC-STAFF1, ping SRV1 at `192.168.100.10`.
6. From PC-GUEST, ping SRV1 at `192.168.100.10`.
7. Confirm connectivity works before applying security policy.

### Part D: Configure Switch Management IP and SSH

On SW1, type:

```text
enable
configure terminal
hostname SW1
interface vlan 1
 ip address 192.168.80.2 255.255.255.0
 no shutdown
exit
ip default-gateway 192.168.80.1
ip domain-name femtect.local
username admin secret StrongLabPass123
crypto key generate rsa
```

When asked for key size, type:

```text
1024
```

Continue:

```text
ip ssh version 2
line vty 0 15
 login local
 transport input ssh
exit
end
show ip ssh
```

From PC-STAFF1 Command Prompt, test SSH if Packet Tracer PC supports the SSH client:

```text
ssh -l admin 192.168.80.2
```

If Packet Tracer does not support the SSH client in your PC version, verification with `show ip ssh` and VTY configuration is acceptable.

### Part E: Configure Port Security on PC-STAFF1 Port

On SW1, type:

```text
enable
configure terminal
interface fa0/1
 description PC-STAFF1_SECURE_PORT
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
end
show port-security interface fa0/1
```

Generate traffic from PC-STAFF1 by pinging `192.168.80.1`, then run:

```text
show running-config interface fa0/1
show port-security address
```

### Part F: Apply an ACL to Block Guest Access to the Server

On R1, type:

```text
enable
configure terminal
ip access-list extended BLOCK_GUEST_TO_SERVER
 deny ip 192.168.90.0 0.0.0.255 host 192.168.100.10
 permit ip any any
exit
interface gigabitEthernet0/1
 ip access-group BLOCK_GUEST_TO_SERVER in
end
show access-lists
show running-config interface gigabitEthernet0/1
```

### Part G: Test Security Policy

1. From PC-GUEST, ping `192.168.100.10`.
2. The ping should fail because the ACL blocks guest traffic to the server.
3. From PC-GUEST, ping `192.168.80.1`.
4. This should succeed because the ACL permits other traffic.
5. From PC-STAFF1, ping `192.168.100.10`.
6. This should succeed because the ACL is applied inbound on the guest interface only.
7. On R1, type `show access-lists`.
8. Confirm the deny or permit counters increase after tests.

## Verification Commands

```text
show ip ssh
show running-config | section line vty
show port-security interface fa0/1
show port-security address
show access-lists
show running-config interface gigabitEthernet0/1
```

## Student Deliverable

Submit SSH verification, port security output, ACL configuration, and screenshots proving guest-to-server traffic is denied while staff-to-server traffic works.
