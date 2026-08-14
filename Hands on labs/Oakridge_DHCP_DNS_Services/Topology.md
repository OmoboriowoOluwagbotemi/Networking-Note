# Oakridge DHCP and DNS Services - Topology

## Aligned Theory Lesson

Lesson 18

## Scenario Context

A company wants automatic addressing and name resolution for two departments. The DHCP/DNS server is in the server VLAN, so router relay is required.

## Physical Topology Requirement

Router-on-a-stick connects VLAN10 Users, VLAN20 Admin, and VLAN99 Servers.

## Topology Picture

~~~mermaid
flowchart TD
  R1["R1 Router-on-a-Stick<br/>DHCP Relay"]
  SW1["SW1<br/>VLAN 10,20,99"]
  Users["VLAN10 Users<br/>DHCP Clients"]
  Admin["VLAN20 Admin<br/>DHCP Clients"]
  Server["VLAN99 Server<br/>DHCP + DNS<br/>192.168.99.10"]
  R1 ---|"Trunk"| SW1
  SW1 --- Users
  SW1 --- Admin
  SW1 --- Server
~~~

## Devices Required

1 router, 1 switch, 1 server, 4 PCs

## Addressing Plan

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN99 192.168.99.0/24 gateway .1, Server 192.168.99.10.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.





