## Identity

- Name: Aleksei Petukhov
- Student ID: 6280775
- AI tool: GitHub Copilot (used for implementation)
- Discussion partners: Worked independently (AI used to implement and format my review.md)

## Review decision

AI implemented service.py function move_booking. It Retrieves the existing target booking by booking_id using find_booking() which enforces that only bookings marked as "active" can be modified. validations were also used to confirm validation. It also compares current slot attributes (room, start, end) against the target attributes. If is identical it returns immediately without further checks or modifications.It were supposed and it dows filtering out the target booking itself (candidate is not booking) to construct other_bookings then checks for schedule overlaps against the new parameters using has_conflict(). As the last piece it directly updates the room, start and end fields on the original booking instance and returns it.

## Checks

- Baseline: `uv run --python 3.12 python -m unittest -v test_baseline` — 6 tests, OK.
- Final suite: `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student` — 11 tests, OK.

Adding 2 test cases:
1. 

Given: an active booking with ID 1 in room "A" from 10 to 12, and no conflicting bookings.

When: move_booking is called with ID 1, room "B", new start 13, new end 15.

Expect: the booking's room, start, and end are updated to "B", 13, and 15, and the modified booking is returned.

-----
Given: an active booking with ID 1 in room "A" from 10 to 12.

When: move_booking is called with ID 1, room "A", start 10, end 12 (identical parameters).

Expect: the operation short-circuits and returns the booking unchanged without triggering conflict checks.

-----
Given: an active booking with ID 1 in room "A" from 10 to 12.

When: move_booking is called to shift its time in room "A" to 11 to 13 (overlaps with its own previous slot).

Expect: the self-conflict is ignored via identity check and the booking is updated successfully.


2.

Given: a booking list that does not contain booking ID 999.

When: move_booking is called with booking_id 999.

Expect: find_booking raises an error indicating the booking was not found.

-----
Given: a booking with status "cancelled" or "completed".

When: move_booking is called for this booking.

Expect: raises ValueError("Only active bookings can be moved").

-----
Given: an active booking.

When: move_booking is called with an invalid room value (e.g., empty or nonexistent room).

Expect: validate_room raises an error and booking state remains unchanged.

-----
Given: an active booking.

When: move_booking is called with an invalid time interval (e.g., new_end <= new_start).

Expect: validate_interval raises an error and booking state remains unchanged.


3.

Given: an active booking and another existing booking in room "B" from 14 to 16.

When: move_booking is called to move the active booking to room "B" from 13 to 15.

Expect: raises ValueError("Booking conflict") and original booking parameters remain unchanged.

## Remaining uncertainty

- I don't have test case to check if room names matches eactly including whitespace and capitalized ones. Because none of my test cases cover it.