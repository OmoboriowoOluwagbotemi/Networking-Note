# Pacesetters Multi-Switch Trunking and STP - Topology
## Aligned Theory Lesson

Lesson 14

## Scenario Context

The school now has two floors. VLANs must work across two switches, and students must verify trunking and Spanning Tree behavior.

## Physical Topology Requirement

SW1 connects to SW2 using two links. PCs for each VLAN exist on both switches.

## Topology Picture

~~~mermaid
flowchart TD
  SW1["SW1<br/>Floor 1"]
  SW2["SW2<br/>Floor 2"]
  SW1 ===|"Trunk Fa0/23<br/>VLANs 10,20,30,40"| SW2
  SW1 ===|"Redundant trunk Fa0/24<br/>STP blocks one path"| SW2
  SW1 --- F1["Floor 1 PCs<br/>VLAN 10/20/30/40"]
  SW2 --- F2["Floor 2 PCs<br/>VLAN 10/20/30/40"]
~~~

## Devices Required

2 switches, 8 PCs

## Addressing Plan

Use VLANs 10, 20, 30, 40. Same subnets as Lab 13.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.



