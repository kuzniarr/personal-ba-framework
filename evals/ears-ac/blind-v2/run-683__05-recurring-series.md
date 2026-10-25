**Story:** As an Employee, I want to create a weekly recurring booking, so that I don't book the same meeting every week.

**Design:** `TBD`

**Acceptance Criteria**

**Setting up the series**
1. The user selects a room, a start date and time, an end date and time, and a number of occurrences, and submits the weekly series.
2. The user can add attendees to the series; attendees are optional.
3. The system must offer weekly as the only recurrence frequency.

**Validation**
4. The system must reject the series if any field value falls outside its accepted information.
5. The system must reject the series if the selected room is not in the user's home office.
6. When the number of attendees exceeds the room's capacity, the system must warn the user and still allow the series.
7. The system must not apply the 30-day booking horizon to occurrences after the first (proposed — confirm).

**Creating the series**
8. When the series is submitted and passes validation, the system must create one booking per occurrence, each on the same weekday and with the same start time and end time as the first occurrence.
9. When an occurrence is created, the system must set its status to `booked`, record the user as its holder, and set its source to recurring.
10. When the clocks change in the office timezone during the series, the system must keep every occurrence at the same local start and end time in the office timezone (proposed — confirm).
11. When an occurrence overlaps an existing booking for the same room, the system must skip that occurrence and still create the remaining occurrences.
12. When an occurrence is skipped, the system must send the holder a series-skip notice identifying the skipped occurrence.

**Confirmation**
13. When the series is created, the system must send the holder one confirmation with a calendar invite attached for the created occurrences, and send the same invite to each attendee (proposed — confirm).

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in an office where the user holds a role | |
| Start date and time | date-time | Yes | first occurrence no more than 30 days ahead; within the room office's working hours | |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within the room office's working hours | |
| Repeat | select | Yes | Weekly | the only frequency in MVP |
| Number of occurrences | number | Yes | whole number; maximum 12; minimum `TBD` | counted per Open Questions |
| Attendees | multi-select | No | `TBD` — no constraint on the attendee pool is stated in the Product Context | above room capacity shows a warning, not a block |

**Related stories**
1. Cancelling a whole series, which cancels all future occurrences and keeps past ones → see Cancel a recurring series.
2. Moving a single occurrence, which detaches it into a standalone booking → see Move a booking.
3. Checking in to an occurrence and no-show handling → see Check in to a booking.

**Out of Scope**
1. Recurrence frequencies other than weekly — not in MVP.
2. Cross-office booking — excluded from MVP.
3. Catering and equipment requests attached to a booking — excluded from MVP.

**Open Questions**
1. How does the user define the length of the series, and what is the minimum? Proposed: a number of occurrences from 2 to 12, counting the first occurrence, with no end-date option.
2. Does the 30-day booking horizon apply to occurrences after the first? A 12-occurrence weekly series reaches about 84 days ahead. Proposed: the horizon applies to the first occurrence only.
3. What happens when every occurrence of the series overlaps existing bookings? Proposed: the series is rejected with the conflict message naming the conflicting slot and its holder.
4. Does the holder receive one confirmation for the whole series or one per occurrence, and is each attendee invited to every occurrence? Proposed: one confirmation with all invites; attendees invited to every created occurrence.
5. Should an occurrence keep the same local time in the office timezone across a clock change? Proposed: yes.
6. Who can be added as an attendee — only users in the holder's home office, or anyone in the company? Not stated in the Product Context.
7. Does a `no-show` on one occurrence affect the remaining occurrences of the series? Not defined in the Product Context.
