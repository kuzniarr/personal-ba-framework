**Story:** As an Office Manager, I want to cancel any booking in my office with a reason, so that I can resolve room conflicts.

**Design:** `TBD`

**Acceptance Criteria**

**Starting a cancellation**
1. The user can cancel any booking with status `booked` in an office where the user holds the Office Manager role, both before and after the booking's start time.
2. The user must provide a reason to cancel a booking.
3. The user can abandon the cancellation before confirming, and the booking must remain unchanged.

**Result of the cancellation**
4. When the user confirms the cancellation with a reason, the system must set the booking's status to `cancelled` and retain the booking.
5. When the booking is cancelled, the system must release the room immediately, so that the slot is available for new bookings.

**Validation and blocked cases**
6. If the reason is empty or contains only whitespace, then the system must reject the cancellation, keep the booking unchanged, and show the message `TBD`.
7. If the reason exceeds `TBD` characters, then the system must reject the cancellation, keep the booking unchanged, and show the message `TBD`.
8. If the booking's status has changed to `cancelled`, `no-show`, or `completed` after the user opened it and before the user confirmed, then the system must reject the cancellation and show the booking's current status.
9. If the booking belongs to an office where the user does not hold the Office Manager role, then the system must reject the cancellation.

**Related stories**
1. Notifying the holder by email about the cancellation, including the reason → see the booking notifications story.
2. Showing the released slot as available in room search → see Search for rooms available in a time slot.
3. Cancelling an own booking as holder → see Cancel own booking.
4. Cancelling a recurring series → see the recurring booking cancellation story.

**Out of Scope**
1. Moving another user's booking — an Office Manager resolves conflicts through cancellation only.
2. Separate notification of attendees about the cancellation — only the holder is notified.

**Open Questions**
1. Which design covers the cancellation flow?
2. Is the reason free text, and what is the maximum length? Proposed: free text, 500 characters.
3. What are the approved messages for an empty reason, a reason over the limit, and a booking that is no longer cancellable?
4. Can an Office Manager cancel a booking with status `checked-in` (a meeting in progress)? The Product Context lists only `booked` → `cancelled`. Proposed: yes, since an Office Manager may cancel at any time.
5. When the booking is one occurrence of a recurring series, does the Office Manager cancel only that occurrence, the whole series, or choose between them? Not stated in the Product Context.
