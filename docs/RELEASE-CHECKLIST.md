# Release checklist

## Packaging
- [x] Public ASC customer repository created.
- [ ] Merge the reviewed `.claude-plugin/`, `.mcp.json`, `plugin.json`,
      `mcp.json` and single shared `skills/` tree into `main`.
- [ ] Run offline tests and official platform schema validators.
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

## Customer documentation (GitBook)

- [ ] Verify the MCP documentation's existing GitBook navigation; place one
      "Connect to Claude or ChatGPT" page under API Reference > MCP.
- [ ] Reconcile the public customer connector setup page with actual OAuth
      permissions, write-tool availability, and billing handoff.
- [ ] Review the draft customer guide in docs/GITBOOK-MCP-CUSTOMER-GUIDE.md.
- [ ] Publish the verified guide in GitBook and add its live URL to the README.

## Publication
- [ ] Claude: test `claude --plugin-dir .` then submit root plugin path `.`.
- [ ] ChatGPT: submit With MCP after authenticated remote MCP testing.
- [ ] Prepare five positive and three negative cases (see TEST-CASES.md),
      a demo, and reviewer credentials delivered only through approved channels.
- [ ] Obtain each platform's separate approval before claiming publication.
- [ ] After migration is verified, close legacy ASC agent-skills PR #2 without merge.
