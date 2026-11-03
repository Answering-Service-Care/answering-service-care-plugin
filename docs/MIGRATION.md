# Migration from ASC agent-skills PR #2

## Objective

Ship one Answering Service Care customer plugin for **Claude and ChatGPT**
with **one skills tree**, matching the Kauneonga plugin's root-level Claude
layout while adding portable OpenAI/Agent Plugins metadata.

## Sources

- Original customer extraction: [ASC agent-skills PR #2](https://github.com/Answering-Service-Care/agent-skills/pull/2),
  branch `codex/customer-claude-plugin-extraction-20261102`,
  original head `2343c5ad7f6dcf4d08aeb50d195d50b50b4313fb`.
- Existing public research package: `Answering-Service-Care/agent-skills`
  `main`. **Leave unchanged.**
- Reference customer plugin: `Kauneonga/kauneonga-plugin` `main`.
- Destination repository: `Answering-Service-Care/answering-service-care-plugin`.

## Changes

1. Relocate `claude/skills/*` into a single root `skills/*` directory.
2. Relocate `claude/.claude-plugin/plugin.json` and `claude/.mcp.json`
   to the new repository root; use plugin identity
   `answering-service-care-customer` to avoid conflicting with the
   `answering-service-care` public research plugin.
3. Add portable root `plugin.json` and `mcp.json` for ChatGPT without
   duplicating skills.
4. Retain ASC-specific secure billing handoff only in ASC's customer plugin.
5. Retain both Kauneonga's original MIT notice and ASC attribution.
6. Keep all internal Support/Admin MCP integrations in private repositories.
7. Add offline checks and a separate live OAuth/RBAC acceptance checklist.

## Release sequence

1. Review and merge the new customer plugin PR into the new repository.
2. Verify both Claude and ChatGPT OAuth flows using a dedicated test account.
3. Verify account/phone RBAC, Calendar Management and Billing boundaries.
4. Submit each platform independently and wait for approval.
5. Link the new verified commit in legacy ASC agent-skills PR #2, then close
   that older draft as superseded **without merging it**.

Do not expose internal service keys or production test data in this repo.
