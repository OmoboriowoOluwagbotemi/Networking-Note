# Westgate Branch Static Routing - Solution

## Purpose of This Solution

This solution explains how to complete this case study in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the case-study name.
4. Add the required devices: 3 routers, 2 switches, 2 PCs.
5. Build this topology: Branch LAN--R1--R2--HQ LAN, with optional backup R1--R3--R2 path.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

Branch LAN 192.168.160.0/24, R1-R2 10.0.12.0/30, R1-R3 10.0.13.0/30, R3-R2 10.0.23.0/30, HQ LAN 192.168.170.0/24.

For each PC or server:

1. Click the device.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the IP address, subnet mask, default gateway, and DNS server if the lab requires them.
5. Close the window and move to the next device.

## Step 3: Configure Cisco Devices

Open the CLI of the required Cisco device and use the commands below. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name with the correct one.

~~~text
! R1 key routes
ip route 192.168.170.0 255.255.255.0 10.0.12.2
ip route 192.168.170.0 255.255.255.0 10.0.13.2 10
! R2 key routes
ip route 192.168.160.0 255.255.255.0 10.0.12.1
ip route 192.168.160.0 255.255.255.0 10.0.23.1 10
! Verification
show ip route
show ip route static
traceroute 192.168.170.10
~~~

## Step 4: Verify the Network

Traffic should use the primary static route first. After the primary link is shut down, the floating static route should appear if the backup path is valid.

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



