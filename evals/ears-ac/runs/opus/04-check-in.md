**Story:** As an Employee, I want to check in to my booking, so that the room stays reserved for me.

**Design:** `TBD`

**Pre-conditions:** The user is the holder of the booking, and the booking is in status `booked`.

**Acceptance Criteria**

**Check-in window**
1. The system must open check-in for a booking 10 minutes before the booking start.
2. The system must keep check-in open until the grace period of 15 minutes after the booking start elapses (proposed — confirm).
3. While the check-in window is not open, the system must not offer check-in for the booking.

**Checking in**
4. The holder can check in from the booking in the app.
5. The holder can check in by following the check-in link in the reminder sent 10 minutes before the booking start.
6. When the holder follows the check-in link without being signed in, the system must require sign-in and then return the holder to the check-in.
7. When the holder follows the check-in link, the system must open the booking with check-in offered as a single confirming step (proposed — confirm).
8. When the holder checks in, the system must set the booking status to `checked-in`.
9. When the holder checks in, the system must show the holder that the booking is checked in.
10. While the booking is `checked-in`, the system must not mark the booking `no-show` when the grace period elapses.

**Check-in not possible**
11. If the holder attempts check-in and the booking cannot be checked in, the system must reject the check-in, keep the booking status unchanged, and show the message for the case:

| Case | Message |
|---|---|
| The check-in window has not opened yet (the booking was moved to a later start after the reminder was sent) | `TBD` — includes the time check-in opens, in the office timezone |
| The grace period has elapsed | `TBD` |
| The booking is `no-show`, marked automatically or by an Office Manager | `TBD` |
| The booking is `cancelled` | `TBD` |

12. If the booking is already `checked-in` when the holder attempts check-in, the system must show the booking as checked in and change nothing.

**Related stories**
1. Sending the reminder with the check-in link 10 minutes before start → see Send a booking reminder.
2. Marking the booking `no-show` after the grace period and releasing the room → see Auto-mark a booking as no-show.
3. An Office Manager marking a booking `no-show` before the grace period elapses → see Mark a booking as no-show manually.
4. Moving a `checked-in` booking to `completed` at end time → see Complete a checked-in booking.

**Out of Scope**
1. Check-in through room hardware (door panels, occupancy sensors, badges) — Future Phase.

**Open Questions**
1. Is the 15-minute grace period global for all offices, or configurable per office? Proposed: global 15 minutes in MVP.
2. Does following the check-in link from the reminder check the holder in immediately, or open the booking for a one-step confirmation? Proposed: open the booking for a one-step confirmation.
3. What message does the holder see when check-in is attempted before the check-in window opens? Proposed: "Check-in opens at <time>."
4. What message does the holder see when check-in is attempted after the grace period has elapsed? Proposed: "Check-in has closed for this booking."
5. What message does the holder see when check-in is attempted on a booking already marked as no-show? Proposed: "This booking was marked as a no-show and the room was released."
6. What message does the holder see when check-in is attempted on a cancelled booking? Proposed: "This booking was cancelled."
7. Which design frames cover check-in from the booking in the app and from the reminder link?
