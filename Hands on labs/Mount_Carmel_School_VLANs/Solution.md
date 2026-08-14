# Mount Carmel School VLAN Segmentation - Solution

## Purpose of This Solution

This solution explains how to complete this case study in Cisco Packet Tracer. It follows the same practical style as the Villa University and Nova Care case studies: build the topology first, configure devices carefully, verify each stage, and document the evidence.

## Step 1: Build the Topology

1. Open Cisco Packet Tracer.
2. Create a new blank project.
3. Save the file using the case-study name.
4. Add the required devices: 1 switch, 8 PCs.
5. Build this topology: One central switch connects to eight PCs grouped into four colored departments, two PCs per department.
6. Label all devices clearly.
7. Add Packet Tracer notes for networks, VLANs, departments, or device roles where appropriate.

## Step 2: Apply the Addressing Plan

Use this addressing plan:

Guests VLAN10 192.168.10.10-11/24, Parents VLAN20 192.168.20.12-13/24, Teachers VLAN30 192.168.30.14-15/24, Students VLAN40 192.168.40.16-17/24.

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
hostname SCHOOL_SW1
vlan 10
name GUESTS
exit
vlan 20
name PARENTS
exit
vlan 30
name TEACHERS
exit
vlan 40
name STUDENTS
exit
interface range fa0/1 - 2
switchport mode access
switchport access vlan 10
exit
interface range fa0/3 - 4
switchport mode access
switchport access vlan 20
exit
interface range fa0/5 - 6
switchport mode access
switchport access vlan 30
exit
interface range fa0/7 - 8
switchport mode access
switchport access vlan 40
end
show vlan brief
~~~

## Step 4: Verify the Network

Same-VLAN pings should work. Different-VLAN pings should fail until Lesson 15 inter-VLAN routing is added.

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



