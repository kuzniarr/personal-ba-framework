**Story:** As an Employee, I want to create a weekly recurring booking, so that I don't book the same meeting every week.

**Design:** `TBD`

**Acceptance Criteria**

**Creating the series**
1. The user can create a recurring booking that repeats weekly, on the weekday of the start date, for a chosen number of occurrences.
2. The system must place each occurrence at the same time of day as the first occurrence, 7 days after the previous one, in the office timezone.
3. When the series is created, the system must create each occurrence as a separate booking with status `booked`, the user as its holder, and source `recurring`.

**Validation**
4. The system must reject the series, creating no occurrence, if: 1) any part of the slot falls outside the office's working hours; 2) the duration exceeds 4 hours; 3) the room is not in the user's home office; 4) the number of occurrences is outside the accepted range.
5. When the first occurrence starts more than 30 days ahead, the system must reject the series.
6. The system must not apply the 30-day booking horizon to the second and later occurrences (proposed — confirm).
7. When the number of attendees exceeds the room's capacity, the system must warn the user and still allow the series.

**Conflicts**
8. When an occurrence overlaps an existing booking for the same room, the system must skip that occurrence and create the remaining occurrences.
9. When an occurrence is skipped, the system must send the holder a series-skip notice for that occurrence, with text `TBD`.
10. When every occurrence overlaps an existing booking, the system must reject the series and name the conflicting slot and its holder for each occurrence in the rejection message (proposed — confirm).

**Confirmation**
11. When the series is created, the system must send the holder one confirmation listing the created occurrences, with a calendar invite attached, and send the same invite to each attendee (proposed — confirm).

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | |
| Start date and time | date-time | Yes | within the office's working hours; no more than 30 days ahead | defines the first occurrence and the weekday of the series |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within working hours | same day as the start |
| Number of occurrences | whole number | Yes | 2 to 12, counting the first occurrence | minimum of 2 is proposed — confirm; maximum of 12 and weekly frequency are fixed in MVP |
| Attendees | multi-select | No | `TBD` — no constraint on the attendee pool is stated in the Product Context | above room capacity shows a warning, not a block |

**Related stories**
1. Cancelling all future occurrences of a series → see Cancel a recurring series.
2. Moving a single occurrence, which detaches it from the series → see Move a booking.
3. Checking in to an occurrence and no-show handling → see Check in to a booking.

**Out of Scope**
1. Recurrence other than weekly (daily, monthly, custom) — excluded from MVP.
2. Series longer than 12 occurrences — excluded from MVP.
3. Cross-office booking — excluded from MVP.

**Open Questions**
1. Does the 30-day booking horizon apply to every occurrence of a series? A 12-week series reaches about 84 days ahead, so applying it to all occurrences would make the 12-occurrence maximum unreachable. Proposed: the horizon applies to the first occurrence only.
2. What is the minimum number of occurrences in a series? Proposed: 2.
3. What happens when every occurrence of a series conflicts with existing bookings? Proposed: the series is rejected with a message naming each conflict.
4. Does the holder receive one confirmation and one calendar invite for the whole series, or one per occurrence? Proposed: one confirmation listing all created occurrences.
5. What is the text of the series-skip notice, and does it name the conflicting holder as the single-booking rejection message does?
6. Who can be added as an attendee — only users in the holder's home office, or anyone in the company? Not stated in the Product Context.
