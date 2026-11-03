---
name: setup
description: Help an Answering Service Care customer connect and verify their authorized customer account through OAuth in Claude or ChatGPT. Use after installing the plugin, on connection errors or whenever the customer asks which account or phone the plugin can access.
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
   any write. Explain that Calendar Management and Billing require their own
   account/phone permissions.
5. If OAuth cannot complete or no appropriate records are returned, explain
   the limitation and direct the user to the ASC customer portal or support.
   Do not try another identity, discover hidden IDs, or request a secret.

Run a harmless read-only smoke test before using any write tool. A successful
sign-in does **not** automatically authorize billing, every phone line, or
internal administration.
