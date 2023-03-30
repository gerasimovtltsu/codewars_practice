"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year in Gregorian calendar as integer.

Output: Number of Black Fridays in the year as an integer.

Examples:
unluckyDays(2015) == 3
unluckyDays(1986) == 1
"""

from datetime import date, timedelta


def unluckyDays(year) -> int:
    return sum(date(year, month, 13).isoweekday() == 5 for month in range(1, 13))


print(unluckyDays(2015))
