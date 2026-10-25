**Story:** As an Office Manager, I want to cancel any booking in my office with a reason, so that I can resolve room conflicts.

**Design:** `TBD`

**Acceptance Criteria**

**Which bookings can be cancelled**
1. The user can cancel any booking in their own office with status `booked`, whoever its holder is, both before and after the booking's start time.
2. The user can cancel a booking in their own office with status `checked-in` (proposed — confirm).
3. The system must not allow cancellation of a booking with status `completed`, `no-show`, or `cancelled`.

**Reason**
4. The user must enter a reason to cancel a booking.
5. If the reason is empty or contains only whitespace, then the system must not cancel the booking and must keep its status unchanged.
6. The system must accept a reason of up to `TBD` characters.

**Result of the cancellation**
7. When the user confirms the cancellation with a reason, the system must set the booking status to `cancelled`.
8. When the booking is cancelled, the system must release the room for the booking's slot immediately.
9. When the booking is cancelled, the system must send an email cancellation notice to the holder that includes the reason.
10. When the booking is cancelled, the system must not send a separate cancellation notice to the booking's attendees.

**Edge cases**
11. If the booking has changed to a status other than `booked` or `checked-in` between the user opening it and confirming the cancellation, then the system must not change the booking and must show the user its current status with the message `TBD`.

**Related stories**
1. Finding a booking in the office calendar to cancel → see the story for viewing office bookings.
2. A holder cancelling their own booking before start → see the story for cancelling an own booking.
3. Composing and delivering the cancellation email → see the story for booking notifications.
4. Marking a booking as no-show manually → see the story for manual no-show marking.

**Out of Scope**
1. Moving another user's booking — the Office Manager resolves conflicts by cancellation only.
2. Cancelling bookings in an office where the user does not hold the Office Manager role — excluded from MVP.

**Open Questions**
1. Can an Office Manager cancel a booking with status `checked-in` (the room is in use at that moment)? The Product Context lists the transition only from `booked`, while stating that an Office Manager can cancel at any time. Proposed: yes.
2. What is the maximum length of the cancellation reason, and is it free text? Proposed: free text, up to 500 characters.
3. What is the approved message text shown when the booking is no longer cancellable at the moment of confirmation?
4. When the booking is an occurrence of a recurring series, does the Office Manager cancel only that occurrence or the whole series? Proposed: that occurrence only.
5. Which design covers this flow?
