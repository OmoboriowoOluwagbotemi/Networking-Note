# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 9

## Lab Title: Scenario - Get a Whole Office Online Using NAT/PAT

## Aligned Lessons

This lab aligns with Lesson 18, Dynamic Routing and NAT/PAT.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because most offices use private IPv4 addresses internally but need access to public networks. PAT, also called NAT overload, allows many internal devices to share one public-facing IP address.

## Important How

Students will configure inside and outside interfaces, define which private addresses are allowed to be translated, configure PAT overload, test connectivity, and verify NAT translations.

## Addressing Plan

| Area | Addressing |
|---|---|
| Inside LAN | 192.168.50.0/24 |
| Office Router G0/0 | 192.168.50.1/24 |
| Office Router G0/1 | 203.0.113.2/30 |
| ISP Router G0/0 | 203.0.113.1/30 |
| ISP Server LAN | 198.51.100.0/24 |
| ISP Router G0/1 | 198.51.100.1/24 |
| Server | 198.51.100.10/24, gateway 198.51.100.1 |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Add two routers and name them `R-OFFICE` and `R-ISP`.
2. Add one switch named `SW-OFFICE`.
3. Add two PCs named `PC1` and `PC2`.
4. Add one server named `WEB-SERVER`.
5. Connect PC1 and PC2 to SW-OFFICE.
6. Connect SW-OFFICE to R-OFFICE G0/0.
7. Connect R-OFFICE G0/1 to R-ISP G0/0.
8. Connect WEB-SERVER to R-ISP G0/1.

### Part B: Configure R-OFFICE

```text
enable
configure terminal
hostname R-OFFICE
interface gigabitEthernet0/0
 description INSIDE_LAN
 ip address 192.168.50.1 255.255.255.0
 ip nat inside
 no shutdown
exit
interface gigabitEthernet0/1
 description OUTSIDE_TO_ISP
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 no shutdown
exit
access-list 1 permit 192.168.50.0 0.0.0.255
ip nat inside source list 1 interface gigabitEthernet0/1 overload
ip route 0.0.0.0 0.0.0.0 203.0.113.1
end
show ip interface brief
show running-config | include nat
```

### Part C: Configure R-ISP

```text
enable
configure terminal
hostname R-ISP
interface gigabitEthernet0/0
 description TO_OFFICE
 ip address 203.0.113.1 255.255.255.252
 no shutdown
exit
interface gigabitEthernet0/1
 description SERVER_LAN
 ip address 198.51.100.1 255.255.255.0
 no shutdown
exit
end
show ip interface brief
```

### Part D: Configure PCs and Server

1. Configure PC1 as `192.168.50.11/24` with gateway `192.168.50.1`.
2. Configure PC2 as `192.168.50.12/24` with gateway `192.168.50.1`.
3. Configure WEB-SERVER as `198.51.100.10/24` with gateway `198.51.100.1`.
4. On WEB-SERVER, open Services.
5. Click HTTP.
6. Make sure HTTP is On.

### Part E: Test and Verify NAT

1. From PC1, open Command Prompt.
2. Type `ping 192.168.50.1` and press Enter.
3. Type `ping 203.0.113.1` and press Enter.
4. Type `ping 198.51.100.10` and press Enter.
5. From PC2, ping `198.51.100.10`.
6. On R-OFFICE, type `show ip nat translations`.
7. Confirm inside local addresses such as `192.168.50.11` are translated to the outside interface address `203.0.113.2`.
8. Type `show ip nat statistics`.
9. Confirm NAT has active translations or hits.

## Verification Commands

```text
show ip nat translations
show ip nat statistics
show access-lists
show ip route
ping
```

## Accuracy Note

The documentation addresses `203.0.113.0/24` and `198.51.100.0/24` are reserved for examples. They are safe to use in labs and should not be used as real public assignments in production.

## Student Deliverable

Submit NAT configuration, NAT translation output, and successful pings from both PCs to the server.
