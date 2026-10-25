**Story:** As an Employee, I want to move my booking to another time or room, so that I keep a room when my plans change.

**Design:** `TBD`

**Acceptance Criteria**

**Moving a booking**
1. The user can move a booking they hold, up to the booking's start time, by changing its room, its time slot, or both.
2. When the user submits a valid new room and time slot, the system must update the booking with the new values and keep its holder and status unchanged.
3. When the move is saved, the system must send an updated calendar invite to the holder and to each attendee.

**Validation**
4. If the new room or time slot overlaps another booking for the same room, then the system must reject the move.
5. When the move is rejected because of an overlap, the system must name the conflicting slot and its holder in the rejection message.
6. If the new values are outside the accepted information of Room, Start date and time, or End date and time, then the system must reject the move.
7. When the move is rejected, the system must keep the booking's room and time slot unchanged.
8. When the number of attendees exceeds the capacity of the new room, the system must warn the user and still allow the move (proposed — confirm).

**Moving is no longer possible**
9. While the booking's start time has passed, the system must not allow the booking to be moved.

**Recurring bookings**
10. When the user moves a single occurrence of a recurring booking, the system must detach it from the series and keep it as a standalone booking that no longer follows series-level cancellation.

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | the booking's own current slot is not a conflict for the same room |
| Start date and time | date-time | Yes | not in the past; no more than 30 days ahead; within the office's working hours | granularity `TBD` |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within the office's working hours | granularity `TBD` |

**Related stories**
1. Creating the booking that is later moved, including the shared conflict, horizon, duration, and working-hours rules → see Create a booking.
2. Resolving a conflict by cancelling someone else's booking, and cancelling after the start time → see Cancel a booking.
3. Checking in to a booking → see Check in to a booking.

**Out of Scope**
1. Moving another user's booking, including by an Office Manager — conflicts are resolved by cancellation with a reason.
2. Moving a booking to a room in another office — cross-office booking is excluded from MVP.
3. Editing the 30-day horizon, the 4-hour maximum duration, or notification templates — fixed values in MVP.

**Open Questions**
1. What time granularity does the slot picker use when moving a booking — 15, 30, or 60 minutes? Proposed: the same as when creating a booking.
2. Can a booking that the holder has already checked in to (check-in opens 10 minutes before start) still be moved before its start time? Proposed: yes, until the start time, with the status unchanged.
3. When a move puts the attendee count above the new room's capacity, should the system warn and allow it, as it does at creation? Proposed: warn and allow.
4. Can the holder move a whole recurring series at once, or only single occurrences? Not stated in the Product Context. Proposed: single occurrences only.
