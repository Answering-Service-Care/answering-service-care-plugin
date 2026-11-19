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
| Set up the ASC customer connection | `setup` |
| Catch up on messages and find anything urgent | `message-triage` |
| Acknowledge or update messages, add notes, read a message's history | `message-triage` |
| See, add or close follow-up To Dos, or find out why a follow-up or callback didn't happen | `follow-ups` |
| Who's on call now or tonight; cover time off, swap or move a shift | `oncall-changes` |
| Add many shifts at once, or set the line's standard shift times | `oncall-changes` |
| See, add, edit or copy escalation levels | `oncall-changes` |
| Update a contact or how they receive a call, SMS, email or other delivery | `contact-delivery` |
| A message didn't arrive, arrived late, or went to the wrong person | `message-delivery` |
| Check upcoming on-call coverage for gaps | `coverage-check` |
| See who has portal access, look up or export contacts, list the account's lines | `account-and-access` |
| Check the balance or get the secure link to pay in the Client Portal | `billing-handoff` |

**Someone wasn't reached:** start with `message-delivery`. It checks the message's
history, who was on call and how they're reached, then hands the fix to
`oncall-changes` or `contact-delivery`.

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
