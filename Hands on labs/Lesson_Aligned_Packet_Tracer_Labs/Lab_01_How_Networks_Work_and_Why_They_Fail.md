# Lab 01 - Small Office Network Discovery and Failure Testing

## Aligned Theory Lesson

Lesson 1

## Scenario

Femtect Support has been asked to check a small office where four staff computers should communicate through one switch. Students will build the LAN, assign IP addresses, prove that the network works, then intentionally create simple faults and diagnose them.

## Devices Required

1 Cisco 2960 switch, 4 PCs

## Physical Topology

PC1, PC2, PC3, and PC4 connect to SW1.

## Addressing Plan

PC1 192.168.17.10/24, PC2 192.168.17.11/24, PC3 192.168.17.12/24, PC4 192.168.17.13/24. No default gateway is required because this is one LAN.

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

1. Open Packet Tracer and place one 2960 switch in the center of the workspace.
2. Place four PCs below the switch and rename them PC1, PC2, PC3, and PC4.
3. Use copper straight-through cables from each PC FastEthernet0 port to switch ports Fa0/1 through Fa0/4.
4. Click each PC, open Desktop, open IP Configuration, and enter the assigned IP address and subnet mask 255.255.255.0.
5. Open PC1 Desktop, Command Prompt, and run ping tests to PC2, PC3, and PC4.
6. Create Fault 1 by unplugging PC3 cable, then ping PC3 from PC1 and record the failure.
7. Reconnect PC3, then create Fault 2 by changing PC4 IP address to 192.168.18.13 and test again.
8. Restore PC4 to 192.168.17.13 and prove all pings work again.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
interface range fastEthernet0/1 - 4
description OFFICE_LAN_USERS
no shutdown
end
show interfaces status
copy running-config startup-config
~~~

## Verification

From PC1 command prompt: ping 192.168.17.11, ping 192.168.17.12, and ping 192.168.17.13. On SW1, run show interfaces status.

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
