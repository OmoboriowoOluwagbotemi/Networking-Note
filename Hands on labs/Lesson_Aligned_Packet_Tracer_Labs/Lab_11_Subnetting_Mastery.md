# Lab 11 - Subnetting a Branch into Three Departments

## Aligned Theory Lesson

Lesson 11

## Scenario

A branch received 192.168.120.0/24 and must divide it into Admin, Sales, and Support networks. Students calculate subnets, assign gateways, and verify routing.

## Devices Required

1 router, 3 switches, 6 PCs

## Physical Topology

R1 connects separately to Admin-SW, Sales-SW, and Support-SW.

## Addressing Plan

Admin 192.168.120.0/26 gateway .1, Sales 192.168.120.64/26 gateway .65, Support 192.168.120.128/26 gateway .129.

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

1. Calculate each /26 network address, first usable address, last usable address, and broadcast address.
2. Build R1 with three switch connections.
3. Place two PCs per department.
4. Configure each router interface as the gateway for one subnet.
5. Assign PC addresses from the correct subnet.
6. Ping from Admin PC to Sales PC and Support PC.
7. Use failed tests to identify wrong masks or gateways.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname R1
interface g0/0
description ADMIN_GATEWAY
ip address 192.168.120.1 255.255.255.192
no shutdown
exit
interface g0/1
description SALES_GATEWAY
ip address 192.168.120.65 255.255.255.192
no shutdown
exit
interface g0/2
description SUPPORT_GATEWAY
ip address 192.168.120.129 255.255.255.192
no shutdown
end
show ip interface brief
show ip route
~~~

## Verification

Each PC must ping its gateway and PCs in other subnets through R1.

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
