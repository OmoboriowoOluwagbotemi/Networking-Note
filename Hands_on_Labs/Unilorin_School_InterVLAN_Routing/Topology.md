# Unilorin School Inter-VLAN Routing - Topology

## Aligned Theory Lesson

Lesson 15

## Scenario Context

Management now wants controlled communication between Guests, Parents, Teachers, and Students. Students first learn the direct-cable method, then compare it with router-on-a-stick.

## Physical Topology Requirement

Method A: four switch access ports connect to four router interfaces, one per VLAN. Method B: one trunk connects switch to router subinterfaces.

Accuracy note for Packet Tracer: the direct-router-interface method requires a router model or added module with enough Ethernet interfaces for the VLANs being tested. If your selected router has only two or three Ethernet interfaces, test two or three VLANs with the direct method first, then complete all four VLANs with the router-on-a-stick method.

## Topology Picture

~~~mermaid
flowchart TD
  R1["R1<br/>Inter-VLAN Gateway"]
  SW1["SCHOOL_SW1<br/>VLAN Access Switch"]
  V10["VLAN 10 Guests<br/>192.168.10.0/24"]
  V20["VLAN 20 Parents<br/>192.168.20.0/24"]
  V30["VLAN 30 Teachers<br/>192.168.30.0/24"]
  V40["VLAN 40 Students<br/>192.168.40.0/24"]
  R1 ---|"direct interfaces or trunk subinterfaces"| SW1
  SW1 --- V10
  SW1 --- V20
  SW1 --- V30
  SW1 --- V40
~~~

## Devices Required

1 router, 1 switch, 4 PCs minimum

## Addressing Plan

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN30 192.168.30.0/24 gateway .1, VLAN40 192.168.40.0/24 gateway .1.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





