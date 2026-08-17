# Greenfield ICT TCP/IP Services - Topology

## Aligned Theory Lesson

Lesson 5

## Scenario Context

A school ICT room has a web server and DNS server. Students observe ARP, ICMP, DNS, TCP, and HTTP behavior using Packet Tracer Simulation Mode.

## Physical Topology Requirement

PC1 and SERVER1 connect to SW1.

## Topology Picture

~~~mermaid
flowchart TD
  PC1["PC1<br/>192.168.60.10<br/>DNS: 192.168.60.20"]
  SW1["SW1"]
  SERVER1["SERVER1<br/>HTTP + DNS<br/>192.168.60.20"]
  PC1 --- SW1
  SERVER1 --- SW1
  PC1 -->|"ping, DNS, HTTP"| SERVER1
~~~

## Devices Required

1 switch, 1 PC, 1 server

## Addressing Plan

PC1 192.168.60.10/24 DNS 192.168.60.20. SERVER1 192.168.60.20/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





