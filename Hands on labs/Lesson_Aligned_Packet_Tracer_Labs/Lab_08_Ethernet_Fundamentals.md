# Lab 08 - MAC Address Learning and Ethernet Frame Forwarding

## Aligned Theory Lesson

Lesson 8

## Scenario

A network technician must prove how a switch learns MAC addresses and forwards Ethernet frames. Students clear the MAC table, generate traffic, and observe learning.

## Devices Required

1 switch, 3 PCs

## Physical Topology

PC1, PC2, and PC3 connect to SW1.

## Addressing Plan

PC1 192.168.90.10/24, PC2 192.168.90.11/24, PC3 192.168.90.12/24.

## Standard Packet Tracer Working Method

Use Cisco Packet Tracer for this lab. Build the topology first, label every device, connect the correct cables, configure the devices, then verify with commands and screenshots. Do not move to the next task until the current task works.

When a Cisco switch or router must be configured, use this exact access method:

1. Click the Cisco device.
2. Click the CLI tab.
3. If Packet Tracer asks "Continue with configuration dialog?", type "no" and press Enter.
4. Press Enter again if the prompt is blank.
5. Type enable and press Enter.
6. Type configure terminal and press Enter.
7. Paste or type the lab commands carefully.
8. Use "end" to return to privileged EXEC mode.
9. Run the verification commands.
10. Type "copy running-config startup-config" and press Enter to save.

Use this cable rule unless the lab states otherwise: PC/server to switch uses copper straight-through, switch to router uses copper straight-through, switch to switch can use copper straight-through in modern Packet Tracer devices, and router-to-router Ethernet links use crossover or automatic connection depending on the device model.

## Step-by-Step Tasks

1. Build one switch with three PCs.
2. Configure all PC IP addresses in 192.168.90.0/24.
3. Open SW1 CLI and check the MAC address table before traffic.
4. Ping from PC1 to PC2.
5. Check the MAC address table again.
6. Ping from PC1 to PC3 and check the table again.
7. Use Simulation Mode to observe ARP broadcast and unicast ICMP replies.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
end
show mac address-table
clear mac address-table dynamic
show mac address-table
~~~

## Verification

After pings, SW1 should learn MAC addresses on the correct ports. ARP request should flood; later frames should forward based on the MAC table.

## Troubleshooting Checklist

- Check cable type and link lights before changing IP settings.
- Confirm every PC has the correct IP address, subnet mask, and default gateway when a gateway is required.
- Confirm switch access ports are in the correct VLAN when VLANs are used.
- Confirm trunk links allow the required VLANs when traffic crosses switches or router subinterfaces.
- Confirm router interfaces are up/up before testing routes.
- Use ping first, then use tracert or traceroute when traffic crosses routers.
- Record the exact command output that proves the lab works.

## Student Deliverables

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.
