# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 10

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - DEPLOY DHCP, DNS, AND DHCP RELAY

## Aligned Lessons

This lab aligns with Lesson 19, DHCP and DNS Fundamentals.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will configure DHCP for multiple VLANs and use DHCP relay when the DHCP server is not in the same subnet as the clients.

## Important Why

This lab matters because DHCP and DNS are core services users depend on every day. When these services fail, users often say the network is down even when switching and routing are working.

## Important How

Students finish this lab by creating DHCP scopes, configuring DNS records, adding IP helper addresses, switching clients to DHCP, and proving clients receive correct settings.

## Scenario

The company wants clients in Admin and Sales VLANs to receive IP settings automatically. A central server provides DHCP and DNS.

## Network Plan

| VLAN | Name | Subnet | Gateway |
|---:|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.1 |
| 20 | SALES | 192.168.20.0/24 | 192.168.20.1 |
| 99 | SERVER | 192.168.99.0/24 | 192.168.99.1 |

## Step-by-Step Tasks

1. Build a router-on-a-stick or Layer 3 switch topology with VLAN 10, VLAN 20, and VLAN 99.
2. Place one server in VLAN 99.
3. Assign the server IP address `192.168.99.10/24`.
4. Set the server default gateway to `192.168.99.1`.
5. Open the server Services tab.
6. Enable DHCP.
7. Create a DHCP pool for VLAN 10 with gateway `192.168.10.1` and DNS server `192.168.99.10`.
8. Create a DHCP pool for VLAN 20 with gateway `192.168.20.1` and DNS server `192.168.99.10`.
9. Enable DNS service on the server.
10. Add an A record for `intranet.femtect.local` pointing to `192.168.99.10`.
11. On the router subinterface for VLAN 10, configure `ip helper-address 192.168.99.10`.
12. On the router subinterface for VLAN 20, configure `ip helper-address 192.168.99.10`.
13. Set client PCs to DHCP.
14. Confirm clients receive IP addresses automatically.
15. Test `ping intranet.femtect.local` from a client if Packet Tracer DNS behavior supports it.

## Verification Commands

```text
show ip interface brief
show running-config
ipconfig /all
nslookup
```

## Student Deliverable

Submit DHCP pool settings, client IP configuration results, and explain why DHCP relay is needed.

---

