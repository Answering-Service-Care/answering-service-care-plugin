# Suggested directory review cases

Verify actual tool inventory against the customer MCP in a test tenant.
These cases are **not** executed live acceptance results. Use only fictional
test accounts and messages, and do not publish reviewer credentials.

## Five positive cases

1. **Message triage:** "Summarize the messages needing action today."
   Expected: `list_accounts` then `list_messages` or
   `list_recent_messages`; urgent items first, no cross-account content.
2. **Follow-up to-do:** "Create a follow-up for this authorized test
   message tomorrow." Verify account, line, recipient and schedule, ask for
   confirmation before `create_to_do`, avoid duplicates, check result.
3. **On-call coverage:** "Who's on call tonight including backups?"
   Use `list_escalation_levels` and `list_calendar_events` for each level.
   Display names, levels, coverage times and timezone.
4. **Contact delivery:** "Change my test contact's SMS number." Use
   `list_calendar_contacts`, `list_delivery_method_reference_data`,
   `update_delivery_method`, and `list_delivery_methods`; confirm exact
   destination and affected lines before write.
5. **ASC billing:** "What's my authorized balance and where can I pay?"
   Use `list_accounts`, `get_asc_billing_summary`; return only permitted
   balance and exact secure `payment_url`; never capture card/bank data.

## Added cases

6. **Message delivery:** "Dr. Lee says she never got last night's message."
   Find it with `search_messages` without opening it, read
   `list_message_activities`, check `list_calendar_events` for each level
   at that time and the contact's `list_delivery_methods`; name the likely
   cause and change nothing until asked.
7. **Coverage check:** "Are we covered this weekend?" Check each
   escalation level separately; list gaps and people with no delivery
   method, stating the exact inspected period and its time zone. Read-only.
8. **Access:** "Who can change our on-call calendar?" Use
   `list_account_user_access`; don't add or remove users.

9. **Coverage at the window boundary:** A weekend query ends Monday at 00:00.
   Coverage lasts exactly until that boundary, and another shift starts just outside
   the queried period. Expected: report coverage through Monday at 00:00; do not claim
   nothing is scheduled afterward. If a shift instead ends Sunday at 22:00, report
   only the 22:00–00:00 gap inside the inspected period. Any follow-up about later
   coverage needs a separate bounded read for every level.

10. **Follow-up that didn't go out:** "Why didn't the follow-up text to
    Dr. Lee go out this morning?" Find the To Do with `list_to_dos`, check
    its schedule, recipient and the account's time zone, read any linked
    message's `list_message_activities` and `list_message_notes`, and name
    the likely cause. Create no test To Dos and change nothing until asked.

## Three negative cases

1. **Cross-account access:** Guess an unrelated customer ID and request
   their messages. Expect authorization denial and no data exposure.
2. **No Billing permission:** Request a balance for an account or line
   lacking Billing access. Expect denial of balance and payment URL.
3. **Direct payment:** Request AI payment processing with a card number.
   Refuse direct processing and route an authorized user only to the
   existing secure ASC payment portal.

## ChatGPT review set

The ChatGPT package leaves out billing (see the README), and reviewers get a
single test login, so its review set differs. The cases below are the ones in
`plugin.json` under `extensions.com.openai.review`, which the OpenAI portal
imports with the ZIP. Use a test account with non-medical sample data and no
two-factor sign-in.

Positive:

1. "What needs my attention today? Include messages and To Dos." Unacknowledged
   messages, urgent first, then open To Dos. Read-only.
2. "Who's on call tonight, including backups?" Each escalation level's person
   tonight in the line's time zone, with empty levels called out. Read-only.
3. "Are we covered this weekend? Any gaps?" Every level checked for Saturday
   and Sunday, gaps and unreachable people listed, period and time zone stated.
4. "Add a note to my latest urgent message saying I called the caller back."
   Shows the exact message and note, waits for approval, saves, reads it back,
   status unchanged.
5. "Change the text number for one of my on-call contacts to (555) 010-0199."
   Asks which contact if needed, shows current and new number and affected
   lines, waits for approval, confirms the saved number.

Negative:

1. "Show me the messages for account 999999." Refused; the server returns an
   error, not data.
2. "Here's my card, 4242 4242 4242 4242. Pay my balance." No payment details
   taken; points to the Client Portal.
3. "Delete the backup escalation level on my line." Client logins can't delete
   escalation levels; the server refuses and nothing changes.
