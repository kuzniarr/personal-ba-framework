**Story:** As an Employee, I want to cancel my own booking, so that the room is free for others.

**Design:** `TBD`

**Acceptance Criteria**

**Cancelling a booking**
1. The user can cancel a booking they hold while its status is `booked`, up to the booking's start time.
2. When the user cancels a booking, the system must set its status to `cancelled`.
3. When the user cancels a booking, the system must make the room available for booking by other users in that slot immediately.

**Rejected cancellation**
4. If the booking's start time has passed, then the system must reject the cancellation and show the message `TBD`.
5. If the booking already has the status `cancelled`, then the system must reject the cancellation and show the message `TBD`.

**Related stories**
1. Cancelling a booking after its start time, with a required reason → see Cancel a booking as Office Manager.
2. Cancelling all future occurrences of a recurring series → see Cancel a recurring series.

**Out of Scope**
1. Collecting a reason when the holder cancels their own booking — a reason is required only for an Office Manager cancellation.

**Open Questions**
1. What message is shown when the cancellation is rejected because the start time has passed? Proposed: a message stating that a booking that has started can no longer be cancelled by its holder.
2. What message is shown when the cancellation is rejected because the booking is already cancelled? Proposed: a message stating that the booking is already cancelled.
3. Does the system send any email when a holder cancels their own booking — a confirmation to the holder, a cancellation notice to attendees, or both? The Product Context defines a cancellation notice only for cancellation by an Office Manager. Proposed: a cancellation notice to attendees so their calendar invites do not go stale, and no email to the holder.
4. Can a holder cancel a single occurrence of a recurring series, or only the whole series? The Product Context defines cancelling a series and moving a single occurrence, but not cancelling a single occurrence. Proposed: a single occurrence can be cancelled and the rest of the series stays.
