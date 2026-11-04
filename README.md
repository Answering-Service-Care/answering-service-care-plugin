# Answering Service Care for Claude and ChatGPT

For Answering Service Care customers. Connect Claude or ChatGPT to your account
with your own Client Portal login, then ask about your messages, To Dos and
who's on call, and make the changes your login allows.

## What you can do

- **Catch up on messages.** See what needs action first, add or delete a note,
  mark a message read or unread, acknowledge it, change its status, or add a
  new message.
- **Follow up.** Set up a To Do (a call, text or email, now or on a schedule),
  or delete one.
- **Check and change who's on call.** See who's on call tonight and who backs
  them up. If your login has **Oncall Calendar Management** access, cover time
  off, swap or move shifts, change escalation levels, and update your on-call
  contacts and how each one is reached.
- **See your balance (Claude).** If your login has billing access, see your
  balance and get a secure link to pay in the Client Portal.

Try asking: "What came in overnight that needs action?", "Who's on call
tonight?" or "Move Saturday's shift from Dr. Lee to Dr. Patel."

Before any change, Claude or ChatGPT tells you exactly what it will do and asks
you to confirm.

## What it won't do

- It never asks for card or bank details, and nothing is paid in the chat.
- It works only with the accounts your Client Portal login can see.
- Phone lines, scripts and AI answering settings stay with our team. If you
  ask for one of these, it tells you and suggests contacting your account
  manager.

## Install

### Claude

**Your whole team (Claude Team or Enterprise):** an owner of your Claude
organization opens **Organization settings > Plugins & skills** and adds this
repository, `Answering-Service-Care/answering-service-care-plugin`.

**Claude Code:**

```
/plugin install answering-service-care --marketplace Answering-Service-Care/answering-service-care-plugin
```

On Claude Code older than 2.1.275, add the marketplace first:

```
/plugin marketplace add Answering-Service-Care/answering-service-care-plugin
/plugin install answering-service-care@answering-service-care
```

**Just the connector:** in Claude, open **Settings > Connectors** and add a
custom connector with this address:
`https://mcp.answeringservicecare.com/api/v2/mcp`.
See the [Claude setup guide](https://answeringservicecare.com/docs/ai/ask-asc-and-mcp/mcp/claude).

### ChatGPT

Add the connector address `https://mcp.answeringservicecare.com/api/v2/mcp`
in ChatGPT. See the
[ChatGPT setup guide](https://answeringservicecare.com/docs/ai/ask-asc-and-mcp/mcp/chatgpt).

### Sign in

The first time Claude or ChatGPT uses Answering Service Care, it opens our
sign-in page. Sign in with your Client Portal login, enter your two-factor
code if you use one, and allow access.

## Your data and permissions

- Each person connects with their own login, and gets the same access they
  have in the Client Portal. Approving a change in the app never gives your
  login more access.
- You can disconnect at any time from your AI app's connector settings.
- See our [privacy policy](https://answeringservicecare.com/privacy-policy/)
  and [terms](https://answeringservicecare.com/terms-and-conditions/).

## Help

- [Ask ASC and MCP guide](https://answeringservicecare.com/docs/ai/ask-asc-and-mcp/mcp)
- Your account manager, or [success@answeringservicecare.com](mailto:success@answeringservicecare.com)

---

Maintaining this package? See [docs/MAINTAINING.md](docs/MAINTAINING.md).
Licensed under the [MIT License](LICENSE).
