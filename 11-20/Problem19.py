def next_day(day, month, year):
    if month == 2:
        if day == 29:
            return 1, 3, year
        if day == 28:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29, 2, year
            return 1, 3, year
        return day + 1, 2, year
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
            return 1, month + 1, year
    if day == 31 and month == 12:
        return 1, 1, year + 1
    if day == 31:
        return 1, month + 1, year
    return day + 1, month, year
if __name__ == '__main__':
    day = 1
    month = 1
    year = 1901
    day_of_week = 1
    sundays = 0
    target_reached = False
    while year < 2001:
        day_of_week = (day_of_week + 1) % 7
        if day_of_week == 0 and day == 1:
            sundays += 1
            print('7, {}   {}/{}/{}'.format(sundays, day, month, year))
        day, month, year = next_day(day, month, year)
    print(sundays)