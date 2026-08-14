# Summit Branch Subnetting - Topology
## Aligned Theory Lesson

Lesson 11

## Scenario Context

A branch received 192.168.120.0/24 and must divide it into Admin, Sales, and Support networks. Students calculate subnets, assign gateways, and verify routing.

## Physical Topology Requirement

R1 connects separately to Admin-SW, Sales-SW, and Support-SW.

## Topology Picture

~~~mermaid
flowchart TD
  R1["R1<br/>Three Department Gateways"]
  ASW["Admin-SW<br/>192.168.120.0/26"]
  SSW["Sales-SW<br/>192.168.120.64/26"]
  SUPSW["Support-SW<br/>192.168.120.128/26"]
  R1 ---|".1"| ASW
  R1 ---|".65"| SSW
  R1 ---|".129"| SUPSW
  ASW --- A1["Admin PCs"]
  SSW --- S1["Sales PCs"]
  SUPSW --- U1["Support PCs"]
~~~

## Devices Required

1 router, 3 switches, 6 PCs

## Addressing Plan

Admin 192.168.120.0/26 gateway .1, Sales 192.168.120.64/26 gateway .65, Support 192.168.120.128/26 gateway .129.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.



