# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 3

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: VERIFY REAL HOST NETWORK SETTINGS AND CAPTURE BASIC TRAFFIC

## Aligned Lessons

This lab aligns with Lesson 4, OSI Model Deep Dive, Lesson 5, TCP/IP Protocol Suite, and Lesson 6, Common Ports, Protocols, and Traffic Types.

## Main Tools

Windows Command Prompt or PowerShell, Linux terminal, and Wireshark.

## Lab Goal

Students will inspect real network configuration on a computer and use Wireshark to observe ARP, ICMP, DNS, and TCP/HTTPS traffic.

## Important Why

This lab matters because real IT Support work starts on the user device. A technician who can read host IP settings, test the gateway, test DNS, and capture packets can separate user-device problems from network problems.

## Important How

Students finish this lab by collecting host configuration, testing loopback, gateway, internet IP, and DNS, then using Wireshark filters to connect command output with packet evidence.

## Scenario

An IT Support technician must verify whether a user computer has valid network settings and whether traffic is leaving the computer correctly.

## Step-by-Step Tasks on Windows

1. Open Command Prompt.
2. Run `ipconfig /all`.
3. Identify the IPv4 address, subnet mask, default gateway, DNS server, and MAC address.
4. Run `ping 127.0.0.1`.
5. Run `ping <your-default-gateway>`.
6. Run `ping 8.8.8.8`.
7. Run `nslookup google.com`.
8. Run `tracert 8.8.8.8`.
9. Record each result.

## Step-by-Step Tasks on Linux

1. Open the terminal.
2. Run `ip addr`.
3. Run `ip route`.
4. Run `ping -c 4 127.0.0.1`.
5. Run `ping -c 4 <your-default-gateway>`.
6. Run `ping -c 4 8.8.8.8`.
7. Run `dig google.com`.
8. Run `traceroute 8.8.8.8` if traceroute is installed.

## Step-by-Step Tasks in Wireshark

1. Open Wireshark.
2. Select the active network adapter.
3. Start a capture.
4. In Command Prompt or terminal, ping the default gateway.
5. Stop the capture after the ping completes.
6. Use the filter `arp`.
7. Use the filter `icmp`.
8. Use the filter `dns`.
9. Use the filter `tcp.port == 443`.
10. Visit a secure website in a browser and observe TCP/HTTPS-related packets.

## Verification

| Test | Meaning |
|---|---|
| Loopback ping works | Local TCP/IP stack is working |
| Gateway ping works | Local LAN path is working |
| 8.8.8.8 ping works | Internet Layer 3 connectivity is working |
| DNS lookup works | Name resolution is working |
| Wireshark shows ARP/ICMP/DNS | Traffic is visible and interpretable |

## Student Deliverable

Submit a short host network report showing IP settings, gateway test, DNS test, and one Wireshark screenshot.

---

