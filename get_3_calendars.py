#!/usr/bin/env python3
# https://docs.python.org/3/library/calendar.html
# https://www.geeksforgeeks.org/python-calendar-module/
# https://realpython.com/python-calendar-module/

import calendar
from datetime import datetime

if __name__ == '__main__':
	today = datetime.today()
	curr_year = today.year
	curr_mon = today.month

#	today_obj = datetime(today.year, today.month, 1)
#	print(today_obj)

	next_mon = curr_mon + 1
	if (next_mon == 13):
		next_mon = 1
		next_year = curr_year + 1
	else:
		next_year = curr_year

	prev_mon = curr_mon - 1
	if (prev_mon == 0):
		prev_mon = 12
		prev_year = curr_year - 1
	else:
		prev_year = curr_year

#	print(f'{prev_mon}/{prev_year} -> {curr_mon}/{curr_year} -> {next_mon}/{next_year}')

#	prev_str = calendar.month(prev_year, prev_mon)
#	curr_str = calendar.month(curr_year, curr_mon)
#	next_str = calendar.month(next_year, next_mon)

	text_calendar = calendar.TextCalendar()
	text_calendar.setfirstweekday(calendar.SUNDAY)
	prev_str = text_calendar.formatmonth(prev_year, prev_mon)
	curr_str = text_calendar.formatmonth(curr_year, curr_mon)
	next_str = text_calendar.formatmonth(next_year, next_mon)

	print(prev_str)
	print(curr_str)
	print(next_str)
