# Helios Helpdesk Network Investigation — Instructor Solution

> Keep this file unavailable to students until the assessed investigation closes.

## Purpose

The exercise measures evidence-led troubleshooting. A student should not receive credit merely for finding and correcting the visible fault.

## Approved fault variants

Use one variant for guided practice and a different variant for independent assessment.

### Variant A: Incorrect PC1 address

Change PC1 from 192.168.40.10/24 to 192.168.50.10/24.

Expected evidence:

- physical links are active;
- PC1 and WEB1 are in different IP networks;
- no router or gateway exists;
- ping and HTTP fail;
- correcting PC1 to 192.168.40.10/24 restores local communication.

### Variant B: HTTP service disabled

Keep addressing correct and disable HTTP on WEB1.

Expected evidence:

- physical link and IP addressing are correct;
- PC1 can ping WEB1;
- the browser request fails;
- Simulation Mode or server inspection shows the application service is unavailable;
- enabling HTTP restores the page without changing IP settings.

### Variant C: Access link disconnected

Disconnect PC1 from SW1 or disable the relevant switch port.

Expected evidence:

- link state fails before an IP or application test can succeed;
- the student identifies the physical/access failure without resetting addressing;
- restoring the intended link resolves the first dependency;
- the student still validates IP and HTTP after restoration.

Do not inject several faults during the first guided attempt. Multiple faults can be used later only when the student has mastered the single-fault method.

## Expected investigation logic

1. Restate the required outcome: PC1 must open the authorised page on WEB1.
2. Confirm the written scope and intended addressing.
3. Capture link state, addressing, ping, HTTP state, and browser result.
4. Select one hypothesis supported by evidence.
5. Run a test capable of disproving that hypothesis.
6. Record the before-state and rollback.
7. Correct one confirmed fault.
8. Repeat the original browser task.
9. Add reachability, addressing, and Simulation Mode validation.
10. Write a concise closure update.

## Interpretation guide

| Observation | Supported conclusion | Conclusion not yet supported |
|---|---|---|
| Link is down | Physical/access connectivity is unavailable | IP configuration is definitely wrong |
| PC1 and WEB1 are in different /24 networks with no router | They cannot communicate through the intended local design | The switch is faulty |
| Ping succeeds | IP reachability and ICMP response exist | HTTP is working |
| Ping succeeds but HTTP fails | Investigate TCP/HTTP or application state | Readdress both endpoints |
| Browser page opens | The original HTTP task works | Every network service is healthy |
| ARP appears before local IP traffic | PC1 is resolving the local destination MAC address | DNS caused the ARP exchange |

## Model ticket update

> HEL-NET-001 affected only PC1’s access to the internal portal on WEB1. Baseline evidence showed active switch links and WEB1 at 192.168.40.20/24, while PC1 was incorrectly configured as 192.168.50.10/24. With no router in scope, the endpoints could not communicate locally. After recording the original value, I changed PC1 to the approved 192.168.40.10/24 address. PC1 then reached WEB1, the HTTP page opened, and Simulation Mode showed ARP followed by successful TCP/HTTP communication. No gateway, VLAN, or unrelated device was changed. Recommend closure after instructor confirmation.

Adapt the details to the injected variant. Do not accept a copied model that contradicts the student’s evidence.

## Common weak behaviours

- changing settings before recording the baseline;
- using random changes instead of a hypothesis;
- claiming that ping proves HTTP;
- adding an unnecessary gateway or router;
- submitting screenshots without interpretation;
- describing the symptom as the root cause;
- failing to repeat the original browser task; and
- hiding an unsuccessful test.

## Assessment answer key for Lesson 1

Multiple-choice answers:

1. C
2. A
3. D
4. B
5. C

Short and scenario responses should be marked for technical accuracy, narrow interpretation of evidence, safe sequencing, and clarity. Accept alternative valid hypotheses when the proposed test could genuinely disprove them.
