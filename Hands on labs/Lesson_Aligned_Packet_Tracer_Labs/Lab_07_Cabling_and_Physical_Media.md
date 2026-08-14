# Lab 07 - Cabling, Link Lights, and Physical Fault Isolation

## Aligned Theory Lesson

Lesson 7

## Scenario

A newly installed training room has intermittent connectivity. Students must choose correct cables, verify link lights, and isolate physical faults before blaming IP addressing.

## Devices Required

2 switches, 4 PCs

## Physical Topology

PC1 and PC2 connect to SW1. PC3 and PC4 connect to SW2. SW1 connects to SW2.

## Addressing Plan

All PCs in 192.168.80.0/24: PC1 .10, PC2 .11, PC3 .12, PC4 .13.

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

1. Place two 2960 switches and four PCs.
2. Connect PC1 and PC2 to SW1 using copper straight-through cables.
3. Connect PC3 and PC4 to SW2 using copper straight-through cables.
4. Connect SW1 to SW2 using copper straight-through or automatic cable.
5. Assign IP addresses to all PCs.
6. Verify ping from PC1 to PC4.
7. Create a fault by disconnecting the SW1-to-SW2 cable.
8. Use link lights and show interfaces status to identify the down connection.
9. Reconnect the cable and verify recovery.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
! SW1
enable
configure terminal
hostname SW1
interface range fa0/1 - 3
no shutdown
end
show interfaces status
! SW2
enable
configure terminal
hostname SW2
interface range fa0/1 - 3
no shutdown
end
show interfaces status
~~~

## Verification

PC1 should ping PC4 before and after the fault is repaired. Switch uplink ports should show connected.

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
