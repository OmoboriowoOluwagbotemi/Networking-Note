# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 5

## Lab Title: Configure IPv4 Addressing and Subnetting

## Aligned Lessons

This lab aligns with Lesson 10, IPv4 Addressing Fundamentals, and Lesson 11, Subnetting Mastery.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because IP addressing decides whether devices see each other as local or remote. Students must learn that physical connection alone does not guarantee communication. Two PCs may be connected to the same switch but fail to communicate if their IP addresses and subnet masks place them in different networks.

## Important How

Students will divide `192.168.30.0/24` into `/26` subnets, assign host addresses, test same-subnet communication, and prove that different-subnet communication requires a router or Layer 3 gateway.

## Subnet Plan

| Department | Network | First Host | Last Host | Broadcast | Mask |
|---|---|---|---|---|---|
| Admin | 192.168.30.0/26 | 192.168.30.1 | 192.168.30.62 | 192.168.30.63 | 255.255.255.192 |
| Sales | 192.168.30.64/26 | 192.168.30.65 | 192.168.30.126 | 192.168.30.127 | 255.255.255.192 |
| Support | 192.168.30.128/26 | 192.168.30.129 | 192.168.30.190 | 192.168.30.191 | 255.255.255.192 |

## Addressing Table

| Device | Department | IP Address | Mask | Gateway |
|---|---|---|---|---|
| PC-ADMIN-1 | Admin | 192.168.30.11 | 255.255.255.192 | Blank |
| PC-ADMIN-2 | Admin | 192.168.30.12 | 255.255.255.192 | Blank |
| PC-SALES-1 | Sales | 192.168.30.71 | 255.255.255.192 | Blank |
| PC-SALES-2 | Sales | 192.168.30.72 | 255.255.255.192 | Blank |
| PC-SUPPORT-1 | Support | 192.168.30.131 | 255.255.255.192 | Blank |
| PC-SUPPORT-2 | Support | 192.168.30.132 | 255.255.255.192 | Blank |

## Detailed Step-by-Step Procedure

### Part A: Build the Topology

1. Open Cisco Packet Tracer.
2. Add one 2960 switch.
3. Rename it `SW1`.
4. Add six PCs.
5. Rename the PCs according to the addressing table.
6. Connect all PCs to SW1 using copper straight-through cables.
7. Use ports Fa0/1 to Fa0/6.

### Part B: Configure IP Addresses

1. Click PC-ADMIN-1.
2. Open Desktop > IP Configuration.
3. Type IP address `192.168.30.11`.
4. Type subnet mask `255.255.255.192`.
5. Leave default gateway blank.
6. Repeat this process for every PC using the addressing table.
7. After configuring each PC, open Command Prompt and run `ipconfig` to confirm the settings.

### Part C: Test Same-Subnet Communication

1. Click PC-ADMIN-1.
2. Open Desktop > Command Prompt.
3. Type `ping 192.168.30.12` and press Enter.
4. Confirm the ping succeeds.
5. Click PC-SALES-1.
6. Open Command Prompt.
7. Type `ping 192.168.30.72` and press Enter.
8. Confirm the ping succeeds.
9. Click PC-SUPPORT-1.
10. Open Command Prompt.
11. Type `ping 192.168.30.132` and press Enter.
12. Confirm the ping succeeds.

### Part D: Test Different-Subnet Communication

1. On PC-ADMIN-1, type `ping 192.168.30.71` and press Enter.
2. Observe that the ping fails.
3. On PC-SALES-1, type `ping 192.168.30.131` and press Enter.
4. Observe that the ping fails.
5. Explain that no router or Layer 3 switch exists to route between the subnets.

### Part E: Prove the Switch Is Not the Problem

1. Click SW1.
2. Open CLI.
3. Type `enable` and press Enter.
4. Type `show mac address-table dynamic` and press Enter.
5. Confirm the switch has learned MAC addresses for the PCs.
6. Understand that Layer 2 can be working even when Layer 3 communication fails between subnets.

## Verification Table

| Test | Expected Result | Reason |
|---|---|---|
| Admin to Admin | Success | Same /26 subnet |
| Sales to Sales | Success | Same /26 subnet |
| Support to Support | Success | Same /26 subnet |
| Admin to Sales | Fail | Different subnet, no router |
| Sales to Support | Fail | Different subnet, no router |

## Troubleshooting Notes

If same-subnet pings fail, check the subnet mask carefully. A common mistake is using `255.255.255.0` instead of `255.255.255.192`, which changes the subnet boundary.

## Student Deliverable

Submit the subnet table, successful same-subnet ping results, failed different-subnet ping results, and one paragraph explaining why routing is required.
