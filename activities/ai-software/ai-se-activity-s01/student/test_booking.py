"""Public acceptance examples. Add independent cases; do not weaken these."""
import unittest
from booking import BookingService


class BookingContract(unittest.TestCase):
    def setUp(self):
        self.app = BookingService()

    def test_R01_happy_path(self):
        booking = self.app.reserve("r1", "LAB-A", 540, 600)
        self.assertEqual((booking.room, booking.start, booking.end), ("LAB-A", 540, 600))
        self.assertFalse(booking.cancelled)

    def test_R02_adjacent_is_allowed(self):
        self.app.reserve("r1", "LAB-A", 540, 600)
        self.app.reserve("r2", "LAB-A", 600, 660)
        self.assertEqual(len(self.app.list_active()), 2)

    def test_R02_overlap_rejected(self):
        self.app.reserve("r1", "LAB-A", 540, 600)
        with self.assertRaises(ValueError):
            self.app.reserve("r2", "LAB-A", 590, 650)
        self.assertEqual(len(self.app.list_active()), 1)

    def test_R02_different_rooms(self):
        self.app.reserve("r1", "LAB-A", 540, 600)
        self.app.reserve("r2", "LAB-B", 540, 600)
        self.assertEqual(len(self.app.list_active()), 2)

    def test_R03_validation_has_no_effects(self):
        for room, start, end in [("X", 540, 600), ("LAB-A", 450, 500),
                                 ("LAB-A", 600, 600), ("LAB-A", 540, 721)]:
            with self.subTest(room=room, start=start, end=end):
                with self.assertRaises(ValueError):
                    self.app.reserve("bad", room, start, end)
                self.assertEqual(self.app.list_active(), [])

    def test_R04_retry_same_request(self):
        first = self.app.reserve("r1", "LAB-A", 540, 600)
        self.assertEqual(self.app.reserve("r1", "LAB-A", 540, 600), first)
        self.assertEqual(len(self.app.list_active()), 1)

    def test_R04_conflicting_request_id(self):
        self.app.reserve("r1", "LAB-A", 540, 600)
        with self.assertRaises(ValueError):
            self.app.reserve("r1", "LAB-B", 700, 760)
        self.assertEqual(len(self.app.list_active()), 1)

    def test_R05_cancel_frees_room_and_retry_stays_cancelled(self):
        self.app.reserve("r1", "LAB-A", 540, 600)
        cancelled = self.app.cancel("r1")
        self.assertTrue(cancelled.cancelled)
        self.assertEqual(self.app.cancel("r1"), cancelled)
        self.assertEqual(self.app.reserve("r1", "LAB-A", 540, 600), cancelled)
        self.app.reserve("r2", "LAB-A", 540, 600)
        self.assertEqual([x.request_id for x in self.app.list_active()], ["r2"])

    def test_R06_sorted_active_list(self):
        self.app.reserve("late", "LAB-A", 720, 780)
        self.app.reserve("early", "LAB-A", 540, 600)
        self.assertEqual([x.request_id for x in self.app.list_active()], ["early", "late"])


if __name__ == "__main__":
    unittest.main()
