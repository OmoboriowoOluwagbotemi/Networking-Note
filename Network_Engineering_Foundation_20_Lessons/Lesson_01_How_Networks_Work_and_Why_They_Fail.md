# Lesson 1: How Networks Work and How to Isolate Failure

> Practical outcome: Given a simple connectivity complaint, students can identify the affected scope, collect baseline evidence, form a testable hypothesis, and recommend the next safe action without making random changes.

## Why this lesson matters

Users rarely report a network problem in technical language. They say, “the internet is down,” “the server is not working,” or “the Wi-Fi is bad.” A technician must turn that complaint into a specific, testable problem.

This lesson introduces a small mental model that will be reused throughout the course:

~~~text
User task
   |
Endpoint and network interface
   |
Access connection: cable, switch port, or Wi-Fi
   |
IP configuration and local network
   |
Default gateway and routed path
   |
DNS and required service
   |
Application or remote system
~~~

The aim is not to memorize every possible failure. The aim is to identify where communication stops and collect evidence before changing anything.

## Learning outcomes

By the end of the lesson, a student should be able to:

1. explain what a computer network enables;
2. distinguish an endpoint, switch, router, access point, firewall, and server;
3. describe the difference between local and remote communication;
4. identify whether a problem affects one user, a group, or an entire service;
5. use read-only checks to test interface, addressing, gateway, DNS, and service availability;
6. separate fact, hypothesis, action, and result; and
7. write a concise helpdesk update supported by evidence.

## Opening case

A staff member reports:

> “The training portal is down on my computer. I need it before class begins.”

Before touching the computer, ask:

- What exact task is failing?
- What error appears?
- Did it work previously?
- Is one user affected or are several users affected?
- Can the user reach any local or remote service?
- What changed recently?
- Which systems are you authorised to test?

“The network is down” is a complaint, not a diagnosis.

## 1. What a network does

A computer network is a controlled communication system that allows devices and applications to exchange data and use shared services. A network includes:

- endpoints such as laptops, phones, printers, and servers;
- network interfaces and transmission media;
- switches and wireless access points for local connectivity;
- routers or Layer 3 gateways for communication between networks;
- addressing and protocols;
- services such as DHCP and DNS;
- security controls such as firewalls and access rules; and
- monitoring, documentation, and operational processes.

A network is successful only when it supports the required business task reliably and securely. A device showing “connected” does not prove that the required application works.

## 2. Essential device roles

| Component | Primary role | Useful first question |
|---|---|---|
| Endpoint | Runs the user’s application and network interface | Does the problem affect this device only? |
| Switch | Connects devices within a local Ethernet network | Is the link active and is the device on the intended network? |
| Access point | Connects wireless devices to the network | Is the client associated with the correct network and signal? |
| Router/default gateway | Forwards traffic between IP networks | Can the endpoint reach its gateway? |
| Firewall | Permits or blocks traffic according to policy | Is the required traffic allowed and logged? |
| DHCP service | Supplies automatic IP configuration | Did the endpoint receive the expected address, gateway, and DNS? |
| DNS service | Resolves names to addresses | Does the required name resolve to the expected address? |
| Server/application | Provides the business service | Is the required port and application responding? |

More detailed device operation is taught in Lesson 2. The OSI model and packet encapsulation are taught in Lessons 3 and 4.

## 3. Local and remote communication

Two devices in the same IP network can normally communicate through the local access network. Traffic for another network is sent to a default gateway.

Consider:

- PC1: 192.168.40.10/24
- WEB1: 192.168.40.20/24

Both addresses belong to 192.168.40.0/24, so they can communicate locally through a switch. A default gateway is not required for communication between them.

If WEB1 were on 192.168.50.0/24, a router or Layer 3 gateway and a valid route would be required.

This distinction prevents a common troubleshooting mistake: investigating the internet or ISP when the failure exists entirely inside the local network.

## 4. Scope before tools

Scope identifies how widely the symptom is experienced.

| Observed scope | Likely starting area |
|---|---|
| One application on one device | Application, local configuration, identity, or service dependency |
| Every application on one device | Interface, access connection, addressing, or endpoint policy |
| Several users in one area | Access switch, wireless coverage, VLAN, DHCP scope, uplink, or power |
| Users can reach IP addresses but not names | DNS configuration or DNS service |
| Everyone loses one service | Server, application, shared dependency, firewall policy, or upstream service |
| Entire site loses remote access | Gateway, firewall, WAN, ISP, routing, or power |

Scope guides the investigation; it does not prove the cause.

## 5. Evidence-first troubleshooting

Use the same sequence in every beginner investigation.

### Step 1: Confirm the required outcome

State the user’s task in testable language.

Weak: “The network is broken.”

Better: “PC1 cannot open the authorised HTTP page on WEB1 at 192.168.40.20.”

### Step 2: Protect scope and evidence

Confirm:

- authorised devices and addresses;
- prohibited actions;
- whether the user is remote;
- whether a change could disconnect a session; and
- what evidence must be preserved.

### Step 3: Inspect before changing

Check physical link, interface state, current addressing, routes, and the exact error. Do not reset, reinstall, flush, release, or disable controls before recording the original state.

### Step 4: Form one hypothesis

A hypothesis must be testable.

Weak: “It is probably the network.”

Better: “PC1 may be addressed outside the server’s local subnet because its current IPv4 address is not in 192.168.40.0/24.”

### Step 5: Choose a test that could disprove it

A useful test can show that the hypothesis is wrong. If PC1 has the correct address and can reach WEB1 by IP, the addressing hypothesis is weakened.

### Step 6: Make the smallest authorised change

Change one relevant item. Record the before-state, action, approval, and rollback.

### Step 7: Validate the original task

A successful ping does not prove that a web page works. Repeat the user’s original task and add related positive and negative tests.

### Step 8: Document and communicate

Record what failed, what evidence showed, what changed, how the result was validated, and what risk remains.

## 6. Beginner command sequence

Use only instructor-approved lab targets.

### Windows configuration

~~~powershell
ipconfig /all
~~~

Record the active adapter, IPv4 address, subnet mask or prefix, default gateway, DHCP state, and DNS servers. An address beginning with 169.254 suggests that DHCP did not supply an IPv4 address when automatic configuration was expected.

### Gateway or local target

~~~powershell
ping <APPROVED_GATEWAY_OR_LOCAL_TARGET>
~~~

Interpret narrowly. A reply supports IP reachability and ICMP response. A timeout can also result from filtering, so it does not prove that the destination is powered off.

### DNS

~~~powershell
nslookup <APPROVED_HOSTNAME>
~~~

Record the DNS server used, returned address, and any explicit response such as timeout, refusal, or non-existent domain.

### Required TCP service

~~~powershell
Test-NetConnection <APPROVED_HOSTNAME_OR_IP> -Port <APPROVED_PORT>
~~~

This tests a specific TCP service. It is stronger evidence for an application dependency than ping alone.

## 7. Evidence table

| Question | Evidence | Result | Interpretation | Next action |
|---|---|---|---|---|
| Is the active interface connected? | Interface/link state |  |  |  |
| Is addressing correct for the intended network? | ipconfig /all |  |  |  |
| Is the local target or gateway reachable? | ping |  |  |  |
| Does the name resolve correctly? | nslookup |  |  |  |
| Is the required TCP service available? | Test-NetConnection or application test |  |  |  |
| Does the original user task now work? | Reproduction test |  |  |  |

Evidence is useful only when the student explains what it proves and what it does not prove.

## 8. Guided reasoning activity

For each symptom, state the first dependency you would test and explain why.

1. One laptop has no IPv4 address, while nearby users are working.
2. A user can reach a server by IP address but not by hostname.
3. All users connected to one access switch are offline.
4. Ping to a web server succeeds, but HTTPS does not open.
5. A local printer works, but a remote cloud application does not.

Do not propose a corrective action until you have proposed a confirming or disproving test.

## 9. Practical investigation

Complete the Helios Helpdesk Network Investigation in:

Hands_on_Labs/Helios_Helpdesk_OSI_Investigation/Problem.md

The topology is small, but the exercise is assessed on reasoning, evidence, controlled change, validation, and communication. Completing steps without explaining decisions is not mastery.

## 10. Essential vocabulary

| Term | Meaning |
|---|---|
| Endpoint | A user or service device connected to the network |
| Interface | The wired, wireless, virtual, or tunnel connection used by a device |
| IP address | A logical Layer 3 address |
| Prefix/subnet mask | Identifies the local network portion of an IP address |
| Default gateway | The next-hop device used to reach other IP networks |
| DHCP | A service that supplies automatic IP configuration |
| DNS | A service that resolves names to addresses and other records |
| Port | A transport-layer identifier used by a TCP or UDP service |
| Baseline | Recorded state before an investigation or change |
| Hypothesis | A testable explanation for observed evidence |
| Validation | Evidence that the required outcome works after action |
| Rollback | A planned method for reversing a change |

## 11. Assessment

### Short-answer questions

1. Explain why “the internet is down” is not a sufficient technical diagnosis.
2. PC1 is 192.168.40.10/24 and WEB1 is 192.168.40.20/24. Explain whether a gateway is required between them.
3. Distinguish a fact, hypothesis, test, and corrective action using one network example.

### Multiple-choice questions

1. One user cannot connect, but every nearby user can. What should the technician do first?
   A. Restart the access switch
   B. Replace the router
   C. Confirm the user’s exact symptom and inspect the endpoint
   D. Contact the ISP

2. A workstation can reach 192.168.40.20 but cannot resolve portal.femtech.example. Which dependency should be tested next?
   A. DNS
   B. Monitor resolution
   C. Keyboard layout
   D. Switch hostname

3. Which statement about ping is most accurate?
   A. A failed ping always proves the host is offline
   B. A successful ping proves every application is working
   C. Ping repairs incorrect addressing
   D. Ping provides limited reachability evidence and may be affected by filtering

4. Why should a technician record the baseline before changing configuration?
   A. To make documentation longer
   B. To preserve evidence and support comparison or rollback
   C. To avoid speaking with the user
   D. To guarantee that the first hypothesis is correct

5. Which is the strongest final validation after repairing access to a web portal?
   A. The cable light is green
   B. The device has an IP address
   C. The original user task succeeds and relevant related tests pass
   D. The technician believes the change should work

### Scenario

PC1 cannot open an authorised internal web service. Another device on the same switch can open it. Write:

1. the first four facts you need;
2. two plausible hypotheses;
3. one test that could disprove each hypothesis;
4. the evidence required before a change;
5. the validation required before closure; and
6. a two-sentence user update.

## 12. Exit ticket

Without notes, complete these statements:

1. The most important question I ask before using a tool is...
2. One result that ping cannot prove is...
3. If I can reach a service by IP but not by name, I will next test...
4. Evidence differs from a screenshot because...
5. When my hypothesis is disproved, I should...

## Lesson boundary

This lesson establishes the troubleshooting mindset and minimum network path. Detailed network types and topologies are reference topics for later study. Device internals, the OSI model, Ethernet switching, addressing, routing, DNS, DHCP, wireless, and security are developed in subsequent lessons.
