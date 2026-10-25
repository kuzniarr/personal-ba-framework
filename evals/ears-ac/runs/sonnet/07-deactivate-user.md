**Story:** As an Admin, I want to deactivate a user, so that people who left the company cannot sign in.

**Design:** `TBD`

**Acceptance Criteria**

**Deactivating a user**
1. The Admin can deactivate any user of an active state from the user list across all offices.
2. When the Admin deactivates a user, the system must set the user's state to `deactivated`.
3. When the user is deactivated while holding an open session, the system must end that session (proposed — confirm).

**Effect on sign-in**
4. While a user is `deactivated`, the system must deny that user's sign-in through Google Workspace SSO.
5. When a `deactivated` user attempts to sign in, the system must show the message `TBD`.

**Effect on bookings**
6. When a user is deactivated, the system must cancel all future bookings held by that user and release the rooms.
7. When a user is deactivated, the system must retain the user's past bookings for reporting.

**Related stories**
1. Reactivating a deactivated user → see Reactivate a user.
2. Finding a user in the user list → see View the user list.

**Out of Scope**
1. Automatic deactivation of the app user when the Workspace account is deactivated — not defined in the Product Context.
2. Restoring cancelled bookings on reactivation — reactivation does not restore them.

**Open Questions**
1. What message does a deactivated user see when attempting to sign in? Not stated in the Product Context.
2. Must an open session of a user end at the moment of deactivation, or may it run until it expires? Proposed: end the session immediately.
3. Can an Admin deactivate their own account? Proposed: no.
4. Can an Admin deactivate the only remaining Office Manager of an office? The last-Office-Manager safeguard is defined only for role removal. Proposed: allowed.
5. Are the holder and the attendees of the auto-cancelled bookings notified? The Product Context defines a cancellation notice only for cancellation by an Office Manager. Proposed: no notification.
6. Which design covers the deactivation action?
