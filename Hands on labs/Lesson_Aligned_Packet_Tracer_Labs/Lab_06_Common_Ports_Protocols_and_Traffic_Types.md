# Lab 06 - Service Ports and Traffic Testing for a Small Company

## Aligned Theory Lesson

Lesson 6

## Scenario

A company server hosts web, DNS, and file-transfer services. Students enable services, test ports, and identify which application uses which traffic type.

## Devices Required

1 switch, 1 PC, 1 server

## Physical Topology

PC1 and SRV1 connect to SW1.

## Addressing Plan

PC1 192.168.70.10/24 DNS 192.168.70.20. SRV1 192.168.70.20/24.

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

1. Build PC1--SW1--SRV1.
2. Configure SRV1 IP 192.168.70.20/24.
3. On SRV1 Services, enable HTTP, HTTPS if available, DNS, and FTP.
4. Create DNS A records for www.company.local and ftp.company.local pointing to 192.168.70.20.
5. Configure PC1 with IP 192.168.70.10/24 and DNS 192.168.70.20.
6. From PC1 browser, open http://www.company.local.
7. From PC1 Command Prompt, test DNS using nslookup www.company.local.
8. Open Simulation Mode and observe DNS, TCP, HTTP, and FTP traffic.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname SW1
interface range fa0/1 - 2
description SERVICE_PORT_LAB
no shutdown
end
show mac address-table
~~~

## Verification

DNS resolution should succeed. HTTP should open. FTP should require configured credentials if Packet Tracer prompts for them.

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
