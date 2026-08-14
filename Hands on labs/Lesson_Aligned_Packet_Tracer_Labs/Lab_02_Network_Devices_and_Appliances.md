# Lab 02 - Choosing and Placing Network Devices for a Branch Office

## Aligned Theory Lesson

Lesson 2

## Scenario

A new branch office needs PCs, a server, a switch, a router, an access point, and a firewall placeholder. Students will identify each device role and build a working internal network with a routed server segment.

## Devices Required

1 router, 1 switch, 1 server, 3 PCs, 1 access point, 1 laptop

## Physical Topology

Branch PCs and AP connect to SW1. SW1 connects to R1. R1 connects to a server network.

## Addressing Plan

LAN 192.168.20.0/24 gateway 192.168.20.1. Server network 192.168.30.0/24 gateway 192.168.30.1. Server 192.168.30.10.

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

1. Place router R1, switch SW1, server SRV1, three PCs, one access point, and one laptop.
2. Cable PCs and AP to SW1. Cable SW1 to R1 G0/0. Cable SRV1 directly to R1 G0/1 or through a small server switch.
3. Configure PC addresses 192.168.20.10 to 192.168.20.12 with gateway 192.168.20.1.
4. Configure SRV1 as 192.168.30.10/24 with gateway 192.168.30.1.
5. Configure R1 interfaces using the copyable commands.
6. Test from PC1 to the server IP.
7. Label every device with its role.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname R1
interface gigabitEthernet0/0
description BRANCH_LAN_GATEWAY
ip address 192.168.20.1 255.255.255.0
no shutdown
exit
interface gigabitEthernet0/1
description SERVER_NETWORK_GATEWAY
ip address 192.168.30.1 255.255.255.0
no shutdown
end
show ip interface brief
copy running-config startup-config
~~~

## Verification

From PC1, ping 192.168.20.1, then ping 192.168.30.10. On R1, run show ip interface brief.

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
