# Northstar Service Port Testing - Topology
## Aligned Theory Lesson

Lesson 6

## Scenario Context

A company server hosts web, DNS, and file-transfer services. Students enable services, test ports, and identify which application uses which traffic type.

## Physical Topology Requirement

PC1 and SRV1 connect to SW1.

## Topology Picture

~~~mermaid
flowchart TD
  PC1["PC1<br/>192.168.70.10"]
  SW1["SW1"]
  SRV1["SRV1<br/>192.168.70.20<br/>HTTP DNS FTP"]
  PC1 --- SW1
  SRV1 --- SW1
  PC1 -->|"DNS 53"| SRV1
  PC1 -->|"HTTP 80 / FTP 21"| SRV1
~~~

## Devices Required

1 switch, 1 PC, 1 server

## Addressing Plan

PC1 192.168.70.10/24 DNS 192.168.70.20. SRV1 192.168.70.20/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.



