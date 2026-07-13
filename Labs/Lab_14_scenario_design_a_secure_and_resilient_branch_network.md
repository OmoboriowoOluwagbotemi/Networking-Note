# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 14

## Lab Title: Scenario - Design a Secure and Resilient Branch Network

## Aligned Lessons

This lab aligns with Lesson 23, VPNs and Remote Access Security, and Lesson 24, Power and Resilience.

## Main Tools

Cisco Packet Tracer and a written resilience worksheet.

## Important Why

This lab is important because a branch network must be secure and available. Secure WAN design protects traffic between locations, while power resilience keeps the network alive during outages. A branch router, switch, access point, and modem are only useful if they remain powered and if the traffic path is protected.

## Important How

Students will build a headquarters-and-branch topology, configure normal routed reachability, label the WAN as untrusted, document VPN design parameters, and complete a power-resilience worksheet. This lab does not pretend that every Packet Tracer router image supports every production VPN feature.

## Packet Tracer Accuracy Note

Cisco Packet Tracer support for site-to-site VPN depends on device model, IOS image, and activity type. To keep this lab correct for all students, the required task is to build and verify the routed underlay and document the VPN overlay design. If the instructor provides a Packet Tracer file or router model that supports IPsec configuration, the instructor may add the VPN configuration as an extension.

## Addressing Plan

| Area | Network | Gateway |
|---|---|---|
| HQ LAN | 10.10.10.0/24 | 10.10.10.1 |
| Branch LAN | 10.20.20.0/24 | 10.20.20.1 |
| HQ to ISP | 198.51.100.0/30 | HQ: 198.51.100.2, ISP: 198.51.100.1 |
| Branch to ISP | 203.0.113.0/30 | Branch: 203.0.113.2, ISP: 203.0.113.1 |
| ISP transit | Use ISP router routes | Not a user LAN |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Add three routers.
2. Rename them `R-HQ`, `R-ISP`, and `R-BRANCH`.
3. Add two switches.
4. Rename them `SW-HQ` and `SW-BRANCH`.
5. Add one server named `HQ-SERVER`.
6. Add one PC named `HQ-PC`.
7. Add two branch PCs named `BR-PC1` and `BR-PC2`.
8. Connect HQ-PC and HQ-SERVER to SW-HQ.
9. Connect SW-HQ to R-HQ G0/0.
10. Connect BR-PC1 and BR-PC2 to SW-BRANCH.
11. Connect SW-BRANCH to R-BRANCH G0/0.
12. Connect R-HQ G0/1 to R-ISP G0/0.
13. Connect R-BRANCH G0/1 to R-ISP G0/1.
14. Add a Packet Tracer note near the ISP router that says `UNTRUSTED WAN / INTERNET SIMULATION`.

### Part B: Configure R-HQ

```text
enable
configure terminal
hostname R-HQ
interface gigabitEthernet0/0
 description HQ_LAN
 ip address 10.10.10.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_ISP
 ip address 198.51.100.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 198.51.100.1
end
show ip interface brief
show ip route
```

### Part C: Configure R-BRANCH

```text
enable
configure terminal
hostname R-BRANCH
interface gigabitEthernet0/0
 description BRANCH_LAN
 ip address 10.20.20.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_ISP
 ip address 203.0.113.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 203.0.113.1
end
show ip interface brief
show ip route
```

### Part D: Configure R-ISP

```text
enable
configure terminal
hostname R-ISP
interface gigabitEthernet0/0
 description TO_HQ
 ip address 198.51.100.1 255.255.255.252
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_BRANCH
 ip address 203.0.113.1 255.255.255.252
 no shutdown
exit
ip route 10.10.10.0 255.255.255.0 198.51.100.2
ip route 10.20.20.0 255.255.255.0 203.0.113.2
end
show ip route
```

### Part E: Configure End Devices

1. Configure HQ-PC as `10.10.10.11/24`, gateway `10.10.10.1`.
2. Configure HQ-SERVER as `10.10.10.100/24`, gateway `10.10.10.1`.
3. Configure BR-PC1 as `10.20.20.11/24`, gateway `10.20.20.1`.
4. Configure BR-PC2 as `10.20.20.12/24`, gateway `10.20.20.1`.

### Part F: Verify Routed Underlay Connectivity

1. From BR-PC1, ping `10.20.20.1`.
2. Confirm the branch gateway responds.
3. From BR-PC1, ping `203.0.113.1`.
4. Confirm the ISP-side next hop responds.
5. From BR-PC1, ping `10.10.10.100`.
6. Confirm the HQ server responds.
7. From BR-PC1, run `tracert 10.10.10.100`.
8. Confirm the path crosses the branch router, ISP router, and HQ router.

### Part G: Document VPN Overlay Requirements

Create a table with these fields:

| VPN Parameter | Value to Document |
|---|---|
| HQ peer public IP | 198.51.100.2 |
| Branch peer public IP | 203.0.113.2 |
| HQ protected network | 10.10.10.0/24 |
| Branch protected network | 10.20.20.0/24 |
| Encryption concept | IPsec ESP |
| Authentication concept | Pre-shared key or certificates |
| Interesting traffic | HQ LAN to Branch LAN |
| NAT exemption needed? | Yes in many real NAT designs, not used in this simple underlay |

### Part H: Complete Power-Resilience Worksheet

1. List the branch router.
2. List the branch switch.
3. List the internet modem or ISP CPE.
4. List the access point if branch Wi-Fi exists.
5. Estimate wattage for each device.
6. Add the total wattage.
7. Add 25 percent headroom.
8. Choose a target runtime, such as 30 minutes.
9. Identify which devices must remain powered for remote access.
10. Write a safe shutdown order.
11. Write a startup order.
12. Write one power failure risk and one mitigation.

## Verification Commands

```text
show ip interface brief
show ip route
ping
traceroute
```


## Copy-Friendly Command Blocks

### R-HQ Configuration

```text
enable
configure terminal
hostname R-HQ
interface gigabitEthernet0/0
 description HQ_LAN
 ip address 10.10.10.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_ISP
 ip address 198.51.100.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 198.51.100.1
end
show ip interface brief
show ip route
```

### R-BRANCH Configuration

```text
enable
configure terminal
hostname R-BRANCH
interface gigabitEthernet0/0
 description BRANCH_LAN
 ip address 10.20.20.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_ISP
 ip address 203.0.113.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 203.0.113.1
end
show ip interface brief
show ip route
```

### R-ISP Configuration

```text
enable
configure terminal
hostname R-ISP
interface gigabitEthernet0/0
 description TO_HQ
 ip address 198.51.100.1 255.255.255.252
 no shutdown
exit
interface gigabitEthernet0/1
 description TO_BRANCH
 ip address 203.0.113.1 255.255.255.252
 no shutdown
exit
ip route 10.10.10.0 255.255.255.0 198.51.100.2
ip route 10.20.20.0 255.255.255.0 203.0.113.2
end
show ip route
```

### Branch Tests

```text
ping 10.20.20.1
```

```text
ping 203.0.113.1
```

```text
ping 10.10.10.100
```

```text
tracert 10.10.10.100
```

## Student Deliverable

Submit the topology, routing verification, VPN design table, and power-resilience worksheet.
