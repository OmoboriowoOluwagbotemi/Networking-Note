# Mount Carmel School VLAN Segmentation - Topology

## Aligned Theory Lesson

Lesson 13

## Scenario Context

A school has one switch but four user groups must be separated: Guests, Parents, Teachers, and Students. Students build the topology shown in the supplied VLAN screenshots and prove that VLANs isolate broadcasts.

## Physical Topology Requirement

One central switch connects to eight PCs grouped into four colored departments, two PCs per department.

## Topology Picture

~~~mermaid
flowchart TD
  SW1["SCHOOL_SW1<br/>One 2960 Switch"]
  G["Guests VLAN 10<br/>PC1-PC2<br/>192.168.10.10-11"]
  P["Parents VLAN 20<br/>PC3-PC4<br/>192.168.20.12-13"]
  T["Teachers VLAN 30<br/>PC5-PC6<br/>192.168.30.14-15"]
  S["Students VLAN 40<br/>PC7-PC8<br/>192.168.40.16-17"]
  G --- SW1
  P --- SW1
  T --- SW1
  S --- SW1
~~~

## Devices Required

1 switch, 8 PCs

## Addressing Plan

Guests VLAN10 192.168.10.10-11/24, Parents VLAN20 192.168.20.12-13/24, Teachers VLAN30 192.168.30.14-15/24, Students VLAN40 192.168.40.16-17/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





