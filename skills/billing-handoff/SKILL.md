---
name: billing-handoff
description: Check an Answering Service Care customer's balance and give them the secure Client Portal link to pay. Use when a customer asks what they owe, whether a bill is overdue, or how to pay their Answering Service Care bill.
---

# ASC balance and secure payment portal

Use this skill only for an Answering Service Care customer's own account. The
signed-in login must have billing access on that account.

1. Find the customer's own account with `list_accounts`. Use an account ID
   returned for that login; never infer or guess an ID.
2. Call `get_asc_billing_summary` for that account. If it returns several
   billable phone lines, show the allowed choices and ask which line before
   calling it again with the selected `phone_id`.
3. Report only the returned balance and overdue amount, when available.
   If the balance can't be retrieved, say so; never describe it as zero.
4. Return the exact `payment_url` from the tool and explain that payment
   must be completed after signing in to the secure ASC customer portal.

Never request, collect, retain or transmit card numbers, CVV, routing numbers,
bank account numbers, payment tokens, or credentials through Claude or ChatGPT.
Never initiate payment or charges from this skill, and never build or guess any
other payment link. If the tool refuses account or billing access, do not try
another identity or account to work around that restriction.
