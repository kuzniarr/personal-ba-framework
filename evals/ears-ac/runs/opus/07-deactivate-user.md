**Story:** As an Admin, I want to deactivate a user, so that people who left the company cannot sign in.

**Design:** `TBD`

**Acceptance Criteria**

**Deactivating a user**
1. The user can deactivate an active user in any office.
2. The system must offer deactivation only for users in the `active` state.
3. When the user requests deactivation, the system must ask for confirmation and state that every future booking held by the deactivated user will be cancelled.
4. When the user confirms deactivation, the system must set the deactivated user's state to `deactivated`.
5. When the user cancels the confirmation, the system must leave the user's state and bookings unchanged.

**Effect on bookings**
6. When a user is deactivated, the system must cancel every future booking that user holds, including every future occurrence of a recurring series the user holds.
7. When a user is deactivated, the system must retain the past bookings that user holds, with their statuses unchanged.

**Sign-in**
8. When a user is deactivated, the system must end every active session of that user.
9. If a deactivated user signs in through Google Workspace, then the system must reject the sign-in and show the message `TBD`.

**Safeguards**
10. If the user being deactivated is the only Office Manager in an office, then the system must reject the deactivation and state that another Office Manager must be assigned to that office first (proposed — confirm).
11. The system must not allow an Admin to deactivate their own account (proposed — confirm).

**Related stories**
1. Finding the user to deactivate → see View the user list.
2. Restoring a deactivated user's access → see Reactivate a user.

**Out of Scope**
1. Automatic deactivation of the app user when the Google Workspace account is deactivated — app state is managed separately by an Admin.
2. Restoring bookings cancelled by deactivation — reactivation does not restore them.

**Open Questions**
1. What message does a deactivated user see when the sign-in is rejected? Proposed: "Your account has been deactivated. Contact your administrator."
2. What happens to a booking held by the user that has already started (`booked` within its grace period, or `checked-in`) at the moment of deactivation — is it cancelled, or left to complete or fall to `no-show`? Proposed: left to run its normal course; only bookings that have not started are cancelled.
3. When a deactivated user's future bookings are cancelled, should attendees of those bookings receive a notice or an updated calendar invite? The Product Context defines no notification for this case. Proposed: attendees receive a cancellation calendar update; the deactivated holder receives nothing.
4. Does the last-Office-Manager safeguard also block deactivating the only Office Manager in an office? Proposed: yes — deactivation is rejected until another Office Manager is assigned.
5. Can an Admin deactivate their own account, and must at least one active Admin always remain? Proposed: an Admin cannot deactivate their own account.
6. Which design covers the deactivation flow and its confirmation step? No design is linked yet.
