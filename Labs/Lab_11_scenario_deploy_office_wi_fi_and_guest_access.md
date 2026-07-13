# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 11

## Lab Title: Scenario - Deploy Office Wi-Fi and Guest Access

## Aligned Lessons

This lab aligns with Lesson 20, Wireless Fundamentals and Deployment.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because wireless networks are still part of the access layer. Wireless clients need SSIDs, security settings, IP addressing, and separation between staff and guest users. A guest device should not automatically have the same access as an employee device.

## Important How

Students will create a Packet Tracer wireless topology using two wireless routers or access devices to represent staff and guest wireless networks. This is Packet Tracer-safe because some Packet Tracer wireless devices support only limited SSID behavior.

## Packet Tracer Accuracy Note

Real enterprise networks often use lightweight APs and WLAN controllers with multiple SSIDs mapped to VLANs. Packet Tracer support depends on the device model. This lab uses two wireless routers/APs as a beginner-friendly simulation of separate staff and guest WLANs.

## Wireless Plan

| Network | SSID | Subnet | Gateway | Security |
|---|---|---|---|---|
| Staff Wi-Fi | FEMTECT-STAFF | 192.168.60.0/24 | 192.168.60.1 | WPA2-PSK |
| Guest Wi-Fi | FEMTECT-GUEST | 192.168.70.0/24 | 192.168.70.1 | WPA2-PSK |

## Detailed Step-by-Step Procedure

### Part A: Add Devices

1. Open Cisco Packet Tracer.
2. Add two wireless routers or two wireless access-capable devices.
3. Rename them `WR-STAFF` and `WR-GUEST`.
4. Add two laptops.
5. Rename them `LAPTOP-STAFF` and `LAPTOP-GUEST`.
6. If the laptop does not have a wireless adapter, click the laptop, go to Physical, power it off, remove the Ethernet module if required, insert a wireless module, then power it on.

### Part B: Configure Staff Wireless Router

1. Click WR-STAFF.
2. Open the GUI or Config tab depending on the Packet Tracer device.
3. Set the LAN IP address to `192.168.60.1`.
4. Set subnet mask to `255.255.255.0`.
5. Enable DHCP if available.
6. Set DHCP start address to `192.168.60.100`.
7. Set maximum users to a small number such as `50`.
8. Set SSID to `FEMTECT-STAFF`.
9. Set wireless security to WPA2 Personal if available.
10. Set passphrase to `StaffLab123`.
11. Save settings.

### Part C: Configure Guest Wireless Router

1. Click WR-GUEST.
2. Open the GUI or Config tab.
3. Set the LAN IP address to `192.168.70.1`.
4. Set subnet mask to `255.255.255.0`.
5. Enable DHCP if available.
6. Set DHCP start address to `192.168.70.100`.
7. Set SSID to `FEMTECT-GUEST`.
8. Set wireless security to WPA2 Personal if available.
9. Set passphrase to `GuestLab123`.
10. Save settings.

### Part D: Connect Staff Laptop

1. Click LAPTOP-STAFF.
2. Click Desktop.
3. Click PC Wireless.
4. Click Connect.
5. Select SSID `FEMTECT-STAFF`.
6. Click Connect.
7. Enter passphrase `StaffLab123`.
8. Wait for connection.
9. Open IP Configuration.
10. Choose DHCP.
11. Confirm an address in `192.168.60.0/24` is received.
12. Open Command Prompt.
13. Type `ping 192.168.60.1` and press Enter.
14. Confirm the staff gateway replies.

### Part E: Connect Guest Laptop

1. Click LAPTOP-GUEST.
2. Click Desktop.
3. Click PC Wireless.
4. Select SSID `FEMTECT-GUEST`.
5. Enter passphrase `GuestLab123`.
6. Choose DHCP in IP Configuration.
7. Confirm an address in `192.168.70.0/24` is received.
8. Open Command Prompt.
9. Type `ping 192.168.70.1` and press Enter.
10. Confirm the guest gateway replies.

### Part F: Compare Staff and Guest Networks

1. From LAPTOP-STAFF, ping the guest laptop IP address.
2. From LAPTOP-GUEST, ping the staff laptop IP address.
3. If the two wireless routers are not connected to each other, the pings should fail.
4. Explain that separation is expected in this beginner simulation.

## Verification Table

| Test | Correct Result |
|---|---|
| Staff laptop joins FEMTECT-STAFF | Connected |
| Guest laptop joins FEMTECT-GUEST | Connected |
| Staff receives 192.168.60.x | Correct |
| Guest receives 192.168.70.x | Correct |
| Staff pings 192.168.60.1 | Success |
| Guest pings 192.168.70.1 | Success |


## Copy-Friendly Command Blocks

### Staff Wireless Values to Type

```text
SSID: FEMTECT-STAFF
Security: WPA2 Personal
Passphrase: StaffLab123
LAN IP: 192.168.60.1
Subnet Mask: 255.255.255.0
DHCP Start IP: 192.168.60.100
```

### Guest Wireless Values to Type

```text
SSID: FEMTECT-GUEST
Security: WPA2 Personal
Passphrase: GuestLab123
LAN IP: 192.168.70.1
Subnet Mask: 255.255.255.0
DHCP Start IP: 192.168.70.100
```

### Staff Laptop Test

```text
ping 192.168.60.1
```

### Guest Laptop Test

```text
ping 192.168.70.1
```

## Student Deliverable

Submit screenshots of SSID settings, laptop IP settings, and successful gateway pings.
