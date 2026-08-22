# Instructor Delivery Card — Lesson 1 and Helios Investigation

## Session profile

- Audience: beginner networking, IT support, or cybersecurity students
- Duration: 90 minutes
- Delivery mode: classroom or live virtual lab
- Prerequisites: basic computer use and access to Cisco Packet Tracer
- Performance outcome: independently isolate one simple network failure using evidence and communicate the result
- Required files: Lesson 1, Topology, Student Brief, Evidence Worksheet
- Instructor-only files: Solution and fault-injection baseline

## Preparation checklist

Before class:

1. Test the intended Packet Tracer baseline.
2. Save separate files for fault variants A, B, and C.
3. Assign one fault variant per student or group.
4. Confirm that students can access Packet Tracer.
5. Keep the solution unavailable.
6. Prepare a visible timer and competency record.
7. Decide which students require guided prompts or low-resource pairing.

## Lesson sequence

| Time | Instructor action | Student performance | Evidence |
|---:|---|---|---|
| 0–8 min | Present “the portal is down” without explaining the cause | Ask clarifying questions and define scope | Questions recorded |
| 8–18 min | Draw endpoint-to-service path | Explain each dependency in plain language | One-minute explanation |
| 18–28 min | Model fact, hypothesis, disproof test, and action | Classify four statements correctly | Verbal checks |
| 28–38 min | Demonstrate a read-only baseline on a working topology | Predict what each test can and cannot prove | Prediction sheet |
| 38–63 min | Release faulty Helios files; observe without solving | Investigate, document, and request approval for one change | Evidence Worksheet |
| 63–73 min | Pair students with different variants | Defend hypothesis and challenge peer evidence | Peer-review note |
| 73–83 min | Debrief all three fault variants | Compare symptoms, tests, and causes | Class decision table |
| 83–90 min | Administer exit ticket | Answer independently without notes | Exit ticket |

Do not lecture through the entire note. Use the note as preparation and reference; use class time for reasoning, observation, practice, feedback, and retrieval.

## Questions that develop reasoning

Ask:

- What fact do you have?
- What are you assuming?
- What result would make your hypothesis less likely?
- Why are you using that tool now?
- What does this successful result still not prove?
- What is the smallest authorised change?
- How will you reproduce the user’s original task?
- What evidence would another technician need?

Avoid:

- “Do you understand?”
- “Is it the IP address?”
- “Why don’t you restart it?”
- questions that reveal the injected fault.

## Likely misconceptions

| Misconception | Instructor response |
|---|---|
| Every connectivity problem requires a router | Ask whether both endpoints are in the same IP network |
| Ping proves the application works | Ask which protocol and port the user actually needs |
| A timeout proves the destination is offline | Ask whether filtering or service state could produce the same symptom |
| The first plausible cause must be correct | Require a test that could disprove it |
| Screenshots are self-explanatory | Require timestamp, source, target, result, and interpretation |
| Fast correction is more important than evidence | Score the process, not speed alone |

## Fault release strategy

- Guided round: use Variant A and model only the first baseline check.
- Independent round: assign Variant B or C without hints.
- Remediation round: repeat with a different variant and fewer prompts.
- Extension: introduce two faults only after the learner reaches independent mastery on a single fault.

## Competency rubric

| Category | Points | Full-credit behaviour |
|---|---:|---|
| Scope and safety | 10 | Confirms authorised devices, required outcome, and constraints |
| Baseline evidence | 15 | Records relevant starting state before changes |
| Hypothesis quality | 20 | Uses evidence and proposes a test capable of disproving the hypothesis |
| Tool/test selection | 15 | Tests dependencies in a logical order and interprets results narrowly |
| Controlled correction | 10 | Makes one justified change with before-state and rollback |
| Validation | 15 | Repeats the original task and performs relevant related tests |
| Communication | 10 | Writes a clear, accurate, concise ticket update |
| Reflection | 5 | Identifies a limitation, mistake, or improved next action |
| Total | 100 |  |

Mastery requires:

- at least 75/100 overall;
- no unauthorised target or unsafe action;
- at least 12/20 for hypothesis quality; and
- successful validation of the original task.

A student who guesses the correct setting but cannot explain the evidence has not demonstrated mastery.

## Observation codes

Use these during live practice:

- I: independent
- P: completed after a prompting question
- D: completed after direct instruction
- U: unsafe or outside scope

Record the most independent level consistently demonstrated. A student should repeat the exercise when essential steps require direct instruction.

## Feedback structure

Give feedback in three parts:

1. Evidence: “You recorded the address before changing it.”
2. Effect: “That made your hypothesis reviewable and preserved rollback.”
3. Next performance: “On the next case, state what result would disprove your hypothesis before running the test.”

## Remediation

If a student struggles:

1. reduce the topology to PC1 and WEB1 with a known-good switch;
2. provide the dependency sequence but not the answer;
3. allow one verbal think-aloud attempt;
4. repeat with a different single fault;
5. reassess independently.

Do not remediate by giving the complete solution procedure.

## Instructor reflection after class

Record:

- percentage reaching mastery;
- most common misconception;
- step requiring the most prompts;
- fault variant that produced the best reasoning;
- time students became independent;
- accessibility or resource barrier observed; and
- one change for the next delivery.
