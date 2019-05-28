#!/usr/bin/python3

import datetime as dt

today = dt.datetime.today()
end_year = dt.datetime(today.year, 12, 31, 23, 59, 59)
print("Days/Hours to end of year: " + str(end_year - today))