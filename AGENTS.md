# Development rules

This repository contains only customer-facing ASC Claude and ChatGPT plugin
metadata, MCP configuration, and skills. Keep **one shared** skills tree, in
`plugins/answering-service-care/skills/`. That folder is the Claude plugin and
what the Claude directory scans: keep only Markdown, JSON, the logo PNG and the
license there, with no scripts, no AGENTS.md or CLAUDE.md, and no file that names
the logo (`tests/test_package.py` checks this).
Do not put customer skills under `claude/` or `chatgpt/` independently.

- Never put credentials, tokens, signing keys, production customer data,
  Admin/Support tools, or secret service-key instructions in this repository.
- `plugins/answering-service-care/` is the package root for every app: the portable
  `plugin.json` and `mcp.json` sit beside the Claude manifest and the skills. Don't add
  logo fields to the portable `plugin.json`; the ChatGPT build adds them.
- Both `plugins/answering-service-care/.mcp.json` (Claude) and `plugins/answering-service-care/mcp.json` (portable) must use only
  `https://mcp.answeringservicecare.com/api/v2/mcp` for the customer server.
- Do not add unrelated public research, pricing, documentation or privileged service tools to this customer plugin.
- All customer actions require matching OAuth membership and backend RBAC.
  Never fabricate account IDs, phone IDs, calendar events or payment URLs.
- Ask confirmation before writing that sends calls/texts/emails, changes
  coverage, or deletes items. Verify the result before claiming success.
- Never accept a card, bank account, or payment credential through an AI chat.
  A billing operation ends at an authenticated secure payment-link handoff.
- Preserve Kauneonga LLC's original MIT copyright notice for adapted skills.
- Skills name only tools the customer connector serves. A tool that is
  announced but not yet served may be named only with a one-line fallback
  saying what to do when it isn't in the tool list.
- Customers can't delete an escalation level. Skills never offer to.
- Write for the customer: plain language, no em dashes, made-up example
  names such as Dr. Lee and Northwind.
- Add every new skill to `EXPECTED_SKILLS` in `tests/test_package.py` and to
  the skills table in `README.md`.
- Run `python3 tests/test_package.py` before PR submission.
