# Connect Answering Service Care to Claude or ChatGPT

Use your AI assistant to work with information from your **Answering Service Care (ASC)** customer account through a secure connection.

> **Availability:** This guide describes the customer MCP integration being prepared for Claude and ChatGPT. Connection options, available actions and any write permissions depend on your AI platform, your ASC account and the live connector configuration. The plugin is not generally available in either directory until its listing and OAuth integration have been approved and tested.

## Connect your account

The ASC customer connection uses **Model Context Protocol (MCP)** and a normal ASC sign-in. Your AI assistant does not need your password pasted into a chat.

1. In a supported Claude or ChatGPT integration, select the **Answering Service Care** connection or add a custom MCP server if your app or workspace supports that option.
2. If a server URL is required, use:

   `https://mcp.answeringservicecare.com/api/v2/mcp`

3. Follow the OAuth sign-in flow to your usual ASC customer portal. Review the permissions shown and approve only if you want to connect.
4. Start with a read-only question such as "Which ASC accounts can I access?" or "Show my recent messages." If your login has access to multiple accounts or phone lines, select the one you want to use.

Do not paste a password, API key, access token, card number or bank details into the conversation.

**Claude:** Once the official ASC Claude plugin is available, follow its installation prompt and complete customer sign-in. Until directory publication, availability depends on the Claude client and its support for custom remote MCP connections.

**ChatGPT:** Once the official ASC ChatGPT plugin is available, connect it and complete customer sign-in. Workspace policies and support for custom remote MCP connections may affect availability before publication.

## What you can ask

The connected customer MCP is intended to help you:

- **Review messages:** Catch up on recent or unread messages, search for a specific caller and identify follow-ups.
- **Review follow-up tasks:** See relevant To Dos and what needs attention.
- **Review on-call coverage:** Find who's on call for a line, including applicable escalation levels and schedules.
- **Review delivery contacts:** Check which phone numbers, email addresses or other methods are configured for an on-call contact.

**Changes to data:** Some accounts may be able to create or update follow-ups, on-call schedules, escalation levels or delivery contacts. These actions are **not guaranteed** for every account or client: they require a supported tool, the correct permissions, and confirmation of any action that could send calls, email or text messages or change coverage. If a requested change is not enabled, use the ASC customer portal or contact ASC.

**Billing:** An ASC-only, read-only account-balance summary and secure payment-portal link are part of the plugin's planned customer workflow but still require live permission and backend verification. Do not rely on that function until it is explicitly enabled for your account. **Payments are never taken inside Claude or ChatGPT.** Use only an authenticated link supplied by ASC to complete payment in the secure portal; do not share card or banking information in a chat.

Actual capabilities are determined by the live MCP server after authentication, not by this guide or by a plugin's descriptive skills.

## Account access and security

- Your ASC login determines which customer accounts and phone lines you are allowed to access.
- Calendar-management and billing permissions are separate from ordinary message-reading access.
- The assistant should show the intended change and ask for confirmation before consequential updates.
- A rejected request or a missing tool is not permission to try a different identity or guess another account ID.
- Ask the assistant to summarize only information you need. Customer messages can contain personal or sensitive information; follow your organization's handling requirements.

This is a **customer** integration. Internal ASC or Kauneonga administrator, support, service-key, source-code and log-management tools are **not available** through this public customer plugin.

## Troubleshooting

| Issue | What to try |
|---|---|
| No ASC connection appears | The plugin may not yet be published for your platform. Check supported connections or contact ASC. |
| Sign-in fails | Verify you're using the normal ASC customer portal and complete the OAuth approval flow again. Don't share credentials in chat. |
| An account or line is missing | Confirm your ASC user has permission to access that account or line. |
| An update cannot be made | The live connector may allow read-only access, or your user may lack the required permission. Make the change in the customer portal. |
| A balance or payment link isn't available | Billing access or the ASC billing feature may be unavailable. Use the authenticated ASC customer portal instead. |
| The assistant reports an action completed, but nothing changed | Re-check the record in the ASC portal. Do not assume a change succeeded without confirmation from the connector. |

## Useful links

- [ASC customer portal](https://secure.answeringservicecare.com/)
- [ASC developer and MCP overview](https://answeringservicecare.com/developers/)
- [ASC customer MCP sign-in information](https://mcp.answeringservicecare.com/)
- [Customer plugin source and release notes](https://github.com/Answering-Service-Care/answering-service-care-plugin)

### Developer note: public research MCP versus customer MCP

ASC also offers an **unauthenticated, read-only public information MCP** at
`https://answeringservicecare.com/mcp`. It can answer questions about ASC services
and pricing but **cannot access your account**. Use the authenticated customer endpoint
above for account information. The documentation MCP at
`https://answeringservicecare.com/docs/~gitbook/mcp` is also separate.
