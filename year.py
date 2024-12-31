#!/usr/bin/env python3
# https://docs.python.org/3/library/calendar.html
# https://www.geeksforgeeks.org/python-calendar-module/
# https://realpython.com/python-calendar-module/

import calendar

if __name__ == '__main__':
	print ("The calendar of year 2024 is : ") 
	cal_str = calendar.calendar(2024)
	print(cal_str) 
