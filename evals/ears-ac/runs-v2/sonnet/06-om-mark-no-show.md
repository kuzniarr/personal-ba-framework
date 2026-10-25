**Story:** As an Office Manager, I want to mark a booking as no-show manually, so that an empty room is released before the grace period ends.

**Design:** `TBD`

**Acceptance Criteria**

**Marking a no-show**
1. While a booking in the user's office has the status `booked` and the grace period has not elapsed, the user can mark the booking as no-show.
2. When the user marks the booking as no-show, the system must set the booking status to `no-show`.
3. When the booking status is set to `no-show`, the system must release the room immediately, so that the room can be booked for the freed slot.

**Bookings that cannot be marked**
4. The system must not allow marking as no-show a booking whose status is `checked-in`, `completed`, `cancelled`, or `no-show`.
5. If the booking status changes before the marking is processed (the holder checks in, the grace period elapses, or the booking is cancelled), then the system must reject the marking and leave the booking in its current status.

**Related stories**
1. Holder checks in to the booking in the app → see the check-in story.
2. Automatic `no-show` after the grace period elapses → see the automatic no-show story.
3. Viewing no-show statistics → see the no-show statistics story.
4. Cancelling a booking with a reason → see the Office Manager cancellation story.

**Out of Scope**
1. A manual room release that does not change the booking status — no such action exists; rooms are released only on `no-show` and on cancellation.
2. Hardware-based occupancy detection to identify an empty room — Future Phase.

**Open Questions**
1. Which design covers the manual no-show action? The design link is `TBD`.
2. Can the Office Manager mark a booking as no-show before its start time, or only from the start time until the grace period elapses? The Product Context says "before the grace period elapses" without a lower bound. Proposed: only from the start time.
3. When a recurring occurrence is marked `no-show`, does it affect the remaining occurrences of the series? Not defined in the Product Context. Proposed: only the marked occurrence changes.
4. Is the 15-minute grace period global for all offices, or configurable per office? The global value is currently `proposed — confirm` in the Product Context.
5. Does the holder receive a notification when an Office Manager marks the booking as no-show? The Product Context lists no such notification. Proposed: no notification.
6. Does the Office Manager have to provide a reason when marking a no-show, as is required for cancellation? Not stated in the Product Context. Proposed: no reason is required.
