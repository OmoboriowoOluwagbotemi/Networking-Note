# LESSON 25: DIAGNOSE, DOCUMENT, DECIDE

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 25.1 What Does Diagnose, Document, Decide Mean?

This final lesson converts the knowledge from Lessons 1 through 24 into professional practice.

**Diagnose** means identifying the actual cause of a problem through evidence, structured testing, and technical reasoning. It is not random command entry or changing several settings until the symptom disappears.

**Document** means creating an accurate record of the network, incident, change, decision, and operational state so that another qualified person can understand and support it.

**Decide** means selecting the next technical action and career direction based on evidence, risk, business need, and personal capability.

These three activities are connected:

```text
Good diagnosis produces reliable evidence.
Reliable evidence produces useful documentation.
Useful documentation supports better decisions.
```

### 25.2 Why This Lesson Matters

Employers do not only need people who can define VLAN, DHCP, OSPF, or VPN. They need people who can enter an unfamiliar environment, understand the service, collect evidence, communicate clearly, restore operation safely, and prevent recurrence.

A technically correct fix can still be unprofessional if it:

- Creates an undocumented security weakness
- Breaks another service
- Cannot be reproduced
- Has no rollback plan
- Hides the root cause
- Leaves no record for the next shift
- Exposes passwords or customer information

Professional networking combines technical skill, process discipline, communication, and judgment.

### 25.3 How the Course Fits Together

| Course Foundation | Capstone Use |
|---|---|
| Physical media and Ethernet | Check power, links, errors, speed, duplex, frames |
| VLANs and STP | Verify access/trunk state, VLAN path, and loop prevention |
| IPv4/IPv6 and subnetting | Validate addressing, masks, gateways, and routes |
| Routing and NAT | Trace remote paths and Internet translation |
| DHCP and DNS | Separate configuration and name-resolution failures |
| Wireless | Distinguish RF, association, authentication, and IP problems |
| Security | Preserve least privilege while troubleshooting |
| Monitoring and logging | Compare behavior with baselines and timelines |
| Power and resilience | Identify environmental dependencies and recovery needs |

## 25.4 Troubleshooting as a Controlled Process

A troubleshooting methodology prevents guesswork and reduces the chance of creating a second problem.

A practical process is:

1. Identify and define the problem.
2. Establish a theory of probable cause.
3. Test the theory.
4. Create a plan of action.
5. Implement the approved solution or escalate.
6. Verify full functionality and apply preventive measures.
7. Document findings, actions, results, and lessons.

The process is iterative. If evidence disproves the theory, return to the evidence and form a better theory.

### 25.4.1 Identify the Problem

Ask precise questions:

- What exactly fails?
- Who is affected?
- Which locations, VLANs, applications, and times are involved?
- Did it ever work?
- What changed?
- Is the problem constant or intermittent?
- What error does the user see?
- What still works?
- What is the business impact?

"The network is down" is not a diagnosis. "Four Finance PCs on access switch SW2 cannot reach their default gateway after yesterday's desk move, while other VLANs remain operational" is a usable problem statement.

### 25.4.2 Establish Scope

Start with the smallest confirmed facts:

```text
One application or all applications?
One host or many hosts?
One port, VLAN, switch, site, or entire organization?
Local network, remote network, Internet, or DNS only?
Wired, wireless, or both?
```

The scope helps locate the likely failure domain.

### 25.4.3 Gather Evidence Before Changing Anything

Evidence may include:

- User report and screenshot
- Time the failure began
- Interface status and counters
- Client IP configuration
- VLAN and trunk state
- MAC and ARP tables
- Routing table
- DHCP lease and DNS results
- Logs and monitoring alerts
- Recent change records
- Physical labels and cable tests
- Packet capture

Capture the current state before commands such as clearing counters, rebooting, renewing addresses, or replacing equipment erase evidence.

## 25.5 Troubleshooting Approaches

### 25.5.1 Bottom-Up

Begin at OSI Layer 1 and move upward. This is effective when link lights are absent, cabling was disturbed, or physical failure is likely.

### 25.5.2 Top-Down

Begin with the application and move downward. This is useful when only one service fails but basic connectivity works.

### 25.5.3 Divide-and-Conquer

Begin at a middle layer, commonly Layer 3. If the host can reach its gateway, investigate upward or farther along the path. If it cannot, investigate downward and locally.

### 25.5.4 Follow-the-Path

Trace the actual packet path from source to destination, checking every interface, VLAN, route, policy, and return path. This is especially useful for multi-device enterprise networks.

### 25.5.5 Compare-to-Baseline

Compare current behavior with a known healthy state. An interface at 70 percent utilization may be normal or abnormal depending on its baseline.

| Approach | Best Starting Condition |
|---|---|
| Bottom-up | Link or physical fault suspected |
| Top-down | One application/service fails |
| Divide-and-conquer | Layer is not yet known |
| Follow-the-path | Multi-hop or asymmetric problem |
| Compare-to-baseline | Performance degradation or intermittent issue |

## 25.6 The Troubleshooting Toolkit

### 25.6.1 Windows Commands

```powershell
ipconfig /all
Get-NetIPConfiguration
Get-NetAdapter
ping <destination>
tracert <destination>
pathping <destination>
arp -a
route print
nslookup <name>
Resolve-DnsName <name>
Test-NetConnection <host> -Port <port>
netstat -ano
```

### 25.6.2 Linux Commands

```bash
ip address
ip link
ip route
ip neigh
ping -c 4 <destination>
tracepath <destination>
traceroute <destination>
dig <name>
resolvectl status
ss -tulpen
ethtool <interface>
tcpdump -ni <interface>
```

### 25.6.3 Cisco IOS Commands

```cisco
show interfaces
show interfaces status
show interfaces counters errors
show ip interface brief
show vlan brief
show interfaces trunk
show mac address-table
show spanning-tree
show etherchannel summary
show ip arp
show ip route
show access-lists
show cdp neighbors detail
show lldp neighbors detail
show logging
show processes cpu
show memory statistics
```

Commands must be interpreted in context. `up/up` confirms interface protocol state but does not prove that DHCP, DNS, routing, policy, or the application works.

### 25.6.4 Physical and Analysis Tools

| Tool | Purpose |
|---|---|
| Cable tester | Continuity, wire map, opens, shorts, split pairs |
| Certifier | Standards-based cable performance certification |
| Tone generator/probe | Identify an unlabeled copper cable |
| Optical power meter | Measure received optical power |
| Visual fault locator | Locate some fiber breaks or faults |
| Wi-Fi analyzer | Observe channels, signal, noise, and neighboring WLANs |
| Packet analyzer | Capture and decode frames and packets |
| Loopback plug | Test transmit/receive operation on supported interfaces |
| Console cable | Out-of-band device administration |

## 25.7 Forming and Testing a Hypothesis

A useful hypothesis is specific and testable:

```text
Weak: "The switch is bad."

Strong: "The Finance PC cannot reach its gateway because SW2
GigabitEthernet0/18 is assigned to VLAN 30 instead of VLAN 20."
```

Test the least disruptive theory first. Do not restart a core switch to test whether one access port has the wrong VLAN.

Change one relevant variable at a time. If several changes are made simultaneously, the team may restore service without knowing which action worked or what new risk was introduced.

## 25.8 FULL END-TO-END TROUBLESHOOTING CASE STUDY

### 25.8.1 Environment

FEMTECT Services has a headquarters office with:

```text
VLAN 10 - Staff       192.168.10.0/24
VLAN 20 - Finance     192.168.20.0/24
VLAN 30 - Voice       192.168.30.0/24
VLAN 40 - Guest       192.168.40.0/24
VLAN 50 - Management  192.168.50.0/24
```

A multilayer switch, DSW1, performs inter-VLAN routing. Access switch SW2 connects Finance workstations and IP phones. A firewall provides Internet access. DHCP and DNS run on server `192.168.60.10`.

```text
Internet
   |
Firewall
   |
DSW1 (Layer 3 switch)
   |
802.1Q trunk
   |
SW2
   |
Finance PCs and phones
```

### 25.8.2 Incident Report

At 09:10, Finance reports:

- PC-FIN1 shows no network connection.
- PC-FIN2 receives an address but cannot reach the Finance application.
- IP phones on the same desks work.
- Staff users elsewhere are operational.
- The problem began after desks were moved and a switch change was completed the previous evening.

This is a combined Layer 1, Layer 2, and Layer 3 incident. There is more than one fault.

### 25.8.3 Initial Problem Statement

```text
Finance connectivity through SW2 is partially unavailable after a desk
move and switch change. At least two endpoints show different symptoms.
Voice and other office services remain available. Business impact is
high because Finance cannot process transactions.
```

### 25.8.4 Preserve Evidence

Before making changes:

- Record incident and change-ticket numbers.
- Save current SW2 and DSW1 configurations.
- Capture interface, VLAN, trunk, route, DHCP, and log output.
- Photograph cable labels without exposing sensitive information.
- Record times using synchronized clocks.
- Ask the previous engineer exactly what was changed.

### 25.8.5 Layer 1 Investigation: PC-FIN1

PC-FIN1 reports no link.

Windows:

```powershell
Get-NetAdapter
```

Expected observation:

```text
Ethernet: Media disconnected
```

SW2:

```cisco
show interfaces status
show interfaces GigabitEthernet0/18
```

Observation:

```text
Gi0/18  notconnect  20  auto  auto
```

The technician checks:

1. NIC enabled and cable seated.
2. Patch lead at the desk.
3. Patch-panel mapping.
4. Switch port and link light.
5. Cable with a tester.

The tester reports an open conductor in the desk patch lead. A certified replacement cable restores link.

Verification:

```text
Get-NetAdapter now reports Up.
SW2 Gi0/18 reports connected.
```

This repairs PC-FIN1's Layer 1 fault, but the overall incident is not closed because PC-FIN2 still fails.

### 25.8.6 Layer 2 Investigation: PC-FIN2

PC-FIN2 has:

```text
IPv4 address: 192.168.40.87
Mask:         255.255.255.0
Gateway:      192.168.40.1
```

The PC is physically in Finance but received a Guest VLAN address.

Commands:

```cisco
show vlan brief
show interfaces GigabitEthernet0/19 switchport
show mac address-table interface GigabitEthernet0/19
```

Observation:

```text
Gi0/19 access VLAN: 40
Expected access VLAN: 20
```

The previous change assigned the port to the wrong VLAN.

Approved correction:

```cisco
interface GigabitEthernet0/19
 description FINANCE-PC-FIN2
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
```

After changing VLAN membership, the client renews DHCP:

```powershell
ipconfig /release
ipconfig /renew
ipconfig /all
```

PC-FIN2 now receives:

```text
IPv4 address: 192.168.20.87
Gateway:      192.168.20.1
DNS:          192.168.60.10
```

The client can reach its gateway but still cannot reach the application server. The Layer 2 fault is fixed, but a Layer 3 problem remains.

### 25.8.7 Validate the Trunk

Before moving to routing, verify VLAN 20 crosses the SW2-DSW1 trunk:

```cisco
show interfaces trunk
show spanning-tree vlan 20
show mac address-table vlan 20
```

Confirm:

- Correct trunk mode
- VLAN 20 exists on both switches
- VLAN 20 is allowed and forwarding
- Native VLAN matches
- MAC addresses are learned on expected ports

In this case, VLAN 20 is allowed and STP is forwarding. The trunk is not the remaining fault.

### 25.8.8 Layer 3 Investigation

PC-FIN2 tests:

```powershell
ping 192.168.20.1
ping 192.168.60.10
tracert 192.168.60.10
Test-NetConnection 192.168.60.10 -Port 443
```

Results:

```text
Gateway ping succeeds.
Server ping and TCP 443 fail.
Trace stops at 192.168.20.1.
```

This proves local VLAN communication reaches DSW1. Investigate routing and policy on DSW1.

```cisco
show ip interface brief
show ip route
show access-lists
show ip interface Vlan20
```

Observation:

```text
Vlan20 is up/up with 192.168.20.1/24.
Route to 192.168.60.0/24 points to 10.255.0.6.
The correct next hop is 10.255.0.2.
```

A static route was entered incorrectly during the previous change:

```cisco
ip route 192.168.60.0 255.255.255.0 10.255.0.6
```

The team checks the approved implementation and rollback plan before correcting:

```cisco
no ip route 192.168.60.0 255.255.255.0 10.255.0.6
ip route 192.168.60.0 255.255.255.0 10.255.0.2
```

### 25.8.9 End-to-End Verification

Do not stop after one successful ping.

Verify:

- PC-FIN1 and PC-FIN2 have correct link, VLAN, IP, gateway, and DNS.
- Both reach their gateway.
- Finance application TCP 443 works.
- DNS resolves the application hostname.
- Internet access follows policy.
- Guest VLAN remains isolated.
- IP phones still register.
- Monitoring reports healthy interfaces and routes.
- Logs contain no new errors.
- Configuration is saved and backed up.

Example:

```powershell
Resolve-DnsName finance-app.femtect.local
Test-NetConnection finance-app.femtect.local -Port 443
tracert 192.168.60.10
```

### 25.8.10 Root Causes

The incident had three independent causes:

| Layer | Root Cause | Symptom |
|---|---|---|
| Layer 1 | Open conductor in patch cable | PC-FIN1 had no link |
| Layer 2 | Access port assigned to Guest VLAN | PC-FIN2 received wrong DHCP scope |
| Layer 3 | Static route used wrong next hop | Finance could not reach server subnet |

The presence of multiple faults explains why one correction did not restore the entire service.

### 25.8.11 Contributing Process Failures

- Desk-move cables were not tested.
- Port description and floor plan were outdated.
- Switch change lacked peer review.
- Validation tested only link and not application reachability.
- The static route was manually entered without a comparison check.

### 25.8.12 Preventive Actions

- Test and label moved cabling.
- Use standard access-port templates.
- Require peer review for route and VLAN changes.
- Automate configuration backup and difference reporting.
- Add post-change tests for DHCP, gateway, DNS, application, and isolation.
- Update the physical and logical diagrams.
- Monitor critical routes and application reachability.

## 25.9 Packet Capture as Evidence

A packet capture shows what was transmitted and received at the capture point. It can reveal:

- Repeated ARP requests without replies
- DHCP DORA failure
- DNS errors or delays
- TCP SYN retransmissions
- TCP resets
- ICMP unreachable messages
- Duplicate acknowledgments and retransmissions
- TLS negotiation failures at a high level

Capture only with authorization. Packets may contain personal data, authentication material, internal addresses, and sensitive application content. Limit scope, protect files, and follow retention policy.

A capture point matters. A packet absent on one interface may still exist elsewhere. Interpret the packet path, SPAN configuration, VLAN tags, offloading behavior, and encryption boundaries.

## 25.10 Escalation and Communication

Escalate when:

- Safety is at risk.
- Required access or authority is unavailable.
- The issue is outside support scope.
- A change could affect many users.
- A vendor or service provider owns the failing component.
- The recovery exceeds the agreed time target.
- Evidence suggests a security incident.

A useful escalation contains:

```text
Business impact
Affected users/services
Start time and current status
What works and what fails
Evidence collected
Tests completed and results
Changes already made
Current hypothesis
Specific assistance required
Relevant ticket, device, circuit, and contact information
```

Avoid sending "Internet down, please check." Give the receiving team enough evidence to act.

## 25.11 Network Documentation Standards

Network documentation is controlled operational information, not decorative paperwork.

Good documentation is:

- Accurate
- Current
- Consistent
- Version-controlled
- Dated and owned
- Accessible to authorized staff
- Protected according to sensitivity
- Detailed enough to operate and recover the network

### 25.11.1 Documentation Set

| Document | Purpose |
|---|---|
| Physical diagram | Devices, racks, ports, media, and physical links |
| Logical diagram | VLANs, subnets, routing, security zones, services |
| Rack elevation | Device location and rack-unit position |
| IP address plan/IPAM | Addresses, prefixes, gateways, reservations, owners |
| VLAN register | VLAN ID, name, subnet, gateway, purpose |
| Circuit register | Provider, circuit ID, bandwidth, demarcation, support |
| Device inventory | Model, serial, role, location, support status |
| Configuration backup | Recoverable device configuration |
| Dependency map | Relationships between services and infrastructure |
| Runbook | Repeatable operational procedure |
| Change record | Planned and completed change evidence |
| Incident record | Timeline, impact, diagnosis, resolution, lessons |

### 25.11.2 Naming Standards

Names should convey useful information without becoming unmanageably long.

Example:

```text
LAG-HQ-DSW01
LAG-HQ-ASW02
ABJ-BR-FW01
LAG-HQ-AP-F2-03
```

A standard may encode site, building/floor, role, and sequence. Use the organization's approved convention consistently.

### 25.11.3 Interface Descriptions

An interface description should identify the connected device or service:

```cisco
interface GigabitEthernet1/0/24
 description UPLINK_TO_LAG-HQ-DSW01_Gi1/0/12
```

For a provider link:

```text
ISP: Provider name
Circuit ID: NG-LAG-004812
Bandwidth: 100 Mbps
Demarcation: Rack A, RU 38
Support contact: service desk record reference
```

Do not place passwords or secret keys in interface descriptions.

## 25.12 Physical and Logical Diagrams

A physical diagram answers:

```text
What equipment exists?
Where is it?
Which physical port and cable connect it?
Which media and speed are used?
```

A logical diagram answers:

```text
Which VLANs and subnets exist?
Where are Layer 3 boundaries?
How is traffic routed?
Where are firewalls, VPNs, NAT, and services?
```

Example logical diagram:

```text
                    Internet
                       |
                  [Firewall]
                       |
             10.255.0.0/30 transit
                       |
                    [DSW1]
          _____________|_____________
         |             |             |
    VLAN 10        VLAN 20       VLAN 40
    Staff          Finance       Guest
192.168.10/24  192.168.20/24  192.168.40/24
         |
      [SW2]
```

### 25.12.1 Diagram Quality Rules

- Include title, scope, owner, revision, and date.
- Use consistent symbols and line styles.
- Label device names and important interfaces.
- Show prefixes, VLAN IDs, and security boundaries where relevant.
- Distinguish primary and backup paths.
- Avoid crossing lines where possible.
- Include a legend for non-obvious symbols.
- Keep secrets out of diagrams.
- Create separate views when one diagram becomes unreadable.

Diagrams should be understandable when printed or viewed without the author's explanation.

## 25.13 IP Address Management

IP Address Management, or IPAM, tracks addressing and subnet assignments.

Recommended fields include:

| Field | Example |
|---|---|
| Prefix | 192.168.20.0/24 |
| Purpose | Finance user VLAN |
| VLAN | 20 |
| Gateway | 192.168.20.1 |
| DHCP range | 192.168.20.50-199 |
| Exclusions | 192.168.20.1-49 |
| DNS domain | femtect.local |
| Site | Lagos HQ |
| Owner | Network Operations |
| Status | Active |

An unmanaged spreadsheet may work for a very small environment, but a shared IPAM system improves validation, history, automation, and duplicate-address prevention.

## 25.14 Configuration Documentation and Source of Truth

A source of truth is the authoritative record of intended state. It may be an IPAM/DCIM platform, configuration repository, automation inventory, or controlled document system.

Running device configuration is evidence of actual state, but it is not always the intended state. Differences between intended and actual state are configuration drift.

Configuration-management practices include:

- Automated scheduled backups
- Encryption and access control
- Version history
- Difference comparison
- Standard templates
- Peer review
- Validation and compliance checks
- Tested restoration

Never store plaintext passwords, private keys, or community strings in an unprotected public repository.

## 25.15 Baselines

A baseline is a recorded picture of normal performance and behavior under defined conditions. It gives meaning to future measurements.

Baseline dimensions include:

- Time of day and day of week
- Normal and peak utilization
- User or transaction volume
- Application response time
- Interface errors and drops
- CPU and memory
- Wireless channel use and client count
- WAN latency, jitter, and packet loss
- Power load and temperature

One measurement is not a baseline. Collect data across representative business cycles and record major changes.

## 25.16 Performance Metrics

### 25.16.1 Bandwidth, Throughput, and Goodput

- **Bandwidth:** Theoretical or configured link capacity.
- **Throughput:** Actual rate of data transferred.
- **Goodput:** Useful application data delivered, excluding overhead and retransmissions.

A 1 Gbps interface does not guarantee 1 Gbps application goodput.

### 25.16.2 Latency

Latency is the time required for data to travel from source to destination. Round-trip time measures travel to the destination and back.

Latency is affected by distance, propagation, serialization, processing, queueing, congestion, and path selection.

### 25.16.3 Jitter

Jitter is variation in packet delay. Voice and video are especially sensitive because packets must arrive at a steady rate.

### 25.16.4 Packet Loss

Packet loss is the percentage of packets that do not arrive. Congestion, physical errors, wireless interference, overloaded devices, faulty links, and policy can cause loss.

```text
Packet loss % = Lost packets / Sent packets x 100
```

### 25.16.5 Utilization

```text
Utilization % = Used bandwidth / Available bandwidth x 100
```

High average utilization may indicate insufficient capacity. Short peaks may be normal. Baselines and application impact determine significance.

### 25.16.6 Interface Errors and Discards

Useful counters include:

- CRC/FCS errors
- Input errors
- Output errors
- Runts and giants
- Collisions or late collisions on relevant legacy/duplex cases
- Input/output discards
- Queue drops

Counters are cumulative. Record time and calculate the rate of increase. A historical counter that no longer rises may not represent a current fault.

## 25.17 Monitoring Architecture

Monitoring answers:

```text
Is the service available?
Is performance normal?
What changed?
Where is the failure?
Who must respond?
```

Monitoring methods include:

| Method | Use |
|---|---|
| ICMP probe | Basic reachability and latency |
| SNMPv3 polling | Interface, CPU, memory, environment, counters |
| Syslog | Event and fault messages |
| Flow telemetry | Traffic conversations and volume |
| Packet capture | Detailed packet-level evidence |
| API/streaming telemetry | Structured high-frequency metrics |
| Synthetic transaction | Tests application from a user's perspective |
| Agent monitoring | Host/application health |

Monitoring only device reachability is insufficient. A server may answer ping while its application is unavailable.

## 25.18 Thresholds, Alerts, and Alert Fatigue

A threshold defines when a metric requires attention. Static thresholds are simple but may not fit every device or time. Dynamic thresholds compare current behavior with historical patterns.

An actionable alert should contain:

- Affected object and service
- Condition and measured value
- Start time and duration
- Severity and business impact
- Relevant dependency
- Link to dashboard or runbook
- Escalation owner

Too many low-value alerts create alert fatigue. Staff begin ignoring notifications, including important ones. Tune duplicate, flapping, and non-actionable alerts.

## 25.19 Logs and Time Correlation

Lesson 22 introduced NTP and Syslog. In a complete monitoring system:

1. Devices synchronize time.
2. Logs are sent centrally.
3. Metrics and changes use consistent timestamps.
4. Events are correlated across network, server, identity, security, and power systems.

Log retention must match legal, security, operational, and storage requirements. Protect logs from unauthorized alteration and restrict access to sensitive records.

## 25.20 Capacity Planning

Capacity planning predicts when resources will become insufficient.

Consider:

- User and device growth
- New applications
- WAN and Internet demand
- PoE power
- Wireless client density
- CPU, memory, and session limits
- Address-pool consumption
- VPN throughput
- Storage and log growth
- UPS and cooling load

Capacity should be added before sustained demand causes failure. Procurement lead time, budget cycles, licensing, installation, and change windows must be included.

## 25.21 Change Management

A change is an authorized modification to infrastructure, configuration, software, policy, or documentation.

Change management reduces risk by ensuring the work is understood, reviewed, scheduled, tested, reversible, and recorded.

### 25.21.1 Change Types

| Type | Description |
|---|---|
| Standard | Low-risk, repeatable, pre-approved procedure |
| Normal | Assessed, reviewed, and approved before implementation |
| Emergency | Urgent change needed to restore service or reduce immediate risk |

Emergency does not mean undocumented. The review may be expedited, but actions and approvals must still be recorded and reviewed afterward.

### 25.21.2 Change Request Contents

A professional change request contains:

- Title and change owner
- Business reason
- Scope and affected systems
- Risk and impact assessment
- Dependencies
- Implementation steps
- Pre-change validation
- Test plan and success criteria
- Backout/rollback plan
- Maintenance window
- Required approvals
- Communication plan
- Post-change validation
- Documentation updates

### 25.21.3 Maintenance Window

A maintenance window is an approved period for planned work. It does not remove the need for careful design. Some changes can continue affecting users after the window, so the plan must reserve time for testing and rollback.

## 25.22 Implementation and Rollback

The implementation plan should be precise enough that another qualified engineer can follow it.

Weak:

```text
Configure the VLAN and test.
```

Professional:

```text
1. Confirm current config backup completed.
2. Verify VLAN 20 exists on DSW1 and SW2.
3. Confirm Gi0/19 endpoint and approved port mapping.
4. Configure Gi0/19 as static access VLAN 20.
5. Verify switchport mode, VLAN, STP, and MAC learning.
6. Renew client DHCP.
7. Test gateway, DNS, Finance HTTPS, and Guest isolation.
8. Save configuration and archive post-change state.
```

A rollback plan restores the previous known state. "Reboot if it fails" is not a rollback plan.

Rollback must specify:

- Trigger or decision point
- Exact restoration commands or backup
- Responsible person
- Time required
- Validation after rollback
- Communication and escalation

## 25.23 Configuration Management

Configuration management maintains device state throughout its lifecycle.

Core practices:

- Standard approved templates
- Unique device identity
- Version-controlled intended configuration
- Automated backups
- Secure secret handling
- Configuration-drift detection
- Software and firmware inventory
- License and support tracking
- End-of-life planning
- Tested restore procedure

### 25.23.1 Golden Configuration

A golden configuration is an approved secure baseline for a device role. It may define AAA, SSH, NTP, Syslog, SNMPv3, management ACLs, banners, interface defaults, and required security controls.

It must be maintained as technology and policy change. A stale golden configuration can reproduce old vulnerabilities at scale.

### 25.23.2 Backup Before and After Change

Preserve:

```text
Pre-change configuration
Approved intended change
Command/output evidence
Post-change configuration
Difference report
Validation results
```

Never assume that `copy running-config startup-config` replaces an external backup.

## 25.24 Root Cause Analysis

Root Cause Analysis, or RCA, asks why the incident occurred and how recurrence can be reduced.

The immediate technical cause is not always the complete root cause.

```text
Symptom: Finance application unavailable.
Technical causes: wrong VLAN, route, and failed cable.
Process causes: outdated diagram, inadequate review, incomplete testing.
Organizational cause: change process did not require application validation.
```

### 25.24.1 Five Whys

The Five Whys technique repeatedly asks why, but it must be evidence-based.

```text
Why could Finance not reach the server?
Because the route used the wrong next hop.

Why was the wrong route installed?
Because the next hop was entered manually from an outdated note.

Why was the outdated note used?
Because the source-of-truth record was not updated.

Why was it not updated?
Because documentation was not included in change closure.

Why was change closure incomplete?
Because the process lacked a required documentation check.
```

Do not use RCA to blame an individual. Improve systems, controls, training, and verification.

## 25.25 Incident Report Structure

A professional incident report contains:

1. Executive summary
2. Business impact
3. Detection method
4. Timeline
5. Technical evidence
6. Root and contributing causes
7. Resolution
8. Validation
9. Preventive actions
10. Owners and due dates

Separate facts from assumptions. Record times consistently. Do not expose secrets or unnecessary personal information.

### 25.25.1 Example Timeline

| Time | Event |
|---|---|
| 09:10 | Finance reports connectivity failure |
| 09:15 | Incident acknowledged and scope confirmed |
| 09:23 | Failed PC-FIN1 patch cable identified |
| 09:31 | Cable replaced and link restored |
| 09:39 | Wrong access VLAN found on Gi0/19 |
| 09:46 | VLAN corrected; gateway reachable |
| 09:55 | Incorrect server-subnet route identified |
| 10:05 | Approved route correction completed |
| 10:15 | Application, DNS, voice, and isolation validated |
| 10:30 | Incident monitoring period completed |

## 25.26 Handover Documentation

A handover transfers responsibility without losing context.

A shift or project handover should state:

- Current service status
- Work completed
- Outstanding issues
- Risks and temporary workarounds
- Monitoring or alerts to watch
- Pending changes and approvals
- Vendor cases
- Next actions, owners, and deadlines
- Location of evidence and documentation

### 25.26.1 Example Handover

```text
Subject: Finance Network Incident Handover - INC-2026-0142

Status:
Service restored at 10:15 WAT. Monitoring remains normal.

Impact:
Two Finance workstations could not access transaction services.

Resolved:
- Replaced failed patch cable for PC-FIN1.
- Corrected SW2 Gi0/19 from VLAN 40 to VLAN 20.
- Corrected DSW1 route to 192.168.60.0/24 via 10.255.0.2.

Validated:
DHCP, gateway, DNS, HTTPS application, voice registration,
Internet policy, and Guest isolation.

Outstanding:
Update floor-port map and complete peer review of previous change.

Next owner:
Network Operations, due 17:00 WAT.

Evidence:
Incident folder INC-2026-0142 in the controlled operations repository.
```

## 25.27 Building a Portfolio Case Study

A portfolio piece demonstrates thinking, not only a screenshot of commands.

Recommended structure:

1. **Problem:** Describe the business and technical challenge.
2. **Constraints:** State available devices, simulation limits, time, and policy.
3. **Design:** Provide physical/logical diagrams and addressing.
4. **Implementation:** Show key configurations with secrets removed.
5. **Testing:** Show expected and actual results.
6. **Troubleshooting:** Explain one deliberate or real fault and evidence.
7. **Security:** Explain segmentation and management controls.
8. **Resilience:** Explain backup, monitoring, and recovery.
9. **Outcome:** State what worked and what was learned.
10. **Artifacts:** Include sanitized files, diagrams, and runbook.

### 25.27.1 Portfolio Project: Secure Resilient Branch Network

Build in Cisco Packet Tracer or a suitable lab:

- Staff, Finance, Voice, Guest, and Management VLANs
- Trunks and STP protections
- Inter-VLAN routing
- DHCP and DNS
- Static/default or dynamic routing
- NAT/PAT
- ACL segmentation
- SSH management
- NTP, Syslog, and SNMP concepts
- Wireless staff and guest design
- Site-to-site VPN design
- Redundant path or documented resilience plan

Introduce three faults, diagnose them, and include the incident report.

### 25.27.2 Protect Confidential Information

Never publish:

- Real public IP addresses without authorization
- Passwords, secrets, hashes, tokens, or private keys
- Customer names or personal information
- Internal hostnames or diagrams from an employer
- Proprietary configuration
- Vulnerability details that create risk

Use lab data, documentation ranges, fictional names, and sanitized screenshots.

## 25.28 Evidence That Employers Value

Useful evidence includes:

- Clear topology diagram
- Address and VLAN plan
- Configuration excerpts
- Verification matrix
- Before/after evidence
- Troubleshooting decision log
- Change request and rollback
- Incident report and RCA
- Handover note
- README explaining how to reproduce the lab

Quality matters more than the number of screenshots.

## 25.29 Guided Career Branch Point

The course foundation supports several paths. The branches overlap; professionals often move between them.

### 25.29.1 Network Engineering

Network engineers design, implement, automate, secure, and troubleshoot connectivity.

Core interests:

- Routing and switching
- Wireless design
- WAN, VPN, and Internet connectivity
- High availability
- Automation and monitoring
- Performance analysis

Next steps:

- Deepen CCNA-level skills
- Build multi-site labs
- Learn Python, APIs, Git, and automation
- Study enterprise wireless and firewalls
- Practice packet analysis and design documentation

### 25.29.2 Cybersecurity

Cybersecurity professionals protect identities, systems, networks, and data.

Core interests:

- Security monitoring
- Vulnerability management
- Incident response
- Network defense
- Identity and access
- Governance and risk

Next steps:

- Strengthen Linux, Windows, and networking
- Study logs, SIEM, endpoint protection, and threat analysis
- Build defensive labs ethically
- Learn secure configuration and incident handling
- Practice explaining risk and evidence

Networking remains foundational because attacks and controls operate across protocols, identities, devices, and traffic paths.

### 25.29.3 IT Support

IT support professionals restore user productivity and operate endpoints, accounts, applications, and local networks.

Core interests:

- User communication
- Windows and productivity systems
- Hardware and peripherals
- Identity and permissions
- Basic networking
- Ticketing and escalation

Next steps:

- Practice structured troubleshooting
- Learn Microsoft administration and endpoint management
- Build home-office and small-business labs
- Improve ticket notes and customer communication
- Study backup, security, and remote support

IT support is not a lesser path. It develops broad operational judgment and can lead into networking, security, cloud, systems, or management.

### 25.29.4 Cloud

Cloud professionals design and operate services in provider environments.

Core interests:

- Virtual networks, subnets, and routing
- Security groups and identity
- Load balancing and DNS
- Hybrid connectivity and VPN
- Infrastructure as code
- Monitoring, cost, and resilience

Next steps:

- Choose one cloud platform for structured study
- Build virtual-network and hybrid labs
- Learn Linux, scripting, Git, and infrastructure as code
- Study IAM and shared responsibility
- Practice high-availability and cost-aware design

Cloud networking still uses the principles from this course. The interfaces are virtual, but packets still require addressing, routes, policy, DNS, and reachable return paths.

## 25.30 Choosing a Direction

Use evidence rather than pressure or trend alone.

Rate each area from 1 to 5:

| Question | Network | Security | IT Support | Cloud |
|---|---:|---:|---:|---:|
| I enjoy this work |  |  |  |  |
| I persist when it becomes difficult |  |  |  |  |
| I have access to learning resources |  |  |  |  |
| Local/remote job demand is visible |  |  |  |  |
| My current skills transfer well |  |  |  |  |
| I can build portfolio evidence |  |  |  |  |

The score is a discussion tool, not destiny. Choose one primary direction for the next three to six months and maintain foundational networking practice.

### 25.30.1 A 90-Day Development Plan

**Days 1-30: Foundation and repetition**

- Review weak course topics.
- Rebuild one complete network without notes.
- Practice subnetting and command interpretation.
- Improve CV and professional profile.

**Days 31-60: Specialization**

- Follow one structured certification or role path.
- Build one deeper role-specific lab.
- Read job descriptions and identify recurring requirements.
- Conduct weekly troubleshooting drills.

**Days 61-90: Evidence and applications**

- Publish a sanitized capstone.
- Practice interview explanations aloud.
- Apply for appropriate internships, support roles, junior roles, or volunteer projects.
- Track applications and skill gaps.
- Request specific feedback and revise.

## 25.31 Interview Communication

Use the STAR structure where appropriate:

- **Situation:** Context and impact
- **Task:** Your responsibility
- **Action:** Evidence, reasoning, and steps
- **Result:** Verified outcome and lesson

Example:

```text
Situation:
Finance users lost application access after a switch change.

Task:
Restore service while protecting other VLANs and preserving evidence.

Action:
I scoped affected hosts, checked Layer 1 first, corrected a failed cable,
identified a wrong access VLAN, traced the route, corrected the approved
next hop, and tested DHCP, DNS, HTTPS, voice, and Guest isolation.

Result:
Service was restored and monitored. I documented three root causes,
updated diagrams, and added peer review and post-change validation.
```

Do not claim production experience you do not have. A well-explained lab demonstrates honest skill.

## 25.32 Practical Capstone Labs

### Lab 1: Layer 1-3 Fault Challenge

Build the case-study topology. Have an instructor or partner introduce:

- One physical or interface fault
- One access/trunk/VLAN fault
- One addressing, gateway, route, or ACL fault

The student must:

1. Open an incident record.
2. Establish scope and impact.
3. Capture pre-change evidence.
4. State and test hypotheses.
5. Request approval for changes.
6. Correct each fault.
7. verify application and security behavior.
8. Write the incident report and handover.

### Lab 2: Documentation Pack

Produce:

- Physical diagram
- Logical diagram
- VLAN and IP register
- Device and circuit inventory
- Interface description standard
- Configuration backup record
- Service dependency map

Exchange the pack with another student. The reviewer should be able to explain and troubleshoot the network without verbal help.

### Lab 3: Baseline and Monitoring Plan

For the lab network, define:

- Critical devices and services
- Reachability checks
- SNMP metrics
- Syslog events
- Latency, loss, utilization, CPU, memory, and error baselines
- Thresholds and severity
- Alert owner and runbook
- Retention and reporting

Collect sample measurements and explain what would constitute abnormal behavior.

### Lab 4: Change and Rollback

Prepare a normal change to add a new department VLAN.

Include:

- Business reason
- Addressing and VLAN design
- Risk assessment
- Exact commands
- DHCP, trunk, routing, ACL, and monitoring updates
- Test matrix
- Rollback
- Communication
- Documentation updates

Have a peer review the plan before implementation.

### Lab 5: Portfolio and Career Review

Create the sanitized capstone case study and a 90-day development plan. Present the design and incident in ten minutes, then answer:

- Why did you troubleshoot in that order?
- What evidence disproved an early theory?
- How did you protect security during the fix?
- What would you automate?
- Which career branch fits your next step and why?

## 25.33 Verification Matrix

A verification matrix proves that requirements work after a change.

| Test | Source | Destination | Expected | Result |
|---|---|---|---|---|
| DHCP | Finance PC | DHCP service | Receives VLAN 20 scope | Pass/Fail |
| Gateway | Finance PC | 192.168.20.1 | Reachable | Pass/Fail |
| DNS | Finance PC | Internal DNS | Resolves finance app | Pass/Fail |
| HTTPS | Finance PC | Finance server TCP 443 | Permitted | Pass/Fail |
| Guest isolation | Guest client | Finance server | Denied | Pass/Fail |
| Voice | IP phone | Call service | Registered | Pass/Fail |
| Management | Staff PC | Switch SSH | Denied | Pass/Fail |
| Monitoring | NMS | SW2 | Metrics/logs received | Pass/Fail |

Both positive and negative tests matter. A firewall rule is not fully tested until required traffic passes and prohibited traffic remains blocked.

## 25.34 Common Professional Mistakes

| Mistake | Better Practice |
|---|---|
| Reboot first | Preserve evidence and scope the problem |
| Change many settings | Test one evidence-based theory |
| Stop after ping works | Test DNS, application, return path, and security |
| Work without ticket | Record ownership, impact, and actions |
| Skip backup | Capture recoverable pre-change state |
| No rollback | Define trigger and restoration steps |
| Blame user or colleague | Focus on facts and system improvement |
| Publish real configuration | Sanitize all sensitive data |
| Monitor devices only | Monitor end-to-end services |
| Let documentation age | Make updates part of change closure |

## 25.35 Cybersecurity Relevance

Troubleshooting access can expose sensitive systems. Use least privilege, approved accounts, secure protocols, and auditable changes.

Unexpected symptoms may indicate an attack rather than a fault:

- New unauthorized route
- MAC or ARP instability
- Unknown DHCP server
- Repeated authentication failures
- Configuration changed outside a window
- Unusual outbound traffic
- Disabled logging

If evidence suggests compromise, preserve logs, follow incident-response procedures, and avoid destroying evidence through unnecessary resets.

Documentation itself is sensitive. Network diagrams, backups, inventories, and runbooks reveal valuable information to attackers. Classify, encrypt, back up, and restrict them.

## 25.36 Cloud Relevance

Cloud troubleshooting follows the same logic:

```text
Application
Security group / network ACL
Route table
Subnet and address
Load balancer
DNS
VPN or direct connection
Identity and platform service
```

Cloud environments add APIs, IAM, regions, availability zones, managed services, quotas, and provider control planes. Infrastructure as code improves repeatability and review, but a flawed template can reproduce a fault at scale.

Monitor application transactions, not only virtual-machine state. Maintain diagrams, tags, source-controlled configuration, change review, and recovery tests.

## 25.37 Final CCNA 200-301 and Network+ N10-009 Reminders

- Troubleshoot systematically and document every significant action.
- Verify physical link, VLAN, IP configuration, gateway, routing, policy, DNS, and application in a logical order.
- A successful ping does not prove full service.
- Establish a baseline before declaring a measurement abnormal.
- Interface errors must be interpreted as rates and trends.
- Use NTP, Syslog, SNMP, flow data, captures, and synthetic tests appropriately.
- Change plans require risk, testing, rollback, approval, and documentation.
- Positive and negative verification tests are both necessary.
- RTO, RPO, backups, power, and redundancy influence recovery.
- Escalate with evidence and business impact.
- Protect credentials, packet captures, diagrams, and configurations.
- Networking skills remain foundational across IT support, cybersecurity, cloud, and network engineering.

## 26. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Troubleshooting | Structured process of identifying and resolving faults |
| Problem Statement | Precise description of symptom, scope, time, and impact |
| Scope | Boundary of users, systems, locations, and services affected |
| Hypothesis | Testable explanation for observed evidence |
| Bottom-Up | Troubleshooting approach beginning at the physical layer |
| Top-Down | Approach beginning at the application layer |
| Divide-and-Conquer | Approach starting at a middle layer and moving based on results |
| Follow-the-Path | Inspection of every stage in a packet's route |
| Baseline | Recorded normal behavior under defined conditions |
| Root Cause | Underlying reason an incident occurred |
| Contributing Cause | Condition that increased likelihood or impact |
| RCA | Root Cause Analysis |
| Five Whys | Repeated evidence-based questioning to uncover process causes |
| Escalation | Transfer or request for higher/specialized assistance |
| Physical Diagram | Representation of devices, ports, media, and physical links |
| Logical Diagram | Representation of addressing, VLANs, routes, and security boundaries |
| Rack Elevation | Diagram showing rack-unit placement |
| IPAM | IP Address Management |
| Source of Truth | Authoritative record of intended state |
| Configuration Drift | Difference between intended and actual configuration |
| Bandwidth | Theoretical or configured link capacity |
| Throughput | Actual data-transfer rate |
| Goodput | Useful application data delivered per unit time |
| Latency | Time required for data to travel |
| Jitter | Variation in packet delay |
| Packet Loss | Percentage of packets not delivered |
| Utilization | Percentage of available capacity in use |
| Synthetic Transaction | Automated test that imitates user activity |
| Alert Fatigue | Reduced responsiveness caused by excessive low-value alerts |
| Capacity Planning | Forecasting and preparing for future resource demand |
| Change Management | Controlled process for modifying systems |
| Standard Change | Repeatable low-risk pre-approved change |
| Normal Change | Change assessed and approved before implementation |
| Emergency Change | Urgent, expedited change with retained accountability |
| Maintenance Window | Approved period for planned technical work |
| Rollback | Restoration of the prior known state |
| Golden Configuration | Approved secure baseline for a device role |
| Incident Report | Formal record of impact, timeline, cause, and resolution |
| Handover | Transfer of current operational responsibility and context |
| Verification Matrix | Table of required tests, expected results, and outcomes |
| Portfolio | Curated evidence of skills, reasoning, and completed work |
| STAR | Situation, Task, Action, Result interview framework |

## 27. COMPARISON TABLES

### 27.1 Troubleshooting Approaches

| Approach | Starting Point | Best Use |
|---|---|---|
| Bottom-up | Physical layer | Link/media fault |
| Top-down | Application | One service failure |
| Divide-and-conquer | Middle layer | Unknown fault domain |
| Follow-the-path | Source-to-destination path | Multi-hop failure |
| Baseline comparison | Historical normal | Performance issue |

### 27.2 Physical vs Logical Diagram

| Feature | Physical | Logical |
|---|---|---|
| Shows | Ports, cables, racks, media | VLANs, subnets, routes, zones |
| Main question | How is it physically connected? | How does traffic logically flow? |
| Audience | Install/support/operations | Engineering/security/operations |

### 27.3 Bandwidth vs Throughput vs Goodput

| Metric | Meaning |
|---|---|
| Bandwidth | Maximum/configured capacity |
| Throughput | Actual transferred data rate |
| Goodput | Useful application payload rate |

### 27.4 Standard vs Normal vs Emergency Change

| Type | Approval | Risk/Urgency |
|---|---|---|
| Standard | Pre-approved procedure | Low and repeatable |
| Normal | Reviewed before work | Assessed planned change |
| Emergency | Expedited | Urgent service or risk need |

### 27.5 Incident vs Problem vs Change

| Record | Purpose |
|---|---|
| Incident | Restore service and record impact/timeline |
| Problem/RCA | Identify underlying causes and prevention |
| Change | Control modification to systems |

### 27.6 Monitoring Methods

| Method | Strength | Limitation |
|---|---|---|
| ICMP | Simple reachability/latency | Does not prove application |
| SNMPv3 | Broad device metrics | Poll interval may miss short events |
| Syslog | Event detail | Depends on message quality/retention |
| Flow | Conversation visibility | Not complete packet content |
| Packet capture | Deep evidence | Storage, privacy, capture-point limits |
| Synthetic test | User-view service check | Tests only scripted path |

### 27.7 Career Branches

| Path | Primary Focus | Strong Next Skill |
|---|---|---|
| Network Engineering | Connectivity and infrastructure | Routing, automation, design |
| Cybersecurity | Risk, defense, detection, response | Logs, systems, network defense |
| IT Support | User and endpoint operations | Windows, identity, communication |
| Cloud | Virtual infrastructure and services | IAM, automation, cloud networking |

## 28. REAL-WORLD ANALOGY

A professional troubleshooter is like an investigator and an engineer working together. The investigator preserves the scene, collects evidence, forms a testable explanation, and separates fact from assumption. The engineer understands how the system should operate, repairs it safely, verifies every requirement, and strengthens the design.

Documentation is the case file and operating manual. Change management is the controlled authorization to alter the system. Monitoring is the ongoing observation that reveals whether the repair remains healthy.

## 29. QUICK-RECAP CHEAT SHEET

```text
DIAGNOSE
1. Define symptom, scope, time, and impact
2. Gather evidence before changing state
3. Form a specific, testable hypothesis
4. Test the least disruptive theory
5. Plan, approve, implement, and rollback if required
6. Verify complete service and security
7. Document and prevent recurrence

LAYER PATH
Physical -> Link/VLAN -> IP/Gateway -> Route/ACL/NAT
-> DNS/Transport -> Application

DOCUMENT
Physical + logical diagrams
VLAN/IPAM + device/circuit inventory
Config backups + source of truth
Incident + RCA + change + runbook + handover

BASELINE
Bandwidth, throughput, goodput
Latency, jitter, loss
Utilization, errors, discards
CPU, memory, wireless, power, application response

CHANGE
Reason, scope, risk, commands, approvals
Test plan, success criteria, rollback, communication
Pre/post backup and documentation update

VERIFY
Test allowed behavior AND denied behavior
Ping alone is not full validation

PORTFOLIO
Problem, constraints, design, implementation
Testing, troubleshooting, security, resilience, outcome
Sanitize every artifact

CAREER
Choose one primary 90-day direction
Network | Security | IT Support | Cloud
Keep networking fundamentals active
```

## 30. REVIEW QUESTIONS

1. Define diagnose, document, and decide.
2. Why is random configuration change poor troubleshooting?
3. What information belongs in a precise problem statement?
4. Why should evidence be captured before a reboot or counter reset?
5. Compare bottom-up, top-down, divide-and-conquer, and follow-the-path.
6. What makes a hypothesis useful?
7. Why should one relevant variable be changed at a time?
8. In the capstone case, what caused PC-FIN1's failure?
9. Why did PC-FIN2 receive a Guest address?
10. Which evidence proved PC-FIN2 reached Layer 3 locally?
11. What caused the Finance server-subnet failure?
12. Why was one successful ping insufficient verification?
13. Name five post-fix validation tests from the case.
14. What process failures contributed to the incident?
15. What can a packet capture reveal?
16. Why must captures be authorized and protected?
17. What information belongs in an escalation?
18. Name six documents in a professional network documentation set.
19. Compare physical and logical diagrams.
20. What makes a useful interface description?
21. What is IPAM?
22. Define source of truth and configuration drift.
23. What is a performance baseline?
24. Compare bandwidth, throughput, and goodput.
25. Define latency, jitter, packet loss, and utilization.
26. Why should interface counters be measured as a rate of change?
27. Why is ICMP-only monitoring insufficient?
28. What causes alert fatigue?
29. What is capacity planning?
30. Compare standard, normal, and emergency changes.
31. What belongs in a change request?
32. What makes a rollback plan valid?
33. What is a golden configuration?
34. Why is saving startup configuration not an external backup?
35. Compare immediate technical cause with root/process cause.
36. What is the purpose of the Five Whys?
37. What belongs in an incident report?
38. What belongs in a handover?
39. What makes a strong portfolio case study?
40. Which information must not be published in a portfolio?
41. Compare the four career branches.
42. Why should career choice use evidence rather than trends alone?
43. What does STAR mean?
44. Why are positive and negative verification tests necessary?
45. How does cloud troubleshooting retain traditional networking logic?

## 31. SUGGESTED ANSWER GUIDE

1. Diagnose identifies causes through evidence, document records state and actions, and decide selects justified technical or career actions.
2. It can destroy evidence, create new faults, hide the real cause, and produce an unrepeatable result.
3. Exact symptom, affected scope, start time, what works, what fails, recent changes, and business impact.
4. Reboots, renewals, and resets can erase state, logs, leases, counters, and clues.
5. Bottom-up starts physical, top-down starts application, divide-and-conquer starts in the middle, and follow-the-path checks every stage from source to destination.
6. It is specific, consistent with evidence, and can be confirmed or disproved safely.
7. It preserves cause-and-effect understanding and avoids introducing several unknowns.
8. An open conductor in the patch cable.
9. Its access switch port was incorrectly assigned to VLAN 40.
10. It reached its default gateway at `192.168.20.1`.
11. DSW1 had a static route using the wrong next hop.
12. Ping did not prove DNS, TCP 443, the application, voice, Internet policy, or Guest isolation.
13. Correct DHCP, gateway ping, DNS resolution, HTTPS, voice registration, Internet policy, Guest isolation, SSH restriction, and monitoring are valid examples.
14. Inadequate cable testing, outdated labels/diagram, no peer review, manual entry from outdated information, and incomplete post-change testing.
15. ARP, DHCP, DNS, TCP, ICMP, retransmission, reset, delay, and protocol evidence.
16. Captures may contain personal, credential, addressing, and application information.
17. Impact, scope, time, evidence, tests, changes, hypothesis, requested help, and relevant identifiers.
18. Physical diagram, logical diagram, rack elevation, IPAM, VLAN register, circuit register, inventory, configuration backup, dependency map, runbook, change record, and incident record are valid examples.
19. Physical diagrams show devices, ports, cables, and location; logical diagrams show addressing, VLANs, routing, and security zones.
20. It identifies the connected device or service, remote interface where useful, and circuit reference without secrets.
21. IP Address Management tracks prefixes, addresses, gateways, assignments, owners, and status.
22. A source of truth is the authoritative intended-state record; drift is the difference between intended and actual configuration.
23. A representative record of normal behavior under defined conditions.
24. Bandwidth is capacity, throughput is actual transfer rate, and goodput is useful delivered application data.
25. Latency is delay, jitter is delay variation, loss is undelivered packet percentage, and utilization is capacity in use.
26. Counters accumulate; their increase over a known interval shows whether the fault is current.
27. A device can answer ping while DNS, authentication, database, or application services have failed.
28. Excessive duplicate, flapping, low-value, or non-actionable alerts.
29. Forecasting resource demand and preparing capacity before performance or availability fails.
30. Standard is repeatable and pre-approved, normal is assessed and approved before implementation, and emergency is expedited for urgent need but remains documented.
31. Reason, scope, risk, dependencies, implementation, tests, success criteria, rollback, window, approval, communication, and documentation.
32. It defines the trigger, exact restoration, owner, time, validation, and communication.
33. An approved secure baseline configuration for a device role.
34. It remains on the same device and may be lost with hardware failure, corruption, theft, or destructive change.
35. The immediate cause directly creates the symptom; deeper process causes explain why controls allowed it to occur.
36. To use repeated evidence-based questioning to identify deeper system or process causes.
37. Summary, impact, detection, timeline, evidence, causes, resolution, validation, preventive actions, owners, and dates.
38. Current status, completed work, outstanding issues, risks, workarounds, monitoring, next actions, owners, deadlines, and evidence location.
39. It explains problem, constraints, design, implementation, tests, reasoning, troubleshooting, security, resilience, outcome, and reproducible artifacts.
40. Secrets, private keys, real unauthorized customer data, sensitive hostnames/addresses, proprietary configurations, and exploitable details.
41. Network Engineering focuses connectivity, Cybersecurity protection and response, IT Support users/endpoints, and Cloud virtual services and automation.
42. Evidence considers interest, persistence, resources, demand, transferable skills, and ability to build credible work.
43. Situation, Task, Action, Result.
44. Positive tests prove required service works; negative tests prove prohibited access remains blocked.
45. Cloud services still depend on addressing, routes, policy, DNS, identity, return paths, monitoring, change control, and recovery.
