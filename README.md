# Answering Service Care

Customer workflows for **Claude and ChatGPT** in one package, using the same
OAuth-protected Answering Service Care (ASC) customer MCP server:

`https://mcp.answeringservicecare.com/api/v2/mcp`

This repository is intentionally separate from
[Answering-Service-Care/agent-skills](https://github.com/Answering-Service-Care/agent-skills),
which retains the public research/pricing and docs MCP integrations. Internal
Admin and Support plugins must remain in private repositories.

**Plugin identity:** Both Claude and portable manifests use `answering-service-care`.
The legacy `agent-skills` repository has a *separate* research manifest with the
same name. Before distributing or publishing both manifests as separate plugins,
rename the research manifest or designate the new customer package as the sole
published plugin identity. Keep the existing public research MCP server intact.

## Repository layout

| Path | Purpose |
|---|---|
| `.claude-plugin/plugin.json` | Claude plugin identity and metadata |
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

Use `claude --plugin-dir .` to test from the repository root.
For the Claude Directory, submit this repository with plugin path `.`
after the code has merged to `main` and OAuth has passed live testing.
The root Claude layout follows `Kauneonga/kauneonga-plugin`.

## ChatGPT / Codex

Use the portable `plugin.json`, `mcp.json` and shared `skills/` at
the repository root. Submit using the **With MCP** flow, not Skills only,
because the integration requires the remote authenticated ASC MCP.

The OAuth manifest intentionally relies on OAuth discovery. Confirm the
actual client registration approach and callback URLs with the customer
server and platform before publication. Do not guess OAuth client secrets,
scopes or token URLs.

## Customer documentation

A [GitBook-ready customer connection guide](docs/GITBOOK-MCP-CUSTOMER-GUIDE.md)
and [MCP navigation/publishing notes](docs/GITBOOK-MCP-NAVIGATION.md)
are available for review. The proposed GitBook location is **API Reference
> MCP > Connect to Claude or ChatGPT**. This is a draft; merging this
repository does not publish the guide to GitBook. Review live feature
availability, OAuth permissions, and billing behavior before publication.

## Validation

Run `python3 tests/test_package.py` for offline structural checks.
This is not a live OAuth test, schema certification or directory approval.
See [release checklist](docs/RELEASE-CHECKLIST.md) and
[acceptance cases](docs/TEST-CASES.md) before submission.

## Separation and migration

The legacy [agent-skills PR #2](https://github.com/Answering-Service-Care/agent-skills/pull/2)
was closed as superseded without merging. The new customer plugin's initial PR
#1 was merged into this repository. Keep the public research files unchanged.
