# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 15

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: CAPSTONE - DIAGNOSE, DOCUMENT, DECIDE, AND PRESENT

## Aligned Lessons

This lab aligns with Lesson 25, Diagnose, Document, Decide, and reviews the full course.

## Main Tools

Cisco Packet Tracer, diagrams.net, and a text editor.

## Lab Goal

Students will troubleshoot a multi-layer network fault, document the network, produce a change record, and present a portfolio-ready case study.

## Important Why

This lab matters because professional networking is not only configuration. A network professional must diagnose, document, decide, communicate, and leave evidence that another technician can trust.

## Important How

Students finish this lab by troubleshooting controlled faults, recording evidence, fixing one issue at a time, creating diagrams and tables, and presenting a portfolio-ready case study.

## Scenario

FEMTECT has a small enterprise network with VLANs, inter-VLAN routing, DHCP, DNS, NAT, wireless, and basic security. Several users report that some devices cannot access internal services and others cannot reach the internet. Students must diagnose the issue carefully, avoid random changes, document the root cause, and verify the fix.

## Required Network Components

| Component | Requirement |
|---|---|
| VLANs | Admin, Sales, Guest, Server |
| Routing | Inter-VLAN routing and default route |
| Services | DHCP and DNS |
| Internet access | NAT/PAT |
| Security | At least one ACL and SSH management |
| Documentation | Physical and logical diagram |

## Faults to Introduce

The instructor or student should introduce at least three faults:

1. One wrong access VLAN on a switch port.
2. One missing default gateway or wrong DHCP gateway.
3. One missing route, NAT rule, or ACL mistake.

## Step-by-Step Troubleshooting Method

1. Write the user complaint as a problem statement.
2. Define the scope: one user, one VLAN, one department, or whole site.
3. Start with Layer 1 by checking cables and interface status.
4. Check Layer 2 by verifying VLAN membership and trunks.
5. Check Layer 3 by verifying IP address, subnet mask, default gateway, and routing table.
6. Check services by verifying DHCP and DNS.
7. Check internet access by verifying default route and NAT.
8. Check security policy by reviewing ACL hit counts and denied traffic.
9. Make only one change at a time.
10. Test after each change.
11. Record the command used, observation, change made, and result.
12. Confirm the final fix from more than one client.

## Useful Verification Commands

```text
show ip interface brief
show vlan brief
show interfaces trunk
show spanning-tree
show ip route
show access-lists
show ip nat translations
show running-config
ping
traceroute
ipconfig /all
nslookup
```

## Documentation Tasks

1. Create a logical diagram in diagrams.net.
2. Label all VLANs, subnets, gateways, and major devices.
3. Create an IP addressing table.
4. Create a device inventory table.
5. Create a change record.
6. Create a root cause analysis.
7. Create a final handover note.

## Change Record Template

| Field | Student Entry |
|---|---|
| Change title |  |
| Reason for change |  |
| Devices affected |  |
| Pre-checks completed |  |
| Commands used |  |
| Expected result |  |
| Actual result |  |
| Rollback plan |  |
| Final verification |  |

## Root Cause Analysis Template

| Question | Student Answer |
|---|---|
| What failed? |  |
| Who was affected? |  |
| When was it discovered? |  |
| What evidence proved the issue? |  |
| What was the root cause? |  |
| What fixed it? |  |
| What should prevent recurrence? |  |

## Student Deliverable

Submit the final Packet Tracer file, logical diagram, addressing table, troubleshooting log, change record, root cause analysis, and a one-page portfolio case study.

---

