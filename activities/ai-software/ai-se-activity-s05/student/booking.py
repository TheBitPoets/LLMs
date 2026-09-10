"""Deliberately incomplete baseline: run the contract tests before changing it.

The happy path works. Investigate the boundary rule and missing requirements.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Booking:
    request_id: str
    room: str
    start: int
    end: int
    cancelled: bool = False


def overlaps(a_start, a_end, b_start, b_end):
    return a_start <= b_end and b_start <= a_end


class BookingService:
    def __init__(self):
        self.rows = []

    def reserve(self, request_id, room, start, end):
        if any(row.room == room and overlaps(start, end, row.start, row.end)
               for row in self.rows):
            raise ValueError("room already booked")
        result = Booking(request_id, room, start, end)
        self.rows.append(result)
        return result

    def cancel(self, request_id):
        raise NotImplementedError("implement requirement R05")

    def list_active(self):
        return list(self.rows)
