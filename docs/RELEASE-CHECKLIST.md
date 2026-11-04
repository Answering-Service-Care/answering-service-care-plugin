# Release checklist

## Packaging
- [x] Public ASC customer repository created.
- [x] Merge the reviewed `.claude-plugin/`, `.mcp.json`, `plugin.json`,
      `mcp.json` and single shared `skills/` tree into `main`.
- [x] Claude marketplace file; `claude plugin validate --strict` passes for
      the plugin and the marketplace, and a clean Claude Code install loads
      the six skills and the connector.
- [ ] Run the ChatGPT plugin schema validation.
- [ ] Confirm no secrets, production customer records, internal Support/Admin
      tools, or duplicated skills.
- [ ] Check license, copyright, approved assets and production URLs.
- [ ] Confirm platform listing names are available and acceptable.

## Live MCP / OAuth
- [ ] Verify MCP protected-resource and OAuth discovery metadata.
- [ ] Verify actual ChatGPT client registration method, callbacks and scopes.
- [ ] Verify Claude OAuth first sign-in, reconnection and permissions.
- [ ] Verify ChatGPT OAuth first sign-in, reconnection and permissions.
- [ ] Test an ASC customer who can access multiple accounts and phones.
- [ ] Confirm guessing another customer's account or phone ID fails.
- [ ] Confirm missing Calendar Management permission denies unauthorized edits.
- [ ] Confirm missing Billing permission denies balance/payment URLs.
- [ ] Confirm allowed billing returns only the exact backend secure payment URL.
- [ ] Confirm no card/bank collection or payment execution in AI chat.
- [ ] Confirm consequences and explicit confirmation before writes.
- [ ] Validate messages, follow-ups, schedules, contact delivery and billing.
- [ ] Verify separate Client AI MCP tools before adding any AI management skills.

## Publication
- [ ] Claude: test `claude --plugin-dir .` then submit root plugin path `.`.
- [ ] ChatGPT: submit With MCP after authenticated remote MCP testing.
- [x] ChatGPT listing: subtitle within 30 characters, support URL, no billing
      in the listing text; `scripts/build_chatgpt_package.py` builds the ZIP
      without `billing-handoff`.
- [x] ChatGPT listing logo: `assets/logo.png`, the connector's 512 px icon.
- [ ] ChatGPT listing: a demo video URL.
- [ ] ChatGPT domain check: serve the portal's token at
      `/.well-known/openai-apps-challenge` on mcp.answeringservicecare.com
      (needs the gateway update that reads `OPENAI_APPS_CHALLENGES`, then the
      token set on the ASC connector's Worker).
- [ ] ChatGPT: confirm the upload validator accepts `mcp.json`'s
      `extensions."com.openai".auth` on the server entry (the generic
      agent-plugins.org MCP schema rejects extra server properties).
- [ ] Legal sign-off on health data: OpenAI lists PHI as restricted data.
- [ ] Prepare five positive and three negative cases (see TEST-CASES.md),
      a demo, and reviewer credentials delivered only through approved channels.
- [ ] Obtain each platform's separate approval before claiming publication.
- [x] The earlier Claude-only draft in agent-skills was closed without merging.
