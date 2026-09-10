"""Reference solution, contract, persistence and concurrent booking checks."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1] / "labs/ai_software"
spec = importlib.util.spec_from_file_location("booking", ROOT / "reference/booking.py")
booking = importlib.util.module_from_spec(spec)
sys.modules["booking"] = booking
spec.loader.exec_module(booking)
contract_spec = importlib.util.spec_from_file_location("booking_contract", ROOT / "starter/test_booking.py")
contract = importlib.util.module_from_spec(contract_spec)
contract_spec.loader.exec_module(contract)
BookingContract = contract.BookingContract


class SQLiteContract(BookingContract):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.store = booking.SQLiteStore(str(Path(self.directory.name) / "booking.db"))
        self.addCleanup(self.store.close)
        self.app = booking.BookingService(self.store)


class EngineeringChecks(unittest.TestCase):
    def test_overlap_matches_discrete_occupancy(self):
        for a in range(6):
            for b in range(a + 1, 7):
                for c in range(6):
                    for d in range(c + 1, 7):
                        self.assertEqual(booking.overlaps(a, b, c, d),
                                         bool(set(range(a, b)) & set(range(c, d))))

    def test_types_limits_and_id_validation(self):
        app = booking.BookingService()
        for request in [None, "", " ", "x" * 65, 3]:
            with self.assertRaises(ValueError):
                app.reserve(request, "LAB-A", 480, 600)
        for start, end in [(True, 600), (480.0, 600), (480, "600"),
                           (900, 1081), (480, 661)]:
            with self.assertRaises(ValueError):
                app.reserve("r", "LAB-A", start, end)
        self.assertEqual(app.list_active(), [])
        app.reserve("early", "LAB-A", 480, 660)
        app.reserve("late", "LAB-A", 900, 1080)

    def test_unknown_cancel_and_listing_copy(self):
        app = booking.BookingService()
        with self.assertRaises(KeyError):
            app.cancel("missing")
        app.reserve("r", "LAB-A", 540, 600)
        app.list_active().clear()
        self.assertEqual(len(app.list_active()), 1)

    def test_rollback_store_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            sqlite = booking.SQLiteStore(str(Path(directory) / "db"))
            try:
                for store in (booking.MemoryStore(), sqlite):
                    with self.assertRaises(RuntimeError):
                        with store.transaction():
                            store.put(booking.Booking("r", "LAB-A", 540, 600))
                            raise RuntimeError("simulated interrupted transaction")
                    self.assertEqual(store.all(), [])
            finally:
                sqlite.close()

    def test_reopen_sqlite_preserves_cancelled_id(self):
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "db")
            first = booking.SQLiteStore(path)
            app = booking.BookingService(first)
            app.reserve("r", "LAB-A", 540, 600)
            app.cancel("r")
            first.close()
            second = booking.SQLiteStore(path)
            try:
                self.assertTrue(booking.BookingService(second).reserve(
                    "r", "LAB-A", 540, 600).cancelled)
            finally:
                second.close()

    def test_concurrent_conflict_different_connections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "db")
            booking.SQLiteStore(path).close()
            barrier = threading.Barrier(2, timeout=5)
            results = []

            def worker(request_id):
                store = booking.SQLiteStore(path)
                try:
                    barrier.wait()
                    booking.BookingService(store).reserve(request_id, "LAB-A", 540, 600)
                    results.append("reserved")
                except ValueError:
                    results.append("conflict")
                except Exception as error:
                    results.append(type(error).__name__)
                finally:
                    store.close()

            workers = [threading.Thread(target=worker, args=(key,)) for key in ("a", "b")]
            for thread in workers:
                thread.start()
            for thread in workers:
                thread.join(timeout=10)
                self.assertFalse(thread.is_alive())
            self.assertCountEqual(results, ["reserved", "conflict"])


if __name__ == "__main__":
    unittest.main()
