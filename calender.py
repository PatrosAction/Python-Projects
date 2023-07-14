import calendar

print(calendar.weekheader(4))

print()

print(calendar.firstweekday())

print()

print( calendar.month(2023,3))

print(calendar.monthcalendar(2023,3))

print(calendar.calendar(2023))


days_of_the_weak = calendar.weekday(3000,3,8)
is_leap =calendar.isleap(2024)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000,2001)
print(how_many_leap_days)

