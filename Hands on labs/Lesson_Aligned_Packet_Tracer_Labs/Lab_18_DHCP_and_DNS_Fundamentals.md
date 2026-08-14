# Lab 18 - DHCP, DNS, and IP Helper for Two VLANs

## Aligned Theory Lesson

Lesson 18

## Scenario

A company wants automatic addressing and name resolution for two departments. The DHCP/DNS server is in the server VLAN, so router relay is required.

## Devices Required

1 router, 1 switch, 1 server, 4 PCs

## Physical Topology

Router-on-a-stick connects VLAN10 Users, VLAN20 Admin, and VLAN99 Servers.

## Addressing Plan

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN99 192.168.99.0/24 gateway .1, Server 192.168.99.10.

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

1. Build router, switch, server, and four PCs.
2. Create VLANs 10, 20, and 99 on the switch.
3. Configure access ports and one trunk to the router.
4. Configure router subinterfaces and add ip helper-address 192.168.99.10 under VLAN10 and VLAN20 subinterfaces.
5. Configure DHCP pools on the server for VLAN10 and VLAN20.
6. Configure DNS service on the server with intranet.local pointing to 192.168.99.10.
7. Set PCs to DHCP and verify they receive correct addresses.
8. Browse or ping intranet.local from a client.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
interface g0/0
no shutdown
exit
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
ip helper-address 192.168.99.10
exit
interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
ip helper-address 192.168.99.10
exit
interface g0/0.99
encapsulation dot1Q 99
ip address 192.168.99.1 255.255.255.0
end
show ip interface brief
~~~

## Verification

PCs should receive DHCP addresses from the correct subnet and resolve intranet.local through DNS.

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
