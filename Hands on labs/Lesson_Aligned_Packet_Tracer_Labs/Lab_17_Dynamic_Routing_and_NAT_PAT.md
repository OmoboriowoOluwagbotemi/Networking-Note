# Lab 17 - OSPF Routing and PAT Internet Access for a Small Office

## Aligned Theory Lesson

Lesson 17

## Scenario

A small office has multiple internal networks and one public internet link. Students configure OSPF internally and PAT so many users can share one public IP address.

## Devices Required

2 routers, 2 switches, 2 PCs, 1 server

## Physical Topology

Inside LANs connect through R1 and R2. R2 connects to an Internet server network.

## Addressing Plan

LAN1 192.168.180.0/24, LAN2 192.168.181.0/24, R1-R2 10.0.0.0/30, Internet server 203.0.113.10/24 through R2 public side 203.0.113.1.

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

1. Build R1, R2, two LANs, and one outside server.
2. Configure interfaces and PC/server addresses.
3. Enable OSPF area 0 between R1 and R2 for internal routes.
4. Configure PAT on R2 using its outside interface.
5. Ping from inside PCs to the outside server.
6. Use show ip nat translations after traffic is generated.
7. Explain why many private hosts can share one outside interface address.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
! R1 OSPF
router ospf 1
network 192.168.180.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.3 area 0
! R2 OSPF and PAT
router ospf 1
network 192.168.181.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.3 area 0
exit
access-list 1 permit 192.168.180.0 0.0.0.255
access-list 1 permit 192.168.181.0 0.0.0.255
interface g0/0
ip nat inside
exit
interface g0/1
ip nat inside
exit
interface g0/2
ip nat outside
exit
ip nat inside source list 1 interface g0/2 overload
end
show ip ospf neighbor
show ip nat translations
~~~

## Verification

OSPF neighbors must form, routes must appear, and NAT translations should appear after inside hosts ping the outside server.

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
