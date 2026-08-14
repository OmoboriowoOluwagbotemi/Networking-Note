# Summit Branch Subnetting - Solution
## Purpose of This Solution

This solution explains how to complete the lab in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the lab number and title.
4. Add the required devices: 1 router, 3 switches, 6 PCs.
5. Build this topology: R1 connects separately to Admin-SW, Sales-SW, and Support-SW.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

Admin 192.168.120.0/26 gateway .1, Sales 192.168.120.64/26 gateway .65, Support 192.168.120.128/26 gateway .129.

For each PC or server:

1. Click the device.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the IP address, subnet mask, default gateway, and DNS server if the lab requires them.
5. Close the window and move to the next device.

## Step 3: Configure Cisco Devices

Open the CLI of the required Cisco device and use the commands below. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name with the correct one.

~~~text
enable
configure terminal
hostname R1
interface g0/0
description ADMIN_GATEWAY
ip address 192.168.120.1 255.255.255.192
no shutdown
exit
interface g0/1
description SALES_GATEWAY
ip address 192.168.120.65 255.255.255.192
no shutdown
exit
interface g0/2
description SUPPORT_GATEWAY
ip address 192.168.120.129 255.255.255.192
no shutdown
end
show ip interface brief
show ip route
~~~

## Step 4: Verify the Network

Each PC must ping its gateway and PCs in other subnets through R1.

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

