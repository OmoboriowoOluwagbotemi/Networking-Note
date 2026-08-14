# Nova Care Network Problem Interpretation

## Source Files

This problem interpretation is based on:

- `Nova.pkt`
- `Nova_Physical_Topology.png`

## Visible Topology Summary

The Packet Tracer topology represents a small business network named `Nova_Care`. The company has an internal LAN, a wireless access point for wireless workstations, a LAN router, a WAN router, and a remote web server that represents an internet or external service.

The main goal is to make the Nova_Care LAN users reach the external web server across the router-to-router WAN link.

## Topology Seen in the Screenshot

| Area | Devices Seen | Network |
|---|---|---|
| Nova_Care LAN | Workstations, Access Point, LAN Switch, LAN Router | 192.168.1.0/24 |
| Router-to-router WAN link | LAN_Router and WAN_Router | 10.0.0.0/30 |
| Server-side network | WAN Switch and WEB_Server | 172.16.1.0/24 |

## Devices Identified

| Device Name | Role |
|---|---|
| LAN_Router | Default gateway for the Nova_Care LAN and router toward the WAN |
| LAN_Switch | Layer 2 access switch for wired LAN devices and access point |
| AccessPoint | Wireless access point for wireless workstations |
| Workstations | End-user devices inside Nova_Care LAN |
| WAN_Router | Router connecting the WAN link to the web server network |
| WAN_Switch | Layer 2 switch connecting the web server to WAN_Router |
| WEB_Server | Remote server users should be able to access |

## Interpreted Problem

Configure the Nova_Care network so that:

1. Wired workstations inside `192.168.1.0/24` can communicate with their gateway.
2. Wireless workstations can associate with the access point and join the same LAN.
3. The LAN router and WAN router can communicate over the `10.0.0.0/30` WAN link.
4. The WAN router can reach the web server network `172.16.1.0/24`.
5. The Nova_Care LAN can access the WEB_Server in `172.16.1.0/24`.
6. Routing is configured correctly in both directions.
7. The WEB_Server is configured with a valid IP address, default gateway, and HTTP service.

## Assumptions Used for a Working Solution

The screenshot shows the networks but does not show exact interface names or host IP addresses. The following safe addressing plan is used in the solution:

| Device | Interface | IP Address | Purpose |
|---|---|---|---|
| LAN_Router | LAN interface | 192.168.1.1/24 | Default gateway for Nova_Care LAN |
| LAN_Router | WAN interface | 10.0.0.1/30 | Link to WAN_Router |
| WAN_Router | WAN interface | 10.0.0.2/30 | Link to LAN_Router |
| WAN_Router | Server LAN interface | 172.16.1.1/24 | Default gateway for WEB_Server |
| WEB_Server | NIC | 172.16.1.10/24 | Web server IP address |
| AccessPoint | Management IP | 192.168.1.2/24 | Access point management |
| Workstations | NIC/Wireless | 192.168.1.10-192.168.1.50/24 | LAN clients |

## Required Outcome

At the end of the configuration:

- A workstation should ping `192.168.1.1`.
- LAN_Router should ping `10.0.0.2`.
- WAN_Router should ping `10.0.0.1`.
- WAN_Router should ping `172.16.1.10`.
- A Nova_Care workstation should ping `172.16.1.10`.
- A Nova_Care workstation should open the web server using `http://172.16.1.10`.

## Main Skills Practiced

This activity practices IPv4 addressing, default gateways, static routing, router interface configuration, LAN switching, wireless access point setup, server configuration, HTTP service verification, and end-to-end troubleshooting.
