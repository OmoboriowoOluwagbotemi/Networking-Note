# Lab 04 - Packet Journey from LAN Client to Remote Server

## Aligned Theory Lesson

Lesson 4

## Scenario

A clinic workstation must reach a server on a different network. Students trace the packet journey through a router and explain how frames change while IP packets move toward the destination.

## Devices Required

2 routers, 2 switches, 1 PC, 1 server

## Physical Topology

PC1--SW1--R1--R2--SW2--WEB1

## Addressing Plan

LAN 192.168.50.0/24, WAN 10.10.10.0/30, Server LAN 172.16.50.0/24.

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

1. Build the topology PC1 to SW1, SW1 to R1, R1 to R2, R2 to SW2, SW2 to WEB1.
2. Configure PC1 as 192.168.50.10/24 gateway 192.168.50.1.
3. Configure WEB1 as 172.16.50.10/24 gateway 172.16.50.1 and enable HTTP.
4. Configure R1 and R2 using the commands below.
5. Use Simulation Mode to send a ping from PC1 to WEB1.
6. Inspect the PDU at each hop and record source and destination MAC changes.
7. Confirm Layer 3 source and destination IP addresses stay focused on PC1 and WEB1.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
! R1
enable
configure terminal
hostname R1
interface g0/0
ip address 192.168.50.1 255.255.255.0
no shutdown
exit
interface g0/1
ip address 10.10.10.1 255.255.255.252
no shutdown
exit
ip route 172.16.50.0 255.255.255.0 10.10.10.2
end
show ip route
! R2
enable
configure terminal
hostname R2
interface g0/0
ip address 10.10.10.2 255.255.255.252
no shutdown
exit
interface g0/1
ip address 172.16.50.1 255.255.255.0
no shutdown
exit
ip route 192.168.50.0 255.255.255.0 10.10.10.1
end
show ip route
~~~

## Verification

PC1 must ping 172.16.50.10 successfully. R1 and R2 must show connected and static routes.

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
