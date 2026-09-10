"""Reference implementation for the teaching lab, Python 3.11+, no LLM needed.

Single-day room booking. The service owns domain rules; stores own atomicity.
This deliberately omits users, authentication, dates and production deployment.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, replace
import sqlite3
import threading
from typing import ContextManager, Iterator, Protocol


@dataclass(frozen=True)
class Booking:
    request_id: str
    room: str
    start: int
    end: int
    cancelled: bool = False


class Store(Protocol):
    def transaction(self) -> ContextManager[None]: ...
    def all(self) -> list[Booking]: ...
    def put(self, booking: Booking) -> None: ...


class MemoryStore:
    def __init__(self) -> None:
        self._rows: dict[str, Booking] = {}
        self._lock = threading.RLock()

    @contextmanager
    def transaction(self) -> Iterator[None]:
        with self._lock:
            before = self._rows.copy()
            try:
                yield
            except BaseException:
                self._rows = before
                raise

    def all(self) -> list[Booking]:
        return list(self._rows.values())

    def put(self, booking: Booking) -> None:
        self._rows[booking.request_id] = booking


class SQLiteStore:
    """One connection per instance/thread; BEGIN IMMEDIATE serializes writers."""
    def __init__(self, path: str) -> None:
        self.connection = sqlite3.connect(path, isolation_level=None, timeout=5)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS bookings ("
            "request_id TEXT PRIMARY KEY, room TEXT NOT NULL, "
            "start INTEGER NOT NULL, end INTEGER NOT NULL, "
            "cancelled INTEGER NOT NULL)"
        )

    @contextmanager
    def transaction(self) -> Iterator[None]:
        self.connection.execute("BEGIN IMMEDIATE")
        try:
            yield
        except BaseException:
            self.connection.rollback()
            raise
        else:
            self.connection.commit()

    def all(self) -> list[Booking]:
        return [Booking(*row[:4], cancelled=bool(row[4])) for row in
                self.connection.execute(
                    "SELECT request_id, room, start, end, cancelled FROM bookings "
                    "ORDER BY request_id"
                )]

    def put(self, booking: Booking) -> None:
        self.connection.execute(
            "INSERT INTO bookings VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(request_id) DO UPDATE SET cancelled=excluded.cancelled",
            (booking.request_id, booking.room, booking.start, booking.end,
             int(booking.cancelled)),
        )

    def close(self) -> None:
        self.connection.close()


def overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    """Half-open intervals: a booking ending at 600 frees the room at 600."""
    return a_start < b_end and b_start < a_end


class BookingService:
    def __init__(self, store: Store | None = None) -> None:
        self.store = store if store is not None else MemoryStore()

    def reserve(self, request_id: str, room: str, start: int, end: int) -> Booking:
        if not isinstance(request_id, str) or not request_id.strip() or len(request_id) > 64:
            raise ValueError("invalid request id")
        if room not in ("LAB-A", "LAB-B"):
            raise ValueError("unknown room")
        if type(start) is not int or type(end) is not int:
            raise ValueError("minutes must be integers")
        if not 480 <= start < end <= 1080 or end - start > 180:
            raise ValueError("outside opening hours or invalid duration")
        candidate = Booking(request_id, room, start, end)
        with self.store.transaction():
            rows = self.store.all()
            for previous in rows:
                if previous.request_id == request_id:
                    if replace(previous, cancelled=False) != candidate:
                        raise ValueError("request id reused with different data")
                    return previous
            if any(not row.cancelled and row.room == room
                   and overlaps(start, end, row.start, row.end) for row in rows):
                raise ValueError("room already booked")
            self.store.put(candidate)
            return candidate

    def cancel(self, request_id: str) -> Booking:
        with self.store.transaction():
            for previous in self.store.all():
                if previous.request_id == request_id:
                    result = replace(previous, cancelled=True)
                    self.store.put(result)
                    return result
            raise KeyError(request_id)

    def list_active(self) -> list[Booking]:
        with self.store.transaction():
            return sorted((b for b in self.store.all() if not b.cancelled),
                          key=lambda b: (b.start, b.room, b.request_id))
