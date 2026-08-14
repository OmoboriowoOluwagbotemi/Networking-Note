# SwiftMart OSPF and NAT/PAT - Solution

## Purpose of This Solution

This solution explains how to complete this case study in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the case-study name.
4. Add the required devices: 2 routers, 2 switches, 2 PCs, 1 server.
5. Build this topology: Inside LANs connect through R1 and R2. R2 connects to an Internet server network.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

LAN1 192.168.180.0/24, LAN2 192.168.181.0/24, R1-R2 10.0.0.0/30, Internet server 203.0.113.10/24 through R2 public side 203.0.113.1.

For each PC or server:

1. Click the device.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the IP address, subnet mask, default gateway, and DNS server if the lab requires them.
5. Close the window and move to the next device.

## Step 3: Configure Cisco Devices

Open the CLI of the required Cisco device and use the commands below. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name with the correct one.

~~~text
! R1 OSPF
router ospf 1
network 192.168.180.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.3 area 0
! R2 OSPF and PAT
router ospf 1
network 192.168.181.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.3 area 0
exit
access-list 1 permit 192.168.180.0 0.0.0.255
access-list 1 permit 192.168.181.0 0.0.0.255
interface g0/0
ip nat inside
exit
interface g0/1
ip nat inside
exit
interface g0/2
ip nat outside
exit
ip nat inside source list 1 interface g0/2 overload
end
show ip ospf neighbor
show ip nat translations
~~~

## Step 4: Verify the Network

OSPF neighbors must form, routes must appear, and NAT translations should appear after inside hosts ping the outside server.

## Step 5: Troubleshoot If It Fails

- Check cable type and link lights before changing IP settings.
- Confirm every PC has the correct IP address, subnet mask, and default gateway when a gateway is required.
- Confirm switch access ports are in the correct VLAN when VLANs are used.
- Confirm trunk links allow the required VLANs when traffic crosses switches or router subinterfaces.
- Confirm router interfaces are up/up before testing routes.
- Use ping first, then use tracert or traceroute when traffic crosses routers.
- Record the exact command output that proves the lab works.

## Step 6: Save and Submit Evidence

1. A saved Packet Tracer file named after the case-study name.
2. Screenshot of the completed physical topology.
3. Screenshot of the addressing table or PC IP settings.
4. Screenshot of successful verification tests.
5. Short explanation of the problem, the configuration used, and the final result.

## Expected Final Result

At the end of the case study, the required devices should be connected, correctly addressed, correctly configured, and successfully verified using the commands or tests stated above. If the scenario expects isolation, such as VLAN separation before inter-VLAN routing, the failed ping is also correct evidence when it matches the requirement.



