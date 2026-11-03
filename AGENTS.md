# Development rules

This repository contains only customer-facing ASC Claude and ChatGPT plugin
metadata, MCP configuration, and skills. Keep **one shared** `skills/` tree.
Do not put customer skills under `claude/` or `chatgpt/` independently.

- Never put credentials, tokens, signing keys, production customer data,
  Admin/Support tools, or secret service-key instructions in this repository.
- Both `.mcp.json` (Claude) and `mcp.json` (portable) must use only
  `https://mcp.answeringservicecare.com/api/v2/mcp` for the customer server.
- Do not copy the public research/pricing and documentation MCP definitions
  from `Answering-Service-Care/agent-skills` into this customer plugin.
- All customer actions require matching OAuth membership and backend RBAC.
  Never fabricate account IDs, phone IDs, calendar events or payment URLs.
- Ask confirmation before writing that sends calls/texts/emails, changes
  coverage, or deletes items. Verify the result before claiming success.
- Never accept a card, bank account, or payment credential through an AI chat.
  A billing operation ends at an authenticated secure payment-link handoff.
- Preserve Kauneonga LLC's original MIT copyright notice for adapted skills.
- Run `python3 tests/test_package.py` before PR submission.
