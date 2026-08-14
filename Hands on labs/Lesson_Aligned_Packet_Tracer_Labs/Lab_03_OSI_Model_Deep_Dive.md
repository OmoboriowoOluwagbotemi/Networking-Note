# Lab 03 - OSI Layer Evidence in Packet Tracer Simulation Mode

## Aligned Theory Lesson

Lesson 3

## Scenario

A helpdesk trainee must prove which OSI layers are involved when a PC opens a web page from a local server. Students build a small network, generate HTTP traffic, and inspect PDUs in Simulation Mode.

## Devices Required

1 switch, 1 PC, 1 server

## Physical Topology

PC1 and WEB1 connect to SW1.

## Addressing Plan

PC1 192.168.40.10/24, WEB1 192.168.40.20/24. No gateway required.

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

1. Place one 2960 switch, one PC, and one server.
2. Connect PC1 and WEB1 to SW1 using straight-through cables.
3. Configure PC1 IP address 192.168.40.10 mask 255.255.255.0.
4. Configure WEB1 IP address 192.168.40.20 mask 255.255.255.0.
5. Click WEB1, open Services, open HTTP, and turn HTTP On.
6. Switch Packet Tracer from Realtime to Simulation.
7. On PC1, open Web Browser and browse to http://192.168.40.20.
8. Click the captured PDU and observe Layer 7 HTTP, Layer 4 TCP, Layer 3 IP, Layer 2 Ethernet, and Layer 1 movement.
9. Record one example of evidence for each OSI layer from Layer 7 down to Layer 1.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
interface range fastEthernet0/1 - 2
description OSI_LAB_ENDPOINTS
no shutdown
end
show mac address-table
copy running-config startup-config
~~~

## Verification

Successful browser page from WEB1. In Simulation Mode, the event list should show ARP, TCP, and HTTP traffic.

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
