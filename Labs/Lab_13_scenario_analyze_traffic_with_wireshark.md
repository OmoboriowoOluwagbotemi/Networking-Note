# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 13

## Lab Title: Scenario - Analyze Traffic With Wireshark

## Aligned Lessons

This lab aligns with Lesson 5, TCP/IP Protocol Suite, Lesson 6, Common Ports, Protocols, and Traffic Types, Lesson 19, DHCP and DNS Fundamentals, and Lesson 21, Wireless and Network Security Foundations.

## Main Tools

Wireshark, Windows Command Prompt or PowerShell, and Linux terminal.

## Important Why

This lab is important because packet captures help technicians prove what is happening instead of guessing. If DNS fails, the capture can show whether a query was sent and whether a response returned. If ping fails, the capture can show whether ARP or ICMP worked.

## Important How

Students will capture real traffic, apply Wireshark display filters, identify request-and-response behavior, and write what each protocol proves during troubleshooting.

## Detailed Step-by-Step Procedure

### Part A: Start a Capture

1. Open Wireshark.
2. Identify the active network adapter. On Wi-Fi, choose the Wi-Fi adapter. On wired Ethernet, choose the Ethernet adapter.
3. Double-click the active adapter to start capturing.
4. Confirm packets begin appearing.

### Part B: Generate ARP and ICMP Traffic

1. Open Command Prompt.
2. Type `ipconfig` and press Enter.
3. Record the default gateway IP address.
4. Type `arp -d *` and press Enter if Windows allows it. You may need administrator rights. If it fails, continue.
5. Type `ping <default-gateway-ip>` and press Enter.
6. Return to Wireshark.
7. In the display filter bar, type `arp` and press Enter.
8. Look for ARP request and ARP reply packets.
9. Change the filter to `icmp` and press Enter.
10. Look for echo request and echo reply packets.

### Part C: Generate DNS Traffic

1. Return to Command Prompt.
2. Type `nslookup example.com` and press Enter.
3. Return to Wireshark.
4. In the display filter bar, type `dns` and press Enter.
5. Identify the DNS query for `example.com`.
6. Identify the DNS response.
7. Record the DNS server IP address.

### Part D: Generate TCP and HTTPS Traffic

1. Open a web browser.
2. Visit `https://example.com`.
3. Return to Wireshark.
4. In the display filter bar, type `tcp.port == 443` and press Enter.
5. Look for TCP packets using destination or source port 443.
6. If visible, identify the TCP three-way handshake: SYN, SYN/ACK, ACK.
7. Understand that HTTPS payload content is encrypted, so you should not expect to read the web page text in clear form.

### Part E: Save and Document Evidence

1. Click File.
2. Click Save As.
3. Save the capture as `Lab13_protocol_evidence.pcapng` if required by the instructor.
4. Take screenshots of the ARP, ICMP, DNS, and TCP 443 filters.
5. For each screenshot, write one sentence explaining what it proves.

## Display Filters

```text
arp
icmp
dns
tcp.port == 443
ip.addr == <your-ip-address>
```

## Verification Table

| Protocol | What Students Should Identify | What It Proves |
|---|---|---|
| ARP | Request and reply | Local MAC discovery |
| ICMP | Echo request and reply | Basic reachability |
| DNS | Query and response | Name resolution |
| TCP 443 | TCP session to HTTPS service | Web application transport path |

## Accuracy Note

Some networks use encrypted DNS, local DNS proxies, firewall filtering, or ICMP blocking. If a packet type is not visible, students should document what they did see and explain possible reasons.

## Student Deliverable

Submit four screenshots with protocol filters and a short evidence explanation for each one.
