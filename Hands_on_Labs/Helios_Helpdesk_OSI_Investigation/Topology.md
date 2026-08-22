# Helios Helpdesk Network Investigation — Topology

## Aligned learning

- Primary: Lesson 1 — How Networks Work and How to Isolate Failure
- Extension: Lesson 3 — OSI Model Deep Dive
- Extension: Lesson 4 — How Data Travels Through a Network

## Intended topology

~~~mermaid
flowchart LR
  PC1["PC1<br/>Intended: 192.168.40.10/24"]
  SW1["SW1<br/>Layer 2 access switch"]
  WEB1["WEB1<br/>Intended: 192.168.40.20/24<br/>HTTP service"]
  PC1 --- SW1
  SW1 --- WEB1
~~~

## Devices

- One Cisco 2960 switch
- One PC
- One server

## Intended addressing

| Device | IPv4 address | Mask | Gateway |
|---|---:|---:|---|
| PC1 | 192.168.40.10 | 255.255.255.0 | Not required |
| WEB1 | 192.168.40.20 | 255.255.255.0 | Not required |

Both endpoints are in the same local network. A router, DNS server, VLAN, trunk, or internet connection is not required.

## Baseline build

For guided practice, students may build and validate the intended topology before the instructor introduces a fault. For independent assessment, provide a prebuilt faulty Packet Tracer file so students cannot infer the answer from the build instructions.

Use copper straight-through cabling between each endpoint and SW1. Label devices clearly.

## Instructor fault injection

After saving a validated baseline, introduce one fault from the instructor solution:

- incorrect PC1 address;
- disabled HTTP service; or
- disconnected/disabled access link.

Save the faulty assessment copy separately. Do not tell students which layer or component contains the fault.

## Evidence expectations

Students submit:

- one annotated topology image;
- recorded before-state values;
- hypothesis and disproof test;
- relevant Simulation Mode event with interpretation;
- change and rollback record; and
- proof that the original HTTP task works after correction.

Screenshots are supporting evidence, not a replacement for reasoning.
