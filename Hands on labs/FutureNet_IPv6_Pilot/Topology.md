# FutureNet IPv6 Pilot - Topology
## Aligned Theory Lesson

Lesson 12

## Scenario Context

A small office wants to test IPv6 before production. Students configure IPv6 addresses, verify link-local addresses, and ping using IPv6.

## Physical Topology Requirement

PC1 and PC2 connect to SW1. SW1 connects to R1.

## Topology Picture

~~~mermaid
flowchart TD
  R1["R1 IPv6 Gateway<br/>2001:db8:12:1::1/64"]
  SW1["SW1"]
  PC1["PC1<br/>2001:db8:12:1::10/64"]
  PC2["PC2<br/>2001:db8:12:1::11/64"]
  R1 --- SW1
  PC1 --- SW1
  PC2 --- SW1
~~~

## Devices Required

1 router, 1 switch, 2 PCs

## Addressing Plan

IPv6 prefix 2001:db8:12:1::/64. R1 gateway 2001:db8:12:1::1/64. PC1 ::10/64, PC2 ::11/64.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.



