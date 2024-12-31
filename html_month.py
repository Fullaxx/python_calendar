#!/usr/bin/env python3
# https://docs.python.org/3/library/calendar.html
# https://www.geeksforgeeks.org/python-calendar-module/
# https://realpython.com/python-calendar-module/

import calendar

if __name__ == '__main__':
	html_calendar = calendar.HTMLCalendar()
	cal_str = html_calendar.formatmonth(2024, 12, withyear=True)
	print(cal_str)