# GitBook publication plan: MCP customer connection guide

## Intended location

Use a **single customer-facing page** titled **Connect to Claude or ChatGPT**
within the existing API/MCP documentation hierarchy:

- API Reference
  - MCP (create this navigation group only if it does not already exist)
    - Overview (existing page if available)
    - **Connect to Claude or ChatGPT** (new page)
    - Technical reference (existing page if available)

Do **not** add a top-level Customer Integrations section and do not create
four new pages for capabilities, permissions, troubleshooting and setup.
Those are headings within the single new page.

The proposed content is in [GITBOOK-MCP-CUSTOMER-GUIDE.md](GITBOOK-MCP-CUSTOMER-GUIDE.md).
The GitBook page path and IDs must be read from the actual site before editing;
a page has **not** yet been created or published from this PR.

## Checks before publishing

1. Confirm the correct ASC GitBook space, section, and MCP navigation with an
   editor. Do not guess a new live URL.
2. Check the live customer MCP tool inventory and OAuth flows for Claude and
   ChatGPT. Confirm whether customers can only read or can also write
   messages, to-dos, calendars, escalation levels and delivery contacts.
3. Reconcile the current public setup page at
   https://mcp.answeringservicecare.com/ with the actual server behavior.
   That page currently describes mostly read-only access with optional
   create operations and says existing-record edits and billing are unavailable,
   while the GitHub customer plugin describes a broader tool set. Do not
   publish contradictory capabilities.
4. Validate Billing access and the secure ASC payment URL handoff
   independently. Never imply Claude or ChatGPT can take a payment.
5. Verify customer account/line permission boundaries with test accounts,
   including denied cross-account access.
6. Check names, availability status, terms and privacy language with the
   actual product owners before publishing.
7. Publish the single GitBook page under the MCP subsection and link it
   from the official ASC developer/MCP overview; only then add the *verified*
   published URL to the repository README.

The GitHub repository is the canonical source for plugin manifests and skills,
not the GitBook navigation. This PR stages reviewable customer documentation;
**merging the GitHub PR does not publish the page in GitBook.**
