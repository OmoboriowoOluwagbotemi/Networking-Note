# Lab 16 - Static Routes, Default Routes, and Floating Backup Route - Topology

## Aligned Theory Lesson

Lesson 16

## Scenario Context

A branch office must reach headquarters through a primary link and keep a backup route ready. Students configure static routes, default routes, and a floating static route.

## Physical Topology Requirement

Branch LAN--R1--R2--HQ LAN, with optional backup R1--R3--R2 path.

## Devices Required

3 routers, 2 switches, 2 PCs

## Addressing Plan

Branch LAN 192.168.160.0/24, R1-R2 10.0.12.0/30, R1-R3 10.0.13.0/30, R3-R2 10.0.23.0/30, HQ LAN 192.168.170.0/24.

## Physical Layout Guide

Arrange the Packet Tracer workspace so the topology is easy to read. Put network infrastructure devices such as switches, routers, access points, and servers near the top or center of the workspace. Put user devices below them in clear groups. Use Packet Tracer notes, labels, and colored shapes to identify departments, VLANs, networks, or roles.

## Cabling Guide

Use copper straight-through cables for PC-to-switch, server-to-switch, switch-to-router, and most modern switch-to-switch Packet Tracer connections unless a specific lab instruction says otherwise. If a router-to-router Ethernet link does not come up with straight-through, use crossover or the automatic cable option.

## Topology Evidence Students Must Submit

1. Screenshot of the complete physical topology.
2. Screenshot showing device names and labels clearly.
3. Screenshot or written table showing the addressing plan.
4. Screenshot of link lights after the topology is fully connected.
