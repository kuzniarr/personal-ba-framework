**Story:** As an Employee, I want to cancel my own booking, so that the room is free for others.

**Design:** `TBD`

**Acceptance Criteria**

**Cancelling a booking**
1. The user can cancel a booking they hold, up to the booking's start time.
2. When the user cancels a booking, the system must set its status to `cancelled`.
3. When the user cancels a booking, the system must release the room immediately, so that the freed slot can be booked by others.
4. Where the booking is an occurrence of a recurring series, the user can cancel that single occurrence; the other occurrences in the series remain unchanged (proposed — confirm).
5. Where the booking is part of a recurring series, the user can cancel the whole series; the system must cancel all future occurrences and retain past occurrences.

**Cancellation not allowed**
6. If the booking's start time has been reached or has passed, then the system must reject the cancellation and show the message `TBD`.
7. If the booking has already been cancelled, then the system must reject the cancellation and show the message `TBD`.
8. If the booking has status `checked-in`, then the system must reject the cancellation (proposed — confirm).

**Related stories**
1. Cancelling any booking in an office, at any time, with a required reason, and the cancellation notice to the holder → see Cancel a booking as an Office Manager.

**Open Questions**
1. What message does the user see when a cancellation is rejected because the start time has passed, and what message when the booking is already cancelled? Not stated in the Product Context.
2. Can the holder cancel a booking they have already checked in to, during the 10 minutes before start? The Product Context allows the `cancelled` transition only from `booked`. Proposed: no.
3. Can the holder cancel a single occurrence of a recurring series, or only the whole series? The Product Context defines series cancellation and detaching on move, but not single-occurrence cancellation. Proposed: both are allowed.
4. When the holder cancels their own booking, is any email sent to the holder or to the attendees (for example, a calendar cancellation)? The Product Context defines a cancellation notice only for Office Manager cancellations. Proposed: attendees receive a calendar cancellation; the holder receives no notice.
