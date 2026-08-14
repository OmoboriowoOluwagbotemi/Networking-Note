# Lab 05 - TCP, UDP, ICMP, and ARP in a Service Network

## Aligned Theory Lesson

Lesson 5

## Scenario

A school ICT room has a web server and DNS server. Students observe ARP, ICMP, DNS, TCP, and HTTP behavior using Packet Tracer Simulation Mode.

## Devices Required

1 switch, 1 PC, 1 server

## Physical Topology

PC1 and SERVER1 connect to SW1.

## Addressing Plan

PC1 192.168.60.10/24 DNS 192.168.60.20. SERVER1 192.168.60.20/24.

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

1. Build PC1--SW1--SERVER1.
2. Configure SERVER1 IP 192.168.60.20/24.
3. On SERVER1 Services, enable HTTP and DNS. Add DNS record portal.local pointing to 192.168.60.20.
4. Configure PC1 IP 192.168.60.10/24 and DNS server 192.168.60.20.
5. Use PC1 Command Prompt to ping SERVER1.
6. Use PC1 Web Browser to open http://portal.local.
7. In Simulation Mode, filter ARP, ICMP, DNS, TCP, and HTTP and observe the order of events.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
interface range fa0/1 - 2
description TCP_IP_LAB
no shutdown
end
show mac address-table
~~~

## Verification

PC1 should resolve portal.local and load the web page. Simulation Mode should show ARP before first local delivery and TCP before HTTP.

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
