**Story:** As an Admin, I want to remove the Office Manager role from a user in an office, so that access matches current responsibilities.

**Design:** `TBD`

**Acceptance Criteria**

**Removing the role**
1. The user selects a user who holds the Office Manager role in an office and removes that role for that office.
2. When the role is removed, the system must end the user's Office Manager role in the selected office only.
3. When the role is removed, the system must leave the user's roles in all other offices unchanged.
4. When the role is removed, the user holds the Employee role in the selected office (proposed — confirm).

**Last Office Manager safeguard**
5. If the user is the only remaining Office Manager in the office, then the system must reject the removal and state that another Office Manager must be assigned first.
6. When the removal is rejected, the system must leave the user's Office Manager role in that office unchanged.
7. The rejection message text is `TBD`.

**Related stories**
1. Assigning the Office Manager role to a user in an office → see Assign the Office Manager role.
2. Viewing the list of users and their roles per office → see View the user list.
3. Deactivating or reactivating a user → see Deactivate / reactivate a user.

**Open Questions**
1. Which role does the user hold in the office after the Office Manager role is removed? A user holds exactly one role per office, and the Product Context does not state the result of removal. Proposed: Employee, the default role.
2. What is the exact message shown when the removal is rejected because the user is the only remaining Office Manager in the office? Proposed: "Assign another Office Manager to this office first."
3. What is the design link for this story? No design is available yet.
