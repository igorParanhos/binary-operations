from enum import IntFlag, auto
from dataclasses import dataclass


class DayOfTheWeek(IntFlag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

    @staticmethod
    def from_weekday(weekday: int):
        weekday_shift = 1 << (weekday - 1)
        return DayOfTheWeek(weekday_shift)

@dataclass
class Store:
    opened_days: DayOfTheWeek
