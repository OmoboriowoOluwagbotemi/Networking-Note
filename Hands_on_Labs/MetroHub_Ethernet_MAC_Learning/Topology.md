# MetroHub Ethernet MAC Learning - Topology

## Aligned Theory Lesson

Lesson 8

## Scenario Context

A network technician must prove how a switch learns MAC addresses and forwards Ethernet frames. Students clear the MAC table, generate traffic, and observe learning.

## Physical Topology Requirement

PC1, PC2, and PC3 connect to SW1.

## Topology Picture

~~~mermaid
flowchart TD
  SW1["SW1<br/>MAC Address Table"]
  PC1["PC1<br/>192.168.90.10"]
  PC2["PC2<br/>192.168.90.11"]
  PC3["PC3<br/>192.168.90.12"]
  PC1 --- SW1
  PC2 --- SW1
  PC3 --- SW1
  PC1 -->|"ARP broadcast then ICMP"| PC2
~~~

## Devices Required

1 switch, 3 PCs

## Addressing Plan

PC1 192.168.90.10/24, PC2 192.168.90.11/24, PC3 192.168.90.12/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





