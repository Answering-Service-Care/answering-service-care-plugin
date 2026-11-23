# Answering Service Care plugin for Claude

For Answering Service Care customers. Connect Claude to your account with your own
Client Portal login, then ask about your messages, To Dos and who's on call, and make
the changes your login allows.

Try asking: "What came in overnight that needs action?", "Who's on call tonight?" or
"Move Saturday's shift from Sam Lee to Jordan Patel."

## What's included

- **The Answering Service Care connector** at
  `https://mcp.answeringservicecare.com/api/v2/mcp`. Sign in with your Client Portal
  login, and your two-step code if your login uses one.
- **Skills** that guide Claude through common jobs:

| Skill | What it does |
|---|---|
| `answering-service-care` | Picks the right skill for a request, and the order when a job needs several |
| `setup` | Connects your account and checks what your login can reach |
| `message-triage` | Separates the messages that need action now from the ones that can wait, acknowledges them, and records notes |
| `follow-ups` | Lists, adds and closes To Dos, and finds out why a follow-up or callback didn't happen |
| `oncall-changes` | Covers time off, swaps or moves shifts, adds many shifts at once, manages escalation levels, and answers who's on call |
| `contact-delivery` | Updates how on-call people are reached: numbers, texts, email |
| `message-delivery` | Traces a message that didn't arrive and finds the cause |
| `coverage-check` | Finds gaps in upcoming on-call coverage |
| `account-and-access` | Shows who has portal access, the contacts directory and the account's lines |
| `billing-handoff` | Shows your balance and the secure link to pay in the Client Portal |

## Your data and permissions

- Each person connects with their own login and gets the same access they have in
  the Client Portal. Approving a change in Claude never gives your login more access.
- Before a change, the skills show you exactly what will change and ask first.
- It never takes card or bank details in the chat. Payments happen only in the Client
  Portal.
- You can disconnect at any time from Claude's connector settings.
- See our [privacy policy](https://answeringservicecare.com/privacy-policy/) and
  [terms](https://answeringservicecare.com/terms-and-conditions/).

## Help

Setup guide: https://answeringservicecare.com/docs/ai/ask-asc-and-mcp/mcp/claude

Licensed under the MIT License.
