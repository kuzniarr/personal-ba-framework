**Story:** As an Employee, I want to create a weekly recurring booking, so that I don't book the same meeting every week.

**Design:** `TBD`

**Acceptance Criteria**

**Defining the series**
1. The user selects a room, the start and end time of the first occurrence, and the number of occurrences.
2. The system must repeat the series weekly on the weekday of the first occurrence, at the same start and end time.
3. The user can add attendees to the series; attendees are optional and apply to every occurrence.
4. When the number of attendees exceeds the room's capacity, the system must warn the user and still allow the series.
5. The user submits the series.

**Creating the series**
6. When the series is submitted, the system must check each occurrence for a conflict with an existing booking for the same room.
7. When the series is created, the system must create one booking for each occurrence without a conflict, each with status `booked`, source `recurring`, and the user as holder.
8. The system must keep every occurrence at the same local time in the office timezone, including across daylight-saving changes.
9. When the series is created, the system must send the holder one confirmation with a recurring calendar invite covering the created occurrences, and send the same invite to each attendee (proposed — confirm).

**Conflicting occurrences**
10. If an occurrence overlaps an existing booking for the same room, then the system must skip that occurrence and still create the remaining occurrences.
11. When one or more occurrences are skipped, the system must send the series-skip notice to the holder.
12. When one or more occurrences are skipped, the system must show the user which occurrences were created and which were skipped, with the conflicting slot and holder for each skipped one (proposed — confirm).
13. If every occurrence conflicts with an existing booking, then the system must create no series and show the user a rejection message (proposed — confirm).

**Validation**
14. If any input is outside its accepted information, then the system must reject the whole series and create no occurrence.
15. Where an occurrence falls more than 30 days ahead, the system must still create it, provided the first occurrence is within 30 days (proposed — confirm).

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | |
| Start date and time | date-time | Yes | first occurrence; not in the past; no more than 30 days ahead; within the office's working hours | sets the weekday of the series; granularity `TBD` |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within the office's working hours | granularity `TBD` |
| Number of occurrences | number | Yes | 2 to 12, including the first occurrence | default `TBD` |
| Attendees | multi-select | No | `TBD` — no constraint on the attendee pool is stated | above room capacity shows a warning, not a block |

**Related stories**
1. Creating a single booking with the same creation rules → see Book an available room for a time slot.
2. Cancelling all future occurrences of a series → see Cancel a recurring series.
3. Moving one occurrence, which detaches it from the series → see Move a booking.
4. Check-in and no-show on each occurrence → see Check in to a booking.

**Out of Scope**
1. Daily, monthly, or any non-weekly recurrence — weekly only in MVP.
2. Cross-office booking — excluded from MVP.
3. Catering and equipment requests attached to a booking — excluded from MVP.

**Open Questions**
1. Does the 30-day booking horizon apply only to the first occurrence of a weekly series, or to every occurrence? Applied to every occurrence, a series could hold at most 5 occurrences, not 12. Proposed: the horizon applies to the first occurrence only.
2. Does the user define the series length by a number of occurrences or by an end date? Proposed: number of occurrences, from 2 to 12.
3. What is the default number of occurrences when the user starts a series? Proposed: 12.
4. Does the holder receive one confirmation with a single recurring calendar invite for the series, or one confirmation and invite per occurrence? Proposed: one confirmation with one recurring invite covering only the created occurrences.
5. Besides the series-skip notice, should the user see in the app at creation which occurrences were skipped and why? Proposed: yes, listing each skipped date with the conflicting slot and its holder.
6. If every occurrence conflicts with an existing booking, is the series rejected with no booking created? Proposed: yes, with a message that no occurrence could be booked.
7. What is the rejection message copy when all occurrences conflict? `TBD`.
8. What time granularity does the start and end picker use — 15, 30, or 60 minutes? Proposed: 15 minutes, the same as a single booking.
9. Who can be added as an attendee — only users in the holder's home office, or anyone in the company? Not stated in the Product Context.
10. Does a `no-show` on one occurrence affect the remaining occurrences of the series? Not defined in the Product Context. Proposed: no, each occurrence is handled independently.
11. What is the design link for the recurring booking flow? `TBD`.
