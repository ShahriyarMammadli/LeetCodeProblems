# Shahriyar Mammadli
# LeetCode problem '1185. Day of the Week' solution

def dayOfTheWeek(day, month, year):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Take 1968 as a reference since this year was a leap year...
    # ...and first day of that year was a monday
    iYear = 1968
    # Calculate weekday of the first day of that year
    weekday = int(((year - iYear) * 365 + (year - iYear) / 4 + 1) % 7)
    # Check if it is a leap year
    if (year - iYear) % 4 == 0:
        # If given date is before the February 29 decrease the index by one
        if (month < 3):
            weekday = weekday - 1
        return weekdays[(sum(monthes[0:(month - 1)]) + day + weekday - 1) % 7]
    else:
        return weekdays[(sum(monthes[0:(month - 1)]) + day + weekday - 1) % 7]

print(dayOfTheWeek(29, 2, 2016))