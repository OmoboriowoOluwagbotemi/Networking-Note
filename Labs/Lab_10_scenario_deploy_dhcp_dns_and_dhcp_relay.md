# FEMTECT NETWORKING PRACTICAL HANDS-ON LAB 10

## Lab Title: Scenario - Deploy DHCP, DNS, and DHCP Relay

## Aligned Lessons

This lab aligns with Lesson 19, DHCP and DNS Fundamentals.

## Main Tool

Cisco Packet Tracer.

## Important Why

This lab is important because DHCP and DNS are two of the most important services in real networks. Users may say the network is down when the real issue is that the client did not receive an IP address or cannot resolve names.

## Important How

Students will build a multi-VLAN topology, place a DHCP/DNS server in a server VLAN, configure DHCP scopes on the server, configure `ip helper-address` on router subinterfaces, and verify that clients receive correct addressing automatically.

## Network Plan

| VLAN | Name | Subnet | Gateway |
|---:|---|---|---|
| 10 | ADMIN | 192.168.10.0/24 | 192.168.10.1 |
| 20 | SALES | 192.168.20.0/24 | 192.168.20.1 |
| 99 | SERVER | 192.168.99.0/24 | 192.168.99.1 |

## Required Devices

| Device | Quantity |
|---|---:|
| Router | 1 |
| 2960 switch | 1 |
| Server | 1 |
| PCs | 2 |

## Detailed Step-by-Step Procedure

### Part A: Build and Cable the Topology

1. Add one 2911 router named `R1`.
2. Add one 2960 switch named `SW1`.
3. Add one server named `SRV-DHCP-DNS`.
4. Add two PCs named `PC-ADMIN` and `PC-SALES`.
5. Connect R1 G0/0 to SW1 Fa0/24.
6. Connect PC-ADMIN to SW1 Fa0/1.
7. Connect PC-SALES to SW1 Fa0/2.
8. Connect SRV-DHCP-DNS to SW1 Fa0/3.

### Part B: Configure VLANs and Switch Ports

On SW1, type:

```text
enable
configure terminal
vlan 10
 name ADMIN
exit
vlan 20
 name SALES
exit
vlan 99
 name SERVER
exit
interface fa0/1
 switchport mode access
 switchport access vlan 10
exit
interface fa0/2
 switchport mode access
 switchport access vlan 20
exit
interface fa0/3
 switchport mode access
 switchport access vlan 99
exit
interface fa0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
end
show vlan brief
show interfaces trunk
```

### Part C: Configure Router Subinterfaces and DHCP Relay

On R1, type:

```text
enable
configure terminal
interface gigabitEthernet0/0
 no shutdown
exit
interface gigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip helper-address 192.168.99.10
exit
interface gigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip helper-address 192.168.99.10
exit
interface gigabitEthernet0/0.99
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0
exit
end
show ip interface brief
```

### Part D: Configure the Server IP Address

1. Click SRV-DHCP-DNS.
2. Click Desktop.
3. Click IP Configuration.
4. Set IP Address to `192.168.99.10`.
5. Set Subnet Mask to `255.255.255.0`.
6. Set Default Gateway to `192.168.99.1`.
7. Set DNS Server to `192.168.99.10`.

### Part E: Configure DHCP Service on the Server

1. Click SRV-DHCP-DNS.
2. Click Services.
3. Click DHCP.
4. Turn DHCP service On.
5. Create the Admin pool:
   - Pool Name: `ADMIN`
   - Default Gateway: `192.168.10.1`
   - DNS Server: `192.168.99.10`
   - Start IP Address: `192.168.10.100`
   - Subnet Mask: `255.255.255.0`
   - Maximum Number of Users: `50`
6. Click Add or Save depending on Packet Tracer version.
7. Create the Sales pool:
   - Pool Name: `SALES`
   - Default Gateway: `192.168.20.1`
   - DNS Server: `192.168.99.10`
   - Start IP Address: `192.168.20.100`
   - Subnet Mask: `255.255.255.0`
   - Maximum Number of Users: `50`
8. Click Add or Save.

### Part F: Configure DNS Service on the Server

1. Click Services.
2. Click DNS.
3. Turn DNS service On.
4. In Name, type `intranet.femtect.local`.
5. In Address, type `192.168.99.10`.
6. Click Add.

### Part G: Configure Clients for DHCP

1. Click PC-ADMIN.
2. Click Desktop.
3. Click IP Configuration.
4. Select DHCP.
5. Confirm it receives an address in `192.168.10.0/24`.
6. Click PC-SALES.
7. Click Desktop > IP Configuration.
8. Select DHCP.
9. Confirm it receives an address in `192.168.20.0/24`.

### Part H: Test DHCP and DNS

1. On PC-ADMIN, open Command Prompt.
2. Type `ipconfig /all` and press Enter.
3. Confirm IP address, gateway, and DNS server are correct.
4. Type `ping 192.168.99.10` and press Enter.
5. Confirm the server responds.
6. Type `nslookup intranet.femtect.local` and press Enter.
7. Confirm the name resolves to `192.168.99.10` if supported by the Packet Tracer PC.
8. If `nslookup` is not available or behaves differently, use the PC Web Browser and browse to `http://intranet.femtect.local` after confirming DNS service is configured.

## Verification Commands

```text
show ip interface brief
show running-config
show vlan brief
show interfaces trunk
ipconfig /all
ping
nslookup
```

## Troubleshooting Notes

If clients do not receive DHCP addresses, check VLAN membership, trunking, router subinterfaces, `ip helper-address`, server gateway, and DHCP pool configuration.

## Student Deliverable

Submit DHCP pool screenshots, client `ipconfig /all`, router subinterface configuration, and DNS test result.
