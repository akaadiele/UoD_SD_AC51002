# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:00:19 2024
Lab example to use to calculate time duration in hours and minutes.
@author: IMartin
"""
def duration(start_h, start_m, end_h, end_m):
    # If start time is later than end time, then add 24 hours to
    # end time (to make it the next day)
    if (start_h > end_h) or ((start_h == end_h) and (start_m > end_m)):
        end_h += 24

    # If end_m is greater than start_m, we can simply subtract
    # hours and minutes.
    if end_m >= start_m:
        dur_m = end_m - start_m
        dur_h = end_h - start_h
    # Otherwise we need to "borrow", i.e., add 60 to minutes and
    # subtract 1 from hours.
    else:
        dur_m = end_m + 60 - start_m
        dur_h = end_h - 1 - start_h

    return dur_h, dur_m


# Test the
start_h, start_m = map(int, input("Enter the start time in hours and minutes (e.g. 10 45): ").split())
end_h, end_m = map(int, input("Enter the end time in hours and minutes: ").split())
hours, minutes = duration(start_h, start_m, end_h, end_m)
print(f"Duration is {hours} hours {minutes} minutes.")


