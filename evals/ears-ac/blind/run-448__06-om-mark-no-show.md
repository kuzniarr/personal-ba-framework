**Story:** As an Office Manager, I want to mark a booking as no-show manually, so that an empty room is released before the grace period ends.

**Design:** `TBD`

**Acceptance Criteria**

**Marking a booking as no-show**
1. While a booking in the user's own office has the status `booked` and its grace period has not elapsed, the user can mark the booking as no-show.
2. When the user marks the booking as no-show, the system must set its status to `no-show`.
3. When the booking is marked as no-show, the system must release the room immediately, so that the room is available for booking again.

**Bookings that cannot be marked**
4. If the booking has any status other than `booked` (`checked-in`, `completed`, `cancelled`, or `no-show`), then the system must not allow it to be marked as no-show.
5. If the grace period elapses before the user's action is processed, then the system must keep the automatic `no-show` result and show the user the message `TBD`.

**Related stories**
1. Automatic `no-show` and room release when the grace period elapses without check-in → see Automatic no-show after the grace period.
2. Holder's check-in to a booking → see Check in to a booking.
3. Viewing no-show statistics → see View no-show statistics.

**Out of Scope**
1. Reverting a `no-show` booking — `no-show` is a terminal status.
2. Releasing a room without changing the booking status — no manual release action exists.

**Open Questions**
1. Can the Office Manager mark a booking as no-show before its start time, or only after the start time and before the grace period ends? Proposed: only after the start time.
2. Does a manual `no-show` on one occurrence of a recurring booking affect the remaining occurrences of the series? Proposed: no, only the selected occurrence is affected. Not defined in the Product Context.
3. What is the exact message shown when the booking can no longer be marked because the grace period has already elapsed?
4. Is the holder notified when the Office Manager marks the booking as no-show? Proposed: no notification, as none is defined for this action.
5. Does the Office Manager have to enter a reason when marking a booking as no-show, as is required for cancellation? Proposed: no reason required.
