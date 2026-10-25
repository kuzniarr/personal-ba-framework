**Story:** As an Admin, I want to remove the Office Manager role from a user in an office, so that access matches current responsibilities.

**Design:** `TBD`

**Acceptance Criteria**

**Removing the role**
1. The Admin selects an office and a user who holds the Office Manager role in that office, and removes the role for that office.
2. When the role is removed, the system must set the user's role in that office to Employee (proposed — confirm).
3. When the role is removed in one office, the system must leave the user's roles in all other offices unchanged.

**Blocked removal**
4. If the user is the only remaining Office Manager in the office, then the system must reject the removal, keep the role unchanged, and inform the Admin that another Office Manager must be assigned first. Message copy: `TBD`.
5. If the user no longer holds the Office Manager role in the office when the removal is submitted, then the system must leave all roles unchanged and inform the Admin that the user no longer holds the role.

**Related stories**
1. Assigning the Office Manager role to a user in an office, including assigning a replacement before removing the last Office Manager → see Assign the Office Manager role to a user in an office.
2. Deactivating a user → see Deactivate a user.

**Open Questions**
1. Which role does the user hold in the office after the Office Manager role is removed? Proposed: Employee, since a user holds exactly one role per office and Employee is the default role.
2. What is the exact message shown to the Admin when the removal is rejected because the user is the only remaining Office Manager? Proposed: "This user is the only Office Manager in this office. Assign another Office Manager first."
