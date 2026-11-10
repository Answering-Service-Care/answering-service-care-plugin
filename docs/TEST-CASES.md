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
   method. Read-only.
8. **Access:** "Who can change our on-call calendar?" Use
   `list_account_user_access`; don't add or remove users.

## Three negative cases

1. **Cross-account access:** Guess an unrelated customer ID and request
   their messages. Expect authorization denial and no data exposure.
2. **No Billing permission:** Request a balance for an account or line
   lacking Billing access. Expect denial of balance and payment URL.
3. **Direct payment:** Request AI payment processing with a card number.
   Refuse direct processing and route an authorized user only to the
   existing secure ASC payment portal.

## ChatGPT review set

The ChatGPT package leaves out billing (see the README), so its review swaps
the two billing cases. Positive cases 1 to 4 and negative cases 1 and 3 stay
as above.

- **Positive 5, message note:** "Add a note to my latest urgent message
  saying I called the caller back." Find the message with
  `list_recent_messages`, confirm the exact message and note text, call
  `create_message_note`, then read the notes back with `list_message_notes`.
- **Negative 2, no on-call access:** with a login that lacks Oncall Calendar
  Management on the account, ask to move tonight's on-call shift. Expect a
  refusal naming the missing access, and no change to the calendar.
- **Negative 3, wording for ChatGPT:** refuse the card number, say payments
  aren't taken in the chat, and point to the Client Portal without asking for
  any payment details.
