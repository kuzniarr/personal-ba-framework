**Story:** As an Admin, I want to remove the Office Manager role from a user in an office, so that access matches current responsibilities.

**Design:** `TBD`

**Acceptance Criteria**

**Removing the role**
1. The user can see, for a selected user, the role that user holds in each office.
2. The user can remove the Office Manager role from the selected user only in an office where that user currently holds the Office Manager role.
3. When the Office Manager role is removed, the system must set the selected user's role in that office to Employee (proposed — confirm).
4. When the Office Manager role is removed in one office, the system must keep the selected user's roles in every other office unchanged.
5. When the Office Manager role is removed, the system must stop granting the selected user Office Manager capabilities in that office from the user's next action in the app.
6. When the Office Manager role is removed, the system must keep the bookings the selected user holds in that office unchanged.

**Last-Office-Manager safeguard**
7. If the selected user is the only remaining Office Manager in the office, then the system must reject the removal and keep the selected user's Office Manager role in that office.
8. When the removal is rejected by the last-Office-Manager safeguard, the system must show the message `TBD`, stating that another Office Manager must be assigned in that office first.

**Related stories**
1. Assigning the Office Manager role to a user in an office, including the replacement needed before the last Office Manager can be removed → see Assign the Office Manager role to a user in an office.
2. Finding the user whose role is to be changed → see View the user list.
3. Deactivating a user instead of changing their role → see Deactivate a user.

**Open Questions**
1. When the Office Manager role is removed from a user in an office, does that user become an Employee in that office, or lose all access to that office? Proposed: Employee, since a user holds exactly one role per office and Employee is the default role.
2. What is the exact text of the message shown when the removal is blocked because the user is the only remaining Office Manager in the office?
3. Does a deactivated user who holds the Office Manager role count as an Office Manager for the last-Office-Manager safeguard? Proposed: no — only active Office Managers count, so the last active Office Manager in an office cannot lose the role until another active one is assigned.
4. Should the user whose Office Manager role is removed receive an email about the change? Proposed: no — role changes are not among the MVP notifications.
5. Which design frames cover viewing a user's roles per office and removing the Office Manager role?
