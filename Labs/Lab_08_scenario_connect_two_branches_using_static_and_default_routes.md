# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 8

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - CONNECT TWO BRANCHES USING STATIC AND DEFAULT ROUTES

## Aligned Lessons

This lab aligns with Lesson 17, How Routers Work, Static and Default Routing.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will connect two branch LANs using routers and configure static routes and default routes.

## Important Why

This lab matters because routers do not automatically know every remote network. Static and default routes teach students how routers make forwarding decisions and why return paths are required.

## Important How

Students finish this lab by configuring router interfaces, adding static routes to remote LANs, testing end-to-end communication, and reading the routing table.

## Scenario

FEMTECT has a Lagos office and an Abuja office. Each office has its own LAN. The two offices are connected through a WAN link, but users cannot communicate until routing is configured.

## Addressing Table

| Device/Network | Address |
|---|---|
| Lagos LAN | 192.168.100.0/24 |
| Abuja LAN | 192.168.200.0/24 |
| WAN Link | 10.10.10.0/30 |
| Lagos Router LAN IP | 192.168.100.1 |
| Abuja Router LAN IP | 192.168.200.1 |
| Lagos Router WAN IP | 10.10.10.1 |
| Abuja Router WAN IP | 10.10.10.2 |

## Step-by-Step Tasks

1. Place two routers, two switches, and two PCs.
2. Name the routers R-LAGOS and R-ABUJA.
3. Connect each PC to its local switch.
4. Connect each switch to its local router LAN interface.
5. Connect the routers using a serial or gigabit link depending on available Packet Tracer router model.
6. Configure IP addresses on router LAN and WAN interfaces.
7. Configure PC-LAGOS as `192.168.100.10/24` with gateway `192.168.100.1`.
8. Configure PC-ABUJA as `192.168.200.10/24` with gateway `192.168.200.1`.
9. From R-LAGOS, configure `ip route 192.168.200.0 255.255.255.0 10.10.10.2`.
10. From R-ABUJA, configure `ip route 192.168.100.0 255.255.255.0 10.10.10.1`.
11. Test ping from PC-LAGOS to PC-ABUJA.
12. Run `tracert` from PC-LAGOS to PC-ABUJA.
13. On each router, run `show ip route`.

## Verification Commands

```text
show ip interface brief
show ip route
ping
traceroute
```

## Student Deliverable

Submit both routing tables and explain why each router needs a route to the remote LAN.

---

