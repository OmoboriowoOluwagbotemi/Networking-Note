# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 3

## Lab Title: Verify Real Host Network Settings and Capture Basic Traffic

## Aligned Lessons

This lab aligns with Lesson 4, OSI Model Deep Dive, Lesson 5, TCP/IP Protocol Suite, and Lesson 6, Common Ports, Protocols, and Traffic Types.

## Main Tools

Windows Command Prompt or PowerShell, Linux terminal, and Wireshark.

## Important Why

This lab is important because real troubleshooting often begins on the user's computer, not on a router or switch. If a host has the wrong IP address, missing gateway, wrong DNS server, or failed local adapter, the wider network may be healthy but the user will still report that the network is down.

Wireshark is included because packet evidence helps students avoid guessing. Seeing ARP, ICMP, DNS, TCP, and HTTPS traffic helps students connect command-line tests to actual packets.

## Important How

Students will inspect host addressing, test the TCP/IP stack, test the default gateway, test internet reachability by IP, test DNS by name, trace the path, and capture packet evidence in Wireshark. If internet access is unavailable in the classroom, students should still complete the loopback and gateway tests.

## Detailed Step-by-Step Procedure on Windows

### Part A: Identify Host Settings

1. Click Start.
2. Type `cmd`.
3. Open Command Prompt.
4. Type `ipconfig /all` and press Enter.
5. Find the active adapter. It is usually named Wi-Fi or Ethernet.
6. Record the IPv4 Address.
7. Record the Subnet Mask.
8. Record the Default Gateway.
9. Record the DNS Servers.
10. Record the Physical Address. This is the MAC address.

### Part B: Test the Local TCP/IP Stack

1. In Command Prompt, type `ping 127.0.0.1` and press Enter.
2. Confirm replies are received.
3. If this fails, the local TCP/IP stack or firewall/security software may be involved.

### Part C: Test the Local Adapter IP

1. Type `ping <your-own-ip-address>` and press Enter.
2. Replace `<your-own-ip-address>` with the IPv4 address found in `ipconfig /all`.
3. Confirm replies are received.
4. If this fails, check the adapter configuration.

### Part D: Test the Default Gateway

1. Type `ping <default-gateway-ip>` and press Enter.
2. Replace `<default-gateway-ip>` with the gateway shown in `ipconfig /all`.
3. Confirm replies are received.
4. If this fails, the issue may be local Wi-Fi, Ethernet cabling, VLAN assignment, or gateway reachability.

### Part E: Test Internet Reachability by IP

1. Type `ping 8.8.8.8` and press Enter.
2. If replies are received, Layer 3 internet reachability is working.
3. If the ping fails, do not conclude DNS is broken yet because this test does not use DNS.

### Part F: Test DNS

1. Type `nslookup example.com` and press Enter.
2. Confirm a DNS server replies.
3. Confirm at least one IP address is returned.
4. If `ping 8.8.8.8` works but `nslookup example.com` fails, suspect DNS.

### Part G: Trace the Path

1. Type `tracert 8.8.8.8` and press Enter.
2. Record the first hop.
3. The first hop should normally be the default gateway or upstream router.
4. Some hops may show asterisks because routers may block ICMP time-exceeded responses. That does not always mean the network is down.

## Detailed Step-by-Step Procedure on Linux

1. Open Terminal.
2. Type `ip addr` and press Enter.
3. Record the active interface IP address.
4. Type `ip route` and press Enter.
5. Record the default route.
6. Type `ping -c 4 127.0.0.1` and press Enter.
7. Type `ping -c 4 <default-gateway-ip>` and press Enter.
8. Type `ping -c 4 8.8.8.8` and press Enter.
9. Type `dig example.com` and press Enter. If `dig` is not installed, use `nslookup example.com`.
10. Type `traceroute 8.8.8.8` if traceroute is installed.

## Detailed Step-by-Step Procedure in Wireshark

1. Open Wireshark.
2. Select the active Ethernet or Wi-Fi adapter.
3. Click the blue shark-fin icon to start capturing.
4. Open Command Prompt or Terminal.
5. Ping the default gateway.
6. Run `nslookup example.com`.
7. Open a browser and visit `https://example.com`.
8. Return to Wireshark.
9. Click the red square to stop capturing.
10. In the display filter bar, type `arp` and press Enter.
11. Identify ARP request and reply packets if present.
12. Change the filter to `icmp` and press Enter.
13. Identify echo request and echo reply packets.
14. Change the filter to `dns` and press Enter.
15. Identify the DNS query and response.
16. Change the filter to `tcp.port == 443` and press Enter.
17. Identify TCP traffic related to HTTPS.
18. Save the capture if the instructor requires it.

## Verification Table

| Test | Correct Meaning |
|---|---|
| `ping 127.0.0.1` works | Local TCP/IP stack responds |
| Gateway ping works | Local network path is reachable |
| `ping 8.8.8.8` works | Remote IP reachability exists |
| `nslookup example.com` works | DNS resolution works |
| Wireshark shows traffic | Packet evidence supports the tests |

## Accuracy Note

Some networks block ping or traceroute. A blocked ICMP reply does not always mean the network is fully down. Use multiple tests before reaching a conclusion.

## Student Deliverable

Submit host IP settings, command results, and screenshots showing at least two Wireshark filters.
