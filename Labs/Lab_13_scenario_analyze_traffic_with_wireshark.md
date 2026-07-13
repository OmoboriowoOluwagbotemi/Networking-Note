# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 13

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - ANALYZE TRAFFIC WITH WIRESHARK

## Aligned Lessons

This lab aligns with Lesson 5, TCP/IP Protocol Suite, Lesson 6, Common Ports, Protocols, and Traffic Types, Lesson 19, DHCP and DNS Fundamentals, and Lesson 21, Wireless and Network Security Foundations.

## Main Tools

Wireshark, Windows Command Prompt or PowerShell, and Linux terminal.

## Lab Goal

Students will capture and interpret real protocol behavior, including ARP, ICMP, DNS, TCP, and DHCP where available.

## Important Why

This lab matters because packet evidence is stronger than guessing. Wireshark helps students prove whether ARP, ICMP, DNS, TCP, and HTTPS traffic are behaving normally.

## Important How

Students finish this lab by capturing traffic, filtering by protocol, identifying request and response behavior, and writing what each packet type proves during troubleshooting.

## Scenario

A user says, "The internet is not working." The technician must capture evidence instead of guessing.

## Step-by-Step Tasks

1. Open Wireshark.
2. Select the active network adapter.
3. Start a packet capture.
4. Open Command Prompt or terminal.
5. Run a ping to the default gateway.
6. Run a DNS lookup for `example.com`.
7. Open a browser and visit `https://example.com`.
8. Stop the capture.
9. Apply the display filter `arp`.
10. Identify one ARP request and one ARP reply.
11. Apply the display filter `icmp`.
12. Identify echo request and echo reply packets.
13. Apply the display filter `dns`.
14. Identify the DNS query and DNS response.
15. Apply the display filter `tcp.port == 443`.
16. Observe the TCP handshake and encrypted HTTPS traffic.
17. Save the capture file for documentation.

## Evidence Table

| Protocol | What to Identify | Why It Matters |
|---|---|---|
| ARP | MAC address resolution | Proves local LAN discovery |
| ICMP | Echo request and reply | Proves basic reachability |
| DNS | Query and response | Proves name resolution |
| TCP 443 | Handshake and encrypted session | Proves application path to HTTPS service |

## Student Deliverable

Submit one screenshot for each protocol filter and a short explanation of what the packet evidence proves.

---

