**Story:** As an Office Manager, I want to mark a booking as no-show manually, so that an empty room is released before the grace period ends.

**Design:** `TBD`

**Pre-conditions:** The booking is in an office where the user holds the Office Manager role, and its status is `booked`.

**Acceptance Criteria**

**When a booking can be marked**
1. The user can mark as no-show only bookings in an office where the user holds the Office Manager role.
2. The user can mark a booking as no-show only while all of the following hold: 1) the booking status is `booked`; 2) the start time has been reached (proposed — confirm); 3) the 15-minute grace period after the start time has not yet elapsed.

**Marking the no-show**
3. When the user chooses to mark a booking as no-show, the system must ask the user to confirm before changing the booking.
4. When the user confirms, the system must set the booking status to `no-show`.
5. When the booking status is set to `no-show`, the system must release the room for the rest of the booked slot.
6. When the booking status is set to `no-show`, the system must show the user the booking with its new status.
7. When the user cancels the confirmation, the system must leave the booking unchanged with status `booked`.
8. The system must not require a reason to mark a booking as no-show (proposed — confirm).
9. When the user marks a booking as no-show, the system must not send any notification to the holder or the attendees (proposed — confirm).

**Concurrent changes**
10. If the booking status is no longer `booked` when the user confirms, because the holder checked in or the grace period elapsed in the meantime, then the system must reject the action and leave the booking unchanged.
11. When the system rejects the action because the booking status changed, the system must show the user the booking's current status.

**Related stories**
1. Automatic no-show after the grace period elapses with no check-in → see the automatic no-show story.
2. Holder check-in, which removes the booking from the no-show window → see Check in to own booking.
3. Booking the released room → see Book an available room for a time slot.
4. Counting manual no-shows in no-show statistics → see View no-show statistics.
5. Cancelling a booking with a reason, including after the start time → see Cancel any booking in office.

**Out of Scope**
1. Automatic check-in or no-show detection through room hardware (panels, occupancy sensors, badges) — Future Phase.
2. Reverting a booking from `no-show` back to `booked` — `no-show` is a terminal status.

**Open Questions**
1. From what moment can an Office Manager mark a booking as no-show — from the start time, or earlier, for example when check-in opens 10 minutes before start? Proposed: from the start time.
2. Must an Office Manager give a reason when marking a booking as no-show, as for an Office Manager cancellation? Proposed: no reason required.
3. Must the holder receive an email when an Office Manager marks the booking as no-show? Proposed: no notification, as none is listed among MVP notifications.
4. When one occurrence of a recurring booking is marked as no-show, does it affect the remaining occurrences of the series? Proposed: no effect; only that occurrence changes.
5. Can an Office Manager mark their own booking as no-show, or only bookings held by others? Proposed: any `booked` booking in their office, including their own.
6. Which design screens cover marking a booking as no-show? No design is available yet.
