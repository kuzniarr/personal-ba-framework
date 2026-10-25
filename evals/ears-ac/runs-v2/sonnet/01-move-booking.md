**Story:** As an Employee, I want to move my booking to another time or room, so that I keep a room when my plans change.

**Design:** `TBD`

**Acceptance Criteria**

**Starting a move**
1. The user can change the room, the start and end time, or both room and time of a booking they hold.
2. The system must not allow a move once the booking's start time has passed.
3. While the booking is checked in, the system must not allow a move. (proposed — confirm)
4. The system must interpret and display the start and end of the new slot in the timezone of the office that owns the selected room.

**Validation**
5. The system must reject the move if the new slot overlaps an existing booking for the same room; the booking's own current slot is not a conflict.
6. When the new slot overlaps an existing booking, the system must name the conflicting slot and its holder in the rejection message.
7. If any field is outside its accepted information, then the system must reject the move with a message naming the violated rule; message copy `TBD`.
8. If the new start is before the current time, then the system must reject the move. (proposed — confirm)
9. When the number of attendees exceeds the capacity of the new room, the system must warn the user and still allow the move. (proposed — confirm)
10. If the move is rejected, then the system must keep the booking's current room, start, and end unchanged.

**Outcome**
11. When the move is valid, the system must replace the booking's room, start, and end with the new values.
12. When the move is valid, the system must make the previous slot available for other bookings.
13. When the moved booking is a single occurrence of a recurring booking, the system must detach it from the series so that it becomes a standalone booking that no longer follows series-level cancellation.
14. When the move is valid, the system must send an updated invite with a calendar attachment to the holder and to each attendee.

**Data Dictionary**
| Field Name | Field Type | Required? | Accepted Information | Comments |
|---|---|---|---|---|
| Room | select | Yes | an active room in the user's home office | cross-office moves are not supported |
| Start date and time | date-time | Yes | no more than 30 days ahead; within the room office's working hours | granularity `TBD` |
| End date and time | date-time | Yes | after the start; no more than 4 hours after the start; within the room office's working hours | granularity `TBD` |

**Related stories**
1. Creating a booking and the rules a new booking follows → see Create a booking.
2. Finding a room that is free in the wanted slot → see Search for rooms available in a time slot.
3. Resolving a conflict by cancelling another user's booking with a reason → see Cancel a booking.
4. Cancelling a recurring series → see Cancel a recurring booking.

**Out of Scope**
1. Moving another user's booking, including by an Office Manager — conflicts are resolved by cancellation.
2. Moving a booking to a room in another office — cross-office booking is excluded from MVP.
3. Moving a booking after its start time — the booking can only be cancelled.

**Open Questions**
1. What time granularity do the start and end use — 15, 30, or 60 minutes? Proposed: 15 minutes.
2. Can a holder move a booking that is already checked in (check-in opens 10 minutes before start)? Proposed: no, only a booking that is not checked in can be moved.
3. Can the new start be earlier than the current time? Proposed: no, rejected.
4. Does the attendee-over-capacity warning apply when the booking is moved to a smaller room? Proposed: yes, same warning as at creation.
5. Can the holder add or remove attendees during a move? Proposed: no, the attendee list stays as it is.
6. Can a recurring series be moved as a whole, or only single occurrences? Proposed: single occurrences only.
7. What are the rejection messages for the 30-day horizon, the 4-hour maximum duration, and working-hours violations? Only the conflict message is defined.
8. Does the 4-hour maximum and the 30-day horizon apply to the moved booking measured from the moment of the move? Proposed: yes, the same fixed values as at creation.
