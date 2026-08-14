# LESSON 14: VLAN CONFIGURATION, TRUNKING, AND SPANNING TREE

## TRAINING FOCUS

This lesson is part of the FEMTECT Network Engineering Foundation course. It is written to help students build strong networking fundamentals through clear explanations, real enterprise context, practical troubleshooting logic, and certification-aware technical depth.

---

## INTEGRATED SOURCE TOPIC: LESSON 14: VLAN CONFIGURATION AND TRUNKING


## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 14.1 VLAN Configuration

VLAN configuration is the process of creating VLANs on switches, assigning switch ports to the correct VLANs, and configuring trunk links so multiple VLANs can move between network devices. In Lesson 13, VLANs were introduced as logical Layer 2 networks that create separate broadcast domains. Lesson 14 turns that design knowledge into practical switch configuration and verification.

A VLAN design is only useful when the switch configuration matches it. If the design says staff users belong in VLAN 10, voice devices belong in VLAN 20, and guest wireless belongs in VLAN 50, then the switch ports, trunks, VLAN database, and uplinks must be configured correctly. Otherwise, the network may be physically connected but logically wrong.

VLAN configuration exists because modern enterprise switches do not automatically know the business purpose of each port. A switch must be told which VLANs exist, which access ports belong to which VLAN, which links are trunks, which VLANs are allowed across trunks, and what native VLAN should be used on each trunk.

In real enterprise work, VLAN configuration affects user connectivity, DHCP scope selection, wireless SSID mapping, IP phone behavior, server segmentation, firewall policy, and troubleshooting. A wrong VLAN on one access port may affect one user. A wrong trunk configuration may affect an entire floor, building, wireless network, or server environment.

For CCNA and CompTIA Network+, students must understand access ports, trunk ports, 802.1Q tagging, native VLAN behavior, trunk negotiation, allowed VLAN lists, and verification commands.

### 14.2 Technical and Business Importance of VLAN Configuration

VLAN configuration matters because VLAN design and switch behavior must agree. A diagram may show a clean design, but the real network follows the running configuration on the switches. If a port is in the wrong VLAN, the device may receive the wrong IP address. If a trunk does not carry a required VLAN, users on another switch may lose access. If the native VLAN is mismatched, untagged traffic may be placed into the wrong VLAN. If dynamic trunking is left uncontrolled, a user-facing port may negotiate a trunk unexpectedly.

VLAN configuration is also important for security. Guest users should not accidentally land in the staff VLAN. Management ports should not be exposed to ordinary users. Trunks should carry only required VLANs. Unused ports should not remain active in a production VLAN. The native VLAN should be chosen intentionally and documented.

In troubleshooting, VLAN configuration is one of the first places a technician checks. If a user reports no network access after moving desks, the cable may be fine, the NIC may be fine, and the switch port may be up. The issue may simply be that the new switch port is assigned to the wrong VLAN.

## 14.3 VLAN Configuration Workflow

A practical VLAN configuration workflow follows a predictable order.

First, create the VLANs and give them meaningful names. Second, assign access ports to the correct VLANs. Third, configure trunk links between switches or network devices. Fourth, define the native VLAN and allowed VLAN list on trunks. Fifth, verify the result using show commands. Sixth, test endpoint connectivity.

Configuration Workflow

| Step | Task | Purpose |
|---:|---|---|
| 1 | Create VLANs | Makes VLAN IDs available on the switch |
| 2 | Name VLANs | Improves readability and documentation |
| 3 | Configure access ports | Places endpoints into correct VLANs |
| 4 | Configure trunks | Carries multiple VLANs between devices |
| 5 | Set allowed VLANs | Limits which VLANs cross trunks |
| 6 | Verify configuration | Confirms switch behavior |
| 7 | Test endpoints | Confirms user/device connectivity |

This workflow prevents random configuration. A professional engineer configures intentionally and verifies after each major step.

## 14.4 Creating VLANs on Cisco Switches

Before a switch port can be assigned to a VLAN, the VLAN should exist in the switch VLAN database. On Cisco IOS, VLANs are created in global configuration mode.

Example:

```text
enable
configure terminal
vlan 10
 name STAFF_DATA
vlan 20
 name VOICE
vlan 30
 name SERVERS
vlan 50
 name GUEST_WIFI
end
```

The VLAN ID is the numeric identifier. The VLAN name is a human-readable label. A VLAN can technically function without a descriptive name, but professional networks should use clear names.

Verification command:

```text
show vlan brief
```

Example output concept:

| VLAN | Name | Status | Ports |
|---:|---|---|---|
| 1 | default | active | Fa0/1, Fa0/2 |
| 10 | STAFF_DATA | active | Fa0/5, Fa0/6 |
| 20 | VOICE | active | Fa0/7 |
| 30 | SERVERS | active | Fa0/10 |
| 50 | GUEST_WIFI | active | Fa0/15 |

If a VLAN does not appear in `show vlan brief`, it may not exist on that switch. If a port is not listed under the expected VLAN, the port may not be assigned correctly or may be operating as a trunk.

## 14.5 Access Ports

An access port is a switch port that normally carries traffic for one VLAN. Access ports are used for end devices such as desktop computers, printers, cameras, and many servers. When an endpoint sends an untagged Ethernet frame into an access port, the switch associates that frame with the access VLAN configured on the port.

Access ports matter because they determine which VLAN an endpoint belongs to. A PC plugged into an access port in VLAN 10 belongs to VLAN 10. If the same PC is moved to a port in VLAN 50, it belongs to VLAN 50 and may receive a guest network IP address.

Basic access port configuration:

```text
configure terminal
interface fastEthernet 0/5
 description Staff PC - Admin Office
 switchport mode access
 switchport access vlan 10
 no shutdown
end
```

The `switchport mode access` command forces the port to operate as an access port. The `switchport access vlan 10` command assigns the port to VLAN 10.

Access Port Configuration Summary

| Command | Purpose |
|---|---|
| `interface fastEthernet 0/5` | Enters interface configuration mode |
| `description Staff PC - Admin Office` | Documents the port purpose |
| `switchport mode access` | Forces access-port mode |
| `switchport access vlan 10` | Assigns the access VLAN |
| `no shutdown` | Enables the port if administratively down |

Verification commands:

```text
show vlan brief
show interfaces fastEthernet 0/5 switchport
show running-config interface fastEthernet 0/5
```

The output should confirm that the port is an access port and that the access VLAN is correct.

## 14.6 Voice VLAN Configuration

A voice VLAN allows an IP phone and a PC to share one physical switch port while separating their traffic logically. The switch port has a data VLAN for the PC and a voice VLAN for the phone.

Example:

```text
interface fastEthernet 0/15
 description IP Phone + Staff PC
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20
 spanning-tree portfast
```

In this example, the PC uses VLAN 10 and the IP phone uses VLAN 20. The phone may tag voice traffic so the switch identifies it as voice VLAN traffic. The PC traffic remains associated with the access VLAN.

Voice VLANs are important because voice traffic is delay-sensitive. Separating voice traffic helps with Quality of Service, DHCP options, call manager reachability, troubleshooting, and security policy.

Voice Port Design

| Port Component | VLAN | Purpose |
|---|---:|---|
| Access VLAN | 10 | PC/data traffic |
| Voice VLAN | 20 | IP phone traffic |
| Physical Port | Fa0/15 | Shared phone and PC connection |

Students should understand the configuration concept now. Deeper VoIP, QoS, and call manager design are beyond this lesson.

## 14.7 Trunk Ports

A trunk port is a switch port that carries traffic for multiple VLANs. Trunks are used when VLAN traffic must pass between switches or between a switch and another network device such as a router, firewall, wireless access point, or hypervisor.

Without trunks, each VLAN would require a separate physical cable between switches. That would be inefficient and difficult to manage. A trunk allows multiple VLANs to share one physical or logical link while remaining separated by VLAN tags.

Basic trunk configuration:

```text
configure terminal
interface gigabitEthernet 0/1
 description Uplink to SW2
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,50,99
 no shutdown
end
```

This configuration forces the port into trunk mode, sets VLAN 999 as the native VLAN, and allows only VLANs 10, 20, 30, 50, and 99 across the trunk.

Trunk Configuration Summary

| Command | Purpose |
|---|---|
| `switchport mode trunk` | Forces trunk mode |
| `switchport trunk native vlan 999` | Sets the native VLAN |
| `switchport trunk allowed vlan 10,20,30,50,99` | Limits VLANs allowed on trunk |
| `description Uplink to SW2` | Documents trunk purpose |

Verification command:

```text
show interfaces trunk
```

This command shows trunking status, native VLAN, allowed VLANs, and VLANs active on the trunk.

## 14.8 IEEE 802.1Q Tagging

IEEE 802.1Q is the standard used to tag Ethernet frames with VLAN information as they travel across trunk links. When a frame crosses a trunk, the switch must identify which VLAN the frame belongs to. 802.1Q adds a VLAN tag into the Ethernet frame so the receiving switch can place the frame into the correct VLAN.

802.1Q exists because a trunk carries multiple VLANs on one link. Without tagging, the receiving switch would not know whether a frame belongs to VLAN 10, VLAN 20, VLAN 30, or another VLAN.

The 802.1Q tag includes the VLAN ID. This allows traffic from multiple VLANs to share a trunk while staying logically separate.

Simple trunk example:

```text
PC in VLAN 10 -> SW1 -> trunk tag VLAN 10 -> SW2 -> PC in VLAN 10
Phone in VLAN 20 -> SW1 -> trunk tag VLAN 20 -> SW2 -> phone system
```

The trunk does not merge the VLANs. It carries them with identifiers.

802.1Q Tagging Behavior

| Traffic Type | Across Access Port | Across Trunk Port |
|---|---|---|
| Data VLAN endpoint traffic | Usually untagged | Tagged with VLAN ID |
| Voice VLAN traffic | Often tagged by phone | Tagged with VLAN ID |
| Native VLAN traffic | Untagged on trunk | Untagged by default |
| Other VLAN traffic | Not carried on access port | Tagged with VLAN ID |

## 14.9 Native VLAN Behavior

The native VLAN is the VLAN used for untagged traffic on an 802.1Q trunk. Most VLAN traffic is tagged on a trunk. Native VLAN traffic is sent untagged by default.

Native VLAN behavior matters because untagged frames received on a trunk are placed into the native VLAN. If the native VLAN does not match on both ends of the trunk, traffic may be placed into the wrong VLAN.

Example:

```text
SW1 trunk native VLAN: 999
SW2 trunk native VLAN: 1
```

This mismatch is a problem. SW1 expects untagged traffic to belong to VLAN 999. SW2 expects untagged traffic to belong to VLAN 1. The result can be confusing and insecure.

Best practice for many enterprise environments:

- Use a dedicated unused VLAN as the native VLAN.
- Do not use VLAN 1 as the native VLAN where avoidable.
- Ensure the native VLAN matches on both ends of a trunk.
- Do not place normal user devices in the native VLAN.
- Document native VLAN assignments.

Configuration example:

```text
vlan 999
 name NATIVE_UNUSED
interface gigabitEthernet 0/1
 switchport mode trunk
 switchport trunk native vlan 999
```

Verification:

```text
show interfaces trunk
```

## 14.10 Allowed VLAN Lists

An allowed VLAN list controls which VLANs are permitted to cross a trunk. This is an important design and security feature.

By default, some switches may allow many or all VLANs across a trunk. That may be convenient in a lab, but it is not always a good production practice. A trunk should carry the VLANs that are required on that link and no unnecessary VLANs.

Example:

```text
interface gigabitEthernet 0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,50,99
```

If VLAN 40 is not needed across this uplink, it should not be allowed. This reduces unnecessary broadcast traffic exposure and limits mistakes.

Allowed VLAN list operations:

```text
switchport trunk allowed vlan 10,20,30
switchport trunk allowed vlan add 50
switchport trunk allowed vlan remove 20
switchport trunk allowed vlan except 100
```

Allowed VLAN List Examples

| Command | Meaning |
|---|---|
| `switchport trunk allowed vlan 10,20,30` | Allow only VLANs 10, 20, and 30 |
| `switchport trunk allowed vlan add 50` | Add VLAN 50 to the current list |
| `switchport trunk allowed vlan remove 20` | Remove VLAN 20 from the list |
| `switchport trunk allowed vlan all` | Allow all VLANs |

Be careful with this command. Replacing an allowed VLAN list accidentally can remove active VLANs from a trunk and break connectivity.

## 14.11 Trunk Negotiation and DTP

DTP means Dynamic Trunking Protocol. It is a Cisco protocol that can negotiate trunk formation between switch ports.

DTP exists to make trunk setup easier, but automatic negotiation can create security and operational risks. In production networks, many engineers prefer to manually configure trunk ports and manually configure access ports.

Common trunking modes include:

| Mode | Behavior |
|---|---|
| `access` | Forces port to be an access port |
| `trunk` | Forces port to be a trunk |
| `dynamic desirable` | Actively tries to form a trunk |
| `dynamic auto` | Forms trunk if neighbor actively requests |

A common secure approach is:

```text
interface fastEthernet 0/10
 switchport mode access
 switchport nonegotiate
```

For trunk ports:

```text
interface gigabitEthernet 0/1
 switchport mode trunk
 switchport nonegotiate
```

The `switchport nonegotiate` command disables DTP negotiation on supported platforms. Support and syntax may vary depending on switch model and IOS version.

Security principle:

```text
User-facing ports should not negotiate trunks.
```

If a user-facing port accidentally becomes a trunk, an attacker may attempt VLAN hopping or unauthorized VLAN access.

## 14.12 VLAN Configuration Example: Two-Switch Office

Consider two switches, SW1 and SW2. The office has staff devices in VLAN 10, voice devices in VLAN 20, and guest Wi-Fi in VLAN 50. The switches are connected by a trunk on `Gi0/1`.

Design:

| VLAN | Name | Purpose |
|---:|---|---|
| 10 | STAFF_DATA | Staff PCs |
| 20 | VOICE | IP phones |
| 50 | GUEST_WIFI | Guest wireless |
| 999 | NATIVE_UNUSED | Native VLAN |

SW1 configuration:

```text
enable
configure terminal
vlan 10
 name STAFF_DATA
vlan 20
 name VOICE
vlan 50
 name GUEST_WIFI
vlan 999
 name NATIVE_UNUSED

interface fastEthernet 0/5
 description Staff PC
 switchport mode access
 switchport access vlan 10

interface fastEthernet 0/6
 description IP Phone and PC
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20

interface gigabitEthernet 0/1
 description Trunk to SW2
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,50,999
end
```

SW2 should have matching VLANs and a matching trunk configuration on its uplink.

SW2 trunk configuration:

```text
interface gigabitEthernet 0/1
 description Trunk to SW1
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,50,999
```

The allowed VLAN list and native VLAN should match on both ends. If VLAN 50 is missing on one side, guest Wi-Fi traffic may fail across the trunk.

## 14.13 Verification Commands

Configuration without verification is incomplete. A professional technician proves the result.

Core VLAN and trunk verification commands:

```text
show vlan brief
show interfaces status
show interfaces switchport
show interfaces trunk
show running-config interface <interface-id>
show mac address-table
show mac address-table vlan <vlan-id>
```

Verification Command Table

| Command | What It Shows |
|---|---|
| `show vlan brief` | VLANs and access-port membership |
| `show interfaces status` | Port status, VLAN, speed, duplex, type |
| `show interfaces switchport` | Administrative and operational switchport mode |
| `show interfaces trunk` | Trunk status, native VLAN, allowed VLANs |
| `show running-config interface` | Interface configuration |
| `show mac address-table vlan 10` | MAC addresses learned in VLAN 10 |

What to look for:

- Does the VLAN exist?
- Is the port in the correct VLAN?
- Is the port actually access or trunk?
- Is the trunk operational?
- Is the native VLAN correct?
- Is the VLAN allowed on the trunk?
- Is the switch learning MAC addresses in the expected VLAN?

## 14.14 Troubleshooting VLAN and Trunk Problems

VLAN and trunk troubleshooting should be structured. Do not guess. Check the port, VLAN, trunk, and endpoint configuration.

Common VLAN and trunk problems:

| Symptom | Likely Cause | Verification |
|---|---|---|
| User gets wrong IP subnet | Access port in wrong VLAN | `show vlan brief` |
| User gets APIPA address | DHCP not reachable in VLAN | VLAN assignment, trunk, DHCP relay |
| VLAN works on one switch but not another | VLAN not allowed on trunk | `show interfaces trunk` |
| Native VLAN mismatch warning | Trunk native VLAN differs | `show interfaces trunk`, config |
| IP phone works but PC fails | Access VLAN wrong, voice VLAN correct | `show interfaces switchport` |
| PC works but phone fails | Voice VLAN missing or DHCP option issue | Interface config, voice VLAN |
| MAC learned in wrong VLAN | Port VLAN mismatch | `show mac address-table` |

Troubleshooting sequence:

1. Check the endpoint IP address and subnet.
2. Identify the switch port the endpoint uses.
3. Verify port status.
4. Verify port mode.
5. Verify access VLAN or voice VLAN.
6. Confirm the VLAN exists.
7. If traffic crosses switches, verify trunk status.
8. Confirm allowed VLAN list.
9. Confirm native VLAN match.
10. Check MAC address learning.

Example problem:

```text
PC on SW2 should be in VLAN 10.
PC receives no DHCP address.
VLAN 10 exists on SW2.
Access port is correct.
Trunk to SW1 allows VLANs 20,50,999 only.
```

Root cause:

```text
VLAN 10 is missing from the allowed VLAN list on the trunk.
```

Fix:

```text
interface gigabitEthernet 0/1
 switchport trunk allowed vlan add 10
```

Then verify:

```text
show interfaces trunk
```

## 14.15 Windows, Linux, and Cisco IOS Practical Checks

### Windows Checks

```text
ipconfig /all
ping <default-gateway>
arp -a
tracert <destination>
```

Windows does not normally show the switch VLAN directly. The technician uses Windows to check whether the host received the expected IP subnet, gateway, DNS server, and DHCP lease. If a staff PC receives a guest VLAN address, the switch port or wireless VLAN mapping should be checked.

### Linux Checks

```text
ip addr
ip route
ip neigh
ping <default-gateway>
```

Linux can show VLAN subinterfaces if the host itself is doing VLAN tagging, such as `eth0.10` or `ens33.20`. Most ordinary endpoints do not tag their own VLAN traffic, but servers and virtualization hosts may.

### Cisco IOS Checks

```text
show vlan brief
show interfaces status
show interfaces switchport
show interfaces trunk
show running-config interface fastEthernet 0/10
show running-config interface gigabitEthernet 0/1
show mac address-table
show mac address-table vlan 10
```

Cisco IOS is the primary verification point for VLAN configuration. The switch tells the technician what VLAN the port belongs to, whether the trunk is active, which VLANs are allowed, and whether MAC addresses are being learned.

## 14.17 Cybersecurity Relevance

VLAN configuration affects security directly. A secure design can be weakened by a careless switch configuration. If guest VLAN traffic is allowed across trunks where it is not needed, exposure increases. If a user-facing port negotiates a trunk, an attacker may attempt unauthorized VLAN access. If the native VLAN carries real user traffic, native VLAN misuse becomes more dangerous.

Security-focused VLAN configuration practices include:

- Force user ports to access mode.
- Disable DTP on ports where supported and appropriate.
- Do not use VLAN 1 for normal user traffic.
- Use a dedicated unused native VLAN.
- Restrict allowed VLANs on trunks.
- Shut down unused ports or place them in an unused parking VLAN.
- Document port purpose and VLAN assignment.
- Monitor unexpected MAC addresses and VLAN changes.

VLANs are not firewalls. They separate Layer 2 domains. Actual inter-VLAN security policy must be enforced by routers, Layer 3 switches, firewalls, ACLs, or identity-based controls.

## 14.18 Cloud Networking Relevance

In cloud environments, users may not configure physical switch VLANs directly, but VLAN trunking remains important in data centers, private clouds, colocation environments, and virtualization platforms.

A hypervisor host may connect to a physical switch using a trunk. Virtual machines may belong to different VLAN-backed networks. A firewall appliance may connect to a switch trunk so it can route or filter traffic for multiple VLANs. Wireless controllers and access points may also use trunks to carry multiple SSID VLANs.

Public cloud networking often presents subnets, route tables, and security groups instead of physical VLAN commands. Still, the same design thinking applies: separate traffic by function, carry only what is required, and verify the control points.

## 14.19 Interview and Exam Relevance

In IT support interviews, VLAN configuration questions often sound practical: "A user moved desks and now gets the wrong IP address. What do you check?" The answer should include switch port VLAN assignment, DHCP scope, and gateway.

In network engineering interviews, questions may focus on access ports, trunk ports, 802.1Q tags, native VLAN mismatch, DTP, allowed VLAN lists, and show commands.

For CCNA, students should know how to create VLANs, assign access ports, configure trunks, understand 802.1Q tagging, and verify with `show vlan brief` and `show interfaces trunk`. For Network+, students should understand VLAN purpose, trunking concepts, tagged vs. untagged traffic, and troubleshooting symptoms.

## 15. KEY TERMS / GLOSSARY

| Term | Meaning |
|---|---|
| VLAN Configuration | Creating VLANs, assigning ports, and configuring trunks on switches. |
| Access Port | Switch port that normally carries one VLAN for an endpoint. |
| Access VLAN | VLAN assigned to an access port. |
| Voice VLAN | VLAN used for IP phone traffic on a port that may also carry data. |
| Trunk Port | Switch port that carries multiple VLANs. |
| 802.1Q | IEEE standard for VLAN tagging on Ethernet trunks. |
| VLAN Tag | Information added to a frame to identify its VLAN on a trunk. |
| Native VLAN | VLAN that carries untagged traffic on an 802.1Q trunk. |
| Allowed VLAN List | List controlling which VLANs may cross a trunk. |
| DTP | Cisco Dynamic Trunking Protocol used to negotiate trunking. |
| Dynamic Auto | DTP mode that waits for the neighbor to request trunking. |
| Dynamic Desirable | DTP mode that actively tries to form a trunk. |
| Native VLAN Mismatch | Condition where trunk ends use different native VLANs. |
| Tagged Frame | Ethernet frame carrying an 802.1Q VLAN tag. |
| Untagged Frame | Ethernet frame without an 802.1Q VLAN tag. |
| Parking VLAN | Unused VLAN where unused access ports may be placed. |

## 16. COMPARISON TABLES

### 16.1 Access Port vs Trunk Port

| Feature | Access Port | Trunk Port |
|---|---|---|
| VLANs Carried | One VLAN, plus optional voice VLAN | Multiple VLANs |
| Common Use | Endpoint connections | Switch/router/firewall/AP/hypervisor links |
| Tagging | Usually untagged for endpoint data | Uses 802.1Q tags |
| Key Command | `switchport mode access` | `switchport mode trunk` |
| Common Problem | Wrong access VLAN | VLAN missing from allowed list |

### 16.2 Tagged vs Untagged Traffic

| Feature | Tagged Traffic | Untagged Traffic |
|---|---|---|
| VLAN Identifier | Present | Not present |
| Common Location | Trunk links | Access links or native VLAN |
| Standard | 802.1Q | Normal Ethernet frame |
| Switch Interpretation | Uses tag to identify VLAN | Uses access VLAN or native VLAN |

### 16.3 Static Trunking vs Dynamic Trunking

| Feature | Static Trunking | Dynamic Trunking |
|---|---|---|
| Configuration | Manually forced | Negotiated with DTP |
| Predictability | Higher | Lower |
| Security | Preferred in many networks | Risk if uncontrolled |
| Common Command | `switchport mode trunk` | `dynamic auto/desirable` |
| Best Use | Production trunks | Limited labs or controlled environments |

### 16.4 Native VLAN and Allowed VLAN List

| Feature | Native VLAN | Allowed VLAN List |
|---|---|---|
| Purpose | Handles untagged trunk traffic | Controls which VLANs cross trunk |
| Misconfiguration Risk | Native VLAN mismatch | Missing VLAN breaks connectivity |
| Verification | `show interfaces trunk` | `show interfaces trunk` |
| Best Practice | Use dedicated unused VLAN | Allow only needed VLANs |

## 17. REAL-WORLD EXAMPLE / ANALOGY

Think of a trunk as a delivery road shared by several departments. Each package needs a department label so it reaches the correct office at the other end. The 802.1Q tag is the department label. Without the label, the receiving switch would not know which VLAN the frame belongs to.

An access port is like a door into one department. A user entering that door belongs to that department. A trunk is like a service corridor carrying traffic for many departments, with labels keeping everything separated.

## 18. QUICK-RECAP CHEAT SHEET

- Create VLANs before assigning ports to them.
- Use clear VLAN names.
- Access ports normally carry one VLAN.
- `switchport mode access` forces access mode.
- `switchport access vlan <id>` assigns the access VLAN.
- Voice VLANs separate phone traffic from PC data traffic.
- Trunk ports carry multiple VLANs.
- `switchport mode trunk` forces trunk mode.
- 802.1Q tagging identifies VLAN traffic on trunks.
- The native VLAN carries untagged traffic on an 802.1Q trunk.
- Native VLANs should match on both trunk ends.
- Allowed VLAN lists limit which VLANs cross trunks.
- DTP can dynamically negotiate trunks on some Cisco switches.
- User-facing ports should not negotiate trunks.
- `show vlan brief` verifies VLANs and access-port membership.
- `show interfaces trunk` verifies trunks, native VLANs, and allowed VLANs.
- `show interfaces switchport` verifies access/trunk operational mode.
- Missing allowed VLANs can break same-VLAN communication across switches.
- VLANs separate Layer 2 traffic; inter-VLAN routing comes later.

## 7. LESSON ASSESSMENT

This assessment is intentionally focused. Students should answer clearly, use correct networking terminology, and show practical troubleshooting thinking.

### 7.1 Theory Questions

1. Explain the main networking concept covered in this lesson and describe its role in a real enterprise network.
2. Describe two technical problems that can occur when this lesson's concept is poorly designed or incorrectly configured.
3. Explain how a network technician or junior network engineer would verify that this part of the network is working correctly.
4. Describe one security, reliability, or performance concern related to this topic.
5. Explain how this topic connects to CCNA, Network+, IT support, or junior network engineering work.

### 7.2 Multiple-Choice Questions

1. What is the best reason for studying this lesson's topic?
   A. It helps students understand and support real network operation.
   B. It replaces the need for troubleshooting.
   C. It removes the need for IP addressing.
   D. It is only useful for memorizing definitions.

2. When troubleshooting a problem related to this lesson, what should be done first?
   A. Gather evidence and identify the exact scope of the problem.
   B. Replace every network device immediately.
   C. Delete the running configuration without backup.
   D. Assume the Internet service provider is always responsible.

3. Which habit best reflects professional network engineering practice?
   A. Verify changes with commands, tests, and documented results.
   B. Make random changes until something works.
   C. Ignore diagrams and rely only on memory.
   D. Avoid documenting successful fixes.

4. Which item is most useful when proving that a network feature is working?
   A. A successful test result compared with the expected result.
   B. A guess from another user.
   C. A device name with no configuration evidence.
   D. A screenshot unrelated to the problem.

5. What should students connect this lesson to during hands-on practice?
   A. Addressing, device roles, commands, verification, and troubleshooting.
   B. Only typing speed.
   C. Only cable color.
   D. Only memorizing vendor logos.

6. In an enterprise environment, why is documentation important for this topic?
   A. It helps future troubleshooting, audits, handover, and change control.
   B. It makes testing unnecessary.
   C. It disables security risks automatically.
   D. It replaces the need for correct configuration.

7. Which approach gives the strongest learning outcome?
   A. Combining technical explanation with lab practice and verification.
   B. Reading commands without understanding them.
   C. Skipping troubleshooting steps.
   D. Memorizing answers without using the network.

8. If a configuration change causes a new outage, what should the technician use?
   A. A rollback plan and saved baseline information.
   B. A random new subnet.
   C. A different monitor.
   D. A guess without evidence.

9. Which result shows that a student understands the lesson at a practical level?
   A. The student can explain the concept, configure or identify it, test it, and troubleshoot failure.
   B. The student can only repeat the title.
   C. The student avoids using commands.
   D. The student ignores enterprise examples.

10. Why are scenario questions included in this course?
   A. They train students to apply concepts to real network problems.
   B. They remove the need for labs.
   C. They focus only on spelling.
   D. They are unrelated to IT jobs.

### 7.3 Scenario-Based Questions

1. A user or department reports a connectivity problem related to this lesson's topic. Write the first five checks you would perform, the commands or tools you would use, and the evidence you expect to collect.
2. You are asked to explain this topic to a new IT support intern before a hands-on lab. Write a short technical explanation that connects the concept to real devices, real traffic flow, and troubleshooting.

### 7.4 Answer Guide

Theory answers should be marked for technical accuracy, clear explanation, correct terminology, and practical relevance to enterprise networking. Scenario answers should show a logical troubleshooting sequence, evidence gathering, likely causes, verification steps, and a professional final recommendation.

Multiple-choice answers: 1. A; 2. A; 3. A; 4. A; 5. A; 6. A; 7. A; 8. A; 9. A; 10. A
