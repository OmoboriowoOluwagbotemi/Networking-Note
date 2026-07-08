# LESSON 24: POWER AND RESILIENCE

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 24.1 What Is Network Power Resilience?

Network power resilience is the ability of network infrastructure to continue operating, fail safely, and recover predictably when utility power is interrupted or unstable.

Routers, switches, wireless access points, firewalls, servers, storage systems, optical-network terminals, wireless ISP radios, and monitoring systems all depend on electrical power. A perfectly configured network becomes unavailable when its critical devices lose power.

Resilience is broader than buying a UPS. It requires:

- Understanding the electrical load
- Protecting equipment from poor power quality
- Providing short-term and long-term backup power
- Eliminating single points of failure where justified
- Monitoring power systems
- Maintaining batteries and generators
- Documenting shutdown and recovery procedures
- Testing disaster recovery and business continuity plans

### 24.2 Why Power and Resilience Matter

Availability is one objective of the CIA triad introduced in Lesson 21. Users cannot access protected data or services if the network, identity system, DNS server, firewall, or Internet edge is offline.

Power instability can create more than a temporary outage. Repeated abrupt shutdowns may corrupt storage, interrupt software updates, damage power supplies, reset configurations that were not saved, and shorten battery life. Voltage disturbances can destroy multiple devices simultaneously.

In environments with unreliable utility supply, including many offices, schools, clinics, shops, and small data rooms in Nigeria, backup power is part of network design rather than an optional accessory.

### 24.3 Where Resilience Must Be Applied

Power planning should follow the complete service path:

```text
Utility / generator / solar
           |
Protection and transfer equipment
           |
UPS / inverter / battery system
           |
Network rack power distribution
           |
Router - firewall - switch - server - AP
           |
ISP or service-provider equipment
```

Keeping the core switch alive does not preserve Internet service if the ISP modem, optical-network terminal, wireless radio, firewall, or DNS service loses power. The protected load must include every critical dependency.

## 24.4 Electrical Fundamentals for Network Professionals

Network engineers are not automatically qualified electricians. Permanent wiring, earthing, breakers, transfer switches, battery banks, high-voltage DC systems, solar arrays, and generator integration must be designed and installed by qualified professionals according to applicable codes and manufacturer requirements.

Network staff still need enough electrical knowledge to specify loads, identify risks, monitor systems, and communicate requirements.

### 24.4.1 Voltage, Current, Power, and Energy

| Quantity | Symbol | Unit | Meaning |
|---|---|---|---|
| Voltage | V | Volt | Electrical potential difference |
| Current | I | Ampere | Rate of electric charge flow |
| Real power | P | Watt | Power consumed to perform useful work |
| Apparent power | S | Volt-ampere | Product of RMS voltage and current |
| Energy | E | Watt-hour | Power consumed over time |

For a simple DC load:

```text
Power (W) = Voltage (V) x Current (A)
```

Energy over time:

```text
Energy (Wh) = Power (W) x Time (hours)
```

A 200 W network load operating for four hours ideally requires:

```text
200 W x 4 h = 800 Wh
```

The real system needs more than 800 Wh because inverters, batteries, cabling, and power supplies are not 100 percent efficient.

### 24.4.2 Watts and Volt-Amperes

UPS devices are commonly rated in both watts and volt-amperes. Watts represent real power. VA represents apparent power.

```text
Power factor = Watts / Volt-amperes
```

A `1500 VA / 900 W` UPS must stay below both limits. A load of 950 W is too large even if its apparent power remains below 1500 VA.

Do not assume that a 1000 VA UPS can deliver 1000 W. Always read the manufacturer's watt rating and runtime data.

### 24.4.3 AC and DC

Utility and generator output is alternating current, or AC. Batteries and many electronics internally use direct current, or DC. An inverter converts DC from a battery into AC. A charger or rectifier converts AC into controlled DC for charging or powering DC equipment.

Every conversion introduces loss. Reducing unnecessary conversion stages can improve efficiency, but any direct-DC design must use correct voltage regulation, connectors, polarity protection, fusing, and qualified installation.

## 24.5 Power Quality Problems

Power failure is only one electrical threat.

| Problem | Description | Possible Effect |
|---|---|---|
| Blackout | Complete loss of utility power | Immediate shutdown |
| Brownout | Sustained low voltage | Instability, overheating, UPS transfer |
| Sag | Short reduction in voltage | Device reset or malfunction |
| Surge | Longer increase above normal voltage | Stress or damage |
| Spike/transient | Very brief high-voltage event | Component damage |
| Noise | Unwanted electrical interference | Errors, instability |
| Frequency variation | AC frequency outside expected range | UPS/generator incompatibility |

A UPS does not provide identical protection in every design. The topology, input range, filtering, surge protection, grounding, and connected load all matter.

### 24.5.1 Earthing and Surge Protection

Protective earthing provides a controlled path for fault current and supports safety devices. Surge protective devices help divert transient energy. Neither function should be improvised.

Poor earthing can endanger people and equipment. It may also increase problems on copper links between buildings. Fiber-optic cabling provides electrical isolation between buildings and is often preferred for both distance and lightning-risk reasons.

Network cables entering from outdoors, rooftop radios, CCTV systems, and antennas need coordinated lightning and surge protection designed by qualified installers.

## 24.6 Measuring and Classifying the Load

Do not size backup power using guesses alone.

Build an inventory:

| Device | Quantity | Rated/Measured W Each | Total W | Critical? |
|---|---:|---:|---:|---|
| Edge router | 1 | 25 | 25 | Yes |
| Firewall | 1 | 40 | 40 | Yes |
| PoE switch | 1 | 80 base + PoE | Varies | Yes |
| ISP ONT | 1 | 12 | 12 | Yes |
| Server | 1 | 250 | 250 | Depends |
| Monitor | 1 | 30 | 30 | No |

Manufacturer ratings provide a safe planning reference but may represent maximum consumption. A calibrated power meter, managed PDU, UPS telemetry, or device power report can provide measured values.

Loads should be classified:

- **Critical:** Must remain operational.
- **Essential:** May be shed after a defined period.
- **Nonessential:** Should not consume backup capacity.

Desktop printers, kettles, heaters, air conditioners, and unrelated sockets should not be connected to a network UPS unless the system was explicitly engineered for them.

## 24.7 Power over Ethernet and Hidden Load

Power over Ethernet, or PoE, allows a switch to deliver power and data through Ethernet cabling. The switch therefore supplies not only its own electronics but also APs, IP phones, cameras, and other powered devices.

```text
Total switch input load
= switch base consumption
+ delivered PoE power
+ conversion losses
```

A switch drawing 60 W by itself may draw several hundred watts when serving many PoE devices. The configured PoE budget is a maximum capability, not necessarily the present load.

Useful Cisco IOS commands vary by platform but may include:

```cisco
show power inline
show environment
show environment power
show processes cpu
```

When power is limited, critical PoE devices can be prioritized. For example, the reception phone, security camera, and primary AP may have higher priority than a meeting-room phone.

## 24.8 Capacity, Headroom, and Growth

Backup equipment should not be operated continuously at its absolute maximum. Headroom supports startup behavior, battery aging, normal variation, future growth, and safer operation.

A planning process is:

1. Inventory and measure the critical load.
2. Include PoE endpoint demand.
3. Identify startup or peak load.
4. Add documented design headroom.
5. Check both watt and VA ratings.
6. Verify required runtime from manufacturer data.
7. Confirm environmental and expansion requirements.

The exact headroom is an engineering and organizational decision. A common preliminary design may reserve 20 to 30 percent, but manufacturer guidance and professional calculations take priority.

## 24.9 Uninterruptible Power Supply

An Uninterruptible Power Supply, or UPS, supplies temporary power when the input fails and may improve power quality.

A UPS commonly contains:

- Charger/rectifier
- Battery
- Inverter
- Transfer or bypass components
- Monitoring and control electronics

The UPS performs three important jobs:

1. Bridges short outages without service interruption.
2. Provides time for a generator or larger backup system to start.
3. Allows controlled shutdown if power will not return.

### 24.9.1 Standby UPS

A standby, or offline, UPS normally supplies the load from utility power and transfers to the inverter during failure. It is affordable and may suit low-risk endpoints, but it has a transfer time and provides less conditioning.

### 24.9.2 Line-Interactive UPS

A line-interactive UPS can correct some voltage variation without using the battery and transfers to battery during an outage. It is common for network closets and small server rooms.

### 24.9.3 Online Double-Conversion UPS

An online UPS continuously converts input AC to DC and then DC back to AC for the load. This isolates the load from many input disturbances and normally provides no transfer interruption when utility power fails.

It offers strong protection but costs more, produces heat, and has conversion losses.

| Feature | Standby | Line-Interactive | Online Double-Conversion |
|---|---|---|---|
| Normal power path | Utility | Utility with regulation | Through rectifier/inverter |
| Transfer time | Present | Present but short | Effectively none |
| Conditioning | Basic | Moderate | Strong |
| Cost | Lower | Medium | Higher |
| Typical use | Individual low-risk device | Network closet/small server room | Critical infrastructure |

## 24.10 UPS Runtime

UPS VA capacity does not tell the runtime. Runtime depends on the connected watts, battery capacity, battery condition, temperature, inverter efficiency, UPS design, and discharge rate.

Manufacturer runtime charts or calculators are the preferred source for a specific UPS. A simple energy calculation is useful only for preliminary estimation.

Example: critical load is 300 W and required runtime is 30 minutes.

```text
Ideal energy = 300 W x 0.5 h
             = 150 Wh
```

The battery system must provide more than 150 Wh because of losses, discharge characteristics, aging, and reserve. A UPS advertised as 1500 VA may still provide only a short runtime at 300 W if its battery is small.

### 24.10.1 Runtime Objectives

Specify the purpose:

- Bridge a 30-second generator start
- Survive common 10-minute outages
- Keep the Internet edge alive for two hours
- Provide 15 minutes for server shutdown

Without a runtime objective, capacity selection has no clear success criterion.

## 24.11 Battery Fundamentals

### 24.11.1 Battery Capacity

Battery capacity is often stated in ampere-hours:

```text
Nominal watt-hours = Battery voltage x Ampere-hours
```

A nominal `12 V, 100 Ah` battery stores:

```text
12 V x 100 Ah = 1200 Wh nominal
```

This does not mean all 1200 Wh should or can be delivered as usable AC energy. Usable energy depends on battery chemistry, permitted depth of discharge, discharge rate, age, temperature, inverter efficiency, cabling, and low-voltage cut-off.

### 24.11.2 Depth of Discharge

Depth of discharge, or DoD, is the percentage of battery capacity removed during a cycle. Repeated deep discharge can significantly shorten the life of some battery chemistries.

### 24.11.3 State of Charge and State of Health

State of charge estimates how full the battery is now. State of health estimates how its present capability compares with a new battery. A battery can report fully charged but have poor capacity due to age or damage.

### 24.11.4 Common Battery Types

| Type | Characteristics |
|---|---|
| Flooded lead-acid | Lower cost; ventilation and maintenance requirements |
| Sealed lead-acid/VRLA | Common in UPS systems; limited maintenance; heat-sensitive |
| AGM | Sealed lead-acid design with good power delivery |
| Gel | Sealed design requiring compatible charging |
| Lithium iron phosphate | Higher cycle life and usable DoD; higher initial cost; requires BMS |

Battery chemistry must match the charger/inverter profile. Mixing old and new batteries or different capacities and chemistries in one bank creates imbalance and risk.

### 24.11.5 Battery Safety

Battery banks can deliver extremely high fault current. Hazards include fire, electric shock, chemical exposure, toxic gas, burns, and explosion.

Requirements include correctly rated cables, overcurrent protection, disconnects, ventilation where required, physical protection, temperature control, polarity control, battery-management systems, and qualified installation. Never short a battery or place tools across terminals.

## 24.12 Inverter Systems

An inverter converts battery DC into AC for connected equipment. A complete inverter/charger may also charge batteries and transfer between utility, generator, solar, and battery sources.

### 24.12.1 Waveform

Sensitive IT equipment generally operates best with a true or pure sine-wave output. Modified sine-wave products may cause noise, heat, malfunction, or incompatibility in some power supplies.

### 24.12.2 Inverter Rating

Check:

- Continuous watt rating
- Surge rating and duration
- DC input voltage
- AC output voltage and frequency
- Efficiency curve
- Charger capacity and supported chemistry
- Transfer time
- Communications and monitoring
- Environmental limits

Do not size an inverter using only its marketing VA number.

### 24.12.3 Preliminary Battery Runtime Calculation

Suppose the critical network load is 400 W and the goal is four hours. Assume, for preliminary planning only:

- 90 percent inverter efficiency
- 80 percent usable battery fraction

Required nominal battery energy:

```text
Required Wh
= (Load W x Hours) / (Efficiency x Usable fraction)

= (400 x 4) / (0.90 x 0.80)
= 1600 / 0.72
= approximately 2222 Wh
```

At a nominal 24 V:

```text
Required Ah = 2222 Wh / 24 V
            = approximately 92.6 Ah
```

This is not a final installation specification. Battery aging, peak load, temperature, cable loss, actual discharge curves, reserve, manufacturer limits, and growth must be included by a qualified designer.

## 24.13 Solar Integration

A solar power system can extend runtime and reduce dependence on utility supply or fuel.

```text
Solar panels
     |
Charge controller / hybrid inverter
     |
Battery bank
     |
Inverter output
     |
Critical network loads
```

The panels generate DC energy. A charge controller manages battery charging. A hybrid inverter may coordinate solar, batteries, utility, and generator power.

### 24.13.1 Solar Energy Estimation

Daily load energy:

```text
Daily Wh = Average load W x operating hours
```

For a 300 W load operating continuously:

```text
300 W x 24 h = 7200 Wh/day = 7.2 kWh/day
```

If preliminary planning assumes five effective peak-sun-hours:

```text
Ideal panel power = 7200 Wh / 5 h
                  = 1440 W
```

The actual array must be larger to account for temperature, dust, wiring, controller and inverter loss, battery charging, weather, panel orientation, aging, and required reserve. Local site survey and solar-resource data are necessary.

### 24.13.2 Solar Is Not Automatically Backup Power

A grid-tied solar system may shut down during a utility outage for anti-islanding safety. Backup operation requires an architecture specifically designed to form and control an isolated power system, usually with a compatible inverter and storage.

Students must not assume that visible solar panels mean the network remains powered during blackout.

### 24.13.3 Nigerian Operational Considerations

Practical considerations may include:

- Long utility outages
- Generator fuel availability and quality
- High ambient temperature
- Dust reducing solar output and blocking ventilation
- Lightning and surge exposure
- Physical security of panels and batteries
- Access to trained maintenance personnel
- Replacement battery availability
- Harmonic or frequency quality from generators

Design should match local operating reality, not only laboratory conditions.

## 24.14 Generator Integration

A generator provides longer-duration power when fuel and maintenance are available. A UPS bridges the starting and transfer interval and protects critical loads from interruption.

```text
Utility fails
     |
UPS immediately supports load
     |
Generator starts and stabilizes
     |
Transfer system connects generator
     |
UPS accepts input and recharges
```

Generator integration requires correctly designed transfer switching so that generator output cannot back-feed the utility supply. Generator voltage, frequency, waveform quality, grounding arrangement, capacity, and load steps must be compatible with the UPS and facility.

An oversized UPS charger may place a large load on the generator while batteries recharge. Capacity planning must include both the live equipment and charging demand.

Fuel storage, exhaust, ventilation, noise, emissions, fire safety, test schedules, and refueling during prolonged incidents are business continuity issues.

## 24.15 Automatic Transfer Switch and Bypass

An Automatic Transfer Switch, or ATS, transfers a load between approved power sources. Transfer behavior, interlocking, switching time, neutral treatment, and source compatibility must be engineered.

A maintenance bypass can allow qualified staff to service a UPS without shutting down the protected load. Incorrect bypass operation can remove power protection or create dangerous conditions, so procedures and labeling are essential.

## 24.16 Power Distribution in the Network Rack

A Power Distribution Unit, or PDU, distributes power within a rack. PDUs may be:

- Basic
- Metered
- Monitored over the network
- Switched for controlled outlet operation

Dual-power-supply equipment should use separate power paths where the resilience design justifies it:

```text
Device PSU A --> UPS/PDU path A
Device PSU B --> UPS/PDU path B
```

Connecting both supplies to the same PDU and same UPS protects against one power-supply failure but not against PDU or UPS failure.

Do not overload sockets, extension cords, PDUs, breakers, UPS outlets, or phases. Cable management must not block airflow or create trip and fire hazards.

## 24.17 Cooling and Environmental Resilience

Network equipment converts electrical power into heat. A room can retain power and still fail because cooling stops.

Monitor:

- Room and rack inlet temperature
- Humidity
- Device temperature
- Fan state
- Airflow obstruction
- Water leakage
- Smoke/fire alarms
- Door access

Common environmental threats include failed air conditioning, dust, blocked filters, leaking roofs, flooding, rodents, construction debris, and unauthorized access.

High temperature accelerates battery aging. Battery and UPS runtime claims are usually based on specified environmental conditions, not a hot unventilated cupboard.

## 24.18 Monitoring Power Systems

Managed UPS, PDU, inverter, environmental sensor, and generator systems may report:

- Input and output voltage
- Frequency
- Load percentage and watts
- Battery state of charge
- Estimated runtime
- Battery replacement warning
- Temperature
- Source status
- Transfer events
- Overload and fault alarms

Monitoring may use SNMPv3, Syslog, APIs, vendor platforms, dry contacts, or building-management systems. Lesson 22 established why NTP and central logging are essential: power events from different devices must share accurate timestamps.

Alerts should be actionable. Examples include:

- Utility power lost
- UPS on battery
- Runtime below threshold
- Battery fault
- UPS overload
- Generator failed to start
- Rack temperature high
- Critical PDU outlet offline

## 24.19 Graceful Shutdown and Startup

When runtime becomes insufficient, systems should shut down in a controlled order.

Example shutdown sequence:

1. Stop nonessential applications.
2. Shut down application servers.
3. Shut down databases and storage according to vendor procedure.
4. Shut down noncritical network services.
5. Preserve the management, monitoring, firewall, and Internet edge as long as useful.
6. Shut down remaining equipment before battery exhaustion.

Startup is usually performed in dependency order:

1. Power and cooling stable
2. Core network and storage fabric
3. Firewalls, routing, DNS, DHCP, identity, and time
4. Databases and storage
5. Application services
6. User access

The correct order depends on documented service dependencies. Randomly powering every device at once may cause high inrush current and application failures.

## 24.20 Availability, Reliability, and Resilience

| Term | Meaning |
|---|---|
| Availability | Proportion of time a service is usable |
| Reliability | Ability to operate without failure for a period |
| Resilience | Ability to withstand disruption and recover |
| Redundancy | Duplicate components or paths used to reduce failure impact |
| Fault tolerance | Ability to continue operating after a component failure |

Availability can be expressed as:

```text
Availability = Uptime / (Uptime + Downtime)
```

Approximate annual downtime:

| Availability | Annual Downtime |
|---:|---:|
| 99% | About 3 days 15 hours 39 minutes |
| 99.9% | About 8 hours 46 minutes |
| 99.99% | About 52 minutes 34 seconds |
| 99.999% | About 5 minutes 15 seconds |

High availability becomes progressively more expensive. The target must reflect business impact rather than prestige.

## 24.21 Single Points of Failure

A single point of failure, or SPOF, is a component whose failure can stop a required service.

Examples include:

- One utility feed
- One UPS
- One firewall
- One core switch
- One ISP
- One DNS server
- One physical cable path
- One administrator who knows the recovery process

Redundancy must remove the actual failure domain. Two ISP links using the same provider, pole, fiber duct, building entrance, and edge router may fail together.

Ask:

```text
What can fail?
What depends on it?
Will the backup survive the same event?
How is failover detected and tested?
```

## 24.22 High-Availability Design

High availability may use:

- Redundant power supplies
- Separate UPS/PDU paths
- Device pairs
- Switch stacking or chassis redundancy
- First-hop redundancy
- Dynamic routing
- Multiple ISPs
- Diverse physical cable paths
- Server clustering
- Replicated storage
- Multiple cloud zones or regions

Redundancy introduces complexity. Split-brain behavior, inconsistent configuration, failed state synchronization, and untested failover can make a redundant design less dependable than expected.

## 24.23 Disaster Recovery and Business Continuity

Disaster Recovery, or DR, is the organized restoration of technology services after serious disruption.

Business Continuity, or BC, is the broader ability of the organization to continue its critical functions during and after disruption.

```text
Business continuity asks:
How does the organization keep operating?

Disaster recovery asks:
How are technology and data restored?
```

BC may include alternative workplaces, manual procedures, emergency communications, suppliers, staff welfare, finance, and legal obligations. DR supports BC but does not replace it.

## 24.24 Threats and Disaster Scenarios

Plans should consider realistic scenarios:

- Prolonged utility outage
- UPS or battery-bank failure
- Generator failure or fuel shortage
- Fire, flood, or severe weather
- Internet-provider outage
- Hardware failure
- Ransomware
- Accidental deletion or misconfiguration
- Theft or vandalism
- Cloud-region or SaaS outage
- Loss of key personnel
- Building inaccessible

A risk assessment considers likelihood, impact, existing controls, and residual risk.

## 24.25 Business Impact Analysis

A Business Impact Analysis, or BIA, identifies critical business processes, their technology dependencies, and the consequences of interruption.

A BIA asks:

- Which service is critical?
- Who uses it?
- What systems, networks, power, people, and suppliers support it?
- How long can it be unavailable?
- How much data loss is acceptable?
- What financial, safety, legal, and reputational impacts arise?
- Which service must be restored first?

| Service | Dependency | Maximum Tolerable Downtime | Priority |
|---|---|---:|---:|
| Emergency communications | Network, voice, power | 15 minutes | 1 |
| Payment processing | Internet, DNS, application | 1 hour | 2 |
| Internal file archive | Storage, identity | 24 hours | 4 |

The BIA drives technical recovery priorities. Technology teams should not decide business criticality alone.

## 24.26 RTO, RPO, and MTD

### Recovery Time Objective

RTO is the target maximum time to restore a service after disruption.

### Recovery Point Objective

RPO is the maximum acceptable amount of data loss measured in time.

If a system backs up every four hours, a failure just before the next backup could lose nearly four hours of changes. An RPO of 15 minutes requires more frequent replication or backup than daily copying.

### Maximum Tolerable Downtime

Maximum Tolerable Downtime, or MTD, is the longest the business process can remain unavailable before unacceptable harm occurs. The planned RTO should be shorter than the MTD.

```text
Incident occurs
      |
      |---- acceptable data-loss window ----|  RPO looks backward
      |
      |---- target restoration time --------|  RTO looks forward
      |
      |---- maximum tolerable downtime -----|  business limit
```

| Metric | Main Question |
|---|---|
| RTO | How quickly must service return? |
| RPO | How much recent data may be lost? |
| MTD | How long before impact becomes unacceptable? |

## 24.27 Backup Fundamentals

A backup is a recoverable copy of data or configuration stored separately from the working system.

### 24.27.1 Backup Types

| Type | Contents | Backup Speed | Restore Consideration |
|---|---|---|---|
| Full | All selected data | Slowest/largest | Simplest base restore |
| Incremental | Changes since last backup of any type | Fast/small | Requires full plus incrementals |
| Differential | Changes since last full backup | Grows over time | Requires full plus latest differential |

### 24.27.2 The 3-2-1 Principle

A common principle is:

```text
3 copies of important data
2 different storage media or systems
1 copy off-site
```

Modern ransomware resilience may add an offline, immutable, or logically isolated copy. The design must prevent compromised administrator credentials from deleting every backup.

A synchronized replica is not automatically a backup. Corruption, deletion, or ransomware may replicate to it.

### 24.27.3 Network Configuration Backups

Back up:

- Router, switch, firewall, WLC, and VPN configurations
- Device software images where licensing permits
- Certificates and keys using protected procedures
- Network diagrams and IP address plans
- ISP and support contacts
- License information
- Automation scripts and templates

Secrets must be encrypted and access-controlled. A configuration backup is sensitive security information.

## 24.28 Recovery Sites

| Site Type | Characteristics | Recovery Speed | Cost |
|---|---|---|---|
| Cold site | Space and basic facilities; little active equipment | Slow | Lower |
| Warm site | Some equipment, connectivity, and recent data | Medium | Medium |
| Hot site | Operational systems and replicated data | Fast | Higher |

Cloud services can support recovery, but cloud DR still requires architecture, security, data transfer, testing, cost control, and staff capability.

## 24.29 Recovery Documentation

A recovery runbook should contain:

- Scope and activation criteria
- Roles and authority
- Emergency contacts
- Service dependencies
- Current diagrams and inventories
- Backup locations and credentials procedure
- Shutdown and startup order
- Recovery steps
- Validation tests
- Communication plan
- Vendor escalation paths
- Manual workarounds
- Return-to-normal procedure
- Evidence and incident-record requirements

The plan must be available during the incident. A runbook stored only on the failed server is not useful.

## 24.30 Testing and Maintenance

An untested recovery plan is an assumption.

Testing methods include:

| Test | Description |
|---|---|
| Checklist review | Staff review procedures and contacts |
| Tabletop exercise | Team discusses response to a scenario |
| Walkthrough | Staff step through responsibilities and systems |
| Simulation | Controlled scenario tests coordination |
| Parallel test | Recovery systems run without replacing production |
| Full interruption | Production fails over; highest risk and realism |

Tests should have objectives, approvals, safety controls, rollback, observers, evidence, and an after-action review.

Plans change when staff, suppliers, applications, addresses, passwords, circuits, or equipment change. Review them on a defined schedule and after major changes or incidents.

## 24.31 Incident Response, DR, and BC Relationship

Incident response contains and manages the immediate event. Disaster recovery restores technology. Business continuity sustains critical operations.

Example ransomware sequence:

1. Incident response isolates affected systems.
2. Business continuity activates manual or alternate processes.
3. Disaster recovery rebuilds clean infrastructure and restores validated data.
4. Security teams verify that the threat is removed.
5. Business owners validate service.
6. The organization returns to normal operation and reviews lessons.

Restoring too quickly without containment can reintroduce the threat.

## 24.32 Enterprise Power Case Study

A 20-person office has:

- ISP ONT: 12 W
- Edge router: 25 W
- Firewall: 45 W
- 24-port PoE switch including active PoE load: 210 W
- Small server: 180 W
- Monitoring appliance: 30 W

Total measured critical load:

```text
12 + 25 + 45 + 210 + 180 + 30 = 502 W
```

With preliminary 25 percent headroom:

```text
502 W x 1.25 = 627.5 W
```

The team must choose equipment whose continuous watt and VA limits exceed the engineered requirement. The UPS bridges transfer and controlled shutdown; a hybrid inverter and battery bank provide longer runtime; a generator covers prolonged low-solar periods and major outages.

The network team also identifies that the rack air conditioner and ISP rooftop radio are dependencies. The power design would fail its service objective if either were omitted.

Loads are prioritized. The server shuts down after a sustained outage, while the firewall, router, switch, critical AP, phones, and ISP equipment remain available longer.

## 24.33 Business Continuity Case Study

A retail company depends on Internet-based payment processing. Its BIA establishes:

```text
MTD: 4 hours
RTO: 1 hour
RPO: 15 minutes for transaction records
```

Controls include dual Internet providers using diverse paths, UPS and generator power, a cellular payment fallback, replicated transaction data, offline backups, paper-based emergency procedures, and a tested communication plan.

During an area-wide fiber cut, routing fails over to the second provider. If both wired providers fail, essential payment devices use controlled cellular service. The company continues limited operation while the network team works with carriers.

The lesson is that business continuity combines technology, people, suppliers, procedures, and communication.

## 24.34 Practical Labs

### Lab 1: Network Power Audit

Inspect a real or simulated network rack.

1. List every device and power supply.
2. Record rated and measured watts where available.
3. Include PoE endpoint demand.
4. Classify each load as critical, essential, or nonessential.
5. Identify all power-path single points of failure.
6. Record UPS watt/VA rating, load, battery age, and runtime estimate.
7. Recommend monitoring and maintenance improvements.

Do not open electrical panels or battery enclosures.

### Lab 2: Runtime Calculation

Use this example:

```text
Critical load: 350 W
Required runtime: 3 hours
Inverter efficiency: 90%
Usable battery fraction: 80%
Nominal battery voltage: 24 V
```

Calculate preliminary nominal watt-hours and ampere-hours. Then list at least five reasons the final professional design must be larger or differently specified.

### Lab 3: Packet Tracer Resilience Design

Build a headquarters and branch topology with redundant WAN paths where supported.

1. Identify every network SPOF.
2. Add a second path or device where justified.
3. Configure routing that can use the alternate path.
4. Simulate a link failure.
5. Record detection and recovery behavior.
6. Explain which power failures Packet Tracer does not realistically model.

### Lab 4: BIA and Recovery Runbook

Choose a school, clinic, shop, or office. Identify three critical services. Define dependencies, MTD, RTO, RPO, backup method, recovery order, responsible role, and validation test.

Conduct a tabletop exercise involving a 12-hour utility outage followed by a failed generator start.

## 24.35 Troubleshooting Power and Resilience

Use a safety-first process:

1. Protect people and follow site electrical procedures.
2. Determine the scope: one device, rack, room, building, or area.
3. Identify the active source: utility, UPS, inverter, solar, or generator.
4. Check alarms and monitoring without bypassing safety controls.
5. Verify load percentage, estimated runtime, temperature, and battery status.
6. Check which dependencies lost power.
7. Shed approved nonessential loads if the procedure allows.
8. Begin controlled shutdown before reserve is exhausted.
9. Escalate electrical faults to qualified personnel.
10. Record the timeline and preserve logs.

| Symptom | Possible Cause |
|---|---|
| UPS overload alarm | Excess load, PoE growth, failed redundant PSU |
| Runtime much shorter | Aged battery, heat, added load, poor charge |
| UPS rejects generator | Voltage/frequency instability or incompatibility |
| Devices restart during transfer | Transfer time, weak battery, overloaded inverter |
| Battery never fully charges | Charger fault, undersized source, damaged battery |
| Network survives but Internet fails | ISP equipment omitted from backup |
| UPS healthy but rack off | PDU, breaker, outlet, cable, or bypass issue |
| Repeated temperature alarms | Cooling failure, blocked airflow, excess load |

## 24.36 Cybersecurity and Cloud Relevance

Power and physical resilience are cybersecurity concerns. An attacker may target power, cooling, UPS management interfaces, building systems, or recovery backups. Management interfaces should use strong authentication, segmentation, updates, secure protocols, and logging.

Availability attacks include DDoS, ransomware, destructive configuration changes, and physical disruption. Backups must be protected from unauthorized deletion.

Cloud services reduce some local power responsibilities but do not remove resilience planning. Customers still design for availability zones, regions, Internet paths, identity dependencies, backups, quotas, and provider outages. The shared-responsibility model means the provider protects facility infrastructure while the customer remains responsible for appropriate architecture and data protection.

## 24.37 IT Support, Interview, and Exam Relevance

IT support staff may check UPS alarms, coordinate shutdown, verify service recovery, document incidents, and escalate electrical faults. Network engineers calculate network loads, identify service dependencies, design redundancy, monitor power systems, and participate in DR tests.

Interview questions often include:

- Watt versus VA
- UPS topology and runtime
- PoE load effects
- Battery capacity and usable energy
- RTO versus RPO
- Backup versus replication
- Redundancy and common failure domains
- Cold, warm, and hot sites
- Why recovery plans must be tested

### CCNA 200-301 and Network+ N10-009 Reminders

- Availability depends on power, cooling, connectivity, hardware, software, and people.
- A UPS supplies temporary power; its VA rating does not equal runtime.
- Check both watt and VA limits.
- PoE endpoint power contributes to switch and UPS load.
- Redundancy must avoid shared failure domains.
- RTO is target restoration time; RPO is acceptable data-loss time.
- A backup must be recoverable and protected separately.
- DR restores technology; BC sustains business operations.
- Cold sites recover slowly; hot sites recover quickly at higher cost.
- Monitoring, documentation, maintenance, and testing are part of resilience.

## 25. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| Power Resilience | Ability to continue, fail safely, and recover during power disruption |
| Voltage | Electrical potential difference measured in volts |
| Current | Flow of electric charge measured in amperes |
| Watt | Unit of real power |
| Volt-Ampere | Unit of apparent power |
| Watt-Hour | Unit of energy |
| Power Factor | Ratio of real power in watts to apparent power in VA |
| Blackout | Complete loss of electrical supply |
| Brownout | Sustained reduction in voltage |
| Sag | Short-duration voltage reduction |
| Surge | Voltage increase lasting longer than a transient |
| Transient | Very short voltage disturbance |
| UPS | Uninterruptible Power Supply |
| Standby UPS | UPS that transfers from utility to battery during failure |
| Line-Interactive UPS | UPS providing voltage regulation and battery backup |
| Online UPS | Double-conversion UPS continuously supplying through inverter |
| Runtime | Time backup power can support a specified load |
| Battery Capacity | Amount of charge or energy a battery can store |
| Depth of Discharge | Percentage of battery capacity removed |
| State of Charge | Estimate of current battery fullness |
| State of Health | Estimate of present battery capability versus new |
| Inverter | Device converting DC into AC |
| Pure Sine Wave | AC output closely resembling utility waveform |
| Charge Controller | Device regulating energy used to charge batteries |
| Peak Sun Hours | Equivalent hours of full rated solar irradiance |
| ATS | Automatic Transfer Switch |
| Maintenance Bypass | Path allowing service around a UPS |
| PDU | Power Distribution Unit |
| Availability | Proportion of time a service is usable |
| Reliability | Ability to operate without failure |
| Resilience | Ability to withstand and recover from disruption |
| Redundancy | Duplication used to reduce failure impact |
| Fault Tolerance | Continued operation after a failure |
| SPOF | Single Point of Failure |
| Disaster Recovery | Restoration of technology after disruption |
| Business Continuity | Continuation of critical business functions |
| BIA | Business Impact Analysis |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| MTD | Maximum Tolerable Downtime |
| Full Backup | Copy of all selected data |
| Incremental Backup | Changes since the most recent backup |
| Differential Backup | Changes since the most recent full backup |
| Immutable Backup | Backup protected against alteration or deletion |
| Cold Site | Basic alternate location with little active equipment |
| Warm Site | Partially prepared recovery location |
| Hot Site | Operational recovery location with current systems/data |
| Runbook | Documented operational or recovery procedure |
| Tabletop Exercise | Discussion-based test of an incident scenario |

## 26. COMPARISON TABLES

### 26.1 Watts vs VA vs Watt-Hours

| Measure | Meaning | Used For |
|---|---|---|
| Watts | Real power | Load and equipment watt limit |
| VA | Apparent power | UPS/inverter electrical capacity |
| Wh | Energy | Runtime and battery planning |

### 26.2 UPS Topologies

| Feature | Standby | Line-Interactive | Online |
|---|---|---|---|
| Transfer | Yes | Yes | Effectively none |
| Conditioning | Basic | Moderate | Strong |
| Efficiency/cost | Efficient/lower cost | Balanced | More loss/higher cost |
| Use | Low-risk endpoint | Closet/small room | Critical systems |

### 26.3 UPS vs Inverter vs Generator vs Solar

| Technology | Primary Role | Typical Duration | Key Limitation |
|---|---|---|---|
| UPS | Immediate backup and conditioning | Minutes to hours | Battery runtime |
| Inverter/battery | Extended stored-energy supply | Hours | Battery capacity/recharge |
| Generator | Long-duration generated power | Fuel-dependent | Start, fuel, maintenance |
| Solar | Generates energy from sunlight | Resource-dependent | Weather/time/storage |

### 26.4 RTO vs RPO vs MTD

| Metric | Measures | Question |
|---|---|---|
| RTO | Restoration time | How quickly must it return? |
| RPO | Acceptable data-loss period | How much recent data may be lost? |
| MTD | Business tolerance limit | How long before harm is unacceptable? |

### 26.5 DR vs Business Continuity

| Feature | Disaster Recovery | Business Continuity |
|---|---|---|
| Scope | Technology restoration | Whole critical business operation |
| Focus | Systems, data, infrastructure | People, process, facilities, suppliers, technology |
| Relationship | Supports continuity | Includes and depends on DR |

### 26.6 Cold vs Warm vs Hot Sites

| Site | Readiness | Recovery | Cost |
|---|---|---|---|
| Cold | Low | Slow | Lower |
| Warm | Partial | Medium | Medium |
| Hot | High | Fast | Higher |

### 26.7 Full vs Incremental vs Differential Backup

| Type | Copies | Backup Requirement | Restore Requirement |
|---|---|---|---|
| Full | All selected data | More time/storage | Full backup |
| Incremental | Since last backup | Less time/storage | Full plus all required incrementals |
| Differential | Since last full | Grows until next full | Full plus latest differential |

## 27. REAL-WORLD ANALOGY

Think of a hospital emergency power plan. A UPS is the immediate bridge that prevents critical equipment from stopping. A generator supplies longer-duration power. Solar and batteries can reduce fuel dependence. Load classification ensures life-safety systems receive power before nonessential equipment.

Disaster recovery is the technical procedure for restoring failed systems. Business continuity is the larger plan that keeps patient care functioning through alternate rooms, communications, staff roles, suppliers, and manual procedures. Resilience comes from the complete system, not one battery.

## 28. QUICK-RECAP CHEAT SHEET

```text
POWER
W = V x A
Wh = W x hours
Power factor = W / VA
Check both UPS watts and VA
UPS rating does not equal runtime

LOAD
Inventory every dependency
Include PoE devices and ISP equipment
Critical, essential, nonessential
Add engineered headroom

BACKUP POWER
Standby: basic, transfer time
Line-interactive: voltage regulation
Online: double conversion, strongest conditioning
UPS bridges; inverter/battery extends; generator sustains
Solar generates energy but needs correct backup architecture

BATTERY
Nominal Wh = V x Ah
Usable energy depends on DoD, efficiency, age, temperature
Battery work requires qualified installation and protection

RESILIENCE
Find SPOFs and shared failure domains
Power, cooling, ISP, DNS, identity, people all matter
Monitor and test failover

RECOVERY
RTO = target restoration time
RPO = acceptable data loss in time
MTD = maximum business outage tolerance
DR restores technology
BC keeps critical business operating
Backups must be separate, protected, and tested
```

## 29. REVIEW QUESTIONS

1. What is network power resilience?
2. Why is power planning part of network availability?
3. Define voltage, current, real power, and energy.
4. What is the difference between watts and watt-hours?
5. Why must both UPS watt and VA limits be checked?
6. Name five power-quality problems.
7. Why should network staff not perform unqualified electrical installation?
8. How should critical loads be identified?
9. Why can PoE significantly change UPS sizing?
10. What is design headroom?
11. Compare standby, line-interactive, and online UPS designs.
12. Why does a UPS VA rating not reveal runtime?
13. Calculate ideal energy for a 250 W load operating for two hours.
14. What factors reduce usable battery energy?
15. Define depth of discharge, state of charge, and state of health.
16. Why must battery chemistry match charger settings?
17. What does an inverter do?
18. Why is pure sine-wave output preferred for IT equipment?
19. Explain why grid-connected solar may stop during an outage.
20. What role does a UPS play with a generator?
21. Why must generator charging load be included in sizing?
22. What is an ATS?
23. Why should dual power supplies use separate paths?
24. How can cooling failure cause a network outage?
25. Which power conditions should be monitored?
26. Explain availability, reliability, resilience, and redundancy.
27. What is a single point of failure?
28. Why may two ISP links still share one failure domain?
29. Compare disaster recovery and business continuity.
30. What is a Business Impact Analysis?
31. Define RTO, RPO, and MTD.
32. Compare full, incremental, and differential backups.
33. Why is replication not automatically a backup?
34. Explain the 3-2-1 backup principle.
35. Compare cold, warm, and hot recovery sites.
36. Why must recovery runbooks be available offline?
37. Compare tabletop and full-interruption testing.
38. Why is an untested recovery plan unreliable?
39. Calculate the preliminary nominal energy for a 400 W load lasting four hours at 90 percent inverter efficiency and 80 percent usable battery fraction.
40. Describe a safe response to a UPS low-runtime alarm.

## 30. SUGGESTED ANSWER GUIDE

1. It is the ability of network systems to continue, fail safely, and recover during power disruption.
2. Network services cannot remain available when their equipment and dependencies lack usable power.
3. Voltage is electrical potential, current is charge flow, real power is useful power in watts, and energy is power used over time in watt-hours.
4. Watts measure power at a moment; watt-hours measure energy over time.
5. The load must remain below both real-power and apparent-power capacity.
6. Blackout, brownout, sag, surge, transient, noise, and frequency variation are valid examples.
7. High-voltage and battery systems can cause shock, fire, burns, explosion, and death and require code-compliant qualified work.
8. Inventory the complete service path, measure or rate each load, identify dependencies, and classify business criticality.
9. The switch powers attached APs, phones, cameras, and other endpoints in addition to itself.
10. Reserved capacity for peaks, aging, variation, growth, and safer operation.
11. Standby transfers during failure with basic protection; line-interactive regulates some voltage and transfers; online continuously double-converts power.
12. Runtime depends on load watts, battery capacity, condition, temperature, efficiency, and discharge behavior.
13. `250 W x 2 h = 500 Wh` ideal.
14. Inverter/cable losses, permitted DoD, age, temperature, discharge rate, and reserve.
15. DoD is capacity removed, state of charge is current fullness, and state of health is present capability relative to new.
16. Different chemistries require different voltage, current, temperature, and charging profiles.
17. It converts DC, usually from batteries, into AC.
18. It is more compatible with sensitive power supplies and reduces heat, noise, or malfunction risk.
19. A normal grid-tied system may use anti-islanding protection and cannot form an isolated grid without compatible backup equipment.
20. It supplies immediate uninterrupted power while the generator starts and stabilizes.
21. Battery charging can add substantial demand beyond the live equipment load.
22. An Automatic Transfer Switch moves an approved load between power sources.
23. Separate paths reduce the chance that one UPS, PDU, cable, or breaker failure stops both supplies.
24. Equipment overheats, batteries degrade, devices throttle, or protective shutdown occurs.
25. Voltage, frequency, load, source, runtime, battery health, temperature, transfer, overload, and fault status.
26. Availability is usable time, reliability is failure-free operation, resilience is withstanding/recovering, and redundancy duplicates components or paths.
27. A component whose failure stops a required service.
28. They may share a provider, physical route, pole, duct, entrance, router, power source, or upstream facility.
29. DR restores technology; BC sustains the wider critical business operation.
30. Analysis identifying critical processes, dependencies, outage impact, priorities, and recovery requirements.
31. RTO is target restoration time, RPO is acceptable data-loss period, and MTD is the longest tolerable business interruption.
32. Full copies all selected data, incremental copies changes since the last backup, and differential copies changes since the last full.
33. Deletion, corruption, or malware may immediately replicate to the replica.
34. Keep three copies on two different media or systems with one off-site.
35. Cold is minimally prepared and slow, warm is partially prepared, and hot is operational and fast but costly.
36. The normal server, cloud account, or network may be unavailable during the incident.
37. A tabletop discusses decisions without disrupting production; a full interruption exercises real failover and has greater realism and risk.
38. Contacts, credentials, dependencies, backups, timing, or procedures may be wrong and remain undiscovered.
39. `(400 x 4) / (0.90 x 0.80) = approximately 2222 Wh`.
40. Follow the approved procedure, confirm the alarm and scope, shed approved nonessential load, estimate remaining time, begin graceful shutdown before exhaustion, escalate electrical faults, and document events.
