# Maintaining this package

One package serves Claude and ChatGPT, using the same sign-in-protected
customer connector: `https://mcp.answeringservicecare.com/api/v2/mcp`.

Keep this repository limited to authenticated customer workflows. Do not add unrelated tools or additional service endpoints.

## Layout

| Path | Purpose |
|---|---|
| `plugins/answering-service-care/` | The Claude plugin: the folder submitted to the Claude directory |
| `plugins/answering-service-care/.claude-plugin/plugin.json` | Claude plugin identity and metadata |
| `.claude-plugin/marketplace.json` | Claude marketplace listing this plugin, so customers can install it from this repository |
| `plugins/answering-service-care/.mcp.json` | Claude connector configuration |
| `plugins/answering-service-care/plugin.json` | Portable Agent Plugins manifest, including the ChatGPT listing (the ZIP build adds its logo fields) |
| `plugins/answering-service-care/mcp.json` | Portable connector configuration with the sign-in declaration |
| `plugins/answering-service-care/skills/` | One shared source of skills for Claude and ChatGPT |
| `plugins/answering-service-care/assets/logo.png` | ChatGPT listing logo: the 512 px icon the connector already serves |
| `scripts/build_chatgpt_package.py` | Builds the ChatGPT upload ZIP |
| `docs/` | Review test cases and the release checklist |
| `tests/` | Offline structure and safety checks |

## Scope

Customer workflows only, limited to what the signed-in customer's own Client
Portal login allows: messages, To Dos, on-call schedules, escalation levels,
calendar contacts and how they're reached, and, in the Claude package only,
the balance with a secure payment-portal link.

Account membership, sign-in scopes and per-line permissions are enforced by
the server; skills never grant access. Skills confirm changes before making
them, including outbound calls, texts and emails, and check the result.

Out of scope: privileged server operations, service keys, code and log access, and taking payments.

## Claude

- Test with `claude --plugin-dir plugins/answering-service-care`.
- `claude plugin validate --strict .` checks the marketplace;
  `claude plugin validate --strict plugins/answering-service-care` checks the plugin.
- For the Claude Directory, submit this repository with plugin path
  `plugins/answering-service-care`. From an organization that isn't Verified, the
  directory accepts only Markdown, JSON, images and the license in that folder, and
  refuses a version where a file names an image, so scripts, tests and AGENTS.md stay
  outside it.

## ChatGPT

- Build the upload ZIP with `python3 scripts/build_chatgpt_package.py`
  (written to `dist/`). Submit with the **With MCP** flow, not Skills only.
- The ChatGPT package leaves out billing: OpenAI's commerce rules don't allow a
  link to pay a service bill, and ChatGPT picks up every folder under
  `skills/` in the ZIP, so the build drops `billing-handoff` and the main skill's billing
  row. The ChatGPT listing text in `plugin.json` doesn't mention billing.
- Before submitting, the listing still needs a demo video, and the
  domain-check token served at
  `https://mcp.answeringservicecare.com/.well-known/openai-apps-challenge`.
  See the ChatGPT review set in [TEST-CASES.md](TEST-CASES.md).
- `mcp.json` relies on sign-in discovery. Confirm the client registration
  method and callback URLs against the live server before publishing; never
  put secrets, scopes or token URLs in the manifests.

## Checks

Run `python3 tests/test_package.py` for the offline checks. They are not a
live sign-in test or a directory approval. See the
[release checklist](RELEASE-CHECKLIST.md) and
[review test cases](TEST-CASES.md) before submitting.

## Rules

- Keep both copyright notices in `LICENSE`; the offline checks look for them.
- Never commit service keys, reviewer credentials or real customer data.
- One skills tree: no platform-specific copies of a skill.

