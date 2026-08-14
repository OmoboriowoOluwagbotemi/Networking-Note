# Lab 15 - Inter-VLAN Routing by Direct Router Interfaces, Router-on-a-Stick, and Layer 3 Switching

## Aligned Theory Lesson

Lesson 15

## Scenario

Management now wants controlled communication between Guests, Parents, Teachers, and Students. Students first learn the direct-cable method, then compare it with router-on-a-stick.

## Devices Required

1 router, 1 switch, 4 PCs minimum

## Physical Topology

Method A: four switch access ports connect to four router interfaces, one per VLAN. Method B: one trunk connects switch to router subinterfaces.

Accuracy note for Packet Tracer: the direct-router-interface method requires a router model or added module with enough Ethernet interfaces for the VLANs being tested. If your selected router has only two or three Ethernet interfaces, test two or three VLANs with the direct method first, then complete all four VLANs with the router-on-a-stick method.

## Addressing Plan

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN30 192.168.30.0/24 gateway .1, VLAN40 192.168.40.0/24 gateway .1.

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

1. Start with the Lab 13 VLAN switch.
2. For the direct-router-interface method, connect one router interface to an access port in VLAN10, another to VLAN20, another to VLAN30, and another to VLAN40.
3. Configure the switch ports connected to the router as access ports in their matching VLANs.
4. Configure each router physical interface with the gateway IP for that VLAN.
5. Set each PC default gateway to its VLAN router interface.
6. Ping between VLANs and confirm success.
7. Then rebuild or duplicate the topology for router-on-a-stick using one trunk link and router subinterfaces.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
! Direct router-interface method
enable
configure terminal
hostname R1
interface g0/0
description VLAN10_GATEWAY
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
interface g0/1
description VLAN20_GATEWAY
ip address 192.168.20.1 255.255.255.0
no shutdown
exit
interface g0/2
description VLAN30_GATEWAY
ip address 192.168.30.1 255.255.255.0
no shutdown
exit
interface g0/3
description VLAN40_GATEWAY
ip address 192.168.40.1 255.255.255.0
no shutdown
end
show ip interface brief
! Router-on-a-stick method
enable
configure terminal
interface g0/0
no shutdown
exit
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
exit
interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
exit
interface g0/0.30
encapsulation dot1Q 30
ip address 192.168.30.1 255.255.255.0
exit
interface g0/0.40
encapsulation dot1Q 40
ip address 192.168.40.1 255.255.255.0
end
show ip interface brief
~~~

## Verification

Different VLANs should ping only after gateways and routing are configured. Use show vlan brief, show interfaces trunk, and show ip interface brief.

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
