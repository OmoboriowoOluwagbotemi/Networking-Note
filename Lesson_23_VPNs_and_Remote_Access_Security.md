# LESSON 23: VPNs AND REMOTE ACCESS SECURITY

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 23.1 What Is a Virtual Private Network?

A Virtual Private Network, or VPN, creates a protected logical connection across a network that is not fully trusted. The untrusted network is commonly the public Internet, but it may also be a service-provider network, shared cloud infrastructure, or another organization's network.

The word **virtual** means the connection is created logically rather than through a dedicated physical cable between the endpoints. **Private** means approved traffic is protected and access is controlled. **Network** means the connection carries communication between devices, users, applications, or entire IP networks.

A VPN does not make the Internet private. It creates a protected tunnel through it.

```text
Private network A
      |
VPN gateway A
      |
====== Encrypted tunnel across untrusted network ======
      |
VPN gateway B
      |
Private network B
```

### 23.2 Why VPNs Exist

Organizations need secure communication beyond the physical office. A company may connect a Lagos headquarters to an Abuja branch, allow an engineer to work from home, connect an on-premises data center to a cloud virtual network, or provide a contractor with controlled application access.

Sending sensitive traffic directly across the Internet creates risks:

- Attackers may capture traffic.
- Data may be altered in transit.
- An unauthorized system may impersonate a trusted endpoint.
- Internal services may be exposed unnecessarily.
- Users may connect from infected or unmanaged devices.

A properly designed VPN can provide confidentiality, integrity, peer authentication, and controlled access. These security properties support the CIA triad introduced in Lesson 21.

### 23.3 How and Where VPNs Operate

A VPN normally performs four broad functions:

1. It identifies the traffic that should use the tunnel.
2. It authenticates the VPN peer, user, or both.
3. It encapsulates and protects the original traffic.
4. It sends the protected packet across the untrusted network.

VPN components may exist on routers, firewalls, dedicated VPN concentrators, cloud gateways, or endpoint software.

| Component | Purpose |
|---|---|
| VPN gateway | Terminates tunnels and enforces VPN policy |
| VPN client | Software that establishes remote-user connectivity |
| Identity service | Authenticates users or devices |
| PKI/certificate authority | Issues and validates digital certificates |
| Firewall/ACL | Restricts traffic before and after tunnel termination |
| Routing system | Directs protected networks toward the tunnel |
| Logging/monitoring | Records tunnel status, authentication, and security events |

## 23.4 The Security Services of a VPN

### 23.4.1 Confidentiality

Encryption transforms readable plaintext into ciphertext. A party without the correct key should not be able to understand captured traffic.

Encryption protects data in transit, but it does not repair an infected endpoint or prevent an authorized user from mishandling data after decryption.

### 23.4.2 Integrity

Integrity protection allows a recipient to detect unauthorized modification. If an attacker changes a protected packet in transit, the integrity check should fail and the packet should be rejected.

### 23.4.3 Authentication

Peer authentication verifies the identity of VPN gateways. User authentication verifies the person or account requesting remote access. Authentication methods include:

- Pre-shared keys
- Digital certificates
- Passwords
- One-time codes
- Hardware or software tokens
- Multifactor authentication

Pre-shared keys can be practical in small deployments, but unique certificates scale more effectively and avoid distributing the same secret to many peers.

### 23.4.4 Anti-Replay Protection

An attacker may capture a valid protected packet and transmit it again. Anti-replay mechanisms use sequence information and a sliding window to detect and reject duplicated or excessively old packets.

### 23.4.5 Authorization

A successful VPN login should not provide unrestricted access. Authorization determines which networks, applications, and ports the identity may reach. Lesson 22's AAA and ACL concepts therefore remain important after the tunnel forms.

## 23.5 Tunneling, Encapsulation, and Encryption

Tunneling places an original packet inside another packet so that it can cross an intermediate network.

```text
Original private packet
[Original IP header][TCP/UDP header][Data]

After VPN protection
[New outer IP header][VPN security information][Protected original packet]
```

The outer header is used to route the packet across the public network. The original packet is carried inside the protected payload.

Tunneling and encryption are related but not identical:

- **Tunneling** creates the logical path through encapsulation.
- **Encryption** protects confidentiality.
- **Integrity checking** detects modification.
- **Authentication** verifies an identity.

Some tunneling protocols do not encrypt data by themselves. For example, GRE provides flexible encapsulation but does not provide confidentiality. It must be combined with a security protocol such as IPsec when encryption is required.

## 23.6 Site-to-Site VPN

A site-to-site VPN connects entire networks through VPN gateways. End devices usually do not run VPN software or know that encryption is occurring.

```text
Headquarters LAN        Branch LAN
192.168.10.0/24         192.168.20.0/24
       |                      |
   HQ gateway ========== Branch gateway
             IPsec tunnel
```

When a headquarters host sends traffic to the branch subnet, the headquarters gateway identifies it as protected traffic, encrypts it, and sends it to the branch gateway. The branch gateway verifies, decrypts, and forwards the original packet.

### 23.6.1 Where Site-to-Site VPNs Are Used

- Headquarters-to-branch connectivity
- Data-center interconnection
- Business-to-business partner connections
- On-premises-to-cloud hybrid networking
- Backup paths across a secondary ISP
- Temporary secure connection during a migration

### 23.6.2 Benefits and Limitations

| Benefit | Explanation |
|---|---|
| Transparent to users | Gateways protect traffic automatically |
| Network-to-network reachability | Many hosts can communicate through one tunnel |
| Uses available Internet links | Dedicated private circuits may not be required |
| Central policy | Gateways enforce encryption and filtering |

Site-to-site VPN performance depends on Internet quality, gateway capacity, cryptographic processing, packet size, and routing. A VPN does not guarantee the bandwidth or latency of a private leased circuit.

## 23.7 Client-to-Site VPN

A client-to-site VPN, also called a remote-access VPN, connects one endpoint to an organization's VPN gateway.

```text
Remote laptop
     |
VPN client
     |
Internet
     |
Remote-access VPN gateway
     |
Approved internal resources
```

The user starts a VPN client or uses an operating-system VPN function. The gateway authenticates the user and possibly the device. If access is approved, the endpoint receives tunnel parameters, routes, DNS settings, and an address from a VPN pool.

### 23.7.1 Common Uses

- Employees working from home
- Engineers providing approved after-hours support
- Traveling staff using public Wi-Fi
- Contractors reaching a limited project environment
- Administrators managing systems through a controlled path

Remote access creates higher endpoint risk than a gateway-to-gateway tunnel because the remote computer may be outside the organization's physical control. Strong authentication, endpoint security, posture assessment, least privilege, and monitoring are essential.

## 23.8 Remote-Access Connection Process

A typical connection proceeds as follows:

1. The client discovers and contacts the VPN gateway.
2. The client and gateway negotiate supported security settings.
3. The gateway presents its identity, commonly through a certificate.
4. The user and possibly the device authenticate.
5. Authorization policy determines permitted access.
6. Session keys are created.
7. The gateway supplies an address, routes, and DNS settings.
8. Protected traffic begins.
9. The gateway logs session events and enforces timeouts.
10. Keys and security associations are renewed or removed when the session ends.

The exact process varies by VPN technology, but the security goals remain similar.

## 23.9 Full-Tunnel and Split-Tunnel VPN

Routing policy determines which client traffic enters the VPN.

### 23.9.1 Full Tunnel

In a full-tunnel design, most or all endpoint traffic is sent through the organization's VPN gateway, including general Internet traffic.

```text
Remote user --> encrypted tunnel --> company gateway --> Internet/internal systems
```

This allows company security controls to inspect and log Internet access. It increases VPN bandwidth demand and may add latency.

### 23.9.2 Split Tunnel

In a split-tunnel design, traffic for protected company networks enters the VPN while other Internet traffic exits through the user's local connection.

```text
Company traffic --> VPN tunnel
Public Internet traffic --> local Internet gateway
```

Split tunneling reduces gateway load and often improves cloud-application performance. However, the endpoint simultaneously communicates with trusted and untrusted networks, so endpoint controls and policy become especially important.

| Feature | Full Tunnel | Split Tunnel |
|---|---|---|
| Internet traffic path | Through organization | Through local Internet |
| Central inspection | Greater | Reduced for local traffic |
| VPN bandwidth use | Higher | Lower |
| Typical latency | May be higher | Often lower for public cloud/SaaS |
| Endpoint security importance | High | Especially high |

The correct choice depends on risk, bandwidth, regulatory requirements, and application architecture.

## 23.10 IPsec Fundamentals

Internet Protocol Security, or IPsec, is a suite of standards used to protect IP communication. It is widely used for site-to-site VPNs and can also support remote access.

IPsec is not one encryption algorithm or one protocol. It is a framework that combines:

- Peer authentication
- Security parameter negotiation
- Key establishment
- Confidentiality
- Integrity
- Anti-replay protection

### 23.10.1 Security Association

A Security Association, or SA, is a set of agreed security parameters used to protect traffic in one direction. Because an SA is unidirectional, normal two-way communication requires separate inbound and outbound SAs.

An SA can define algorithms, keys, lifetime, mode, and protected traffic. Security associations are replaced periodically so that one key is not used indefinitely.

### 23.10.2 IPsec Protocol Numbers and Supporting Ports

| Function | Protocol/Port |
|---|---|
| ESP | IP protocol 50 |
| AH | IP protocol 51 |
| IKE | UDP 500 |
| NAT Traversal | UDP 4500 |

ESP and AH are IP protocols, not TCP or UDP ports. This distinction is frequently tested.

## 23.11 Encapsulating Security Payload

Encapsulating Security Payload, or ESP, is the primary IPsec protocol used in modern VPNs. ESP can provide:

- Confidentiality through encryption
- Integrity
- Data-origin authentication
- Anti-replay protection

ESP does not encrypt the new outer IP header in tunnel mode because routers need that header to forward the packet across the Internet.

## 23.12 Authentication Header

Authentication Header, or AH, provides integrity, data-origin authentication, and anti-replay protection, but it does not encrypt the payload.

AH also protects selected IP-header fields. NAT changes IP header information, which makes AH incompatible with normal NAT operation. ESP is therefore much more common in practical VPN deployments.

## 23.13 Transport Mode and Tunnel Mode

### 23.13.1 Transport Mode

Transport mode protects the upper-layer payload of the original IP packet while retaining the original IP header. It is commonly associated with host-to-host protection.

```text
[Original IP header][Protected transport data]
```

### 23.13.2 Tunnel Mode

Tunnel mode protects the entire original IP packet and adds a new outer IP header. It is commonly used between VPN gateways.

```text
[New IP header][IPsec information][Protected original IP packet]
```

| Feature | Transport Mode | Tunnel Mode |
|---|---|---|
| Original IP header | Remains outer header | Protected inside tunnel |
| New outer IP header | No | Yes |
| Common use | Host-to-host | Gateway-to-gateway, remote access |
| Overhead | Lower | Higher |

## 23.14 Internet Key Exchange

Internet Key Exchange, or IKE, negotiates IPsec security parameters and establishes keys. Rather than manually configuring every short-lived encryption key, peers use IKE to authenticate and derive shared session keys securely.

### 23.14.1 IKEv1 and IKEv2

IKEv2 is newer, more efficient, and generally preferred where supported. It uses fewer exchanges, handles mobility and address changes more effectively, and simplifies negotiation compared with IKEv1.

At a conceptual level:

1. The peers agree on cryptographic algorithms.
2. They perform a key exchange.
3. They authenticate one another.
4. They create an IKE SA.
5. They negotiate child SAs used to protect application traffic.

Students should understand the process and verification logic before memorizing vendor-specific syntax.

## 23.15 Cryptographic Building Blocks

### 23.15.1 Symmetric Encryption

Symmetric encryption uses a shared secret key for encryption and decryption. It is efficient for protecting large amounts of VPN data. AES is a widely used example.

### 23.15.2 Asymmetric Cryptography

Asymmetric cryptography uses a public key and a private key. It supports digital signatures, certificates, and secure identity verification. It is computationally heavier than symmetric encryption, so VPNs commonly use asymmetric methods during establishment and symmetric keys for the data session.

### 23.15.3 Hashing and Integrity

A cryptographic hash produces a fixed-length digest from input data. Integrity mechanisms such as HMAC combine a hash function with a secret key to detect modification and authenticate the source of protected data.

### 23.15.4 Diffie-Hellman Key Exchange

Diffie-Hellman allows two peers to derive shared key material across an untrusted network without transmitting the resulting shared secret directly. Strong, supported groups should be selected according to current organizational policy.

### 23.15.5 Perfect Forward Secrecy

Perfect Forward Secrecy, or PFS, generates fresh key material for new security associations. Compromise of one long-term key should not automatically reveal previously protected sessions.

## 23.16 NAT Traversal

Traditional IPsec can experience problems when a NAT device changes packet addressing. NAT Traversal, or NAT-T, encapsulates IPsec ESP traffic inside UDP, commonly using port 4500.

```text
Original ESP packet
        |
NAT is detected
        |
ESP is carried inside UDP 4500
        |
NAT device can maintain the translation
```

Firewalls along the path may need to allow UDP 500 for IKE and UDP 4500 for NAT-T. Opening only TCP 443 does not automatically permit a traditional IPsec tunnel.

## 23.17 Interesting Traffic and VPN Policy

In policy-based IPsec designs, "interesting traffic" means traffic selected for VPN protection. ACL-like rules may identify the local and remote protected subnets.

For example:

```text
Local protected subnet:  192.168.10.0/24
Remote protected subnet: 192.168.20.0/24
```

The peer configurations must agree. If one side defines `/24` and the other defines only one host, the tunnel may establish partially or fail to pass expected traffic.

Interesting-traffic classification is not necessarily the same as a firewall permission. A crypto policy identifies what should be encrypted; a security policy determines what is allowed. Both must be correct.

## 23.18 Policy-Based and Route-Based VPNs

### Policy-Based VPN

A policy-based VPN selects protected traffic through policy entries or crypto ACLs. It is straightforward for a small number of subnet pairs but becomes difficult to manage as networks grow.

### Route-Based VPN

A route-based VPN uses a logical tunnel interface. Normal routing sends destination networks toward that interface. It can simplify dynamic routing, redundancy, and many-network designs.

| Feature | Policy-Based | Route-Based |
|---|---|---|
| Traffic selection | Crypto policy/ACL | Routing table |
| Logical tunnel interface | Usually no | Yes |
| Scalability | Best for simpler pairs | Better for complex topology |
| Dynamic routing | More difficult | Commonly supported |
| Troubleshooting focus | Selectors and policy | Routes, interface, and SAs |

Platform terminology and implementation vary, so engineers must consult the applicable vendor design.

## 23.19 VPN Routing, NAT, DNS, and MTU

A tunnel can be established while applications still fail. The protected data path also depends on routing, NAT, DNS, and packet size.

### Routing

Each side needs a route to the remote protected network. Remote-access clients need routes for full or split tunneling. Overlapping subnets create ambiguity: if a home user's LAN and the company both use `192.168.1.0/24`, the endpoint may send traffic to the wrong interface.

### NAT

Site-to-site protected traffic is often exempted from normal Internet PAT. If the source is translated before VPN selection, the traffic may no longer match the expected protected subnet.

### DNS

Remote clients may require internal DNS servers and search suffixes. A tunnel can pass IP traffic while users report failure because internal names do not resolve.

### MTU and Fragmentation

VPN encapsulation adds headers and increases packet size. A packet that fit the physical interface MTU before encryption may become too large afterward. Symptoms can include small pings working while large transfers, web pages, or applications fail. Path MTU Discovery, TCP MSS adjustment, and correct ICMP handling may be relevant.

## 23.20 Remote Access Authentication and Authorization

Passwords alone are weak protection for Internet-facing remote access. Multifactor authentication, or MFA, requires evidence from more than one factor category:

| Factor | Example |
|---|---|
| Something you know | Password or PIN |
| Something you have | Token, phone, smart card |
| Something you are | Fingerprint or other biometric |

Two passwords are not two factors because both are knowledge factors.

Remote access can integrate with RADIUS, directory services, certificates, identity providers, and conditional-access systems. Authorization should map users to only the resources required by their role.

Examples:

- Finance users may reach the finance application.
- Help desk may reach approved support tools.
- Contractors may reach one project subnet during defined hours.
- Network administrators may reach management systems through a separate privileged policy.

## 23.21 Network Access Control

Network Access Control, or NAC, is a framework for deciding whether a user or device may connect and what level of network access it should receive.

VPN authentication answers, "Is this identity allowed to establish a session?" NAC expands the decision:

```text
Who is the user?
What device is being used?
Is the device managed?
Does it meet security policy?
Where and how is it connecting?
What access should it receive?
```

### 23.21.1 NAC Components

| Component | Role |
|---|---|
| Endpoint/supplicant | Requests access and may report posture |
| Enforcement point | Switch, WLAN controller, or VPN gateway |
| Policy server | Evaluates identity, device, posture, and policy |
| Identity store | Directory or identity provider |
| Posture service | Checks endpoint compliance |
| Remediation service | Helps noncompliant devices become compliant |

### 23.21.2 Pre-Admission and Post-Admission Control

Pre-admission control evaluates the endpoint before normal access is granted. Post-admission control continues monitoring after connection and can change access if risk or compliance changes.

### 23.21.3 Endpoint Posture

Posture checks may assess:

- Supported operating-system version
- Required security updates
- Active endpoint protection
- Host firewall status
- Disk encryption
- Device certificate
- Mobile-device-management enrollment
- Indicators that the device is rooted or jailbroken

Posture data must be collected with clear privacy, legal, and operational policy.

### 23.21.4 Enforcement Outcomes

NAC does not only allow or deny. It may:

- Grant normal role-based access
- Assign a VLAN or downloadable ACL
- Place the device in a restricted network
- Redirect it to remediation
- Allow guest Internet access only
- Quarantine a risky endpoint
- Terminate an existing session

## 23.22 VPN Security Risks and Controls

| Risk | Control |
|---|---|
| Stolen password | MFA, risk-based login, account monitoring |
| Rogue gateway | Certificate validation and trusted configuration |
| Infected remote endpoint | EDR, posture checks, least privilege |
| Excessive remote access | Role-based authorization and ACLs |
| Weak cryptography | Approved algorithms and lifecycle management |
| Shared pre-shared key | Unique certificates or carefully managed secrets |
| Unpatched VPN gateway | Vulnerability management and timely updates |
| Brute-force attempts | MFA, rate limits, lockout policy, monitoring |
| Split-tunnel exposure | Endpoint firewall, DNS/web protection, EDR |
| Forgotten contractor account | Expiration, sponsorship, access review |

VPN gateways are Internet-facing security devices and attractive attack targets. They require hardening, patching, restricted administration, configuration backup, central logging, and continuous monitoring.

## 23.23 Site-to-Site Enterprise Design Example

A company has:

```text
Lagos HQ:   10.10.0.0/16
Abuja site: 10.20.0.0/16
```

Each site has an Internet connection and an edge firewall. The design process is:

1. Confirm that private address spaces do not overlap.
2. Define approved subnet and application flows.
3. Select compatible IKE/IPsec settings.
4. Choose certificates or strong unique peer credentials.
5. Configure protected-network selectors or tunnel routing.
6. Exempt protected traffic from Internet PAT where required.
7. Permit IKE, NAT-T, and ESP as needed.
8. Apply firewall policy inside the tunnel.
9. Configure redundant monitoring and logging.
10. Test failover, performance, rekeying, and recovery.

The tunnel should not automatically allow every HQ device to reach every branch device. Segmentation and least privilege remain necessary.

## 23.24 Remote-Worker Enterprise Design Example

A company supports staff using managed Windows laptops. The remote-access design requires:

- Company-issued device certificate
- User credentials and MFA
- Endpoint protection and disk encryption
- Automatic VPN profile
- Internal DNS and approved routes
- Role-based access
- Session timeout and reauthentication
- Central authentication and VPN logs
- Help-desk recovery procedure

A Finance employee receives access to finance services. A contractor receives only a project application. A failed posture check places the device into remediation rather than unrestricted production access.

This design verifies identity, device trust, and business need instead of treating possession of a password as sufficient.

## 23.25 Windows VPN and Route Verification

Windows includes built-in VPN support, and organizations may deploy vendor clients.

Useful PowerShell commands:

```powershell
Get-VpnConnection
Get-NetIPConfiguration
Get-NetRoute
Get-DnsClientServerAddress
Test-NetConnection 10.20.30.10 -Port 443
Resolve-DnsName intranet.example.local
tracert 10.20.30.10
```

`Get-VpnConnection` shows configured Windows VPN profiles. `Get-NetRoute` reveals whether a protected destination uses the VPN interface. `Test-NetConnection` tests a specific application port. Name-resolution tests determine whether the problem is DNS rather than the tunnel.

## 23.26 Linux VPN and Route Verification

Linux clients may use NetworkManager, strongSwan, OpenVPN, WireGuard, or vendor software depending on organizational design.

Useful commands:

```bash
ip address
ip route
ip route get 10.20.30.10
resolvectl status
ping -c 4 10.20.30.10
tracepath 10.20.30.10
ss -tulpen
journalctl -u NetworkManager
```

For an IPsec implementation, platform-specific commands may display IKE and child SAs. Engineers must avoid exposing keys or sensitive configuration in tickets and screenshots.

## 23.27 Cisco IOS Conceptual Verification

Exact commands depend on platform and configuration style. Common IOS/IKEv2 and IPsec verification commands include:

```cisco
show crypto ikev2 sa
show crypto ipsec sa
show crypto session
show access-lists
show ip route
show ip nat translations
show logging
```

Important evidence includes:

- Peer address
- IKE SA state
- IPsec SA state
- Encapsulation and decapsulation counters
- Authentication or negotiation errors
- Selected protected networks
- Routes to the destination
- NAT behavior

Rising encapsulation but zero decapsulation may indicate that packets leave but no protected return traffic arrives. Counters are evidence, not a complete diagnosis.

## 23.28 VPN Troubleshooting Method

Troubleshoot in layers.

### Stage 1: Underlay Reachability

Can each VPN endpoint reach the other's public address? Check interfaces, public addressing, ISP service, routing, and upstream filtering.

### Stage 2: IKE Negotiation

Do the peers agree on version, algorithms, authentication, identity, and credentials? Check clock accuracy and certificate validity.

### Stage 3: IPsec Security Associations

Do protected-traffic selectors, transforms, and lifetimes agree? Is NAT-T required? Are ESP or UDP 4500 permitted?

### Stage 4: Protected Data Path

Check routes, NAT exemption, firewall policy, ACLs, encryption/decryption counters, and return routes.

### Stage 5: Application Services

Check DNS, required ports, server policy, endpoint firewall, MTU, and application authentication.

| Symptom | Likely Investigation |
|---|---|
| Gateway unreachable | Internet, route, DNS, upstream firewall |
| Authentication fails | Credentials, MFA, certificate, AAA |
| IKE up but no IPsec SA | Selectors, transforms, policy mismatch |
| Tunnel up but no traffic | Routes, NAT, ACL, firewall, return path |
| One subnet works | Missing route or selector for other subnet |
| IP works but name fails | VPN DNS settings or DNS reachability |
| Small traffic works, large fails | MTU, fragmentation, blocked ICMP |
| Disconnects regularly | Rekey/lifetime mismatch, unstable link |
| Remote user reaches too much | Authorization or split-tunnel policy |

## 23.29 PRACTICAL LABS

### Lab 1: Site-to-Site VPN Design Worksheet

Given two sites, document:

- Public peer addresses
- Local and remote protected subnets
- IKE version
- Authentication method
- Encryption and integrity policy
- NAT exemption requirement
- Firewall requirements
- Verification commands
- Rollback and escalation plan

Draw both the outer public packet path and the inner protected packet path.

### Lab 2: Packet Tracer Site-to-Site VPN

Where the Packet Tracer version supports IPsec:

1. Build two LANs separated by an Internet router.
2. Verify normal underlay reachability.
3. Configure compatible IKE and IPsec policy on both gateways.
4. Define matching protected subnets.
5. Generate interesting traffic.
6. Verify tunnel state and packet counters.
7. Break one parameter and diagnose the failure.

If full VPN commands are unavailable, complete the topology, routing, ACL classification, design table, and expected verification output as a guided simulation.

### Lab 3: Remote-Access Policy Design

Create three user roles: employee, contractor, and administrator. For each role, define authentication, MFA, posture, permitted resources, split/full-tunnel policy, session timeout, and logging.

The goal is to show that successful authentication does not mean unrestricted authorization.

### Lab 4: Client Troubleshooting

Using Windows or Linux route and DNS commands:

1. Record routes before connection.
2. Connect to an available lab VPN or use a supplied sample output.
3. Record the new interface, address, routes, and DNS servers.
4. Test a protected IP and hostname.
5. Determine whether the design uses full or split tunneling.
6. Diagnose a provided route, DNS, or MTU fault.

## 23.30 Cybersecurity Relevance

VPNs reduce exposure of data in transit, but they can also create an authenticated path around perimeter controls. A compromised remote endpoint may use that path to reach internal systems. Therefore, modern remote access combines encryption with identity, MFA, endpoint detection, posture, segmentation, least privilege, and monitoring.

Security teams monitor unusual countries, impossible travel, repeated MFA failures, new devices, excessive session duration, abnormal data transfer, and access outside a user's role.

Zero Trust does not mean that VPNs disappear. It means network location or tunnel establishment alone should not create unlimited trust. Access decisions should consider identity, device, resource, and context.

## 23.31 Cloud Networking Relevance

Cloud providers commonly offer managed site-to-site VPN gateways and remote-access services. A hybrid design may connect an office firewall to a cloud virtual network.

Cloud VPN design still requires:

- Non-overlapping address plans
- Customer and cloud gateway configuration
- Static or dynamic routing
- Redundant tunnels
- Security groups and network filtering
- Route-table updates
- Monitoring and logs
- Bandwidth and availability planning

Route-based VPNs and BGP are common in resilient hybrid designs. Encryption does not replace cloud security groups, IAM, or workload hardening.

## 23.32 IT Support, Interview, and Exam Relevance

IT support staff frequently diagnose failed authentication, missing routes, wrong DNS, expired certificates, MFA problems, and endpoint posture failures. Network engineers troubleshoot peer negotiation, routing, NAT, SAs, and performance. Cybersecurity teams review remote access policy and logs.

Common interview questions include:

- Site-to-site versus client-to-site VPN
- Full tunnel versus split tunnel
- Tunneling versus encryption
- ESP versus AH
- Tunnel mode versus transport mode
- IKE, SAs, NAT-T, and PFS
- Why a tunnel can be up while applications fail
- How NAC evaluates identity and posture

### CCNA 200-301 and Network+ N10-009 Reminders

- A VPN is a protected logical connection across an untrusted network.
- Site-to-site connects networks; client-to-site connects an endpoint.
- ESP commonly provides confidentiality, integrity, authentication, and anti-replay.
- AH does not encrypt and is not NAT-friendly.
- Tunnel mode protects the original IP packet and adds a new outer header.
- IKE negotiates parameters, authenticates peers, and establishes keys.
- IKE commonly uses UDP 500; NAT-T commonly uses UDP 4500.
- ESP is IP protocol 50, not TCP or UDP port 50.
- Full tunnel sends general traffic through the organization; split tunnel separates protected and local Internet traffic.
- NAC considers identity, device, posture, context, and required access.
- MFA must use different factor categories.

## 24. KEY TERMS / GLOSSARY

| Term | Definition |
|---|---|
| VPN | Protected logical connection across an untrusted network |
| Tunnel | Logical path created by encapsulating traffic |
| Encapsulation | Placing one packet inside another |
| Encryption | Transformation of plaintext into protected ciphertext |
| Ciphertext | Encrypted, unreadable form of data |
| Peer Authentication | Verification of the remote VPN endpoint |
| Anti-Replay | Protection against retransmission of captured valid packets |
| Site-to-Site VPN | VPN connecting two or more networks through gateways |
| Client-to-Site VPN | VPN connecting one endpoint to an organization |
| Remote Access | Connectivity for users or devices outside the local site |
| VPN Concentrator | Device or service terminating many VPN sessions |
| Full Tunnel | Policy sending most or all client traffic through the VPN |
| Split Tunnel | Policy sending only selected traffic through the VPN |
| IPsec | Standards framework for protecting IP communication |
| SA | Security Association containing negotiated protection parameters |
| ESP | IPsec protocol providing encryption and optional integrity/authentication |
| AH | IPsec protocol providing integrity/authentication without encryption |
| Tunnel Mode | IPsec mode protecting the entire original IP packet |
| Transport Mode | IPsec mode protecting the upper-layer payload |
| IKE | Protocol for negotiating IPsec security and keys |
| IKEv2 | Modern version of Internet Key Exchange |
| Symmetric Encryption | Encryption using the same secret key for encryption and decryption |
| Asymmetric Cryptography | Cryptography using related public and private keys |
| Digital Certificate | Signed electronic credential binding identity to a public key |
| PKI | System for issuing, validating, and revoking certificates |
| HMAC | Keyed integrity and authentication mechanism based on hashing |
| Diffie-Hellman | Method for deriving shared key material across an untrusted network |
| PFS | Perfect Forward Secrecy; fresh key material for new sessions |
| NAT-T | NAT Traversal; carries IPsec ESP inside UDP 4500 |
| Interesting Traffic | Traffic selected for VPN protection |
| Policy-Based VPN | VPN selecting traffic through crypto policy |
| Route-Based VPN | VPN using a logical tunnel interface and routing |
| MFA | Authentication using more than one factor category |
| NAC | Network Access Control framework |
| Posture Assessment | Evaluation of endpoint compliance and security state |
| Remediation Network | Restricted access used to correct compliance problems |
| Quarantine | Isolation of a risky or noncompliant endpoint |

## 25. COMPARISON TABLES

### 25.1 Site-to-Site vs Client-to-Site

| Feature | Site-to-Site | Client-to-Site |
|---|---|---|
| Connects | Networks | Individual endpoint |
| Tunnel endpoints | VPN gateways | Client and gateway |
| User action | Usually none | Client/user normally connects |
| Main identity | Peer gateway | User and often device |
| Typical use | Branch or cloud link | Remote worker |

### 25.2 ESP vs AH

| Feature | ESP | AH |
|---|---|---|
| Encryption | Yes, when configured | No |
| Integrity/authentication | Supported | Supported |
| NAT compatibility | Supported through NAT-T | Poor |
| Practical use | Common | Rare |

### 25.3 Tunnel vs Transport Mode

| Feature | Tunnel | Transport |
|---|---|---|
| Protects original IP header | Yes, encapsulated inside | No |
| Adds new IP header | Yes | No |
| Common use | Gateway VPN | Host-to-host |

### 25.4 Full vs Split Tunnel

| Feature | Full | Split |
|---|---|---|
| Public Internet path | Company gateway | Local gateway |
| Central inspection | Greater | Lower |
| VPN bandwidth | Higher | Lower |
| Endpoint dependency | High | Especially high |

### 25.5 VPN vs NAC

| Feature | VPN | NAC |
|---|---|---|
| Primary purpose | Protected connectivity | Access decision and enforcement |
| Core question | How is traffic protected? | Who/what should receive which access? |
| Typical inputs | Peer/user identity, crypto policy | Identity, device, posture, context |
| Relationship | Carries authorized remote traffic | May decide remote-access permission |

## 26. REAL-WORLD ANALOGY

A VPN tunnel is like an armored delivery vehicle traveling on public roads. The public road remains shared, but the contents are protected. The outer address tells the road system where the vehicle must go; the protected package inside contains the original destination information.

Authentication checks the driver and receiving facility. Encryption locks the cargo. Integrity seals reveal tampering. Anti-replay rejects a copied delivery ticket. NAC is the security checkpoint that also inspects the driver, vehicle condition, authorization, and destination before deciding whether entry should be normal, restricted, or denied.

## 27. QUICK-RECAP CHEAT SHEET

```text
VPN = protected logical connection across an untrusted network

SITE-TO-SITE
- Gateway to gateway
- Connects entire networks
- Transparent to end devices

CLIENT-TO-SITE
- Endpoint to gateway
- Remote user/device authentication
- Requires strong endpoint controls

IPSEC
- ESP: protocol 50; encryption + security services
- AH: protocol 51; no encryption; NAT problems
- IKE: UDP 500
- NAT-T: UDP 4500
- SA: one-way negotiated protection parameters
- Tunnel mode: protects complete original packet
- Transport mode: protects upper-layer payload

REMOTE ACCESS
- Full tunnel: most/all traffic through company
- Split tunnel: company traffic through VPN, Internet local
- Use MFA, certificates, least privilege, logging

NAC
- Evaluates user, device, posture, location, and context
- Outcomes: permit, restrict, remediate, quarantine, deny

TROUBLESHOOT
1. Underlay/public reachability
2. IKE negotiation
3. IPsec SAs
4. Routes, NAT, ACLs, counters
5. DNS, ports, MTU, application
```

## 28. REVIEW QUESTIONS

1. What is a VPN?
2. Why does a VPN not make the Internet itself private?
3. Name four security services a VPN can provide.
4. What is the difference between tunneling and encryption?
5. Compare site-to-site and client-to-site VPNs.
6. Why is endpoint security especially important for remote access?
7. Compare full tunneling and split tunneling.
8. What is IPsec?
9. What is a Security Association?
10. Why are at least two SAs required for two-way protected traffic?
11. What security services can ESP provide?
12. Why is AH uncommon with NAT?
13. Compare IPsec tunnel mode and transport mode.
14. What is the purpose of IKE?
15. Why is symmetric encryption used for VPN data transfer?
16. What does Diffie-Hellman accomplish?
17. What is Perfect Forward Secrecy?
18. What is NAT-T and which port does it commonly use?
19. What does "interesting traffic" mean?
20. Compare policy-based and route-based VPNs.
21. Why can overlapping subnets break remote access?
22. How can VPN overhead create an MTU problem?
23. Why are two passwords not multifactor authentication?
24. What is NAC?
25. What is endpoint posture assessment?
26. Give four possible NAC enforcement outcomes.
27. Why should VPN authorization remain least-privileged after authentication?
28. Which evidence should be checked when a tunnel is up but traffic fails?
29. Why are VPN gateways high-value security targets?
30. Explain the five-stage VPN troubleshooting method.

## 29. SUGGESTED ANSWER GUIDE

1. A VPN is a protected logical connection across an untrusted network.
2. It protects selected communication through a tunnel; the underlying Internet remains public and shared.
3. Confidentiality, integrity, authentication, anti-replay, and authorization are valid examples.
4. Tunneling encapsulates traffic to create a logical path; encryption makes content unreadable without the key.
5. Site-to-site joins networks through gateways; client-to-site joins one endpoint to an organization's gateway.
6. The endpoint operates outside physical control and may be unmanaged, unpatched, or compromised.
7. Full tunnel sends most traffic through the organization's gateway; split tunnel sends only selected traffic through it.
8. IPsec is a standards framework for protecting IP traffic through authentication, key management, encryption, integrity, and anti-replay services.
9. An SA is a one-direction set of negotiated security parameters and keys.
10. Each SA protects one direction, so inbound and outbound traffic require separate SAs.
11. Confidentiality, integrity, data-origin authentication, and anti-replay protection.
12. AH protects header fields that NAT changes, causing validation to fail.
13. Tunnel mode protects the entire original packet and adds an outer header; transport mode protects the upper-layer payload.
14. IKE negotiates security settings, authenticates peers, performs key exchange, and establishes SAs.
15. It is computationally efficient for large volumes of session data.
16. It allows peers to derive shared key material without directly transmitting the resulting secret.
17. PFS uses fresh key material so compromise of one key does not automatically reveal earlier sessions.
18. NAT-T carries ESP inside UDP so it can cross NAT, commonly using UDP 4500.
19. It is traffic selected by policy for VPN protection.
20. Policy-based VPNs use selectors or crypto ACLs; route-based VPNs use a tunnel interface and routing.
21. The endpoint cannot unambiguously decide whether the same prefix is local or remote.
22. Added VPN headers can make packets exceed the path MTU, causing fragmentation or loss.
23. Both are the same knowledge-factor category.
24. NAC is a framework that evaluates identity, device, posture, and context to assign network access.
25. It checks whether an endpoint meets security requirements such as updates, protection, and encryption.
26. Permit, role-based restriction, remediation, guest-only access, quarantine, and deny are valid examples.
27. Establishing identity does not prove that every internal resource is required for the user's role.
28. Check routes, NAT, firewall/ACL policy, selectors, packet counters, return path, DNS, ports, and MTU.
29. They are Internet-facing and provide authenticated pathways toward protected resources.
30. Verify underlay reachability, IKE negotiation, IPsec SAs, protected routing/NAT/policy, and finally DNS/MTU/application services.
