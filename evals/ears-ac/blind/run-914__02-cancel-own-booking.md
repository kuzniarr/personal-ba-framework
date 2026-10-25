**Story:** As an Employee, I want to cancel my own booking, so that the room is free for others.

**Design:** `TBD`

**Acceptance Criteria**

**Cancelling a booking**
1. The user can cancel a booking only if: 1) the user is the booking's holder; 2) the booking's status is `booked`; 3) the booking's start time has not passed.
2. When the user starts a cancellation, the system must ask the user to confirm it before cancelling.
3. The system must not require a reason when the holder cancels their own booking.
4. When the user confirms the cancellation, the system must set the booking's status to `cancelled`.
5. When the booking is cancelled, the system must release the room immediately, so that the slot is available for booking.
6. When the booking is cancelled, the system must send a calendar cancellation to each attendee of the booking (proposed — confirm).

**Recurring bookings**
7. When the user cancels a single occurrence of a recurring series, the system must cancel only that occurrence and leave the other occurrences unchanged (proposed — confirm).

**Blocked cancellation**
8. If the booking's start time has passed when the user confirms the cancellation, then the system must reject the cancellation, keep the booking unchanged, and show the message `TBD`.
9. If the booking is already `cancelled` when the user confirms the cancellation, then the system must make no change and inform the user that the booking is already cancelled.

**Related stories**
1. Cancelling all future occurrences of a recurring series → see Cancel a recurring series.
2. Cancelling another user's booking, or any booking after its start time, with a mandatory reason → see Office Manager cancels a booking in their office.
3. Changing the time or room instead of cancelling → see Move a booking.
4. Finding the released room in the freed slot → see Search for rooms available in a time slot.

**Open Questions**
1. Which design frame covers cancelling an own booking? No design is available yet.
2. When the holder cancels their own booking, do attendees receive a calendar cancellation for the invite they were sent? Proposed: yes, each attendee receives a calendar cancellation; the holder receives no separate notice.
3. Can the holder cancel a single occurrence of a recurring series without cancelling the rest of the series? Proposed: yes, only that occurrence is cancelled.
4. What message does the holder see when cancellation is rejected because the start time has passed? Proposed: "This booking has already started and can no longer be cancelled. Contact your Office Manager."
5. When an Office Manager cancels their own booking before its start time, is a reason required, as for any Office Manager cancellation? Proposed: no, the holder flow applies and no reason is required.
