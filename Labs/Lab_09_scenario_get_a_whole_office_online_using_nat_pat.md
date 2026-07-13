# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 9

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - GET A WHOLE OFFICE ONLINE USING NAT/PAT

## Aligned Lessons

This lab aligns with Lesson 18, Dynamic Routing and NAT/PAT.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will configure PAT so multiple private inside hosts can share one public IP address.

## Important Why

This lab matters because most offices use private IP addresses internally and share one or a few public IP addresses externally. NAT/PAT is one of the most common technologies used to get a whole office online.

## Important How

Students finish this lab by marking inside and outside NAT interfaces, creating the NAT ACL, enabling PAT overload, testing outside connectivity, and viewing NAT translations.

## Scenario

A small office has many private IP hosts but only one public IP address from the ISP. The router must translate inside private addresses to the outside public address.

## Addressing Plan

| Area | Network |
|---|---|
| Inside LAN | 192.168.50.0/24 |
| ISP Link | 203.0.113.0/30 |
| Office Router Inside | 192.168.50.1 |
| Office Router Outside | 203.0.113.2 |
| ISP Router | 203.0.113.1 |

## Step-by-Step Tasks

1. Place one office router, one ISP router, one switch, two PCs, and one server.
2. Connect PCs to the office switch.
3. Connect the switch to the office router inside interface.
4. Connect the office router outside interface to the ISP router.
5. Connect the server to the ISP router.
6. Configure the inside LAN IP addresses.
7. Configure the ISP link addresses.
8. Configure a default route on the office router pointing to `203.0.113.1`.
9. Configure a return route on the ISP router pointing to `203.0.113.2` if needed for simulation.
10. Create ACL 1 matching `192.168.50.0 0.0.0.255`.
11. Configure the inside router interface with `ip nat inside`.
12. Configure the outside router interface with `ip nat outside`.
13. Configure PAT with `ip nat inside source list 1 interface <outside-interface> overload`.
14. Ping the outside server from both PCs.
15. Run `show ip nat translations`.

## Cisco IOS Configuration Example

```text
access-list 1 permit 192.168.50.0 0.0.0.255

interface g0/0
 ip nat inside

interface g0/1
 ip nat outside

ip nat inside source list 1 interface g0/1 overload
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

## Student Deliverable

Submit NAT translation output and explain the difference between inside local and inside global addresses.

---

