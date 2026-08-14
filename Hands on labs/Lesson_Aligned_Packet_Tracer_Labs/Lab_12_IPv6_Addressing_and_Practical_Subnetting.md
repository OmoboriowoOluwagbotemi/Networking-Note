# Lab 12 - IPv6 LAN Addressing with Link-Local and Global Unicast

## Aligned Theory Lesson

Lesson 12

## Scenario

A small office wants to test IPv6 before production. Students configure IPv6 addresses, verify link-local addresses, and ping using IPv6.

## Devices Required

1 router, 1 switch, 2 PCs

## Physical Topology

PC1 and PC2 connect to SW1. SW1 connects to R1.

## Addressing Plan

IPv6 prefix 2001:db8:12:1::/64. R1 gateway 2001:db8:12:1::1/64. PC1 ::10/64, PC2 ::11/64.

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

1. Build R1--SW1--PC1 and PC2.
2. Enable IPv6 routing on R1.
3. Configure R1 global unicast address.
4. Configure PC IPv6 addresses and default gateway.
5. Ping from PC1 to PC2 using IPv6.
6. Ping from PC1 to R1 global IPv6 address.
7. Observe that devices also have link-local addresses.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname R1
ipv6 unicast-routing
interface g0/0
description IPV6_LAN
ipv6 address 2001:db8:12:1::1/64
no shutdown
end
show ipv6 interface brief
show ipv6 route
~~~

## Verification

From PC1 command prompt: ping 2001:db8:12:1::1 and ping 2001:db8:12:1::11.

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
