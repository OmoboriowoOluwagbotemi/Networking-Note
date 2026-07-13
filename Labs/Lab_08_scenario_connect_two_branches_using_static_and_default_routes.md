# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 8

## Lab Title: Scenario - Connect Two Branches Using Static and Default Routes

## Aligned Lessons

This lab aligns with Lesson 17, How Routers Work, Static and Default Routing.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because routers only forward traffic to networks they know. A router may have directly connected networks, but it will not automatically know about a remote branch LAN unless a static route, default route, or dynamic routing protocol tells it where to send traffic.

## Important How

Students will configure router interfaces, assign PC gateways, add static routes on both routers, verify the routing table, and test end-to-end communication.

## Scenario

FEMTECT has a Lagos office and an Abuja office. Each office has one LAN. The routers are connected over a point-to-point WAN link.

## Addressing Plan

| Device/Network | Addressing |
|---|---|
| Lagos LAN | 192.168.100.0/24 |
| Abuja LAN | 192.168.200.0/24 |
| WAN Link | 10.10.10.0/30 |
| R-LAGOS G0/0 | 192.168.100.1/24 |
| R-LAGOS G0/1 | 10.10.10.1/30 |
| R-ABUJA G0/0 | 192.168.200.1/24 |
| R-ABUJA G0/1 | 10.10.10.2/30 |
| PC-LAGOS | 192.168.100.10/24, gateway 192.168.100.1 |
| PC-ABUJA | 192.168.200.10/24, gateway 192.168.200.1 |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Add two routers. Use 2911 routers if available.
2. Rename them `R-LAGOS` and `R-ABUJA`.
3. Add two 2960 switches.
4. Rename them `SW-LAGOS` and `SW-ABUJA`.
5. Add two PCs.
6. Rename them `PC-LAGOS` and `PC-ABUJA`.
7. Connect PC-LAGOS to SW-LAGOS.
8. Connect SW-LAGOS to R-LAGOS G0/0.
9. Connect PC-ABUJA to SW-ABUJA.
10. Connect SW-ABUJA to R-ABUJA G0/0.
11. Connect R-LAGOS G0/1 to R-ABUJA G0/1.

### Part B: Configure R-LAGOS

Click R-LAGOS > CLI and type:

```text
enable
configure terminal
hostname R-LAGOS
interface gigabitEthernet0/0
 description LAGOS_LAN
 ip address 192.168.100.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description WAN_TO_ABUJA
 ip address 10.10.10.1 255.255.255.252
 no shutdown
exit
ip route 192.168.200.0 255.255.255.0 10.10.10.2
end
show ip interface brief
show ip route
```

### Part C: Configure R-ABUJA

Click R-ABUJA > CLI and type:

```text
enable
configure terminal
hostname R-ABUJA
interface gigabitEthernet0/0
 description ABUJA_LAN
 ip address 192.168.200.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description WAN_TO_LAGOS
 ip address 10.10.10.2 255.255.255.252
 no shutdown
exit
ip route 192.168.100.0 255.255.255.0 10.10.10.1
end
show ip interface brief
show ip route
```

### Part D: Configure PCs

1. Click PC-LAGOS > Desktop > IP Configuration.
2. Set IP address `192.168.100.10`.
3. Set subnet mask `255.255.255.0`.
4. Set default gateway `192.168.100.1`.
5. Click PC-ABUJA > Desktop > IP Configuration.
6. Set IP address `192.168.200.10`.
7. Set subnet mask `255.255.255.0`.
8. Set default gateway `192.168.200.1`.

### Part E: Test Routing

1. From PC-LAGOS, open Command Prompt.
2. Type `ping 192.168.100.1` and press Enter.
3. Confirm the local gateway responds.
4. Type `ping 10.10.10.2` and press Enter.
5. Confirm the remote router WAN interface responds.
6. Type `ping 192.168.200.10` and press Enter.
7. Confirm PC-ABUJA responds.
8. Type `tracert 192.168.200.10` and press Enter.
9. Confirm the path shows R-LAGOS and R-ABUJA.

## Verification Commands

```text
show ip interface brief
show ip route
ping
traceroute
```

## Troubleshooting Notes

If the routers can ping each other but PCs cannot communicate, check PC default gateways and return routes. Routing must work in both directions.

## Student Deliverable

Submit both routing tables and successful PC-to-PC ping output.
