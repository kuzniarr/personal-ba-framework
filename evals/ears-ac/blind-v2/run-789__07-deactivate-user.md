**Story:** As an Admin, I want to deactivate a user, so that people who left the company cannot sign in.

**Design:** `TBD`

**Acceptance Criteria**

**Deactivating a user**
1. The user can start deactivation for any active user in the user list, across all offices.
2. When the Admin starts deactivation, the system must ask for confirmation and state that every future booking held by the user will be cancelled.
3. When the Admin confirms, the system must set the user's state to `deactivated` and show that state in the user list.
4. When the Admin cancels the confirmation, the system must leave the user's state and bookings unchanged.
5. While a user is `deactivated`, the system must not offer the deactivation action for that user.

**Effect on bookings**
6. When a user is deactivated, the system must cancel every future booking held by that user and release each room immediately.
7. When a user is deactivated, the system must keep that user's past bookings unchanged.

**Sign-in after deactivation**
8. If a `deactivated` user signs in with Google Workspace, then the system must deny access and show the message `TBD`.
9. When a user is deactivated, the system must end every active session of that user immediately (proposed — confirm).

**Edge cases**
10. If the Admin attempts to deactivate their own account, then the system must block the deactivation (proposed — confirm).

**Related stories**
1. Restoring access for a deactivated user, without restoring cancelled bookings → see Reactivate a user.
2. Viewing the user list per office → see View the user list.

**Open Questions**
1. Which message does a deactivated user see when signing in? Proposed: "Your account is deactivated. Contact your administrator."
2. Does deactivation end the user's current sessions immediately, or only block the next sign-in? Proposed: end all sessions immediately.
3. Can an Admin deactivate their own account? Proposed: no, to avoid an Admin locking themselves out.
4. Can an Admin deactivate the only remaining Office Manager in an office, given the safeguard that blocks removing that role? Proposed: block until another Office Manager is assigned.
5. When future bookings are cancelled by deactivation, are the attendees of those bookings notified? Not stated; proposed: attendees receive a cancellation notice.
6. Should deactivating a Google Workspace account also deactivate the app user, or stay managed separately by an Admin? Not defined.
7. Design link for the user list and the deactivation confirmation is `TBD`.
