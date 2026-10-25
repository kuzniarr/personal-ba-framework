**Story:** As an Employee, I want to create a weekly recurring booking, so that I don't book the same meeting every week.

**Design:** `TBD`

**Acceptance Criteria**

**Defining the series**
1. The user selects a room, the start and end time of the first occurrence, and the number of occurrences, and can add attendees before submitting the series.
2. The system must repeat the series weekly, on the same weekday and at the same office-local start and end time as the first occurrence.
3. The system must keep each occurrence at the same office-local time when a daylight-saving change falls within the series.

**Validation**
4. The system must allow occurrences after the first to fall beyond the 30-day booking horizon (proposed — confirm).
5. When the number of attendees exceeds the room's capacity, the system must warn the user and still allow the series.
6. If the user enters a value outside a field's accepted information, then the system must block submission and show that field's validation message.

**Conflicting occurrences**
7. When an occurrence overlaps an existing booking for the same room, the system must skip that occurrence and still create every non-conflicting occurrence.
8. When one or more occurrences are skipped, the system must send the holder a series-skip notice listing the date of each skipped occurrence.
9. If every occurrence of the series overlaps an existing booking, then the system must reject the series and create no booking (proposed — confirm).

**Creating the series**
10. When the series is created, the system must create each non-skipped occurrence with status `booked`, source `recurring`, and the user as its holder.
11. When the series is created, the system must send the holder a confirmation with a calendar invite attached, and send the same invite to each attendee; whether the invite is one recurring invite or one invite per occurrence is `TBD`.

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | |
| Start date and time | date-time | Yes | start of the first occurrence; not in the past; no more than 30 days ahead; within the office's working hours | shown in the office timezone; granularity `TBD` |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within the office's working hours | shown in the office timezone; granularity `TBD` |
| Number of occurrences | number | Yes | whole number from 2 to 12 | default `TBD` |
| Attendees | multi-select | No | `TBD` — no constraint on the attendee pool is stated | above room capacity shows a warning, not a block |

**Related stories**
1. Booking a single, non-recurring slot → see Book an available room for a time slot.
2. Cancelling the series and its future occurrences → see Cancel a recurring series.
3. Moving one occurrence, which detaches it from the series → see Move a booking.
4. Check-in, reminders, and no-show handling of each occurrence → see the check-in and no-show stories.

**Out of Scope**
1. Recurrence patterns other than weekly (daily, monthly, custom) — excluded from MVP.
2. Series longer than 12 occurrences — excluded from MVP.
3. Cross-office recurring booking — excluded from MVP.

**Open Questions**
1. Does the 30-day booking horizon apply only to the first occurrence of a series, or to every occurrence? A 12-week series spans 77 days, so applying it to every occurrence would cap a series at 5 weeks. Proposed: the first occurrence only.
2. If every occurrence of a series conflicts with existing bookings, should the series be rejected outright, or created empty with a series-skip notice? Proposed: reject with a message and create nothing.
3. Should the confirmation carry one recurring calendar invite for the whole series, or one invite per occurrence? Proposed: one recurring invite, with skipped dates excluded.
4. How does the user define the end of the series — by the number of occurrences, or by an end date? Proposed: number of occurrences, from 2 to 12.
5. What is the default number of occurrences offered to the user? Proposed: 4.
6. What time granularity does the slot picker use — 15, 30, or 60 minutes? Proposed: 15 minutes.
7. Who can be added as an attendee — only users in the holder's home office, or anyone in the company? Not stated in the Product Context.
8. Does a `no-show` on one occurrence affect the remaining occurrences of the series? Not stated in the Product Context.
9. Which design frames cover the recurring-series flow? No design link is available yet.
