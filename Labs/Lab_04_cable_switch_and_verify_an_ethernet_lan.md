# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 4

## Lab Title: Cable, Switch, and Verify an Ethernet LAN

## Aligned Lessons

This lab aligns with Lesson 7, Cabling and Physical Media, Lesson 8, Ethernet Fundamentals, and Lesson 9, Enterprise Switching Fundamentals.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because many network problems are caused by simple physical or Layer 2 issues: a wrong cable, a disconnected port, a disabled interface, a bad speed/duplex negotiation, or a switch that has not learned the expected MAC address. A network engineer must be comfortable proving that Ethernet is working before moving to IP routing or services.

## Important How

Students will cable four PCs to one switch, configure IP addresses, generate traffic, and use switch verification commands. They will prove that a switch learns MAC addresses dynamically after traffic enters a port.

## Required Devices

| Device | Quantity |
|---|---:|
| Cisco 2960 switch | 1 |
| PCs | 4 |
| Copper straight-through cables | 4 |

## Addressing Table

| Device | IP Address | Subnet Mask | Switch Port |
|---|---|---|---|
| PC1 | 192.168.20.11 | 255.255.255.0 | Fa0/1 |
| PC2 | 192.168.20.12 | 255.255.255.0 | Fa0/2 |
| PC3 | 192.168.20.13 | 255.255.255.0 | Fa0/3 |
| PC4 | 192.168.20.14 | 255.255.255.0 | Fa0/4 |

## Detailed Step-by-Step Procedure

### Part A: Build and Cable the LAN

1. Open Cisco Packet Tracer.
2. Drag one 2960 switch into the workspace.
3. Rename it `SW-ACCESS-1`.
4. Drag four PCs into the workspace.
5. Rename them `PC1`, `PC2`, `PC3`, and `PC4`.
6. Select Copper Straight-Through cable.
7. Connect PC1 FastEthernet0 to SW-ACCESS-1 FastEthernet0/1.
8. Connect PC2 FastEthernet0 to SW-ACCESS-1 FastEthernet0/2.
9. Connect PC3 FastEthernet0 to SW-ACCESS-1 FastEthernet0/3.
10. Connect PC4 FastEthernet0 to SW-ACCESS-1 FastEthernet0/4.
11. Wait for link lights to become green.

### Part B: Configure the PCs

1. Click PC1.
2. Click Desktop.
3. Click IP Configuration.
4. Type IP address `192.168.20.11`.
5. Type subnet mask `255.255.255.0`.
6. Leave default gateway blank.
7. Repeat the same process for PC2, PC3, and PC4 using the addressing table.

### Part C: Verify Switch Port Status

1. Click SW-ACCESS-1.
2. Click CLI.
3. If prompted for initial configuration dialog, type `no` and press Enter.
4. Press Enter until you see `Switch>`.
5. Type `enable` and press Enter.
6. Type `show interfaces status` and press Enter.
7. Confirm Fa0/1, Fa0/2, Fa0/3, and Fa0/4 are connected.
8. Type `show ip interface brief` and press Enter.
9. Confirm the FastEthernet interfaces are up/up or administratively available depending on Packet Tracer display.

### Part D: Observe MAC Learning

1. On SW-ACCESS-1, type `show mac address-table` and press Enter.
2. Record whether the table is empty or partially populated.
3. Click PC1.
4. Open Desktop > Command Prompt.
5. Type `ping 192.168.20.12` and press Enter.
6. Type `ping 192.168.20.13` and press Enter.
7. Type `ping 192.168.20.14` and press Enter.
8. Return to SW-ACCESS-1 CLI.
9. Type `show mac address-table dynamic` and press Enter.
10. Confirm MAC addresses are learned on Fa0/1, Fa0/2, Fa0/3, and Fa0/4.

### Part E: Simulate a Cable Fault

1. Click the cable between PC4 and SW-ACCESS-1.
2. Press Delete or use the delete tool to remove the cable.
3. Return to SW-ACCESS-1 CLI.
4. Type `show interfaces status` and press Enter.
5. Confirm Fa0/4 is no longer connected.
6. Reconnect PC4 to Fa0/4 with a straight-through cable.
7. Wait for the light to turn green.
8. Run `show interfaces status` again.
9. Confirm Fa0/4 has returned to connected state.

## Verification Commands

```text
enable
show interfaces status
show ip interface brief
show mac address-table
show mac address-table dynamic
```

## Correct Results

The switch ports connected to PCs should show connected or up. After traffic is generated, the MAC address table should show dynamic MAC entries associated with the correct switch ports.

## Troubleshooting Notes

If a MAC address does not appear, generate traffic from that PC. Switches learn source MAC addresses from frames entering a port; they do not learn all addresses just because cables are connected.


## Copy-Friendly Command Blocks

### SW-ACCESS-1 CLI

```text
enable
```

```text
show interfaces status
```

```text
show ip interface brief
```

```text
show mac address-table
```

```text
show mac address-table dynamic
```

### PC1 Command Prompt

```text
ping 192.168.20.12
```

```text
ping 192.168.20.13
```

```text
ping 192.168.20.14
```

## Student Deliverable

Submit the topology, switch port status output, dynamic MAC address table, and a short explanation of how the switch learned the MAC addresses.
