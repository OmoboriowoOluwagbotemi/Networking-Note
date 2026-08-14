# Nova Care Network Step-by-Step Solution

## Purpose

This solution explains how to configure the Nova_Care Packet Tracer network shown in the screenshot. It gives a complete, copy-friendly configuration path so that Nova_Care LAN users can reach the external WEB_Server through the LAN_Router, the WAN link, and the WAN_Router.

## Important Design Explanation

The topology has three IP networks:

| Network | Purpose |
|---|---|
| 192.168.1.0/24 | Internal Nova_Care LAN |
| 10.0.0.0/30 | Point-to-point router link between LAN_Router and WAN_Router |
| 172.16.1.0/24 | Server-side network where WEB_Server is located |

The LAN users are not in the same subnet as the WEB_Server. Therefore, routing is required. The LAN_Router must know how to reach `172.16.1.0/24`, and the WAN_Router must know how to return traffic to `192.168.1.0/24`.

If only one side has a route, the ping may fail because the reply packet cannot find its way back.

## Packet Tracer Accuracy Note

The screenshot does not show exact interface names. The commands below use common Packet Tracer interface names:

- `gigabitEthernet0/0`
- `gigabitEthernet0/1`

If your router uses `fastEthernet0/0`, `fastEthernet0/1`, or serial interfaces instead, run:

```text
show ip interface brief
```

Then replace the interface names in the commands with the actual interfaces shown on your device.

## Addressing Plan

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| LAN_Router | LAN side | 192.168.1.1 | 255.255.255.0 | Not required |
| LAN_Router | WAN side | 10.0.0.1 | 255.255.255.252 | Not required |
| WAN_Router | WAN side | 10.0.0.2 | 255.255.255.252 | Not required |
| WAN_Router | Server side | 172.16.1.1 | 255.255.255.0 | Not required |
| WEB_Server | NIC | 172.16.1.10 | 255.255.255.0 | 172.16.1.1 |
| AccessPoint | Management | 192.168.1.2 | 255.255.255.0 | 192.168.1.1 |
| PC1 | NIC | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| PC2 | NIC | 192.168.1.11 | 255.255.255.0 | 192.168.1.1 |
| Laptop1 | Wireless | 192.168.1.12 | 255.255.255.0 | 192.168.1.1 |
| Laptop2 | Wireless | 192.168.1.13 | 255.255.255.0 | 192.168.1.1 |

---

# Part 1: Build or Confirm the Physical Topology

## What to Confirm

Before configuring commands, confirm the physical connections:

1. LAN workstations connect to `LAN_Switch`.
2. AccessPoint connects to `LAN_Switch`.
3. `LAN_Switch` connects to `LAN_Router`.
4. `LAN_Router` connects to `WAN_Router` using the `10.0.0.0/30` link.
5. `WAN_Router` connects to `WAN_Switch`.
6. `WEB_Server` connects to `WAN_Switch`.

## Why This Matters

If the physical cabling is wrong, IP commands will not solve the problem. Layer 1 and Layer 2 must be working before Layer 3 routing can work.

---

# Part 2: Configure LAN_Router

## What LAN_Router Does

LAN_Router is the default gateway for the Nova_Care LAN. It also forwards traffic toward WAN_Router when users need to reach the WEB_Server network.

## LAN_Router Copyable Configuration

Use this if the LAN interface is `G0/0` and the WAN interface is `G0/1`.

```text
enable
configure terminal
hostname LAN_Router
interface gigabitEthernet0/0
 description NOVA_CARE_LAN
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description LINK_TO_WAN_ROUTER
 ip address 10.0.0.1 255.255.255.252
 no shutdown
exit
ip route 172.16.1.0 255.255.255.0 10.0.0.2
end
show ip interface brief
show ip route
```

## If Your Router Uses FastEthernet

Use this version if the router interfaces are `Fa0/0` and `Fa0/1`.

```text
enable
configure terminal
hostname LAN_Router
interface fastEthernet0/0
 description NOVA_CARE_LAN
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit
interface fastEthernet0/1
 description LINK_TO_WAN_ROUTER
 ip address 10.0.0.1 255.255.255.252
 no shutdown
exit
ip route 172.16.1.0 255.255.255.0 10.0.0.2
end
show ip interface brief
show ip route
```

## Expected Result

`show ip interface brief` should show both configured interfaces as `up/up`. The routing table should show a static route to `172.16.1.0/24`.

---

# Part 3: Configure WAN_Router

## What WAN_Router Does

WAN_Router connects the WAN link to the server-side network. It must also know how to send reply traffic back to Nova_Care LAN.

## WAN_Router Copyable Configuration

Use this if the WAN interface is `G0/0` and the server-side interface is `G0/1`.

```text
enable
configure terminal
hostname WAN_Router
interface gigabitEthernet0/0
 description LINK_TO_LAN_ROUTER
 ip address 10.0.0.2 255.255.255.252
 no shutdown
exit
interface gigabitEthernet0/1
 description SERVER_NETWORK
 ip address 172.16.1.1 255.255.255.0
 no shutdown
exit
ip route 192.168.1.0 255.255.255.0 10.0.0.1
end
show ip interface brief
show ip route
```

## If Your Router Uses FastEthernet

```text
enable
configure terminal
hostname WAN_Router
interface fastEthernet0/0
 description LINK_TO_LAN_ROUTER
 ip address 10.0.0.2 255.255.255.252
 no shutdown
exit
interface fastEthernet0/1
 description SERVER_NETWORK
 ip address 172.16.1.1 255.255.255.0
 no shutdown
exit
ip route 192.168.1.0 255.255.255.0 10.0.0.1
end
show ip interface brief
show ip route
```

## Expected Result

`show ip route` should show:

- Connected route to `10.0.0.0/30`.
- Connected route to `172.16.1.0/24`.
- Static route to `192.168.1.0/24`.

---

# Part 4: Configure the WEB_Server

## Why This Matters

The server must have a correct IP address and default gateway. Without the gateway, the server may receive a packet from the LAN but fail to send the reply back.

## WEB_Server IP Settings

1. Click `WEB_Server`.
2. Click Desktop.
3. Click IP Configuration.
4. Enter the following:

```text
IP Address: 172.16.1.10
Subnet Mask: 255.255.255.0
Default Gateway: 172.16.1.1
DNS Server: Leave blank unless DNS is required
```

## Enable HTTP Service

1. Click `WEB_Server`.
2. Click Services.
3. Click HTTP.
4. Turn HTTP On.
5. If HTTPS is available and required, turn HTTPS On.

---

# Part 5: Configure LAN Workstations

## Wired PC Example

For PC1:

1. Click the PC.
2. Click Desktop.
3. Click IP Configuration.
4. Enter:

```text
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1
```

For PC2:

```text
IP Address: 192.168.1.11
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1
```

## Wireless Laptop Examples

For Laptop1:

```text
IP Address: 192.168.1.12
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1
```

For Laptop2:

```text
IP Address: 192.168.1.13
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1
```

---

# Part 6: Configure the Access Point

## What the Access Point Does

The access point bridges wireless clients into the Nova_Care LAN. In this topology, wireless clients should use the same `192.168.1.0/24` network as wired LAN users.

## Access Point Suggested Settings

1. Click `AccessPoint`.
2. Open Config or GUI, depending on the Packet Tracer device model.
3. Set management IP address:

```text
IP Address: 192.168.1.2
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1
```

4. Set SSID:

```text
SSID: Nova_Care
```

5. Set security if the device supports it:

```text
Security: WPA2-PSK
Passphrase: NovaCare123
```

6. Connect wireless laptops to SSID `Nova_Care`.
7. Use the same passphrase if security is enabled.

## Accuracy Note

Packet Tracer access point models vary. Some use the Config tab, while others use a GUI tab. Use the available wireless settings on the device in your file.

---

# Part 7: Verification Tests

## Test 1: Check LAN PC Settings

On a workstation, open Command Prompt and run:

```text
ipconfig
```

Expected result:

- IP address is in `192.168.1.0/24`.
- Default gateway is `192.168.1.1`.

## Test 2: Ping LAN Gateway

From a workstation:

```text
ping 192.168.1.1
```

Expected result: success.

If this fails, check PC IP settings, cabling, switch connection, and LAN_Router LAN interface.

## Test 3: Ping WAN_Router From LAN_Router

On LAN_Router:

```text
ping 10.0.0.2
```

Expected result: success.

If this fails, check the router-to-router link and `10.0.0.0/30` addressing.

## Test 4: Ping LAN_Router From WAN_Router

On WAN_Router:

```text
ping 10.0.0.1
```

Expected result: success.

## Test 5: Ping WEB_Server From WAN_Router

On WAN_Router:

```text
ping 172.16.1.10
```

Expected result: success.

If this fails, check the WEB_Server IP address, default gateway, server switch connection, and WAN_Router server-side interface.

## Test 6: Ping WEB_Server From a Nova_Care Workstation

From PC1:

```text
ping 172.16.1.10
```

Expected result: success.

This proves that routing works from the LAN to the server and back.

## Test 7: Open the Web Page

From PC1:

1. Open Desktop.
2. Open Web Browser.
3. Enter:

```text
http://172.16.1.10
```

Expected result: the web page on WEB_Server opens.

---

# Part 8: Troubleshooting Guide

## If PC Cannot Ping 192.168.1.1

Check:

```text
ipconfig
```

On LAN_Router, check:

```text
show ip interface brief
```

Likely causes:

- Wrong PC IP address.
- Wrong default gateway.
- LAN_Router LAN interface is shutdown.
- Cable is connected to the wrong port.

## If LAN_Router Cannot Ping WAN_Router

On both routers, check:

```text
show ip interface brief
```

Likely causes:

- Wrong `10.0.0.0/30` IP address.
- Wrong subnet mask.
- Interface is shutdown.
- Wrong cable/interface used.

## If LAN PC Can Ping 10.0.0.2 But Cannot Ping WEB_Server

On LAN_Router, check:

```text
show ip route
```

Make sure this route exists:

```text
ip route 172.16.1.0 255.255.255.0 10.0.0.2
```

On WAN_Router, check:

```text
show ip route
```

Make sure this route exists:

```text
ip route 192.168.1.0 255.255.255.0 10.0.0.1
```

## If Ping Works But Web Page Does Not Open

Check the server:

1. Click `WEB_Server`.
2. Click Services.
3. Click HTTP.
4. Confirm HTTP is On.
5. Confirm the browser uses:

```text
http://172.16.1.10
```

---

# Final Copy-Friendly Command Summary

## LAN_Router

```text
enable
configure terminal
hostname LAN_Router
interface gigabitEthernet0/0
 description NOVA_CARE_LAN
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit
interface gigabitEthernet0/1
 description LINK_TO_WAN_ROUTER
 ip address 10.0.0.1 255.255.255.252
 no shutdown
exit
ip route 172.16.1.0 255.255.255.0 10.0.0.2
end
show ip interface brief
show ip route
```

## WAN_Router

```text
enable
configure terminal
hostname WAN_Router
interface gigabitEthernet0/0
 description LINK_TO_LAN_ROUTER
 ip address 10.0.0.2 255.255.255.252
 no shutdown
exit
interface gigabitEthernet0/1
 description SERVER_NETWORK
 ip address 172.16.1.1 255.255.255.0
 no shutdown
exit
ip route 192.168.1.0 255.255.255.0 10.0.0.1
end
show ip interface brief
show ip route
```

## PC Tests

```text
ipconfig
```

```text
ping 192.168.1.1
```

```text
ping 172.16.1.10
```

```text
http://172.16.1.10
```

## Router Tests

```text
ping 10.0.0.2
```

```text
ping 10.0.0.1
```

```text
ping 172.16.1.10
```

## Save Configuration

Run on both routers:

```text
copy running-config startup-config
```

When asked for destination filename, press Enter.
