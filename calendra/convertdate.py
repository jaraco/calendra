"""
This file is part of convertdate.
http://github.com/fitnr/convertdate
Licensed under the MIT license:
http://opensource.org/licenses/MIT
Copyright (c) 2016, fitnr <fitnr@fakeisthenewreal>
Extended by Daniel Grießhaber <dangrie158@gmail.com> to add typing information
"""

from calendar import isleap
from math import ceil, floor


class islamic:
    EPOCH = 1948439.5

    @classmethod
    def from_gregorian(cls, year: int, month: int, day: int):
        return cls.from_jd(gregorian.to_jd(year, month, day))

    @classmethod
    def to_gregorian(cls, year: int, month: int, day: int):
        return gregorian.from_jd(cls.to_jd(year, month, day))

    @classmethod
    def to_jd(cls, year: int, month: int, day: int) -> float:
        """Determine Julian day count from Islamic date"""
        return (
            day
            + ceil(29.5 * (month - 1))
            + (year - 1) * 354
            + floor((3 + (11 * year)) / 30)
            + cls.EPOCH
        ) - 1

    @classmethod
    def from_jd(cls, jd: float):
        """Calculate Islamic date from Julian day"""
        jd = floor(jd) + 0.5
        year = floor(((30 * (jd - cls.EPOCH)) + 10646) / 10631)
        month = min(
            12, ceil((jd - (29 + cls.to_jd(year, 1, 1))) / 29.5) + 1)
        day = int(jd - cls.to_jd(year, month, 1)) + 1
        return year, month, day


class gregorian:
    EPOCH = 1721425.5
    YEAR_DAYS = 365
    LEAP_CYCLE_YEARS = 4
    LEAP_CYCLE_DAYS = 1461
    LEAP_SUPPRESSION_YEARS = 100
    LEAP_SUPPRESSION_DAYS = 36524
    INTERCALATION_CYCLE_YEARS = 400
    INTERCALATION_CYCLE_DAYS = 146097

    HAVE_30_DAYS = (4, 6, 9, 11)

    @classmethod
    def legal_date(cls, year: int, month: int, day: int) -> bool:
        """Check if this is a legal date in the Gregorian calendar"""
        if month == 2:
            daysinmonth = 29 if isleap(year) else 28
        else:
            daysinmonth = 30 if month in cls.HAVE_30_DAYS else 31

        if not 0 < day <= daysinmonth:
            raise ValueError(
                f"Month {month} doesn't have a day {day}")

        return True

    @classmethod
    def to_jd(cls, year: int, month: int, day: int) -> float:
        """Convert gregorian date to julian day count."""
        cls.legal_date(year, month, day)

        if month <= 2:
            leap_adj = 0
        elif isleap(year):
            leap_adj = -1
        else:
            leap_adj = -2

        return (
            cls.EPOCH
            - 1
            + (cls.YEAR_DAYS * (year - 1))
            + floor((year - 1) / cls.LEAP_CYCLE_YEARS)
            + (-floor((year - 1) / cls.LEAP_SUPPRESSION_YEARS))
            + floor((year - 1) / cls.INTERCALATION_CYCLE_YEARS)
            + floor((((367 * month) - 362) / 12) + leap_adj + day)
        )

    @classmethod
    def from_jd(cls, jd: float):
        """Return Gregorian date in a (Y, M, D) tuple"""
        wjd = floor(jd - 0.5) + 0.5
        depoch = wjd - cls.EPOCH

        quadricent = floor(depoch / cls.INTERCALATION_CYCLE_DAYS)
        dqc = depoch % cls.INTERCALATION_CYCLE_DAYS

        cent = floor(dqc / cls.LEAP_SUPPRESSION_DAYS)
        dcent = dqc % cls.LEAP_SUPPRESSION_DAYS

        quad = floor(dcent / cls.LEAP_CYCLE_DAYS)
        dquad = dcent % cls.LEAP_CYCLE_DAYS

        yindex = floor(dquad / cls.YEAR_DAYS)
        year = (
            quadricent * cls.INTERCALATION_CYCLE_YEARS
            + cent * cls.LEAP_SUPPRESSION_YEARS
            + quad * cls.LEAP_CYCLE_YEARS
            + yindex
        )

        if not (cent == 4 or yindex == 4):
            year += 1

        yearday = wjd - cls.to_jd(year, 1, 1)

        leap = isleap(year)

        if yearday < 58 + leap:
            leap_adj = 0
        elif leap:
            leap_adj = 1
        else:
            leap_adj = 2

        month = floor((((yearday + leap_adj) * 12) + 373) / 367)
        day = int(wjd - cls.to_jd(year, month, 1)) + 1

        return year, month, day
