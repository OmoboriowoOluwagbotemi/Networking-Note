# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 5

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: CONFIGURE IPV4 ADDRESSING AND SUBNETTING

## Aligned Lessons

This lab aligns with Lesson 10, IPv4 Addressing Fundamentals, and Lesson 11, Subnetting Mastery.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will divide a network into multiple subnets and verify which hosts can communicate directly.

## Important Why

This lab matters because IP addressing and subnetting determine whether hosts are local, remote, reachable, or isolated. Students must learn that devices can be physically connected but logically separated by subnet boundaries.

## Important How

Students finish this lab by subnetting a /24 into /26 networks, assigning hosts correctly, testing same-subnet and different-subnet communication, and explaining why routing is needed.

## Scenario

A company has three departments: Admin, Sales, and Technical Support. Each department needs a separate IPv4 subnet.

## Subnet Plan

Use the network `192.168.30.0/24` and create three `/26` subnets.

| Department | Network | Usable Host Range | Broadcast |
|---|---|---|---|
| Admin | 192.168.30.0/26 | 192.168.30.1-192.168.30.62 | 192.168.30.63 |
| Sales | 192.168.30.64/26 | 192.168.30.65-192.168.30.126 | 192.168.30.127 |
| Support | 192.168.30.128/26 | 192.168.30.129-192.168.30.190 | 192.168.30.191 |

## Step-by-Step Tasks

1. Place one switch and six PCs in Packet Tracer.
2. Connect all PCs to the switch.
3. Assign two PCs to each department.
4. Configure Admin PCs with IP addresses `192.168.30.11/26` and `192.168.30.12/26`.
5. Configure Sales PCs with IP addresses `192.168.30.71/26` and `192.168.30.72/26`.
6. Configure Support PCs with IP addresses `192.168.30.131/26` and `192.168.30.132/26`.
7. Leave the default gateway blank for now.
8. Ping between the two Admin PCs.
9. Ping from an Admin PC to a Sales PC.
10. Ping from a Sales PC to a Support PC.
11. Record which tests succeed and fail.

## Expected Result

Hosts in the same subnet should communicate directly. Hosts in different subnets should fail because no router or Layer 3 gateway exists yet.

## Student Deliverable

Submit a subnet table and explain why devices connected to the same switch may still fail to communicate when they are in different IP subnets.

---

