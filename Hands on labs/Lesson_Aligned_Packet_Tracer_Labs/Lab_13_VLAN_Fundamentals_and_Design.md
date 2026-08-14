# Lab 13 - School VLAN Segmentation for Guests, Parents, Teachers, and Students

## Aligned Theory Lesson

Lesson 13

## Scenario

A school has one switch but four user groups must be separated: Guests, Parents, Teachers, and Students. Students build the topology shown in the supplied VLAN screenshots and prove that VLANs isolate broadcasts.

## Devices Required

1 switch, 8 PCs

## Physical Topology

One central switch connects to eight PCs grouped into four colored departments, two PCs per department.

## Addressing Plan

Guests VLAN10 192.168.10.10-11/24, Parents VLAN20 192.168.20.12-13/24, Teachers VLAN30 192.168.30.14-15/24, Students VLAN40 192.168.40.16-17/24.

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

1. Place one 2960 switch and eight PCs.
2. Use drawing rectangles or notes to group PCs into Guests, Parents, Teachers, and Students.
3. Connect PC1-PC8 to switch ports Fa0/1 through Fa0/8.
4. Create VLANs 10, 20, 30, and 40.
5. Assign two ports to each VLAN.
6. Configure each PC with the correct IP address from its VLAN subnet.
7. Ping between two PCs in the same VLAN and confirm success.
8. Ping from a Guest PC to a Teacher PC and confirm failure because no inter-VLAN routing exists yet.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SCHOOL_SW1
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
interface range fa0/1 - 2
switchport mode access
switchport access vlan 10
exit
interface range fa0/3 - 4
switchport mode access
switchport access vlan 20
exit
interface range fa0/5 - 6
switchport mode access
switchport access vlan 30
exit
interface range fa0/7 - 8
switchport mode access
switchport access vlan 40
end
show vlan brief
~~~

## Verification

Same-VLAN pings should work. Different-VLAN pings should fail until Lesson 15 inter-VLAN routing is added.

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
