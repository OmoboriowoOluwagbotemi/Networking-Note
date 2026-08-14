# Lab 07 - Cabling, Link Lights, and Physical Fault Isolation - Solution

## Purpose of This Solution

This solution explains how to complete the lab in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the lab number and title.
4. Add the required devices: 2 switches, 4 PCs.
5. Build this topology: PC1 and PC2 connect to SW1. PC3 and PC4 connect to SW2. SW1 connects to SW2.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

All PCs in 192.168.80.0/24: PC1 .10, PC2 .11, PC3 .12, PC4 .13.

For each PC or server:

1. Click the device.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the IP address, subnet mask, default gateway, and DNS server if the lab requires them.
5. Close the window and move to the next device.

## Step 3: Configure Cisco Devices

Open the CLI of the required Cisco device and use the commands below. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name with the correct one.

~~~text
! SW1
enable
configure terminal
hostname SW1
interface range fa0/1 - 3
no shutdown
end
show interfaces status
! SW2
enable
configure terminal
hostname SW2
interface range fa0/1 - 3
no shutdown
end
show interfaces status
~~~

## Step 4: Verify the Network

PC1 should ping PC4 before and after the fault is repaired. Switch uplink ports should show connected.

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
