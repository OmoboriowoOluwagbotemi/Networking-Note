# LESSON 17: HOW ROUTERS WORK, STATIC AND DEFAULT ROUTING

## DEFINITION AND TECHNICAL IN-DEPTH KNOWLEDGE

### 17.1 What Is Routing?

Routing is the process of forwarding packets from one IP network to another. A router receives a packet, examines the destination IP address, checks its routing table, selects the best matching route, and forwards the packet toward the destination.

In Lesson 16, inter-VLAN routing introduced the idea that devices in different VLANs need Layer 3 routing to communicate. A host sends remote traffic to its default gateway. That gateway may be a router subinterface, firewall interface, or Layer 3 switch SVI. Lesson 17 expands that idea beyond VLANs and explains how routers make forwarding decisions across many networks.

Routing exists because the world is not one flat IP network. An enterprise may have multiple VLANs, branch offices, data centers, cloud networks, VPN users, internet links, and service provider connections. Each network has its own IP prefix. Routers connect those networks and decide where traffic should go.

At Layer 2, switches forward Ethernet frames using MAC addresses. At Layer 3, routers forward IP packets using destination IP addresses and routing tables. The router removes the incoming Layer 2 frame, keeps the Layer 3 packet, makes a routing decision, and then encapsulates the packet into a new Layer 2 frame for the next hop.

For CCNA and CompTIA Network+, students must understand routing tables, connected routes, static routes, default routes, administrative distance, longest-prefix match, route selection, and floating static routes.

### 17.2 Why Routing Matters

Routing matters because almost every enterprise service depends on traffic crossing networks. A staff PC may need to reach a server VLAN. A branch office may need to reach headquarters. A company firewall may need to send internet traffic to an ISP. A cloud VPN may need to route traffic between an office subnet and a cloud subnet. If routing is wrong, the physical network may be working but applications still fail.

Routing also matters for troubleshooting. When a host can reach its gateway but not a remote network, the next question is often: does the router know how to reach the destination, and does the return path exist? Many beginners test only one direction, but routing must work both ways. A packet must reach the destination, and the reply must return.

Routing is also a security and design topic. A route can make a network reachable. A missing route can isolate a network. A wrong default route can send traffic to the wrong place. A broad route can expose more networks than intended. Firewalls and ACLs control traffic, but routing determines whether a path exists.

## 17.3 How Routers Forward Packets

A router forwards packets by following a structured process.

First, the router receives a frame on an interface. The frame is a Layer 2 container, such as an Ethernet frame. The router checks whether the frame is addressed to its local interface MAC address or accepted Layer 2 destination.

Second, the router removes the Layer 2 header and trailer. This is decapsulation at Layer 2. The router then examines the Layer 3 IP packet.

Third, the router reads the destination IP address in the packet.

Fourth, the router checks the routing table for the best matching route.

Fifth, the router identifies the outgoing interface and next-hop address.

Sixth, the router builds a new Layer 2 frame for the next link. If the next link is Ethernet, the router may use ARP for IPv4 or Neighbor Discovery for IPv6 to find the next-hop MAC address.

Seventh, the router forwards the new frame out the selected interface.

Router Forwarding Process

| Step | Router Action |
|---:|---|
| 1 | Receives Layer 2 frame |
| 2 | Removes Layer 2 header/trailer |
| 3 | Reads destination IP address |
| 4 | Searches routing table |
| 5 | Selects best route |
| 6 | Identifies next hop and outgoing interface |
| 7 | Re-encapsulates packet into new Layer 2 frame |
| 8 | Forwards frame out selected interface |

This is why MAC addresses change at every routed hop, while the source and destination IP addresses usually remain the same unless NAT is used.

## 17.4 Routing Table Components

A routing table is the database a router uses to decide where to forward packets. It contains routes to networks and instructions for reaching them.

On Cisco IOS, a routing table may be viewed with:

```text
show ip route
```

A route usually contains:

- Route source or code.
- Destination network/prefix.
- Administrative distance.
- Metric.
- Next-hop address.
- Outgoing interface.

Example route:

```text
S    192.168.50.0/24 [1/0] via 10.0.0.2
```

This means:

| Part | Meaning |
|---|---|
| `S` | Static route |
| `192.168.50.0/24` | Destination network |
| `[1/0]` | Administrative distance 1, metric 0 |
| `via 10.0.0.2` | Next-hop IP address |

Another example:

```text
C    192.168.10.0/24 is directly connected, GigabitEthernet0/0
L    192.168.10.1/32 is directly connected, GigabitEthernet0/0
```

`C` means connected route. `L` means local route for the router's own interface IP address.

Common Cisco Route Codes

| Code | Meaning |
|---|---|
| `C` | Connected route |
| `L` | Local route |
| `S` | Static route |
| `R` | RIP route |
| `O` | OSPF route |
| `D` | EIGRP route |
| `B` | BGP route |

Dynamic routing protocols will be introduced in Lesson 18. In this lesson, the focus is connected, local, static, default, and floating static routes.

## 17.5 Connected and Local Routes

A connected route is automatically added to the routing table when a router interface has an IP address and is up/up. It represents the network directly attached to that interface.

Example:

```text
interface gigabitEthernet 0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
```

The router adds:

```text
C 192.168.10.0/24 is directly connected, GigabitEthernet0/0
L 192.168.10.1/32 is directly connected, GigabitEthernet0/0
```

The connected route tells the router that the `192.168.10.0/24` network is directly reachable through `G0/0`. The local route identifies the router's own interface address.

Connected routes matter because they are the foundation of routing. A router knows directly connected networks automatically, but it does not automatically know remote networks unless a route is configured or learned.

## 17.6 Static Routes

A static route is a route manually configured by an administrator. Static routes tell the router how to reach a network that is not directly connected.

Static routes exist because some networks are simple enough that manual routing is practical. A small branch router may need only a default route to the ISP. A lab router may need a few static routes. A firewall may use static routes to reach internal networks. Static routes are predictable and do not require a dynamic routing protocol.

Basic Cisco IOS static route syntax:

```text
ip route <destination-network> <subnet-mask> <next-hop-ip>
```

Example:

```text
ip route 192.168.50.0 255.255.255.0 10.0.0.2
```

This tells the router:

```text
To reach 192.168.50.0/24, send traffic to next-hop 10.0.0.2.
```

Static route using outgoing interface:

```text
ip route 192.168.50.0 255.255.255.0 gigabitEthernet 0/1
```

Static route using both next hop and outgoing interface:

```text
ip route 192.168.50.0 255.255.255.0 gigabitEthernet 0/1 10.0.0.2
```

In Ethernet networks, using a next-hop IP address is usually preferred because the router can resolve the next hop properly. Point-to-point links may use outgoing interface syntax more safely.

Static Route Components

| Component | Example | Purpose |
|---|---|---|
| Destination network | `192.168.50.0` | Remote network to reach |
| Subnet mask | `255.255.255.0` | Defines destination prefix |
| Next hop | `10.0.0.2` | Router to forward traffic to |
| Outgoing interface | `G0/1` | Interface used to send traffic |

## 17.7 Static Route Example

Consider two routers.

```text
LAN A --- R1 --- 10.0.0.0/30 --- R2 --- LAN B
```

Addressing:

| Network | Details |
|---|---|
| LAN A | 192.168.10.0/24 |
| R1 LAN IP | 192.168.10.1 |
| R1 WAN IP | 10.0.0.1/30 |
| R2 WAN IP | 10.0.0.2/30 |
| R2 LAN IP | 192.168.20.1 |
| LAN B | 192.168.20.0/24 |

R1 knows `192.168.10.0/24` and `10.0.0.0/30` because they are connected. R1 does not automatically know `192.168.20.0/24`.

Configure R1:

```text
ip route 192.168.20.0 255.255.255.0 10.0.0.2
```

R2 knows `192.168.20.0/24` and `10.0.0.0/30` because they are connected. R2 does not automatically know `192.168.10.0/24`.

Configure R2:

```text
ip route 192.168.10.0 255.255.255.0 10.0.0.1
```

This creates two-way reachability.

Important troubleshooting rule:

```text
Routing must work in both directions.
```

If R1 has a route to LAN B but R2 has no route back to LAN A, the ping may fail because the reply cannot return.

## 17.8 Default Routes

A default route is a route used when no more specific route matches the destination. It is often called the gateway of last resort.

Default route syntax in IPv4:

```text
ip route 0.0.0.0 0.0.0.0 <next-hop-ip>
```

Example:

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

This tells the router:

```text
If you do not have a more specific route, send the packet to 203.0.113.1.
```

Default routes are common at the internet edge. A branch router may not need routes for every internet destination. It can send unknown destinations to the ISP using a default route.

Example:

```text
Branch LAN -> Branch Router -> ISP Router -> Internet
```

The branch router may have:

```text
ip route 0.0.0.0 0.0.0.0 <ISP-next-hop>
```

Default Route Summary

| Feature | Description |
|---|---|
| IPv4 default network | `0.0.0.0` |
| IPv4 default mask | `0.0.0.0` |
| CIDR notation | `0.0.0.0/0` |
| Purpose | Match all destinations not matched by a better route |
| Common use | Internet edge, branch routers, stub networks |

For IPv6, the default route is:

```text
ipv6 route ::/0 <next-hop-ipv6>
```

## 17.9 Routing Table Lookup and Longest-Prefix Match

When a router receives a packet, it chooses the most specific matching route. This is called longest-prefix match.

Longest-prefix match means that if multiple routes match the destination IP address, the router chooses the route with the longest prefix length, because it is the most specific.

Example routing table:

| Route | Meaning |
|---|---|
| `0.0.0.0/0` | Default route |
| `10.0.0.0/8` | Broad route for 10.x.x.x |
| `10.10.0.0/16` | More specific route |
| `10.10.20.0/24` | Most specific route |

If the destination is:

```text
10.10.20.55
```

All four routes may match, but the router chooses:

```text
10.10.20.0/24
```

because `/24` is the longest prefix.

Longest-Prefix Match Example

| Destination IP | Matching Routes | Chosen Route |
|---|---|---|
| 10.10.20.55 | `/0`, `/8`, `/16`, `/24` | `10.10.20.0/24` |
| 10.10.99.5 | `/0`, `/8`, `/16` | `10.10.0.0/16` |
| 10.50.1.10 | `/0`, `/8` | `10.0.0.0/8` |
| 8.8.8.8 | `/0` | `0.0.0.0/0` |

This rule is extremely important. A default route is used only when no more specific route exists.

## 17.10 Administrative Distance

Administrative distance, or AD, is a trust value used by Cisco routers to choose between routes to the same destination learned from different sources.

Lower administrative distance is preferred.

Example:

```text
Static route to 192.168.50.0/24
OSPF route to 192.168.50.0/24
```

If both routes describe the exact same prefix, the router compares administrative distance. A static route normally has AD 1. OSPF normally has AD 110. The static route is preferred because 1 is lower than 110.

Common Administrative Distance Values

| Route Source | Administrative Distance |
|---|---:|
| Connected | 0 |
| Static | 1 |
| EIGRP summary | 5 |
| External BGP | 20 |
| Internal EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |
| External EIGRP | 170 |
| Internal BGP | 200 |
| Unknown/unusable | 255 |

Administrative distance is considered only after longest-prefix match determines comparable routes. A more specific route usually wins over a less specific route even if the less specific route has a better AD.

## 17.11 Route Selection Order

Route selection can be understood in a simple order.

First, the router looks for matching routes in the routing table.

Second, it chooses the longest prefix match. The most specific route wins.

Third, if multiple routes have the same prefix length and destination, the router chooses the route with the lowest administrative distance.

Fourth, if administrative distance is tied, the router uses the metric to choose the best route.

Fifth, if equal-cost routes remain, the router may load balance depending on platform and configuration.

Route Selection Order

| Order | Decision Factor | Preferred Value |
|---:|---|---|
| 1 | Longest prefix match | Most specific prefix |
| 2 | Administrative distance | Lowest AD |
| 3 | Metric | Lowest metric |
| 4 | Equal-cost paths | May load balance |

Students should avoid a common misunderstanding: administrative distance does not override longest-prefix match. A `/24` route is more specific than a `/16` route. The router uses the most specific matching route.

## 17.12 Floating Static Routes

A floating static route is a static route configured with a higher administrative distance so it acts as a backup route.

Normal static routes have AD 1. If we configure a static route with AD 200, it will not be used while a better route exists. It "floats" in the background and becomes active only if the primary route disappears.

Example:

Primary route through ISP1:

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

Backup floating static route through ISP2:

```text
ip route 0.0.0.0 0.0.0.0 198.51.100.1 200
```

The first default route has AD 1. The second default route has AD 200. The router uses ISP1 while it is available. If the primary route is removed from the routing table, the backup route can be installed.

Floating Static Route Summary

| Route | Next Hop | AD | Role |
|---|---|---:|---|
| `0.0.0.0/0` | 203.0.113.1 | 1 | Primary |
| `0.0.0.0/0` | 198.51.100.1 | 200 | Backup |

Floating static routes are useful for backup internet links, backup WAN links, and simple failover designs. However, they only work if the primary route is actually removed from the routing table. In some cases, tracking or dynamic routing may be needed for better failure detection.

## 17.13 Static Routing Design Use Cases

Static routing is useful in specific situations.

Common use cases include:

| Use Case | Why Static Routing Fits |
|---|---|
| Stub network | Only one way out |
| Internet edge default route | Send unknown destinations to ISP |
| Small branch | Few networks, simple design |
| Lab environment | Predictable and easy to learn |
| Firewall routing | Explicit paths to internal networks |
| Backup path | Floating static route |

Static routing is not always the best solution. In large networks with many routes and changing paths, dynamic routing is easier to scale. Lesson 18 will introduce dynamic routing concepts.

## 17.14 Common Static Routing Mistakes

Static route mistakes are common because manual routes require exact information.

One mistake is using the wrong next-hop IP address. The next hop must be reachable from the router.

Another mistake is forgetting the return route. If R1 can reach R2's LAN but R2 does not know how to return traffic to R1's LAN, communication fails.

Another mistake is using an incorrect subnet mask. A route to `192.168.10.0 255.255.255.0` is different from a route to `192.168.10.0 255.255.0.0`.

Another mistake is relying on a default route when a more specific route is required through another path.

Common Static Route Mistakes

| Mistake | Result |
|---|---|
| Wrong next hop | Route may fail or traffic goes wrong direction |
| No return route | Replies cannot return |
| Wrong mask | Too much or too little traffic matches |
| Missing default route | Unknown destinations fail |
| Floating route AD too low | Backup route becomes primary |
| Interface down | Connected and static routes may disappear |

## 17.15 Routing Troubleshooting

Routing troubleshooting should be structured and directional.

A practical sequence is:

1. Confirm the source host IP address, mask, and gateway.
2. Confirm the destination IP address.
3. Test the source host's default gateway.
4. Check the first router's routing table.
5. Confirm the router has a route to the destination network.
6. Confirm the next hop is reachable.
7. Check the return path from the destination side.
8. Check ACLs, firewall policy, or NAT if routing appears correct.
9. Use traceroute to identify where the path stops.
10. Check interface status and counters.

Routing Troubleshooting Table

| Symptom | Possible Cause | What to Check |
|---|---|---|
| Host cannot ping gateway | Local VLAN/subnet/gateway issue | Host IP, gateway, switch/SVI |
| Router has no route | Missing static/default route | `show ip route` |
| Route exists but next hop unreachable | Link or addressing problem | `ping <next-hop>`, interface status |
| One-way communication | Missing return route | Remote router routing table |
| Internet unreachable | Missing/wrong default route | `0.0.0.0/0`, ISP next hop |
| Backup link used unexpectedly | AD or primary route issue | Static route AD, interface status |
| Traceroute stops at router | Missing next route or policy block | Routing table, ACL/firewall |

## 17.16 Windows, Linux, and Cisco IOS Practical Commands

### Windows Commands

```text
ipconfig /all
route print
ping <default-gateway>
ping <remote-destination>
tracert <remote-destination>
```

Windows helps verify the host's local route, default gateway, and path to a remote destination. `route print` shows the local host routing table.

### Linux Commands

```text
ip addr
ip route
ping <default-gateway>
ping <remote-destination>
traceroute <remote-destination>
```

Linux shows routes clearly with `ip route`. A missing `default via` route means the host may not know how to reach remote networks.

### Cisco IOS Commands

```text
show ip interface brief
show ip route
show ip route static
show ip route connected
show running-config | include ^ip route
ping <destination>
traceroute <destination>
show arp
```

These commands verify interface status, route sources, static route configuration, next-hop reachability, and forwarding path.

## 17.17 Cisco Packet Tracer Practice

### Practice Lab: Static Routes Between Two Routers

Build a topology:

```text
PC1 --- R1 --- R2 --- PC2
```

Addressing:

| Device/Link | Addressing |
|---|---|
| PC1 | 192.168.10.10/24, gateway 192.168.10.1 |
| R1 LAN | 192.168.10.1/24 |
| R1-R2 link | R1 10.0.0.1/30, R2 10.0.0.2/30 |
| R2 LAN | 192.168.20.1/24 |
| PC2 | 192.168.20.10/24, gateway 192.168.20.1 |

Tasks:

1. Configure router interfaces.
2. Configure PC IP addresses and gateways.
3. Verify connected routes with `show ip route connected`.
4. Configure R1 static route to `192.168.20.0/24`.
5. Configure R2 static route to `192.168.10.0/24`.
6. Ping PC2 from PC1.
7. Remove the return route on R2.
8. Observe the failure.
9. Restore the route and verify connectivity.

Expected learning outcome:

Students should understand that static routing requires routes in both directions.

### Practice Lab: Default Route and Floating Static Route

Build a topology:

```text
LAN --- Branch Router --- ISP1
                    \---- ISP2
```

Tasks:

1. Configure a primary default route to ISP1.
2. Configure a floating default route to ISP2 with higher AD.
3. Verify the routing table.
4. Shut down the primary ISP-facing interface.
5. Observe whether the backup route appears.
6. Bring the primary link back up.
7. Verify route preference returns to the primary path.

Example commands:

```text
ip route 0.0.0.0 0.0.0.0 203.0.113.1
ip route 0.0.0.0 0.0.0.0 198.51.100.1 200
```

Expected learning outcome:

Students should understand how administrative distance makes a static route act as a backup.

## 17.18 Cybersecurity Relevance

Routing affects security because it determines reachability. If a route exists, traffic may be able to reach a network unless policy blocks it. If a sensitive network is accidentally advertised or statically routed where it should not be, exposure increases.

Static routes should be documented and reviewed. A route to a management subnet, server subnet, or partner network should not be added casually. Routes should match business need and security policy.

Attackers may also benefit from misrouting. If traffic is sent to the wrong next hop, it may be intercepted, blackholed, or bypass expected inspection points. In secure designs, routing should guide traffic through firewalls, IDS/IPS, logging points, or zero-trust enforcement where required.

Security principle:

```text
Routing creates paths. Security policy controls who may use those paths.
```

## 17.19 Cloud Networking Relevance

Cloud networking uses routing tables heavily. A cloud subnet may have a route table that sends local traffic inside the virtual network, internet traffic to an internet gateway, private outbound traffic to a NAT gateway, and corporate traffic to a VPN or cloud firewall.

Example cloud route table:

| Destination | Target |
|---|---|
| 10.100.0.0/16 | Local cloud network |
| 0.0.0.0/0 | Internet gateway |
| 10.10.0.0/16 | VPN gateway |
| 10.20.0.0/16 | Cloud firewall |

The same concepts apply: longest-prefix match, default route, next hop, and policy. Cloud engineers must also avoid overlapping routes between office networks, cloud VPCs/VNets, VPNs, and partner networks.

## 17.20 Interview and Exam Relevance

In IT support interviews, routing questions may focus on default gateways, traceroute, and why a host can reach local devices but not remote networks.

In network engineering interviews, routing questions may include routing table interpretation, static route syntax, longest-prefix match, administrative distance, default routes, floating static routes, and return-path troubleshooting.

For CCNA, students should know how to configure and verify IPv4 static routes, default routes, and floating static routes. They should also understand route selection order. For Network+, students should understand routing tables, next hops, default routes, and troubleshooting tools such as ping and traceroute.

## 18. KEY TERMS / GLOSSARY

| Term | Meaning |
|---|---|
| Routing | Forwarding packets between IP networks. |
| Routing Table | Database used by a router to select forwarding paths. |
| Route | Entry that tells a router how to reach a destination network. |
| Next Hop | The next router IP address where traffic should be sent. |
| Outgoing Interface | Interface used to forward traffic. |
| Connected Route | Automatically learned route for a directly connected network. |
| Local Route | Route for the router's own interface IP address. |
| Static Route | Manually configured route. |
| Default Route | Route used when no more specific route matches. |
| Gateway of Last Resort | Cisco term for the default route. |
| Longest-Prefix Match | Route selection rule choosing the most specific matching prefix. |
| Administrative Distance | Trust value used to choose between routes from different sources. |
| Metric | Value used by a routing source to choose best path among similar routes. |
| Floating Static Route | Static route with higher AD used as a backup route. |
| Return Path | Route used by reply traffic to get back to the source. |

## 19. COMPARISON TABLES

### 19.1 Connected vs Static vs Default Routes

| Route Type | How Created | Common Purpose |
|---|---|---|
| Connected | Interface up with IP address | Reach directly attached network |
| Static | Manually configured | Reach specific remote network |
| Default | Manually or dynamically learned | Send unknown destinations to next hop |

### 19.2 Longest-Prefix Match vs Administrative Distance

| Feature | Longest-Prefix Match | Administrative Distance |
|---|---|---|
| Purpose | Chooses most specific matching route | Chooses trusted source for same prefix |
| Preferred Value | Longer prefix | Lower AD |
| Example | `/24` beats `/16` | Static AD 1 beats OSPF AD 110 |
| Common Confusion | Happens before AD comparison | Does not override specificity |

### 19.3 Static Route vs Floating Static Route

| Feature | Static Route | Floating Static Route |
|---|---|---|
| Administrative Distance | Usually 1 | Manually set higher |
| Role | Primary manual path | Backup manual path |
| Installed When | Next hop/interface valid | Better route unavailable |
| Use Case | Small network route | Backup ISP/WAN link |

### 19.4 Routing Troubleshooting Tools

| Tool/Command | Purpose |
|---|---|
| `ping` | Tests reachability |
| `traceroute` / `tracert` | Shows path and where traffic stops |
| `show ip route` | Displays router routing table |
| `show ip interface brief` | Shows interface IP and status |
| `show arp` | Shows IPv4-to-MAC mappings |
| `route print` | Shows Windows routing table |
| `ip route` | Shows Linux routing table |

## 20. REAL-WORLD EXAMPLE / ANALOGY

Routing is like a delivery company choosing roads to reach different towns. The routing table is the driver's map. A specific route to one town is better than a broad instruction such as "send everything north." If the driver has no specific route, the default route is the general road used for unknown destinations.

Administrative distance is like trust in the source of the map. A directly observed road is trusted most. A manually approved route is highly trusted. A route learned from another system may be trusted based on the protocol.

## 21. QUICK-RECAP CHEAT SHEET

- Routers forward packets between IP networks.
- Routers use destination IP addresses.
- Routers consult the routing table.
- Connected routes appear when interfaces are up with IP addresses.
- Local routes represent the router's own interface IP addresses.
- Static routes are manually configured.
- Default routes match unknown destinations.
- IPv4 default route is `0.0.0.0/0`.
- Cisco default route syntax is `ip route 0.0.0.0 0.0.0.0 <next-hop>`.
- Longest-prefix match chooses the most specific route.
- Administrative distance chooses between routes to the same prefix from different sources.
- Lower administrative distance is preferred.
- Connected AD is 0.
- Static AD is 1.
- OSPF AD is 110.
- RIP AD is 120.
- Floating static routes use higher AD as backup routes.
- Routing must work in both directions.
- `show ip route` is the main routing table command.
- `traceroute` helps locate where the path stops.

## 22. REVIEW QUESTIONS

1. What is routing?
2. What does a router examine when forwarding a packet?
3. What is a routing table?
4. What is a connected route?
5. What is a local route?
6. What is a static route?
7. What is a next hop?
8. What is a default route?
9. What is the IPv4 default route written in CIDR notation?
10. What Cisco command configures a default route to next hop `203.0.113.1`?
11. What is longest-prefix match?
12. Which route is preferred for destination `10.10.20.55`: `10.0.0.0/8` or `10.10.20.0/24`?
13. What is administrative distance?
14. Is lower or higher administrative distance preferred?
15. What is the administrative distance of a connected route?
16. What is the default administrative distance of a static route?
17. What is a floating static route?
18. Why is a return route important?
19. Which Cisco command shows the routing table?
20. Which tool helps show where traffic stops along a path?

## 23. SUGGESTED ANSWER GUIDE

1. Routing is forwarding packets between IP networks.
2. The destination IP address.
3. A routing table is the database a router uses to select forwarding paths.
4. A connected route is automatically created for a directly connected network when an interface is up with an IP address.
5. A local route identifies the router's own interface IP address.
6. A static route is a manually configured route.
7. A next hop is the next router IP address where traffic should be sent.
8. A default route is used when no more specific route matches.
9. `0.0.0.0/0`.
10. `ip route 0.0.0.0 0.0.0.0 203.0.113.1`.
11. Longest-prefix match means the router chooses the most specific matching route.
12. `10.10.20.0/24`.
13. Administrative distance is a trust value used to choose between route sources.
14. Lower is preferred.
15. 0.
16. 1.
17. A static route with a higher administrative distance used as a backup route.
18. Replies need a route back to the original source.
19. `show ip route`.
20. `traceroute` or Windows `tracert`.
