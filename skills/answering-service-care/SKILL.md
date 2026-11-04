---
name: answering-service-care
description: Pick the right customer skill for an Answering Service Care request. Use for broad requests, questions about available customer workflows, or tasks spanning messages, on-call coverage, contacts and follow-ups.
---

# Pick the right skill

Match the request to the relevant skill below and follow it. If multiple are
needed, explain the order. If a requested tool is missing, say so and use the
customer portal; never assume availability or improvise privileged access.

| Request | Skill |
|---|---|
| Catch up on messages; review or update messages, notes and follow-up to-dos | `message-triage` |
| See on-call coverage, change a shift or escalation level | `oncall-changes` |
| Update a contact or how they receive a call, SMS, email or other delivery | `contact-delivery` |
| Check the balance or get the secure link to pay in the Client Portal | `billing-handoff` |
| Set up the ASC customer connection | `setup` |

**Someone wasn't reached:** check who was on call with `oncall-changes`, then
how they are reached with `contact-delivery`.

## Access

Use only accounts, phones and records returned by the customer's signed-in
Answering Service Care connection. Answering Service Care enforces account
memberships and line permissions; a skill never grants access. Never select another account
or identity to bypass denial. Ask for confirmation before consequential writes
and verify the action's returned result.

For documentation questions, use `search_resources` and `read_resource_page`
if the connected server exposes them. Cite the help-center page you read.

This package covers only what a customer can do with their own Client Portal
login. Changes to phone lines, scripts or AI answering settings go to the
customer's account manager.
