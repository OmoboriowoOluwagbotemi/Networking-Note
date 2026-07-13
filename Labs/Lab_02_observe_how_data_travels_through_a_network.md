# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 2

## Lab Title: Observe How Data Travels Through a Network

## Aligned Lessons

This lab aligns with Lesson 3, How Data Travels Through a Network, Lesson 4, OSI Model Deep Dive, and Lesson 5, TCP/IP Protocol Suite.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because students must see that a successful ping is not a single mysterious action. Before ICMP can test reachability, the sender must know the destination MAC address for local delivery. ARP discovers that MAC address, Ethernet carries the frame, IP identifies the logical endpoints, and ICMP carries the test message.

This lab turns the theory of encapsulation into something visible. Students observe that Layer 2 addresses are used for local delivery, while Layer 3 addresses identify the source and destination hosts.

## Important How

Students will use Packet Tracer Simulation mode, filter for ARP and ICMP, send a ping, and step through each packet. They will open the packet details and record source and destination MAC addresses, source and destination IP addresses, and the protocol being used.

## Scenario

The simple LAN from Lab 1 works. A junior technician now needs to explain what happens when PC1 communicates with PC2.

## Required Topology

Use the Lab 1 topology with PC1, PC2, PC3, and SW1 in the same subnet.

## Detailed Step-by-Step Procedure

### Part A: Confirm the LAN Works

1. Open the Lab 1 Packet Tracer file or rebuild the Lab 1 topology.
2. Click PC1.
3. Click Desktop.
4. Click Command Prompt.
5. Type `ping 192.168.10.12` and press Enter.
6. Confirm PC1 can reach PC2.
7. Type `ping 192.168.10.13` and press Enter.
8. Confirm PC1 can reach PC3.

### Part B: Prepare Simulation Mode

1. At the bottom-right of Packet Tracer, click Simulation.
2. Locate the Event List panel.
3. Click Edit Filters.
4. Click Show All/None to clear all selected protocols.
5. Select only ARP and ICMP.
6. Close the filter window.
7. Click Delete or Clear Event List if old events are present.

### Part C: Clear ARP Knowledge by Power Cycling PC1

1. Click PC1.
2. Click the Physical tab.
3. Click the power button to turn PC1 off.
4. Wait two seconds.
5. Click the power button again to turn PC1 on.
6. Return to the Desktop tab.
7. Open Command Prompt again.
8. Type `arp -a` and press Enter.
9. Confirm that PC1 does not already have PC2's MAC address cached. If an entry still exists in Packet Tracer, continue; the lab can still show ICMP even if ARP is not repeated.

### Part D: Generate Traffic

1. In PC1 Command Prompt, type `ping 192.168.10.12` and press Enter.
2. Do not click Auto Capture immediately.
3. Click Capture/Forward one time.
4. Observe the first packet leaving PC1.
5. Click the packet envelope.
6. Review the OSI Model or Inbound/Outbound PDU Details tabs.
7. Identify whether the packet is ARP or ICMP.
8. Click Capture/Forward again.
9. Continue one step at a time until the ARP request reaches PC2.
10. Continue until the ARP reply returns to PC1.
11. Continue until ICMP echo request and ICMP echo reply packets complete the ping.

### Part E: Record Addressing Information

1. Click an ARP request packet.
2. Record the source MAC address.
3. Record the destination MAC address. For ARP request, the destination MAC should be a broadcast address.
4. Click an ICMP echo request packet.
5. Record the source IP address.
6. Record the destination IP address.
7. Record the source MAC address and destination MAC address used in the Ethernet frame.

## Verification Table

| Item to Observe | Expected Result |
|---|---|
| ARP request | Broadcast frame asking for PC2 MAC address |
| ARP reply | PC2 replies with its MAC address |
| ICMP echo request | PC1 sends ping request to PC2 |
| ICMP echo reply | PC2 replies to PC1 |
| Switch behavior | Switch forwards frames based on MAC table |

## Troubleshooting Notes

If ARP packets do not appear, PC1 may already know PC2's MAC address. Power cycle the PC or use a different destination PC. If ICMP fails, return to Lab 1 and verify IP addressing and cabling.

## Student Deliverable

Submit a table with one ARP request and one ICMP echo request. Include source MAC, destination MAC, source IP, destination IP, and protocol name.
