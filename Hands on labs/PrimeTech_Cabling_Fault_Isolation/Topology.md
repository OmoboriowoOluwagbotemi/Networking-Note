# PrimeTech Cabling Fault Isolation - Topology

## Aligned Theory Lesson

Lesson 7

## Scenario Context

A newly installed training room has intermittent connectivity. Students must choose correct cables, verify link lights, and isolate physical faults before blaming IP addressing.

## Physical Topology Requirement

PC1 and PC2 connect to SW1. PC3 and PC4 connect to SW2. SW1 connects to SW2.

## Topology Picture

~~~mermaid
flowchart LR
  PC1["PC1<br/>192.168.80.10"] --- SW1["SW1"]
  PC2["PC2<br/>192.168.80.11"] --- SW1
  SW1 ---|"uplink under test"| SW2["SW2"]
  SW2 --- PC3["PC3<br/>192.168.80.12"]
  SW2 --- PC4["PC4<br/>192.168.80.13"]
~~~

## Devices Required

2 switches, 4 PCs

## Addressing Plan

All PCs in 192.168.80.0/24: PC1 .10, PC2 .11, PC3 .12, PC4 .13.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





