# FEMTECT Final Network Operations Case - Topology

## Aligned Theory Lesson

Lesson 20

## Scenario Context

A small organization reports that users cannot reach a server after a change. Students diagnose Layer 1 to Layer 3, harden management access, document the fix, and prepare a handover report.

## Physical Topology Requirement

User VLANs connect through SW1 and R1 to R2 and the server network.

## Topology Picture

~~~mermaid
flowchart LR
  Users["User VLAN10 PCs"] --- SW1["SW1<br/>Access Switch"]
  Admin["Admin VLAN20 PCs"] --- SW1
  SW1 --- R1["R1<br/>Gateway + SSH"]
  R1 ---|"WAN 10.20.20.0/30"| R2["R2<br/>Server Router"]
  R2 --- SW2["Server Switch"]
  SW2 --- Server["Application Server<br/>172.20.20.0/24"]
~~~

## Devices Required

2 routers, 2 switches, 4 PCs, 1 server

## Addressing Plan

Users VLAN10 192.168.10.0/24, Admin VLAN20 192.168.20.0/24, WAN 10.20.20.0/30, Server LAN 172.20.20.0/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





