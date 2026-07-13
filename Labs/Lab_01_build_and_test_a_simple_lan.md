# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 1

## Lab Title: Build and Test a Simple LAN

## Aligned Lessons

This lab aligns with Lesson 1, How Networks Work and Why They Fail, and Lesson 2, Network Devices and Appliances.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because every advanced network begins with a working local area network. Before students configure routers, VLANs, wireless, DHCP, NAT, or security policies, they must first understand how end devices connect through a switch, how IP addresses are assigned, and how basic connectivity is proven.

The important idea is simple: if two hosts are in the same IPv4 subnet and connected through a working Layer 2 switch, they should communicate directly without a router. This helps students understand the difference between local communication and routed communication.

## Important How

Students will build the topology manually in Packet Tracer, assign static IPv4 settings to three PCs, use `ping` to test reachability, and use the switch CLI to verify interface and MAC address learning. The lab intentionally does not use a router because students must first see what a same-subnet LAN can do by itself.

## Scenario

A small training room has three computers. The computers must communicate with one another through one access switch. There is no internet connection and no default gateway in this first lab.

## Required Devices

| Device | Quantity | Packet Tracer Location |
|---|---:|---|
| Cisco 2960 switch | 1 | Network Devices > Switches |
| PC | 3 | End Devices |
| Copper straight-through cable | 3 | Connections |

## Addressing Table

| Device | Interface | IPv4 Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| PC1 | FastEthernet0 | 192.168.10.11 | 255.255.255.0 | Leave blank |
| PC2 | FastEthernet0 | 192.168.10.12 | 255.255.255.0 | Leave blank |
| PC3 | FastEthernet0 | 192.168.10.13 | 255.255.255.0 | Leave blank |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Open Cisco Packet Tracer.
2. Click Network Devices.
3. Click Switches.
4. Drag one 2960 switch into the workspace.
5. Click the switch name under the icon.
6. Rename the switch to `SW1`.
7. Click End Devices.
8. Drag three PCs into the workspace.
9. Rename the PCs as `PC1`, `PC2`, and `PC3`.
10. Click Connections.
11. Select Copper Straight-Through cable.
12. Click PC1, choose FastEthernet0, then click SW1 and choose FastEthernet0/1.
13. Click PC2, choose FastEthernet0, then click SW1 and choose FastEthernet0/2.
14. Click PC3, choose FastEthernet0, then click SW1 and choose FastEthernet0/3.
15. Wait until the link lights become green. If they are orange, wait a few seconds because the switch port may still be transitioning.

### Part B: Configure IP Addresses on the PCs

1. Click PC1.
2. Click the Desktop tab.
3. Click IP Configuration.
4. In IPv4 Address, type `192.168.10.11`.
5. In Subnet Mask, type `255.255.255.0`.
6. Leave Default Gateway blank.
7. Close the PC1 window.
8. Click PC2.
9. Click Desktop.
10. Click IP Configuration.
11. Type IPv4 Address `192.168.10.12`.
12. Type Subnet Mask `255.255.255.0`.
13. Leave Default Gateway blank.
14. Close the PC2 window.
15. Click PC3.
16. Click Desktop.
17. Click IP Configuration.
18. Type IPv4 Address `192.168.10.13`.
19. Type Subnet Mask `255.255.255.0`.
20. Leave Default Gateway blank.
21. Close the PC3 window.

### Part C: Test Connectivity From PC1

1. Click PC1.
2. Click Desktop.
3. Click Command Prompt.
4. Type `ipconfig` and press Enter.
5. Confirm PC1 shows IP address `192.168.10.11` and subnet mask `255.255.255.0`.
6. Type `ping 192.168.10.12` and press Enter.
7. Confirm that replies are received from PC2.
8. Type `ping 192.168.10.13` and press Enter.
9. Confirm that replies are received from PC3.
10. If the first ping fails but later pings succeed, explain that ARP resolution and switch learning may have occurred during the first attempt.

### Part D: Verify the Switch From the CLI

1. Click SW1.
2. Click the CLI tab.
3. If Packet Tracer asks `Would you like to enter the initial configuration dialog?`, type `no` and press Enter.
4. Press Enter until you see the prompt `Switch>`.
5. Type `enable` and press Enter.
6. Confirm the prompt changes to `Switch#`.
7. Type `show interfaces status` and press Enter.
8. Confirm Fa0/1, Fa0/2, and Fa0/3 are connected.
9. Type `show mac address-table` and press Enter.
10. Confirm the switch has learned MAC addresses on Fa0/1, Fa0/2, and Fa0/3 after the PCs have communicated.

## Verification Table

| Verification Step | Command or Action | Correct Result |
|---|---|---|
| PC1 IP settings | `ipconfig` | PC1 shows 192.168.10.11/24 |
| PC1 to PC2 | `ping 192.168.10.12` | Successful replies |
| PC1 to PC3 | `ping 192.168.10.13` | Successful replies |
| Switch ports | `show interfaces status` | Fa0/1-Fa0/3 connected |
| MAC learning | `show mac address-table` | MACs learned dynamically |

## Troubleshooting Notes

If ping fails, check the cable type, switch link lights, PC IP addresses, subnet masks, and whether the PC is connected to the expected switch port. A default gateway is not needed in this lab because all hosts are in the same subnet.


## Copy-Friendly Command Blocks

### PC1 Command Prompt

```text
ipconfig
```

```text
ping 192.168.10.12
```

```text
ping 192.168.10.13
```

### PC2 Command Prompt

```text
ping 192.168.10.13
```

### SW1 CLI Verification

```text
enable
```

```text
show interfaces status
```

```text
show mac address-table
```

## Student Deliverable

Submit a screenshot of the completed topology, PC1 ping results, and SW1 MAC address table. Add two sentences explaining why a router is not required for same-subnet communication.
