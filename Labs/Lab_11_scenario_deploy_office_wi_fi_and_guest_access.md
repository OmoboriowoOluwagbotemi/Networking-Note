# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 11

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - DEPLOY OFFICE WI-FI AND GUEST ACCESS

## Aligned Lessons

This lab aligns with Lesson 20, Wireless Fundamentals and Deployment.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will deploy wireless clients using SSIDs, security settings, IP addressing, and guest network separation.

## Important Why

This lab matters because wireless is now an access-layer network, not a convenience feature. Students must understand SSIDs, security, client addressing, guest separation, and basic wireless validation.

## Important How

Students finish this lab by configuring staff and guest SSIDs, applying WPA2 security, connecting wireless clients, validating IP settings, and testing allowed connectivity.

## Scenario

FEMTECT wants one staff wireless network and one guest wireless network. Staff users should reach internal resources. Guest users should only receive internet-style access in the simulation.

## Wireless Plan

| SSID | Purpose | Security | Subnet |
|---|---|---|---|
| FEMTECT-STAFF | Employee Wi-Fi | WPA2-PSK | 192.168.60.0/24 |
| FEMTECT-GUEST | Visitor Wi-Fi | WPA2-PSK | 192.168.70.0/24 |

## Step-by-Step Tasks

1. Place a wireless router or access point in Packet Tracer.
2. Place two laptops or wireless PCs.
3. Configure the first SSID as `FEMTECT-STAFF`.
4. Set WPA2 security and choose a strong lab password.
5. Configure staff addressing using DHCP or static IP addressing.
6. Connect one wireless client to `FEMTECT-STAFF`.
7. Confirm it receives an IP address in `192.168.60.0/24`.
8. Configure a second SSID or second wireless device for `FEMTECT-GUEST`.
9. Set WPA2 security with a different password.
10. Connect the second wireless client to `FEMTECT-GUEST`.
11. Confirm it receives an IP address in `192.168.70.0/24`.
12. Test ping between wireless clients.
13. Test ping from staff client to a server.
14. Record the difference between staff and guest access.

## Student Deliverable

Submit SSID settings, wireless client IP settings, and a short note explaining why guest Wi-Fi should not share the same network as staff devices.

---

