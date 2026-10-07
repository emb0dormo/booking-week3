"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking

class MoveBookingTests(unittest.TestCase):
    # Given one active booking and no other booking in its room, moving it to
    # an interval that overlaps its old interval should succeed.
    def test_same_room_move_overlapping_old_interval(self):
        booking = Booking(1, "Room 201", 600, 660)
        bookings = [booking]

        result = move_booking(bookings, 1, "Room 201", 630, 690)

        self.assertIs(result, booking)
        self.assertEqual(bookings, [booking])
        self.assertEqual((booking.id, booking.room, booking.start, booking.end, booking.status),
                         (1, "Room 201", 630, 690, "active"))

    # Given an active booking, requesting its current room and times again
    # should succeed and leave the booking and list unchanged.
    def test_unchanged_move_succeeds_without_changes(self):
        booking = Booking(1, "Room 201", 600, 660)
        bookings = [booking]

        result = move_booking(bookings, 1, "Room 201", 600, 660)

        self.assertIs(result, booking)
        self.assertEqual(bookings, [booking])
        self.assertEqual((booking.id, booking.room, booking.start, booking.end, booking.status),
                         (1, "Room 201", 600, 660, "active"))

if __name__ == "__main__":
    unittest.main()
