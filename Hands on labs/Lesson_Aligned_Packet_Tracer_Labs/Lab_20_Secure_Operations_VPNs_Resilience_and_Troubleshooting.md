# Lab 20 - Final Integrated Troubleshooting, Hardening, Documentation, and Handover

## Aligned Theory Lesson

Lesson 20

## Scenario

A small organization reports that users cannot reach a server after a change. Students diagnose Layer 1 to Layer 3, harden management access, document the fix, and prepare a handover report.

## Devices Required

2 routers, 2 switches, 4 PCs, 1 server

## Physical Topology

User VLANs connect through SW1 and R1 to R2 and the server network.

## Addressing Plan

Users VLAN10 192.168.10.0/24, Admin VLAN20 192.168.20.0/24, WAN 10.20.20.0/30, Server LAN 172.20.20.0/24.

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

1. Build or reuse a topology with VLANs, routing, and a server network.
2. Intentionally create three faults: one wrong VLAN port, one missing default gateway, and one missing static route.
3. Use a documented troubleshooting method: physical link, VLAN, IP address, gateway, route, DNS or service.
4. Fix the faults one by one and record evidence.
5. Configure SSH instead of Telnet on the router or switch.
6. Configure device hostname, enable secret, local username, domain name, RSA keys, and VTY SSH-only access.
7. Create a short handover note listing topology, IP plan, commands used, tests passed, and remaining risks.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
hostname R1
enable secret Femtect@123
ip domain-name femtect.local
username admin secret Admin@12345
crypto key generate rsa modulus 1024
line vty 0 4
login local
transport input ssh
exit
service password-encryption
banner motd #Authorized access only#
end
show ip ssh
copy running-config startup-config
~~~

## Verification

Final evidence must include successful pings, correct VLAN output, correct routes, SSH enabled, and a written handover summary.

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
