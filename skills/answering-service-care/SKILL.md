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
| Check an authorized ASC balance or obtain a secure payment portal link | `billing-handoff` |
| Set up the ASC customer connection | `setup` |

**Someone wasn't reached:** check who was on call with `oncall-changes`, then
how they are reached with `contact-delivery`.

## Authorization and source of truth

Use only accounts, phones and records returned by the authorized ASC customer
MCP session. Account memberships and line permissions must be enforced by the
backend; do not treat a skill as an access grant. Never select another account
or identity to bypass denial. Ask for confirmation before consequential writes
and verify the action's returned result.

For documentation questions, use `search_resources` and `read_resource_page`
if the connected server exposes them. Cite the help-center page you read.

This public package is customer-facing only. Admin, Support, Super Admin,
service-key and code/log workflows are out of scope.
