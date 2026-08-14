# Lab 15 - Inter-VLAN Routing by Direct Router Interfaces, Router-on-a-Stick, and Layer 3 Switching - Solution

## Purpose of This Solution

This solution explains how to complete the lab in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the lab number and title.
4. Add the required devices: 1 router, 1 switch, 4 PCs minimum.
5. Build this topology: Method A: four switch access ports connect to four router interfaces, one per VLAN. Method B: one trunk connects switch to router subinterfaces.

Accuracy note for Packet Tracer: the direct-router-interface method requires a router model or added module with enough Ethernet interfaces for the VLANs being tested. If your selected router has only two or three Ethernet interfaces, test two or three VLANs with the direct method first, then complete all four VLANs with the router-on-a-stick method.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

VLAN10 192.168.10.0/24 gateway .1, VLAN20 192.168.20.0/24 gateway .1, VLAN30 192.168.30.0/24 gateway .1, VLAN40 192.168.40.0/24 gateway .1.

For each PC or server:

1. Click the device.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the IP address, subnet mask, default gateway, and DNS server if the lab requires them.
5. Close the window and move to the next device.

## Step 3: Configure Cisco Devices

Open the CLI of the required Cisco device and use the commands below. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name with the correct one.

~~~text
! Direct router-interface method
enable
configure terminal
hostname R1
interface g0/0
description VLAN10_GATEWAY
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
interface g0/1
description VLAN20_GATEWAY
ip address 192.168.20.1 255.255.255.0
no shutdown
exit
interface g0/2
description VLAN30_GATEWAY
ip address 192.168.30.1 255.255.255.0
no shutdown
exit
interface g0/3
description VLAN40_GATEWAY
ip address 192.168.40.1 255.255.255.0
no shutdown
end
show ip interface brief
! Router-on-a-stick method
enable
configure terminal
interface g0/0
no shutdown
exit
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
exit
interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
exit
interface g0/0.30
encapsulation dot1Q 30
ip address 192.168.30.1 255.255.255.0
exit
interface g0/0.40
encapsulation dot1Q 40
ip address 192.168.40.1 255.255.255.0
end
show ip interface brief
~~~

## Step 4: Verify the Network

Different VLANs should ping only after gateways and routing are configured. Use show vlan brief, show interfaces trunk, and show ip interface brief.

## Step 5: Troubleshoot If It Fails

- Check cable type and link lights before changing IP settings.
- Confirm every PC has the correct IP address, subnet mask, and default gateway when a gateway is required.
- Confirm switch access ports are in the correct VLAN when VLANs are used.
- Confirm trunk links allow the required VLANs when traffic crosses switches or router subinterfaces.
- Confirm router interfaces are up/up before testing routes.
- Use ping first, then use tracert or traceroute when traffic crosses routers.
- Record the exact command output that proves the lab works.

## Step 6: Save and Submit Evidence

1. A saved Packet Tracer file named after the lab number and title.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Expected Final Result

At the end of the lab, the required devices should be connected, correctly addressed, correctly configured, and successfully verified using the commands or tests stated above. If the scenario expects isolation, such as VLAN separation before inter-VLAN routing, the failed ping is also correct evidence when it matches the requirement.
