---
name: setup
description: Help an Answering Service Care customer connect Claude or ChatGPT to their account with their Client Portal login, and check which accounts and phone lines it can reach. Use after installing the plugin, when the connection fails, or when the customer asks what the plugin can access.
---

# Connect the ASC customer account

1. Ask the user to connect the **Answering Service Care customer** MCP
   integration using the platform's own OAuth consent flow. Never request a
   portal password, access token or API key in chat.
2. The customer endpoint is
   `https://mcp.answeringservicecare.com/api/v2/mcp`; do not confuse it with
   ASC's unauthenticated research MCP at `https://answeringservicecare.com/mcp`.
3. After authorization, use `list_accounts` to show only accounts returned for
   the signed-in identity. If more than one account is returned, ask which one
   should be used for the current request.
4. If needed, verify access to a single phone/line with a read-only tool before
   any write. Explain that Oncall Calendar Management and billing access are
   separate permissions on each account.
5. If OAuth cannot complete or no appropriate records are returned, explain
   the limitation and direct the user to the ASC customer portal or support.
   Do not try another identity, discover hidden IDs, or request a secret.

Run a harmless read-only smoke test before using any write tool. A successful
sign-in does **not** automatically allow billing, every phone line, or changes
to phone lines, scripts and AI answering settings, which stay with the
customer's account manager.
