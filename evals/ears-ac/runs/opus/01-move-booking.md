**Story:** As an Employee, I want to move my booking to another time or room, so that I keep a room when my plans change.

**Design:** `TBD`

**Pre-conditions:** The user is the holder of a booking in status `booked` whose start time has not passed.

**Acceptance Criteria**

**Moving a booking**
1. The user can start a move from one of their own bookings; the move form opens with the booking's current room, start, and end filled in.
2. The user can change the start and end time, the room, or both, and submit the move.
3. When the move is accepted, the system must update the existing booking with the new room, start, and end, and keep its holder, attendees, and status `booked` unchanged.
4. When the move is accepted, the system must send an updated calendar invite to the holder and to each attendee.
5. When the user submits the move without changing the room, start, or end, the system must keep the booking as it is and send no updated invite.

**Validation**
6. The system must reject the move if: 1) the new slot overlaps an existing booking for the same room, other than the booking being moved; 2) the new start is more than 30 days ahead; 3) the new duration exceeds 4 hours; 4) any part of the new slot falls outside the office's working hours.
7. When the new slot overlaps an existing booking, the system must name the conflicting slot and its holder in the rejection message.
8. When a move is rejected, the system must keep the booking at its original room, start, and end.
9. When the number of attendees exceeds the capacity of the new room, the system must warn the user and still allow the move.

**Start time and status**
10. If the booking's start time has passed when the user submits the move, then the system must reject the move and keep the booking unchanged.
11. While the booking's start time has passed, the system must not allow the user to start a move of that booking.
12. If the booking is in status `checked-in`, then the system must not allow the move (proposed — confirm).

**Recurring occurrences**
13. When the user moves a single occurrence of a recurring series, the system must detach that occurrence into a standalone booking.
14. While an occurrence is detached, the system must exclude it from series-level cancellation.

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | defaults to the booking's current room |
| Start date and time | date-time | Yes | not in the past; no more than 30 days ahead; within the room office's working hours | defaults to the current start; granularity `TBD` |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within working hours | defaults to the current end; granularity `TBD` |

**Related stories**
1. Creating the booking and the creation rule set → see Book an available room for a time slot.
2. Finding a room that is free in the wanted slot → see Search for rooms available in a time slot.
3. Cancelling the booking, including after the start time → see Cancel own booking.
4. Reminder and check-in timing for the new start → see Reminder and check-in.

**Out of Scope**
1. Moving another user's booking, including by an Office Manager — conflicts are resolved through cancellation instead.
2. Cross-office moves — excluded from MVP.

**Open Questions**
1. What time granularity does the slot picker use when moving a booking — 15, 30, or 60 minutes? Proposed: 15 minutes, the same as creation.
2. Can a booking already checked in (check-in opens 10 minutes before start) still be moved before its start time? Proposed: no, only bookings in status `booked` can be moved.
3. Can the holder move a whole recurring series at once, or only single occurrences? Proposed: single occurrences only in MVP.
4. Can the holder change the time of a booking in a room that has since been set inactive while keeping the same room, or must the move go to an active room? Proposed: the move must go to an active room.
5. Can the holder change attendees as part of a move? Proposed: no, a move changes only the room and time.
6. Design link for the move flow is not available yet — which screens cover it?
