# Lab 19 - Secure School Wireless with Staff and Guest SSIDs

## Aligned Theory Lesson

Lesson 19

## Scenario

A school needs two wireless networks: Staff and Guest. Staff should use stronger security and connect to the internal network; Guest should be isolated in its own VLAN.

## Devices Required

1 wireless router or AP, 1 switch, 1 router, 2 laptops, 1 server

## Physical Topology

Router connects to switch. AP connects to switch. Laptops join Staff-WiFi and Guest-WiFi.

## Addressing Plan

Staff VLAN30 192.168.30.0/24, Guest VLAN40 192.168.40.0/24, Server VLAN99 192.168.99.0/24.

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

1. Place router, switch, AP or wireless router, server, and two laptops.
2. Create Staff and Guest network labels.
3. Configure AP SSID Staff-WiFi with WPA2-PSK password Staff@12345 if using Packet Tracer AP options.
4. Configure Guest-WiFi with WPA2-PSK password Guest@12345 if the selected wireless device supports multiple SSIDs.
5. Assign laptop wireless adapters to the correct SSID.
6. Configure DHCP or static IP addressing depending on the device support.
7. Test Staff laptop access to server.
8. Test Guest laptop only to its gateway unless routing policies are added.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

~~~text
enable
configure terminal
vlan 30
name STAFF_WIFI
exit
vlan 40
name GUEST_WIFI
exit
vlan 99
name SERVERS
exit
interface fa0/1
switchport mode trunk
switchport trunk allowed vlan 30,40,99
exit
interface fa0/2
switchport mode access
switchport access vlan 99
end
show vlan brief
show interfaces trunk
~~~

## Verification

Laptops must associate to the correct SSID, receive or use the correct IP network, and pass the required ping tests.

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
