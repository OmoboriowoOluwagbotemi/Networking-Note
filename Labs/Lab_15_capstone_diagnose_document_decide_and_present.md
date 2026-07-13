# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 15

## Lab Title: Capstone - Diagnose, Document, Decide, and Present

## Aligned Lessons

This lab aligns with Lesson 25, Diagnose, Document, Decide, and reviews the full course.

## Main Tools

Cisco Packet Tracer, diagrams.net, and a text editor.

## Important Why

This lab is important because professional networking is not only about typing commands. A network professional must diagnose carefully, avoid random changes, document evidence, explain the root cause, and hand over a network so another technician can support it.

## Important How

Students will build or receive a small enterprise topology, introduce controlled faults, troubleshoot from Layer 1 to Layer 3 and services, fix one issue at a time, verify the result, and produce a portfolio-ready report.

## Required Network Components

| Component | Requirement |
|---|---|
| VLANs | Admin, Sales, Guest, Server |
| Switching | At least one trunk and multiple access ports |
| Routing | Inter-VLAN routing and a default route if internet simulation is included |
| Services | DHCP and DNS |
| Security | At least one ACL or port-security setting |
| Documentation | Logical diagram, IP table, change record, and RCA |

## Recommended VLAN Plan

| VLAN | Name | Subnet | Gateway |
|---:|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.1 |
| 20 | SALES | 192.168.20.0/24 | 192.168.20.1 |
| 30 | GUEST | 192.168.30.0/24 | 192.168.30.1 |
| 99 | SERVER | 192.168.99.0/24 | 192.168.99.1 |

## Detailed Step-by-Step Procedure

### Part A: Build the Healthy Baseline

1. Open Cisco Packet Tracer.
2. Build two switches named `SW1` and `SW2`.
3. Add one router named `R1`.
4. Add at least one PC for each VLAN.
5. Add one server in VLAN 99.
6. Create VLANs 10, 20, 30, and 99 on both switches.
7. Assign access ports to the correct VLANs.
8. Configure a trunk between SW1 and SW2.
9. Configure a trunk from SW1 to R1.
10. Configure router-on-a-stick subinterfaces on R1 for VLANs 10, 20, 30, and 99.
11. Configure the server with static IP `192.168.99.10/24`, gateway `192.168.99.1`.
12. Configure DHCP pools on the server or router.
13. Configure DNS on the server with a record such as `intranet.femtect.local` pointing to `192.168.99.10`.
14. Verify all clients receive correct IP information.
15. Verify Admin and Sales can reach the server.
16. Apply an ACL if required to restrict Guest access to the server.
17. Save the working Packet Tracer file as `Lab15_Healthy_Baseline.pkt`.

### Part B: Introduce Controlled Faults

Introduce at least three faults. The instructor may do this before giving the file to students.

1. Fault 1: Change one user switch port to the wrong VLAN.
2. Fault 2: Remove or misconfigure one default gateway or DHCP gateway.
3. Fault 3: Remove one VLAN from a trunk allowed list, misconfigure an ACL, or remove a route.
4. Save the broken version as `Lab15_Troubleshooting_Challenge.pkt`.

## Detailed Troubleshooting Procedure

### Part C: Write the Problem Statement

1. Do not change anything yet.
2. Write the user complaint in one sentence.
3. Example: `Sales users can get IP addresses but cannot reach the intranet server.`
4. Identify affected users.
5. Identify unaffected users.
6. Identify whether the problem appears to be one device, one VLAN, one service, or the whole site.

### Part D: Check Layer 1

1. On each affected PC, check that the cable link light is green.
2. On the switch, type:

```text
enable
show interfaces status
```

3. Confirm the affected ports show connected.
4. If a port is disconnected, fix the cable or port before moving upward.

### Part E: Check Layer 2

1. On the switch, type:

```text
show vlan brief
show interfaces trunk
show mac address-table dynamic
```

2. Confirm the affected PC port is in the correct VLAN.
3. Confirm the trunk allows the affected VLAN.
4. Confirm MAC addresses are being learned.
5. If a port is in the wrong VLAN, document the evidence before fixing it.
6. To fix a wrong access VLAN, type:

```text
configure terminal
interface fa0/x
 switchport mode access
 switchport access vlan <correct-vlan-id>
end
show vlan brief
```

Replace `fa0/x` and `<correct-vlan-id>` with the real port and VLAN.

### Part F: Check Layer 3 Host Settings

1. On the affected PC, open Desktop > Command Prompt.
2. Type `ipconfig /all` and press Enter.
3. Confirm the IP address belongs to the correct subnet.
4. Confirm the subnet mask is correct.
5. Confirm the default gateway matches the VLAN gateway.
6. Ping the default gateway.
7. If the PC cannot ping its gateway, return to Layer 1 and Layer 2 checks.

### Part G: Check Router-on-a-Stick or Layer 3 Gateway

On R1, type:

```text
enable
show ip interface brief
show running-config
show ip route
```

Confirm each VLAN subinterface exists, has the correct 802.1Q VLAN number, has the correct IP address, and is up/up.

### Part H: Check DHCP and DNS

1. If the PC uses DHCP, renew the IP address if Packet Tracer supports it by switching from Static to DHCP again.
2. On the DHCP server, check the pool settings.
3. Confirm the default gateway in the DHCP pool is correct.
4. Confirm DNS server settings are correct.
5. From the affected PC, ping the DNS server IP.
6. Test name resolution using `nslookup intranet.femtect.local` if available.
7. If DNS tools are limited in Packet Tracer, test by using the PC Web Browser to open `http://intranet.femtect.local`.

### Part I: Check ACLs and Security Controls

On R1, type:

```text
show access-lists
show running-config | include access-group
show running-config
```

1. Identify where the ACL is applied.
2. Identify whether it is inbound or outbound.
3. Check whether the ACL denies the affected subnet.
4. If an ACL is wrong, document the line and effect before correcting it.
5. After correction, test again from the affected PC.

### Part J: Make One Fix at a Time

1. Write the suspected fault.
2. Write the evidence.
3. Apply one change only.
4. Test again.
5. If the test improves, record the result.
6. If the test does not improve, reverse the change unless the instructor confirms it is still required.
7. Continue until all faults are fixed.

## Required Verification Commands

```text
show interfaces status
show vlan brief
show interfaces trunk
show spanning-tree
show ip interface brief
show ip route
show access-lists
show running-config
ping
tracert
ipconfig /all
nslookup
```

## Documentation Requirements

### Logical Diagram

1. Open diagrams.net.
2. Draw routers, switches, PCs, server, and WAN/internet if used.
3. Label VLAN IDs.
4. Label subnets.
5. Label default gateways.
6. Label trunks and routed links.

### IP Addressing Table

| Device | Interface | VLAN | IP Address | Gateway | Notes |
|---|---|---:|---|---|---|
|  |  |  |  |  |  |

### Troubleshooting Log

| Time | Test | Evidence | Action Taken | Result |
|---|---|---|---|---|
|  |  |  |  |  |

### Change Record

| Field | Student Entry |
|---|---|
| Change title |  |
| Reason for change |  |
| Device affected |  |
| Commands used |  |
| Risk |  |
| Rollback plan |  |
| Verification result |  |

### Root Cause Analysis

| Question | Student Answer |
|---|---|
| What failed? |  |
| Who was affected? |  |
| What evidence proved the issue? |  |
| What was the root cause? |  |
| What fixed it? |  |
| How can it be prevented? |  |

## Student Deliverable

Submit the final working Packet Tracer file, logical diagram, IP addressing table, troubleshooting log, change record, root cause analysis, and a one-page portfolio case study explaining the incident.
