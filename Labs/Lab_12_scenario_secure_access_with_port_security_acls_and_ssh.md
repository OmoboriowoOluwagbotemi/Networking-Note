# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 12

This lab is part of the 15-lab practical companion to the 25-lesson FEMTECT Professional Networking Course.

## Lab Title: SCENARIO - SECURE ACCESS WITH PORT SECURITY, ACLS, AND SSH

## Aligned Lessons

This lab aligns with Lesson 21, Wireless and Network Security Foundations, and Lesson 22, Access Control, Hardening, and Essential Services.

## Main Tool

Cisco Packet Tracer.

## Lab Goal

Students will secure switch access ports, configure SSH for management, and apply an ACL to limit traffic.

## Important Why

This lab matters because a working network is not enough; it must also be controlled and managed securely. Port security, ACLs, and SSH introduce the habit of reducing unauthorized access.

## Important How

Students finish this lab by enabling SSH, protecting switch ports with port security, applying an ACL, testing permitted and denied traffic, and verifying the security configuration.

## Scenario

An unauthorized laptop was connected to the office switch. Management now requires basic access-layer protection and secure device administration.

## Step-by-Step Tasks

1. Build a topology with one router, one switch, two valid PCs, one unauthorized PC, and one server.
2. Configure IP addressing so all valid devices can communicate.
3. On the switch, configure hostname `SW-ACCESS-1`.
4. Configure a management IP address on VLAN 1 or a management VLAN.
5. Configure `ip default-gateway` on the switch.
6. Configure a local username and secret password.
7. Configure a domain name using `ip domain-name femtect.local`.
8. Generate RSA keys using `crypto key generate rsa`.
9. Configure VTY lines to allow SSH only.
10. On access ports, configure `switchport mode access`.
11. Enable port security with `switchport port-security`.
12. Set maximum MAC addresses to 1.
13. Enable sticky MAC learning.
14. Set violation mode to restrict or shutdown.
15. Connect the unauthorized PC to a protected port and observe the result.
16. Configure an extended ACL on the router to deny Guest subnet access to the internal server but allow other traffic.
17. Test allowed and denied traffic.

## Cisco IOS Port Security Example

```text
interface fa0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

## Cisco IOS SSH Example

```text
hostname SW-ACCESS-1
ip domain-name femtect.local
username admin secret StrongLabPass123
crypto key generate rsa
line vty 0 15
 login local
 transport input ssh
```

## Verification Commands

```text
show port-security
show port-security interface fa0/1
show ip ssh
show access-lists
show running-config
```

## Student Deliverable

Submit port security evidence, SSH verification, ACL test results, and a short security explanation.

---

