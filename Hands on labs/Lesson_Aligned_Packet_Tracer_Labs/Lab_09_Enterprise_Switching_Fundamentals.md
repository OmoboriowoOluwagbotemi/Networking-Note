# Lab 09 - Switch Port Modes and Basic Port Security

## Aligned Theory Lesson

Lesson 9

## Scenario

A finance office wants each desk port protected so unknown devices cannot easily connect. Students configure access ports and basic port security.

## Devices Required

1 switch, 2 authorized PCs, 1 unauthorized PC for testing

## Physical Topology

PC1 and PC2 connect to SW1. Later, replace PC2 with RoguePC on the same port.

## Addressing Plan

PC1 192.168.100.10/24, PC2 192.168.100.11/24, RoguePC 192.168.100.99/24.

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

1. Build SW1 with PC1 on Fa0/1 and PC2 on Fa0/2.
2. Configure PC IP addresses.
3. Configure Fa0/1 and Fa0/2 as access ports.
4. Enable port security with maximum 1 MAC address on Fa0/2.
5. Ping PC1 to PC2 to learn the secure MAC.
6. Disconnect PC2 and connect RoguePC to Fa0/2.
7. Ping from RoguePC and observe the port-security violation.
8. Recover the port if it becomes err-disabled.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
interface range fa0/1 - 2
switchport mode access
spanning-tree portfast
no shutdown
exit
interface fa0/2
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address sticky
switchport port-security violation shutdown
end
show port-security interface fa0/2
show mac address-table
~~~

## Verification

Use show port-security interface fa0/2. If violated, recover with configure terminal, interface fa0/2, shutdown, no shutdown.

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
