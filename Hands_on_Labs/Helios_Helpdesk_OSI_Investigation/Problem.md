# Helios Helpdesk Network Investigation — Student Brief

## Ticket

**Ticket ID:** HEL-NET-001  
**Reported by:** Training Coordinator  
**Affected service:** Internal training portal  
**Symptom:** PC1 cannot open the page hosted on WEB1. The portal is required for a scheduled class.  
**Last known working state:** The instructor confirms that the approved baseline worked before a controlled fault was introduced.

## Your role

You are the helpdesk trainee assigned to investigate. Your goal is not merely to make the page open. You must identify the fault through evidence, make the smallest authorised correction, prove restoration, and write a useful ticket update.

## Authorised scope

- PC1
- SW1
- WEB1
- Network 192.168.40.0/24
- HTTP service on WEB1
- Packet Tracer Simulation Mode

Do not add routers, internet links, extra networks, VLANs, or public targets.

## Intended design

| Device | Intended configuration | Role |
|---|---|---|
| PC1 | 192.168.40.10/24 | User endpoint |
| SW1 | Layer 2 access switch | Local connectivity |
| WEB1 | 192.168.40.20/24; HTTP enabled | Internal portal |

PC1 and WEB1 are in the same local network. No default gateway is required for this task.

## Constraints

- Inspect and record the starting state before changing anything.
- Do not delete the topology or replace every device.
- Do not use automatic configuration as a substitute for diagnosis.
- Make one controlled change at a time.
- Ask the instructor for authority if the evidence points outside the written scope.
- Preserve the faulty version before saving the repaired version.

## Investigation tasks

### 1. Clarify and plan

Write:

- the exact required outcome;
- what is known, unknown, and assumed;
- the authorised targets;
- two possible failure areas; and
- your first safe test.

### 2. Capture the baseline

Record:

- cable and link state;
- PC1 IPv4 address and subnet mask;
- WEB1 IPv4 address and subnet mask;
- WEB1 HTTP service state;
- ping result from PC1 to WEB1; and
- browser result for http://192.168.40.20.

Do not correct a value while collecting the baseline.

### 3. Form a hypothesis

Use this structure:

> Because I observed ______, I think ______ may be causing the failure. I will test this by ______. If the hypothesis is wrong, I expect ______.

### 4. Test systematically

Move through the path:

1. physical link;
2. endpoint addressing;
3. local IP reachability;
4. TCP/HTTP service;
5. browser request.

Use Simulation Mode when it helps show where ARP, ICMP, TCP, or HTTP stops. Do not claim that an OSI layer is faulty without evidence.

### 5. Correct one confirmed fault

Before changing anything, record:

- current value or state;
- intended value or state;
- reason for the change; and
- rollback method.

Make only the smallest correction supported by the evidence.

### 6. Validate

Your validation must include:

- the original page opens from PC1;
- PC1 can reach WEB1 as expected;
- the addressing remains inside 192.168.40.0/24;
- Simulation Mode shows the expected communication; and
- no unrelated device or setting was changed.

### 7. Communicate

Write a ticket update containing:

- confirmed symptom and scope;
- evidence collected;
- root cause;
- corrective action;
- validation;
- remaining risk or limitation; and
- closure recommendation.

## Required deliverables

1. Completed [Evidence Worksheet](Evidence_Worksheet.md).
2. Faulty Packet Tracer file preserved as Helios-Before.pkt.
3. Repaired Packet Tracer file saved as Helios-Validated.pkt.
4. One annotated topology image.
5. One Simulation Mode evidence image with a written interpretation.
6. Final ticket update of no more than 150 words.

A collection of screenshots without timestamps, labels, and interpretation does not meet the evidence standard.

## Success standard

You pass when you can explain:

- why you chose each test;
- what each result proved or failed to prove;
- why the correction was appropriate;
- how you validated the original business task; and
- what you would do next if the correction failed.
