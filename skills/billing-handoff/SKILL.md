---
name: billing-handoff
description: Check a customer's authorized Answering Service Care account balance and provide the secure ASC portal link to pay. Use when a customer asks what they owe, whether an ASC balance is overdue, or how to pay an ASC bill.
---

# ASC balance and secure payment portal

Use this skill only for Answering Service Care customers. It is not a Kauneonga
billing function. The customer's signed-in account must grant Billing access.

1. Find the customer's own account with `list_accounts`. Use an account ID
   returned for that login; never infer or guess an ID.
2. Call `get_asc_billing_summary` for that account. If it returns several
   billable phone lines, show the allowed choices and ask which line before
   calling it again with the selected `phone_id`.
3. Report only the returned balance and overdue amount, when available.
   If the billing backend is unavailable, do not describe the balance as zero.
4. Return the exact `payment_url` from the tool and explain that payment
   must be completed after signing in to the secure ASC customer portal.

Never request, collect, retain or transmit card numbers, CVV, routing numbers,
bank account numbers, payment tokens, or credentials through Claude or ChatGPT.
Never initiate payment or charges from this skill. Do not generate or guess an
EasyPay /pay/:id notice link. If the tool refuses account or Billing access,
do not try another identity or account to work around that restriction.
