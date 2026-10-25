**Story:** As an Admin, I want to deactivate a user, so that people who left the company cannot sign in.

**Design:** `TBD`

**Acceptance Criteria**

**Deactivating a user**
1. The user can deactivate any user whose state is active, in any office.
2. When the user deactivates a user, the system must set that user's state to deactivated.

**Sign-in after deactivation**
3. While a user is deactivated, the system must deny that user sign-in.
4. When a deactivated user attempts to sign in, the system must show the message `TBD`.
5. When a user is deactivated while signed in, the system must end that user's active session (proposed — confirm).

**Bookings of the deactivated user**
6. When a user is deactivated, the system must set the status of every future booking held by that user to `cancelled` and release the rooms.
7. When a user is deactivated, the system must retain the user's past bookings unchanged for reporting.

**Related stories**
1. Reversing a deactivation → see Reactivate a user.
2. Finding the user to deactivate → see View the user list.
3. Sign-in and provisioning through Google Workspace → see Sign in with Google Workspace.

**Open Questions**
1. Which design covers deactivating a user? The design link is not available yet.
2. What message does a deactivated user see when attempting to sign in? Proposed: a generic "access denied, contact your administrator" message.
3. Must a user who is signed in at the moment of deactivation lose access immediately, or only at the next sign-in? Proposed: immediately.
4. Are the holder and the attendees notified when a future booking is auto-cancelled by deactivation? The Product Context defines a cancellation notice only for cancellation by an Office Manager. Proposed: no notification.
5. Should deactivating a Google Workspace account also deactivate the app user, or stay a separate Admin action? The Product Context states the two are not synced and leaves the question undefined. Proposed: separate, as in the current behaviour.
6. Can an Admin deactivate the only remaining Office Manager of an office? The last-Office-Manager safeguard in the Product Context covers role removal only. Proposed: allowed.
7. Can an Admin deactivate their own account? Proposed: not allowed, to prevent losing all Admin access.
