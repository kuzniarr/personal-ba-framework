**Story:** As an Employee, I want to check in to my booking, so that the room stays reserved for me.

**Design:** `TBD`

**Acceptance Criteria**

**When check-in is available**
1. While a booking is in status `booked`, the holder can check in from 10 minutes before the booking's start time.
2. The holder can check in through the check-in link in the reminder email.
3. While the booking is in status `booked`, the holder can check in after the start time until 15 minutes after the start time (proposed — confirm).

**Checking in**
4. When the holder checks in, the system must set the booking status to `checked-in`.
5. While the booking is in status `checked-in`, the system must not mark it `no-show`.

**Check-in not possible**
6. If the holder attempts to check in earlier than 10 minutes before the start time, then the system must not check in the booking and must show the message `TBD`.
7. If the booking status is `cancelled`, `no-show`, or `completed`, then the system must not check in the booking and must show the message `TBD`.
8. If the booking is already `checked-in`, then the system must keep the status unchanged.

**Related stories**
1. Sending the reminder email that carries the check-in link → see the booking notifications story.
2. Automatically marking a booking `no-show` after the grace period and releasing the room → see the no-show handling story.
3. Marking a booking `no-show` manually by an Office Manager → see the manual no-show story.
4. Completing a checked-in booking at its end time → see the booking completion story.

**Out of Scope**
1. Hardware check-in (door panels, occupancy sensors, badge) — Future Phase.

**Open Questions**
1. Is the 15-minute grace period the same in every office, or must it be configurable per office? Proposed: one global value of 15 minutes.
2. What message is shown when check-in is attempted before it opens, and what message when the booking is `cancelled`, `no-show`, or `completed`? Proposed: a message naming the time check-in opens for the first case, and a message naming the current booking status for the second.
3. Which design covers the check-in action and its rejection messages?
