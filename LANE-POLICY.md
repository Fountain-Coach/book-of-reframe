# Reframe lane policy

This is the public explanation of the current routing contract. It is a policy projection, not proof that every
capability is live-accepted or released.

## Default

For writer-facing work, Reframe elects the best eligible paid lane when one is configured, authorised, constructible,
and healthy. The decision is made once and carries its provider, client, and budget. Internal delegation to bounded
on-device work is an implementation detail and is not presented as a separate assistant or ceremony.

An explicit local-only instruction is authoritative. On-device work is the appropriate path for bounded, private,
deterministic, or offline tasks. Provider presence alone does not elect a paid lane, and a paid failure is reported as
a typed failure rather than silently becoming a different lane.

## What this makes possible

The paid lane can support larger-context, open-ended reasoning; sustained manuscript coaching; reference research;
identity escalation; and other economically meaningful semantic work that is not suitable for a bounded on-device
window. These are governed possibilities. The capability atlas and live evidence still decide what Reframe may teach
as working now.

## Evidence boundary

The current development snapshot has 55 capability identities, 24 executable, 31 unavailable, and 2 live-accepted.
There is no named released build and the release allow-list is empty. Paid-first policy therefore changes routing
semantics and acceptance requirements; it does not turn an executable or screenshot-mentioned capability into a
released feature.
