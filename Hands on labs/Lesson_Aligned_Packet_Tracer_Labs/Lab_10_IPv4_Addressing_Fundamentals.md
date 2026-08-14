# Lab 10 - IPv4 Addressing, Gateway Decisions, and APIPA Faults

## Aligned Theory Lesson

Lesson 10

## Scenario

A support technician must configure PCs correctly and identify when a host is in the wrong network or has an APIPA-style address.

## Devices Required

1 router, 1 switch, 3 PCs

## Physical Topology

PCs connect to SW1. SW1 connects to R1.

## Addressing Plan

LAN 192.168.110.0/24 gateway 192.168.110.1. PC1 .10, PC2 .11, PC3 intentionally wrong first.

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

1. Build R1--SW1--three PCs.
2. Configure R1 LAN gateway.
3. Configure PC1 and PC2 correctly.
4. Configure PC3 first as 169.254.10.5/16 and test failure.
5. Change PC3 to 192.168.111.12/24 and test failure due to wrong subnet.
6. Correct PC3 to 192.168.110.12/24 gateway 192.168.110.1.
7. Record how IP address, subnet mask, and default gateway affect connectivity.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname R1
interface g0/0
ip address 192.168.110.1 255.255.255.0
no shutdown
end
show ip interface brief
~~~

## Verification

PCs should ping 192.168.110.1 and each other only after correct addressing is configured.

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
