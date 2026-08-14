# CarePoint IPv4 Addressing Repair - Topology
## Aligned Theory Lesson

Lesson 10

## Scenario Context

A support technician must configure PCs correctly and identify when a host is in the wrong network or has an APIPA-style address.

## Physical Topology Requirement

PCs connect to SW1. SW1 connects to R1.

## Topology Picture

~~~mermaid
flowchart TD
  R1["R1 Gateway<br/>192.168.110.1/24"]
  SW1["SW1"]
  PC1["PC1<br/>192.168.110.10"]
  PC2["PC2<br/>192.168.110.11"]
  PC3["PC3<br/>wrong IP first<br/>then 192.168.110.12"]
  R1 --- SW1
  PC1 --- SW1
  PC2 --- SW1
  PC3 --- SW1
~~~

## Devices Required

1 router, 1 switch, 3 PCs

## Addressing Plan

LAN 192.168.110.0/24 gateway 192.168.110.1. PC1 .10, PC2 .11, PC3 intentionally wrong first.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.



