# Answering Service Care

Customer workflows for **Claude and ChatGPT** in one package, using the same
OAuth-protected Answering Service Care (ASC) customer MCP server:

`https://mcp.answeringservicecare.com/api/v2/mcp`

This repository is intentionally separate from
[Answering-Service-Care/agent-skills](https://github.com/Answering-Service-Care/agent-skills),
which retains the public research/pricing and docs MCP integrations. Internal
Admin and Support plugins must remain in private repositories.

**Plugin identity:** Both Claude and portable manifests use `answering-service-care`.
The public research plugin in `agent-skills` is renamed to
`answering-service-care-research` (Answering-Service-Care/agent-skills#3), so the
two can be published side by side. Its public research MCP server is unchanged.

## Repository layout

| Path | Purpose |
|---|---|
| `.claude-plugin/plugin.json` | Claude plugin identity and metadata |
| `.claude-plugin/marketplace.json` | Claude marketplace that lists this plugin, so customers can install it from this repository |
| `.mcp.json` | Claude customer MCP server configuration |
| `plugin.json` | Portable Agent Plugins / OpenAI manifest |
| `mcp.json` | Portable remote MCP configuration with OAuth declaration |
| `skills/` | **One shared source** for Claude and ChatGPT |
| `docs/` | Migration, acceptance tests, and release checklist |
| `tests/` | Offline structure and security checks |

Platform manifests both use the same skill files without duplicate copies.
Each platform must independently authenticate customers and pass OAuth tests.

## Customer capabilities

- Review authorized messages, activity history, and follow-up to-dos.
- View or change authorized on-call schedules, escalation levels, calendar
  contacts and contact-delivery methods.
- For **ASC only**, read a limited balance with Billing permission and open
  the **exact secure ASC payment URL supplied by the connector**.
- Neither Claude nor ChatGPT requests card or bank details, processes
  payments, or charges a customer.

Backend OAuth, account membership, scope and per-line permissions are the
source of truth. Skills do not grant access. Confirm consequential writes
including outbound calls, SMS or emails, and verify the returned result.

**Excluded:** internal Admin, Super Admin or Support tools; service keys;
code/log access; direct payments. This initial extraction does not claim
additional Client AI management tools until the customer MCP tool inventory
and permission boundaries are verified.

## Claude

Install in Claude Code (2.1.275 or later):

```
/plugin install answering-service-care --marketplace Answering-Service-Care/answering-service-care-plugin
```

On older versions, add the marketplace first, then install:

```
/plugin marketplace add Answering-Service-Care/answering-service-care-plugin
/plugin install answering-service-care@answering-service-care
```

A Claude Team or Enterprise owner can roll it out to everyone under
Organization settings > Plugins & skills by adding this repository.
After installing, the customer signs in with their Client Portal login when
Claude first uses the connector.

Use `claude --plugin-dir .` to test from the repository root, and
`claude plugin validate --strict .` to check the marketplace and plugin
manifests. For the Claude Directory, submit this repository with plugin path
`.` after OAuth has passed live testing. The root Claude layout follows
`Kauneonga/kauneonga-plugin`.

## ChatGPT / Codex

Use the portable `plugin.json`, `mcp.json` and shared `skills/` at
the repository root. Submit using the **With MCP** flow, not Skills only,
because the integration requires the remote authenticated ASC MCP.

The OAuth manifest intentionally relies on OAuth discovery. Confirm the
actual client registration approach and callback URLs with the customer
server and platform before publication. Do not guess OAuth client secrets,
scopes or token URLs.

## Validation

Run `python3 tests/test_package.py` for offline structural checks.
This is not a live OAuth test, schema certification or directory approval.
See [release checklist](docs/RELEASE-CHECKLIST.md) and
[acceptance cases](docs/TEST-CASES.md) before submission.

## Separation and migration

The legacy [agent-skills PR #2](https://github.com/Answering-Service-Care/agent-skills/pull/2)
was closed as superseded without merging. The new customer plugin's initial PR
#1 was merged into this repository. Keep the public research files unchanged.
