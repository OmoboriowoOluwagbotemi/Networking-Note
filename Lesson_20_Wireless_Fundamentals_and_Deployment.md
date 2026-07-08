# LESSON 20: WIRELESS FUNDAMENTALS AND DEPLOYMENT

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 20.1 What Is Wireless Networking?

Wireless networking is the use of radio frequency signals to connect devices to a network without a physical Ethernet cable. In a wired Ethernet network, the signal travels through copper or fiber. In a wireless LAN, the signal travels through the air between a wireless client and a wireless access point.

Wireless LAN is commonly written as WLAN. A WLAN still belongs to the larger network. It still uses IP addressing, VLANs, DHCP, DNS, routing, NAT, firewalls, authentication, monitoring, and troubleshooting. The main difference is the access medium. Instead of plugging into a switchport with a cable, the user connects through a radio signal.

Wireless answers this question:

```text
How can devices connect to the LAN without a physical Ethernet cable?
```

A wireless network is not separate from normal networking. It is an extension of the wired LAN. The access point acts like a bridge between wireless clients and the wired network. Behind the access point, the traffic still reaches switches, routers, DHCP servers, DNS servers, firewalls, internet links, cloud services, and enterprise applications.

### 20.2 Why Wireless Networking Matters

Wireless matters because modern users expect mobility. Laptops, smartphones, tablets, barcode scanners, point-of-sale terminals, wireless printers, warehouse devices, CCTV cameras, IoT sensors, guest devices, and medical devices often need network access without being tied to a desk.

In an enterprise, wireless is no longer a convenience feature. It is a production network. If Wi-Fi fails in a school, teachers may not access online lessons. If Wi-Fi fails in a hospital, mobile workstations may not reach clinical systems. If Wi-Fi fails in a hotel, guests complain immediately. If Wi-Fi fails in a warehouse, scanners and inventory systems may stop working.

Wireless also matters because it introduces problems that do not exist in the same way on wired Ethernet. A cable either links up or it does not. Wireless depends on signal strength, noise, interference, walls, distance, client capability, channel planning, power levels, roaming behavior, authentication, and radio design.

For CCNA and CompTIA Network+, students must understand that wireless troubleshooting is not only about checking whether the SSID is visible. A professional troubleshooter checks radio conditions, authentication, VLAN mapping, DHCP, DNS, routing, NAT, firewall policy, and user device behavior.

### 20.3 How Wireless Fits Into the Network Path

A wireless client follows a full communication path before it can use applications.

Wireless Client Connectivity Path

| Stage | What Happens | Related Earlier Lesson |
|---|---|---|
| 1 | Client discovers SSID | Wireless fundamentals |
| 2 | Client associates to AP | Wireless fundamentals |
| 3 | Client authenticates | Wireless security |
| 4 | AP maps client to VLAN | VLAN design |
| 5 | Client receives IP settings | DHCP |
| 6 | Client resolves names | DNS |
| 7 | Client sends remote traffic to gateway | Routing |
| 8 | Firewall/NAT handles internet access | NAT/PAT and security |

This sequence is important. A user may say, "Wi-Fi is connected but internet is not working." That statement may mean the radio association succeeded, but DHCP failed. It may also mean DHCP worked, but DNS failed. It may also mean DNS worked, but the firewall or NAT policy is blocking internet traffic.

Wireless troubleshooting must therefore move from radio to network services.

## 20.4 RF Basics

RF means radio frequency. Wireless networks use radio waves to carry data through the air. A radio wave is electromagnetic energy that travels from a transmitter to a receiver.

In Wi-Fi, the access point and the client both transmit and receive radio signals. The AP is not only "sending internet." The client also sends frames back to the AP. Good wireless communication requires both directions to work.

Important RF ideas:

| Concept | Meaning |
|---|---|
| Frequency | The band where the radio signal operates |
| Channel | A smaller range inside a frequency band |
| Signal Strength | How strong the received wireless signal is |
| Noise | Unwanted RF energy that interferes with communication |
| SNR | Signal-to-noise ratio, the difference between useful signal and noise |
| Interference | Another signal or device disrupting communication |
| Attenuation | Signal weakening as it travels through distance or materials |
| Absorption | Signal energy being absorbed by walls, metal, glass, water, or people |
| Reflection | Signal bouncing off surfaces |
| Multipath | Signal reaching receiver through multiple reflected paths |

Wireless performance is not only about AP speed. A powerful AP cannot fully solve a weak client radio. Many laptops and phones transmit at lower power than an AP. If the AP is too far away, the client may hear the AP, but the AP may not hear the client clearly.

### 20.4.1 Signal Strength

Signal strength is commonly measured in dBm. Wireless signal values are usually negative numbers. A value closer to zero is stronger.

Example Signal Strength Guide

| Signal Strength | General Meaning |
|---|---|
| -30 dBm | Excellent, very close to AP |
| -50 dBm | Very good |
| -67 dBm | Common design target for voice/video |
| -70 dBm | Usable for normal data in many networks |
| -80 dBm | Weak and unreliable |
| -90 dBm | Very poor |

These values are practical guidelines, not absolute guarantees. Application type, noise, client capability, channel width, and environment all matter.

### 20.4.2 Noise and SNR

Noise is unwanted RF energy. SNR means signal-to-noise ratio. It compares the useful wireless signal to the background noise.

If signal strength is -65 dBm and noise is -90 dBm, the SNR is about 25 dB. That is usually much better than a signal of -65 dBm with noise at -72 dBm, because the useful signal is only slightly above the noise.

SNR Example

| Signal | Noise | Approximate SNR | Meaning |
|---|---|---|---|
| -60 dBm | -90 dBm | 30 dB | Good |
| -67 dBm | -90 dBm | 23 dB | Usually usable |
| -70 dBm | -80 dBm | 10 dB | Poor |
| -75 dBm | -78 dBm | 3 dB | Very poor |

Wireless troubleshooting should therefore consider both signal and noise. Strong signal with high noise can still perform badly.

## 20.5 Wi-Fi Frequency Bands: 2.4 GHz, 5 GHz, and 6 GHz

Wi-Fi commonly uses the 2.4 GHz, 5 GHz, and 6 GHz bands. Each band has different behavior.

Frequency Band Comparison

| Band | Main Strength | Main Limitation | Common Use |
|---|---|---|---|
| 2.4 GHz | Longer range, better wall penetration | Crowded, fewer non-overlapping channels, more interference | IoT, older devices, basic coverage |
| 5 GHz | More channels, better capacity than 2.4 GHz | Shorter range than 2.4 GHz | Enterprise laptops, phones, normal business Wi-Fi |
| 6 GHz | More spectrum and cleaner channels where allowed | Shorter range, newer client support needed, country rules vary | High-density, high-performance modern WLAN |

### 20.5.1 2.4 GHz Band

The 2.4 GHz band travels farther and penetrates walls better than higher bands, but it is often crowded. Bluetooth, microwave ovens, older cordless devices, wireless cameras, neighboring Wi-Fi networks, and many IoT devices can contribute to congestion.

The 2.4 GHz band has very limited clean channel capacity. In many deployments, channels 1, 6, and 11 are used because they do not overlap in the common 20 MHz channel plan. Using overlapping channels causes adjacent-channel interference, which can make the network slower and less reliable.

2.4 GHz is useful for coverage and compatibility, but it should not be treated as the main high-performance band in a modern enterprise if 5 GHz or 6 GHz are available.

### 20.5.2 5 GHz Band

The 5 GHz band provides more channels and usually less interference than 2.4 GHz. It is commonly used for enterprise laptops, smartphones, tablets, and general office Wi-Fi.

5 GHz does not travel as far as 2.4 GHz and does not penetrate walls as well. This is not always a disadvantage. Shorter range can allow better frequency reuse because APs interfere less with distant APs when the design is done properly.

5 GHz is usually the practical workhorse band for many enterprise WLANs.

### 20.5.3 6 GHz Band

The 6 GHz band provides additional spectrum for newer Wi-Fi generations such as Wi-Fi 6E and Wi-Fi 7, depending on country regulations and device support. It can provide cleaner spectrum and wider channels for high-throughput applications.

The limitation is that both the AP and client must support 6 GHz, and regulatory availability depends on the country. 6 GHz also has shorter range and weaker wall penetration than 2.4 GHz.

In a modern enterprise, 6 GHz is useful for high-density areas, newer devices, low-latency applications, and reducing load from crowded 2.4 GHz and 5 GHz bands.

## 20.6 Channels and Channel Width

A Wi-Fi band is divided into channels. A channel is a smaller range of frequencies that an AP uses to transmit.

Channel planning matters because nearby APs should not all use the same or overlapping channels. If they do, they must share airtime or interfere with each other.

Channel width controls how much spectrum one channel uses. Common channel widths include 20 MHz, 40 MHz, 80 MHz, 160 MHz, and in Wi-Fi 7, 320 MHz support in 6 GHz environments where available.

Channel Width Tradeoff

| Channel Width | Advantage | Disadvantage |
|---|---|---|
| 20 MHz | More channels, better reuse, more stable in dense networks | Lower peak throughput |
| 40 MHz | More throughput than 20 MHz | Uses more spectrum |
| 80 MHz | Higher throughput | Fewer clean channels, more interference risk |
| 160 MHz | Very high throughput | Hard to use cleanly in many enterprise areas |
| 320 MHz | Wi-Fi 7 high-throughput capability in 6 GHz | Requires compatible APs/clients and clean spectrum |

In enterprise design, wider is not always better. A school, hotel, office, or hospital with many APs may perform better with narrower channels because APs can reuse channels more effectively.

## 20.7 Channel Planning and Overlap

Channel planning is the process of choosing channels so APs can provide coverage without causing unnecessary interference.

There are two major problems:

1. Co-channel interference
2. Adjacent-channel interference

Co-channel interference happens when nearby APs use the same channel. Wi-Fi can coordinate shared channel use, but all devices on that channel must share airtime. This reduces capacity.

Adjacent-channel interference happens when nearby APs use overlapping channels. This is often worse because devices may not coordinate properly and instead corrupt each other's transmissions.

2.4 GHz Channel Planning

| Recommended 2.4 GHz Practice | Reason |
|---|---|
| Use 20 MHz channels | Preserves limited channel space |
| Commonly use channels 1, 6, and 11 | Avoids overlap in many regulatory domains |
| Avoid 40 MHz in most enterprises | Consumes too much 2.4 GHz spectrum |
| Reduce 2.4 GHz power if needed | Prevents excessive cell overlap |
| Disable 2.4 GHz on some APs if design allows | Reduces congestion in dense areas |

5 GHz and 6 GHz offer more channel options, but channel planning still matters. Automatic radio resource management can help, but administrators must still validate results.

## 20.8 Wi-Fi Standards: 802.11 a/b/g/n/ac/ax/be

IEEE 802.11 is the family of wireless LAN standards. The letters identify amendments and generations of Wi-Fi technology.

Wi-Fi Standards Summary

| Standard | Common Name | Main Bands | Practical Notes |
|---|---|---|---|
| 802.11a | Wi-Fi 2-era naming, not commonly branded today | 5 GHz | Older standard, up to 54 Mbps theoretical |
| 802.11b | Wi-Fi 1-era naming, not commonly branded today | 2.4 GHz | Older, slow, can reduce performance if supported |
| 802.11g | Wi-Fi 3-era naming, not commonly branded today | 2.4 GHz | Older, up to 54 Mbps theoretical |
| 802.11n | Wi-Fi 4 | 2.4 GHz and 5 GHz | Introduced MIMO, common legacy support |
| 802.11ac | Wi-Fi 5 | 5 GHz | Wider channels, higher throughput, common in enterprises |
| 802.11ax | Wi-Fi 6 / Wi-Fi 6E | 2.4 GHz, 5 GHz, 6 GHz for 6E | Better efficiency, OFDMA, high-density improvements |
| 802.11be | Wi-Fi 7 | 2.4 GHz, 5 GHz, 6 GHz | Multi-link operation, wider channels, very high throughput features |

Theoretical speed values are not the same as real user throughput. Wireless speed depends on signal, noise, distance, channel width, number of spatial streams, client capability, AP capability, interference, encryption, application behavior, and wired uplink capacity.

### 20.8.1 Wi-Fi 4, Wi-Fi 5, Wi-Fi 6, Wi-Fi 6E, and Wi-Fi 7

Wi-Fi generation names make standards easier to discuss.

Wi-Fi Generation Comparison

| Generation | IEEE Standard | Key Idea |
|---|---|---|
| Wi-Fi 4 | 802.11n | MIMO and improved throughput |
| Wi-Fi 5 | 802.11ac | Better 5 GHz performance and wider channels |
| Wi-Fi 6 | 802.11ax | Efficiency and high-density improvements |
| Wi-Fi 6E | 802.11ax in 6 GHz | Extends Wi-Fi 6 into 6 GHz where allowed |
| Wi-Fi 7 | 802.11be | Extremely high throughput, MLO, wider channels |

For CCNA and Network+, students should not only memorize names. They should understand the trend: newer standards improve efficiency, capacity, and client experience, but real performance still depends on design.

## 20.9 SSID, BSSID, and ESSID

An SSID is the wireless network name users see, such as `FEMTECT-STAFF`, `FEMTECT-GUEST`, or `WAREHOUSE-SCANNERS`.

A BSSID is the MAC address of a radio interface advertising a WLAN. If three APs advertise the same SSID, each AP radio still has its own BSSID.

An ESSID is an extended service set name. In practical use, many administrators use SSID to refer to the network name across multiple APs.

SSID Concepts

| Term | Meaning |
|---|---|
| SSID | Wireless network name |
| BSSID | MAC address of a specific AP radio/WLAN instance |
| ESS | Multiple APs providing the same WLAN across an area |
| Hidden SSID | SSID not advertised in beacon name field, but not true security |

Hiding an SSID is not strong security. Wireless frames can still reveal network information. Proper security comes from strong authentication and encryption, not hiding the name.

## 20.10 Wireless Association and Authentication

A wireless client must associate before it can send normal network traffic through an AP. Association is the process of joining a wireless network at Layer 2.

Basic Wireless Join Process

| Step | Explanation |
|---|---|
| 1 | Client scans for available SSIDs |
| 2 | Client selects an SSID |
| 3 | Client and AP negotiate capabilities |
| 4 | Client authenticates using the WLAN security method |
| 5 | Client associates to the AP |
| 6 | Client is placed into the mapped VLAN or policy |
| 7 | Client obtains IP configuration through DHCP |
| 8 | Client begins normal network communication |

Authentication may be simple, such as a pre-shared key in a small office, or enterprise-grade, such as 802.1X authentication using a RADIUS server. Lesson 21 will go deeper into wireless and network security. This lesson focuses on deployment fundamentals.

## 20.11 Access Points

An access point is a network device that provides wireless access to the wired LAN. It has radio interfaces for wireless clients and a wired Ethernet uplink to the switching infrastructure.

The AP does not replace switching, routing, DHCP, DNS, or firewalls. It provides the wireless access layer.

Access Point Functions

| Function | Explanation |
|---|---|
| Advertise SSIDs | Makes WLANs available to clients |
| Bridge wireless to wired | Moves client traffic into the LAN |
| Enforce WLAN security | Applies authentication/encryption settings |
| Map SSIDs to VLANs | Places users into the correct network segment |
| Manage radio settings | Uses channels, power, and band steering |
| Support roaming | Allows clients to move between AP coverage cells |

Most enterprise APs are powered using PoE. This allows a single Ethernet cable to provide both data and power from a PoE switch.

## 20.12 Autonomous APs vs Lightweight APs

Autonomous APs are individually configured and managed. Each AP stores its own configuration. This can work in a small office or lab, but it becomes difficult when many APs are deployed.

Lightweight APs are centrally managed by a wireless LAN controller or cloud controller. The APs focus on radio service, while the controller provides centralized configuration, monitoring, firmware management, WLAN policy, and roaming support.

Autonomous vs Lightweight APs

| Feature | Autonomous AP | Lightweight AP |
|---|---|---|
| Management | Individually configured | Centrally managed |
| Best Fit | Small sites, simple networks, labs | Enterprise WLANs |
| Scaling | Difficult as AP count grows | Easier for many APs |
| Policy Consistency | Manual consistency needed | Central policy |
| Roaming Support | Limited or less centralized | Better enterprise roaming support |
| Troubleshooting | AP-by-AP | Central visibility |

In real enterprises, lightweight or cloud-managed APs are common because wireless networks need consistent SSID settings, security, VLAN mapping, channel planning, and monitoring across many APs.

## 20.13 Wireless LAN Controllers

A wireless LAN controller, or WLC, centrally manages lightweight APs. Depending on the design, the WLC may manage control traffic only, or it may also tunnel user traffic.

WLC Functions

| Function | Explanation |
|---|---|
| AP Registration | Lightweight APs join the controller |
| WLAN Configuration | SSIDs, security, VLAN mapping, QoS |
| RF Management | Channel and power control |
| Roaming Support | Helps clients move between APs |
| Monitoring | Client, AP, and radio visibility |
| Firmware Management | Updates AP software |
| Security Integration | RADIUS, guest portals, access policy |

Some modern WLAN systems use cloud management instead of an on-premises controller. The same design principles still apply: SSID, VLAN, security, RF, DHCP, DNS, routing, and policy must all align.

## 20.14 SSID Design

SSID design is the process of deciding how many wireless networks to advertise, what they are used for, and how they map to VLANs and security policies.

A common mistake is creating too many SSIDs. Each SSID adds management overhead and consumes airtime because beacon and management frames must be transmitted. In enterprise design, fewer well-planned SSIDs are usually better than many casual SSIDs.

Example SSID Design

| SSID | Users | VLAN | Authentication | Access Policy |
|---|---|---|---|---|
| FEMTECT-STAFF | Employees | VLAN 10 | WPA2/WPA3 Enterprise | Internal apps, internet |
| FEMTECT-GUEST | Visitors | VLAN 30 | Captive portal or guest PSK | Internet only |
| FEMTECT-VOICE | Wi-Fi phones | VLAN 20 | Enterprise/PSK depending design | Voice services |
| FEMTECT-IOT | Cameras, sensors, devices | VLAN 60 | Device-specific policy | Limited internal access |

SSID design should follow segmentation design from the VLAN lessons. A guest SSID should not drop users into the staff VLAN. An IoT SSID should not provide unrestricted access to servers. A staff SSID should use stronger authentication than a guest SSID.

## 20.15 Guest Networks

A guest network provides internet access for visitors while protecting internal resources. Guest Wi-Fi is common in offices, schools, churches, hotels, restaurants, hospitals, training centers, and event venues.

Guest Wi-Fi should be separated from internal networks using VLANs, firewall rules, captive portals, client isolation, rate limits, and DNS/security filtering where appropriate.

Guest Wi-Fi Design Principles

| Principle | Why It Matters |
|---|---|
| Separate guest VLAN | Prevents guests from sharing staff subnet |
| Internet-only firewall policy | Protects internal servers and devices |
| Client isolation | Prevents guests from attacking each other |
| Bandwidth limits | Protects business-critical traffic |
| Clear DNS policy | Supports filtering and logging |
| Captive portal where needed | Provides terms, branding, or access control |
| Lease time planning | Handles high turnover of guest devices |

Guest networks should be treated as untrusted networks.

## 20.16 SSID-to-VLAN Mapping

An SSID often maps to a VLAN. This connects wireless design to Layer 2 segmentation.

For example:

```text
FEMTECT-STAFF -> VLAN 10 -> 192.168.10.0/24
FEMTECT-GUEST -> VLAN 30 -> 192.168.30.0/24
FEMTECT-IOT   -> VLAN 60 -> 192.168.60.0/24
```

The AP uplink port is commonly configured as a trunk so it can carry multiple VLANs. The AP tags client traffic according to the SSID/VLAN mapping.

SSID-to-VLAN Mapping

| SSID | VLAN | Subnet | Gateway | DHCP Scope | DNS |
|---|---|---|---|---|---|
| FEMTECT-STAFF | 10 | 192.168.10.0/24 | 192.168.10.1 | Staff scope | Internal DNS |
| FEMTECT-GUEST | 30 | 192.168.30.0/24 | 192.168.30.1 | Guest scope | Public/filtered DNS |
| FEMTECT-IOT | 60 | 192.168.60.0/24 | 192.168.60.1 | IoT scope/reservations | Internal/filtered DNS |

This is why earlier lessons matter. If VLANs, trunks, DHCP scopes, DNS options, routing, NAT, or firewall policy are wrong, Wi-Fi clients may associate successfully but still fail to use the network.

## 20.17 Roaming

Roaming is the process where a wireless client moves from one AP to another while staying on the same WLAN. The client usually decides when to roam. The infrastructure can encourage roaming, but the client makes many of the final decisions.

Good roaming matters for mobile users, Wi-Fi calling, voice handsets, scanners, warehouse devices, hospitals, and campuses.

Roaming Problems

| Symptom | Possible Cause |
|---|---|
| Device sticks to far AP | Client roaming behavior, AP power too high |
| Voice call drops while walking | Poor overlap, slow authentication, weak signal |
| Scanner disconnects in warehouse aisle | Coverage hole or interference |
| User reconnects but loses IP | VLAN mismatch between APs |
| Roaming works in one area but not another | RF design inconsistency |

Enterprise roaming may use features such as 802.11k, 802.11v, and 802.11r, depending on client and infrastructure support. Students should understand the purpose: helping clients discover, choose, and transition between APs more efficiently.

## 20.18 Site Survey Concepts

A wireless site survey is the process of measuring and planning wireless coverage, capacity, interference, and AP placement.

Wireless should not be designed only by guessing where APs look nice on the ceiling. Walls, concrete, metal, glass, elevators, generators, shelves, machinery, people, neighboring networks, and building layout all affect Wi-Fi.

Types of Wireless Survey

| Survey Type | Purpose |
|---|---|
| Predictive Survey | Uses floor plans and software to estimate AP placement before installation |
| Passive Survey | Measures existing RF signals without actively connecting |
| Active Survey | Connects to the WLAN and tests performance |
| Spectrum Analysis | Detects RF energy and non-Wi-Fi interference |
| Post-Deployment Survey | Validates actual coverage after installation |

A professional deployment often combines predictive planning with real-world validation.

## 20.19 Capacity Planning

Coverage means the signal reaches an area. Capacity means the network can support the number of users, devices, and applications in that area.

A single AP may cover a large open hall, but it may not support hundreds of active users well. A classroom, conference room, hotel lobby, church auditorium, lecture hall, or event center may require multiple APs because of capacity, not just coverage.

Capacity Planning Factors

| Factor | Why It Matters |
|---|---|
| Number of users | More users share airtime |
| Number of devices per user | Phones, laptops, tablets increase load |
| Application type | Video and voice need more stable performance |
| Airtime use | Slow clients consume more airtime |
| Channel reuse | Determines how APs share spectrum |
| Wired uplink | AP performance can be limited by switch uplink |
| PoE budget | APs may need PoE+, PoE++, or reduced features |

Wireless design should ask what users will do, not only whether the signal reaches them.

## 20.20 AP Placement and Power

AP placement affects coverage, roaming, interference, and performance.

APs should usually be placed where users are, not only where cabling is convenient. Ceiling-mounted APs often provide better coverage than APs hidden in cabinets, above metal ceilings, behind walls, or beside electrical noise sources.

AP Placement Guidelines

| Guideline | Reason |
|---|---|
| Place APs near user areas | Supports usable signal |
| Avoid hiding APs behind metal or concrete | Reduces attenuation |
| Avoid placing APs too close together at high power | Prevents excessive overlap |
| Use proper mounting orientation | Antenna pattern matters |
| Plan for cable and PoE | AP must connect reliably |
| Validate after installation | Real buildings differ from drawings |

Higher transmit power is not always better. If APs transmit too loudly, clients may remain connected to a far AP instead of roaming to a closer AP. This creates sticky client problems and poor performance.

## 20.21 Local Realities in Wireless Deployment

Real deployments must consider local conditions. In many environments, especially where power and cabling are inconsistent, wireless performance can fail for reasons that are not purely RF.

Local Deployment Considerations

| Reality | Design Response |
|---|---|
| Unstable power | Use UPS, inverter, or proper PoE switching |
| Thick walls/concrete | Perform survey and add APs where needed |
| Metal roofs/shelves | Expect reflection and attenuation |
| Generator noise/electrical issues | Protect switches and APs with stable power |
| Mixed old/new devices | Keep compatibility without letting old clients hurt performance |
| ISP instability | Separate Wi-Fi issue from internet issue |
| Outdoor coverage needs | Use proper outdoor-rated APs and grounding |
| High guest turnover | Use correct DHCP lease time and guest isolation |

In Nigerian offices, schools, training centers, shops, and warehouses, power stability and building materials can strongly affect wireless reliability. A good wireless design includes power protection and physical installation quality, not only AP model selection.

## 20.22 Windows Wireless Verification

Windows clients can show useful wireless information.

Useful Windows Wireless Commands

| Command | Purpose |
|---|---|
| `netsh wlan show interfaces` | Shows SSID, BSSID, radio type, channel, signal, receive/transmit rate |
| `netsh wlan show profiles` | Lists saved wireless profiles |
| `ipconfig /all` | Shows IP, DHCP, DNS, gateway, adapter details |
| `ping gateway` | Tests local connectivity after association |
| `nslookup name` | Tests DNS resolution |
| `tracert destination` | Tests routed path |

Example troubleshooting flow on Windows:

```text
netsh wlan show interfaces
ipconfig /all
ping default-gateway
nslookup www.example.com
tracert 8.8.8.8
```

This sequence checks wireless association, IP configuration, gateway reachability, DNS, and path.

## 20.23 Linux Wireless Verification

Linux commands vary by distribution, but the troubleshooting logic is the same.

Useful Linux Wireless Commands

| Command | Purpose |
|---|---|
| `iw dev` | Shows wireless interfaces |
| `iw dev wlan0 link` | Shows current wireless link information |
| `nmcli dev wifi list` | Lists visible Wi-Fi networks on NetworkManager systems |
| `nmcli connection show` | Shows configured connections |
| `ip addr` | Shows IP addresses |
| `ip route` | Shows default gateway and routes |
| `resolvectl status` | Shows DNS resolver details |
| `dig name` | Tests DNS resolution |

Linux verification should confirm both the wireless link and normal IP connectivity.

## 20.24 Cisco Wireless and Switching Verification

In Cisco-based networks, wireless troubleshooting often requires checking the AP, switchport, VLAN trunking, PoE, WLC, and client state.

Useful Cisco Switching Checks for APs

| Command | Purpose |
|---|---|
| `show interfaces status` | Confirms AP port status and speed |
| `show power inline` | Verifies PoE delivery |
| `show interfaces trunk` | Confirms VLANs allowed to AP |
| `show vlan brief` | Confirms VLAN exists |
| `show mac address-table interface` | Verifies learned MACs |
| `show cdp neighbors` | Identifies connected Cisco APs where supported |
| `show lldp neighbors` | Identifies connected APs using LLDP |

Wireless controller commands vary by platform. In general, administrators verify AP join status, client association, WLAN/SSID configuration, VLAN mapping, authentication logs, RF health, and client DHCP behavior.

## 20.25 Troubleshooting Wireless Problems

Wireless troubleshooting must separate radio problems from network service problems.

Wireless Troubleshooting Table

| Symptom | Likely Area | Example Checks |
|---|---|---|
| SSID not visible | AP/radio/SSID broadcast | AP online, WLAN enabled, radio enabled |
| Cannot connect to SSID | Authentication/security | Password, 802.1X, RADIUS, client support |
| Connected but no IP | DHCP/VLAN/relay | VLAN mapping, DHCP scope, helper address |
| Has IP but no internet | Gateway/routing/NAT/firewall | Default gateway, route, NAT, policy |
| Internet works but internal names fail | DNS | DNS server option, internal zone |
| Slow Wi-Fi | RF/capacity/interference | Signal, SNR, channel, airtime, clients |
| Drops while moving | Roaming/coverage | AP overlap, power, roaming support |
| Only old devices fail | Compatibility/security | Supported standards and encryption |

Do not troubleshoot wireless only from the AP. Always test from the client perspective too.

## 20.26 Packet Tracer Practice

### Practice Lab 1: Basic Wireless LAN

Build a simple wireless network with:

| Device | Role |
|---|---|
| Wireless router or AP | Provides WLAN |
| Laptop | Wireless client |
| Switch | Wired LAN connection |
| Server | DHCP and DNS |
| Router/firewall | Default gateway/internet path |

Configure one SSID named `FEMTECT-STAFF`. Configure WPA2-Personal for the lab. Configure DHCP so the wireless laptop receives an IP address, default gateway, and DNS server. Verify that the laptop can ping the gateway and resolve a DNS name.

### Practice Lab 2: SSID-to-VLAN Design

Build a design with two SSIDs:

| SSID | VLAN | Subnet | Purpose |
|---|---|---|---|
| FEMTECT-STAFF | 10 | 192.168.10.0/24 | Staff users |
| FEMTECT-GUEST | 30 | 192.168.30.0/24 | Guest users |

Configure the AP uplink as a trunk if the Packet Tracer device supports it. Configure DHCP scopes for both VLANs. Verify that staff and guest clients receive addresses from the correct subnet.

Expected result:

```text
Staff wireless client receives 192.168.10.x
Guest wireless client receives 192.168.30.x
Guest client cannot access internal server if firewall/ACL policy is configured
Both clients can reach the internet path if NAT/routing is configured
```

### Practice Lab 3: Wireless Troubleshooting

Intentionally create faults:

| Fault | Expected Symptom |
|---|---|
| Wrong Wi-Fi password | Client cannot authenticate |
| Wrong VLAN mapping | Client receives wrong subnet |
| Missing DHCP scope | Client fails to obtain IP |
| Missing DNS option | Client has IP but name resolution fails |
| Blocked VLAN on trunk | Clients on one SSID fail |

Students should document symptoms, test results, root cause, and fix.

## 20.27 Cybersecurity Relevance

Wireless extends the network beyond physical walls. An attacker does not need to plug into a switchport if wireless security is weak. A person near the building may see SSIDs and attempt attacks.

Wireless security topics include encryption, authentication, rogue APs, evil twin APs, weak pre-shared keys, guest isolation, management frame protection, RADIUS authentication, and monitoring.

Wireless Security Risks

| Risk | Explanation |
|---|---|
| Weak PSK | Attackers may guess or capture handshake for offline cracking |
| Shared guest password | Password spreads beyond intended users |
| Rogue AP | Unauthorized AP connected to network |
| Evil twin | Fake AP impersonates legitimate SSID |
| No client isolation | Guests can attack other guests |
| Wrong VLAN mapping | Guest or IoT users reach internal systems |
| Open management interface | AP/controller exposed to attackers |

Lesson 21 will go deeper into WPA2, WPA3, enterprise 802.1X, and broader network security. For now, students should remember that wireless deployment must be designed with segmentation and authentication from the beginning.

## 20.28 Cloud Networking Relevance

Wireless itself is local radio access, but many modern WLAN systems are cloud-managed. Cloud-managed wireless platforms allow administrators to configure SSIDs, view clients, monitor AP health, push firmware, and apply policy from a web portal.

Cloud-managed does not mean the wireless traffic always goes through the cloud. In many systems, the management plane is cloud-based while user traffic remains local. Students must distinguish management traffic from user data traffic.

Cloud Wireless Concepts

| Concept | Explanation |
|---|---|
| Cloud-managed AP | AP receives configuration and monitoring through cloud dashboard |
| Local switching | Client traffic exits locally into VLANs |
| Centralized policy | SSID/security settings managed centrally |
| Remote monitoring | Admin can view AP/client health from anywhere |
| Dependency planning | Internet outage may affect management visibility |
| Hybrid DNS/RADIUS | Cloud-managed WLAN may still use local enterprise services |

Cloud-managed WLANs are common in branch offices, schools, retail stores, and distributed organizations.

## 20.29 Interview and Exam Relevance

In IT support interviews, wireless questions often focus on practical troubleshooting. Candidates may be asked what to check when a laptop connects to Wi-Fi but has no internet, why a client gets APIPA, why guest Wi-Fi should be separated, or why Wi-Fi is slow in one area.

In network engineering interviews, wireless questions may focus on RF design, channel planning, AP placement, SSID-to-VLAN mapping, WLCs, guest isolation, roaming, and site surveys.

For CCNA, students should know AP roles, WLC concepts, CAPWAP at a high level, WLAN security basics, SSID-to-VLAN design, and wireless troubleshooting logic.

For CompTIA Network+ N10-009, students should know wireless standards, bands, channel planning, antenna/RF concepts, SSIDs, encryption concepts, guest networks, and troubleshooting.

## 21. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| WLAN | Wireless Local Area Network. |
| RF | Radio frequency, electromagnetic signal used for wireless communication. |
| Frequency | The radio band used for transmission, such as 2.4 GHz, 5 GHz, or 6 GHz. |
| Channel | A smaller frequency range inside a Wi-Fi band. |
| Channel Width | Amount of spectrum used by a Wi-Fi channel. |
| Signal Strength | Power level of received wireless signal, often measured in dBm. |
| Noise | Unwanted RF energy that disrupts communication. |
| SNR | Signal-to-noise ratio. |
| Interference | Disruption caused by other RF signals or devices. |
| Attenuation | Signal weakening over distance or through materials. |
| SSID | Wireless network name. |
| BSSID | MAC address of a specific AP radio/WLAN instance. |
| AP | Access point, a device that provides wireless access to the wired LAN. |
| WLC | Wireless LAN controller. |
| Autonomous AP | AP that is individually configured and managed. |
| Lightweight AP | AP centrally managed by a controller or cloud platform. |
| Roaming | Moving between APs while staying connected to the WLAN. |
| Site Survey | Wireless planning and measurement process. |
| Co-channel Interference | Nearby devices sharing the same channel and airtime. |
| Adjacent-channel Interference | Interference from overlapping channels. |
| Guest Network | Separated WLAN for visitors. |
| Captive Portal | Web-based guest access or terms page. |
| Client Isolation | Feature that prevents wireless clients from communicating directly with each other. |
| Band Steering | Encouraging capable clients to use a preferred band, often 5 GHz or 6 GHz. |

## 22. COMPARISON TABLES

### 22.1 2.4 GHz vs 5 GHz vs 6 GHz

| Feature | 2.4 GHz | 5 GHz | 6 GHz |
|---|---|---|---|
| Range | Best | Medium | Shorter |
| Wall Penetration | Best | Medium | Lowest |
| Channel Capacity | Low | Higher | Highest where available |
| Interference | Often high | Usually lower | Usually cleaner |
| Device Support | Very broad | Broad | Newer devices |
| Best Use | Compatibility/IoT | Enterprise general use | High capacity/new devices |

### 22.2 Autonomous AP vs Lightweight AP

| Feature | Autonomous AP | Lightweight AP |
|---|---|---|
| Configuration | Per AP | Centralized |
| Scaling | Limited | Strong |
| Best Environment | Small office/lab | Enterprise |
| Troubleshooting | Device by device | Central dashboard/controller |
| Policy Consistency | Manual | Central template/policy |

### 22.3 Coverage vs Capacity

| Feature | Coverage | Capacity |
|---|---|---|
| Main Question | Does signal reach the area? | Can the network support the users/apps? |
| Solved By | AP placement and signal design | AP density, channel reuse, airtime planning |
| Common Mistake | Assuming signal bars prove quality | Ignoring number of active devices |
| Example | One AP covers a hall | Three APs needed for 300 users |

### 22.4 Co-channel vs Adjacent-channel Interference

| Feature | Co-channel Interference | Adjacent-channel Interference |
|---|---|---|
| Meaning | Same channel nearby | Overlapping channels nearby |
| Behavior | Devices share airtime | Devices may corrupt transmissions |
| Common Fix | Better channel reuse and power control | Use non-overlapping channels |
| 2.4 GHz Example | Two APs on channel 6 | APs on channels 4 and 6 |

### 22.5 Wireless Troubleshooting Domains

| Domain | What to Check |
|---|---|
| RF | Signal, noise, SNR, interference, channel |
| Association | SSID visibility, AP availability, client support |
| Authentication | PSK, 802.1X, RADIUS, certificates |
| VLAN | SSID mapping, trunk, allowed VLANs |
| DHCP | Scope, relay, lease, APIPA |
| DNS | Resolver, records, name resolution |
| Routing/NAT | Gateway, routes, firewall, internet path |

## 23. REAL-WORLD EXAMPLE / ANALOGY

Think of wireless coverage like speaking in a crowded hall. If the speaker is close and the room is quiet, communication is easy. If the speaker is far away, many people are talking, and walls block the sound, communication becomes difficult.

An AP is like the speaker and listener for the wireless network, but communication is two-way. The client must also be heard clearly. This is why simply increasing AP power is not always the answer. The AP may shout loudly, but a phone or laptop may still whisper back weakly.

Professional wireless design is about clear two-way communication, enough capacity for the people in the room, and proper connection to the rest of the network.

## 24. QUICK-RECAP CHEAT SHEET

- WLAN means wireless local area network.
- Wi-Fi uses RF signals instead of copper or fiber to reach clients.
- Wireless still depends on VLANs, DHCP, DNS, routing, NAT, and security.
- 2.4 GHz has better range but more congestion.
- 5 GHz provides better enterprise capacity than 2.4 GHz.
- 6 GHz provides newer, cleaner spectrum where supported and allowed.
- Channel planning prevents unnecessary interference.
- 2.4 GHz commonly uses non-overlapping channels 1, 6, and 11.
- Wider channels increase peak speed but reduce channel reuse.
- SSID is the wireless network name.
- BSSID is the MAC address of a specific AP radio/WLAN instance.
- APs bridge wireless clients to the wired LAN.
- Autonomous APs are individually managed.
- Lightweight APs are centrally managed by WLC or cloud platform.
- WLCs centralize WLAN configuration, AP management, RF control, and monitoring.
- SSIDs should map to correct VLANs and security policies.
- Guest Wi-Fi should be isolated from internal networks.
- Roaming allows clients to move between APs.
- Site surveys validate coverage, capacity, and interference.
- Wi-Fi troubleshooting must separate RF, authentication, VLAN, DHCP, DNS, routing, NAT, and firewall issues.

## 25. REVIEW QUESTIONS

1. What does WLAN stand for?
2. What does RF mean?
3. Why is wireless still part of the normal LAN?
4. Which Wi-Fi band usually has the best range?
5. Which Wi-Fi band usually provides more capacity than 2.4 GHz in enterprise networks?
6. What is the main advantage of 6 GHz Wi-Fi?
7. What are the commonly used non-overlapping 2.4 GHz channels?
8. Why are wider channels not always better in enterprise WLANs?
9. What is an SSID?
10. What is a BSSID?
11. What is an access point?
12. What is the difference between an autonomous AP and a lightweight AP?
13. What does a WLC do?
14. Why should guest Wi-Fi be placed in a separate VLAN?
15. What is SSID-to-VLAN mapping?
16. What is roaming?
17. What is a wireless site survey?
18. What is the difference between coverage and capacity?
19. What should be checked when a wireless client connects but receives no IP address?
20. Why is increasing AP transmit power not always the correct fix?

## 26. SUGGESTED ANSWER GUIDE

1. Wireless Local Area Network.
2. Radio frequency.
3. Because wireless clients still use VLANs, IP addressing, DHCP, DNS, routing, NAT, and security services.
4. 2.4 GHz.
5. 5 GHz.
6. More spectrum and cleaner channels where supported and allowed.
7. Channels 1, 6, and 11.
8. Wider channels consume more spectrum and reduce channel reuse, which can hurt dense deployments.
9. The wireless network name.
10. The MAC address of a specific AP radio/WLAN instance.
11. A device that provides wireless access to the wired LAN.
12. An autonomous AP is individually managed; a lightweight AP is centrally managed.
13. It centrally manages APs, WLANs, RF settings, roaming support, monitoring, and policy.
14. To protect internal resources and apply separate guest security policy.
15. Assigning clients from a specific SSID into a specific VLAN/subnet.
16. Moving from one AP to another while staying connected to the WLAN.
17. A process for measuring and planning wireless coverage, capacity, interference, and AP placement.
18. Coverage means signal reaches the area; capacity means the WLAN can support the number of users and applications.
19. VLAN mapping, trunk allowed VLANs, DHCP scope, DHCP relay/helper address, and DHCP server reachability.
20. Because clients may not transmit back strongly enough and high AP power can create sticky clients and excessive overlap.
