**Story:** As an Employee, I want to check in to my booking, so that the room stays reserved for me.

**Design:** `TBD`

**Acceptance Criteria**

**Check-in window**
1. While a booking has status `booked`, the holder can check in to it from 10 minutes before the booking's start until the grace period elapses; the grace period is 15 minutes after the start (proposed — confirm).

**Checking in**
2. When the holder checks in within the check-in window, the system must set the booking status to `checked-in`.
3. While a booking has status `checked-in`, the system must not mark it `no-show` and must not release the room when the grace period elapses.

**Check-in not possible**
4. If the holder attempts to check in outside the check-in window, then the system must reject the check-in, keep the booking status unchanged, and show the message `TBD`. Outside the window means: 1) earlier than 10 minutes before the start; 2) after the grace period has elapsed.
5. If the holder attempts to check in to a booking whose status is not `booked`, then the system must reject the check-in, keep the booking status unchanged, and show the message `TBD`. The statuses are: 1) `checked-in`; 2) `completed`; 3) `cancelled`; 4) `no-show`.

**Related stories**
1. Reminder email with the check-in link, sent 10 minutes before the start → see Send booking reminder.
2. Automatic `no-show` marking after the grace period and room release → see Mark a booking as no-show automatically.
3. Manual `no-show` marking by an Office Manager before the grace period elapses → see Mark a booking as no-show manually.
4. Automatic `checked-in` → `completed` at end time → see Complete a booking automatically.

**Out of Scope**
1. Hardware check-in (door panels, occupancy sensors, badge) — Future Phase.

**Open Questions**
1. Is the 15-minute grace period global for all offices, or should it be configurable per office? Proposed: one global value of 15 minutes in MVP.
2. What is the approved message text when check-in is rejected because it is outside the check-in window, and when it is rejected because the booking status is not `booked`? Proposed: one message per case.
3. Which design covers the check-in action? No design link is available yet.
