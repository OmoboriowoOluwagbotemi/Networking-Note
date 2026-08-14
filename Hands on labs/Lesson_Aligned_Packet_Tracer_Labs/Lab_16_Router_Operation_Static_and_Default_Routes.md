# Lab 16 - Static Routes, Default Routes, and Floating Backup Route

## Aligned Theory Lesson

Lesson 16

## Scenario

A branch office must reach headquarters through a primary link and keep a backup route ready. Students configure static routes, default routes, and a floating static route.

## Devices Required

3 routers, 2 switches, 2 PCs

## Physical Topology

Branch LAN--R1--R2--HQ LAN, with optional backup R1--R3--R2 path.

## Addressing Plan

Branch LAN 192.168.160.0/24, R1-R2 10.0.12.0/30, R1-R3 10.0.13.0/30, R3-R2 10.0.23.0/30, HQ LAN 192.168.170.0/24.

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

1. Build the routers and LANs.
2. Configure all router interfaces.
3. Configure PC1 in Branch LAN and PC2 in HQ LAN.
4. Add static routes across the primary path.
5. Add a default route on R1 toward R2 if R2 represents the upstream router.
6. Add a floating static route using a higher administrative distance through R3.
7. Shut the primary interface and observe route change.
8. Restore the primary interface and confirm normal path returns.

## Copyable Cisco IOS Commands

Use the commands below on the named Cisco device. If your Packet Tracer device uses different interface names, first run show ip interface brief or show interfaces status, then replace the interface name in the command with the correct one.

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

## Verification

Traffic should use the primary static route first. After the primary link is shut down, the floating static route should appear if the backup path is valid.

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
