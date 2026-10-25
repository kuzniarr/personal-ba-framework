**Story:** As an Office Manager, I want to cancel any booking in my office with a reason, so that I can resolve room conflicts.

**Design:** `TBD`

**Acceptance Criteria**

**Scope of cancellation**
1. The user can cancel any booking for a room in an office where the user holds the Office Manager role, regardless of who holds the booking.
2. The user can cancel a booking in status `booked` both before and after its start time.
3. The user can cancel a booking in status `checked-in` (proposed — confirm).
4. The user can cancel a booking for a room that is inactive.
5. The system must not offer cancellation for a booking in an office where the user does not hold the Office Manager role.

**Cancelling with a reason**
6. The user enters a reason and confirms the cancellation.
7. The reason is free text of up to `TBD` characters.
8. If the user confirms the cancellation without a reason, then the system must reject the cancellation and keep the booking unchanged.
9. When the user cancels a booking held by the user, the system must not require a reason (proposed — confirm).

**Outcome**
10. When the cancellation is confirmed, the system must set the booking status to `cancelled`.
11. When the cancellation is confirmed, the system must release the room for the cancelled slot immediately, so that the slot becomes available for new bookings.
12. When the cancellation is confirmed, the system must keep the booking record with its reason; a cancelled booking is never deleted.
13. When the cancellation is confirmed, the system must send a cancellation notice by email to the holder, including the reason.
14. When the user cancels a booking that is an occurrence of a recurring series, the system must cancel that single occurrence only and leave the other occurrences unchanged (proposed — confirm).

**Errors**
15. If the booking is no longer in a cancellable status when the user confirms the cancellation — because it has meanwhile become `no-show`, `completed`, or `cancelled` — then the system must reject the cancellation, keep the booking in its current status, and show the message `TBD`.

**Related stories**
1. Cancelling an own booking as its holder before the start time → see the holder self-cancellation story.
2. Marking a booking `no-show` manually when the room is visibly empty → see the manual no-show story.
3. Automatic cancellation of future bookings when a user is deactivated → see the user deactivation story.

**Out of Scope**
1. Moving another user's booking — conflicts are resolved through cancellation only.
2. A separate cancellation notice to attendees — only the holder is notified.
3. Customising the cancellation notice template — Future Phase.

**Open Questions**
1. Can an Office Manager cancel a booking that is already `checked-in`, for example to free a room while a meeting is in progress? Proposed: yes, with a reason, same as a `booked` booking.
2. What is the maximum length of the cancellation reason? Proposed: free text, up to 500 characters.
3. When an Office Manager cancels a booking they hold themselves, is a reason still required? Proposed: no — the holder self-cancellation rules apply.
4. When an Office Manager cancels an occurrence of a recurring series, is only that occurrence cancelled, or can the Office Manager cancel the whole series? Proposed: that occurrence only; cancelling the whole series stays with the holder.
5. What message does the Office Manager see when the booking is no longer cancellable at the moment of confirmation (it has meanwhile become `no-show`, `completed`, or `cancelled`)? Proposed: "This booking can no longer be cancelled — its current status is <status>."
6. Which design covers the Office Manager cancellation flow? The design link is not yet available.
