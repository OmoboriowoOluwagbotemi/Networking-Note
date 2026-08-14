# Lab 14 - Multi-Switch VLAN Trunking and STP Verification

## Aligned Theory Lesson

Lesson 14

## Scenario

The school now has two floors. VLANs must work across two switches, and students must verify trunking and Spanning Tree behavior.

## Devices Required

2 switches, 8 PCs

## Physical Topology

SW1 connects to SW2 using two links. PCs for each VLAN exist on both switches.

## Addressing Plan

Use VLANs 10, 20, 30, 40. Same subnets as Lab 13.

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

1. Place SW1 and SW2.
2. Connect SW1 Fa0/23 to SW2 Fa0/23 and SW1 Fa0/24 to SW2 Fa0/24.
3. Place PCs on both switches for VLAN 10, 20, 30, and 40.
4. Create VLANs on both switches.
5. Configure access ports for user PCs.
6. Configure both inter-switch links as trunks allowing VLANs 10,20,30,40.
7. Use show interfaces trunk to verify trunking.
8. Use show spanning-tree to identify which redundant link is forwarding or blocking.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
vlan 10
name GUESTS
exit
vlan 20
name PARENTS
exit
vlan 30
name TEACHERS
exit
vlan 40
name STUDENTS
exit
interface range fa0/23 - 24
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
no shutdown
end
show interfaces trunk
show spanning-tree
~~~

## Verification

A PC in VLAN 10 on SW1 should ping a PC in VLAN 10 on SW2. STP should prevent a loop by blocking one redundant path.

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
