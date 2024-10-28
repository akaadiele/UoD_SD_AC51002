"""
2. Convert a function into a class
Download duration.py from the MyDundee Week 6 lab folder. Build and run it. Read
through the code to see how it works (hint, use the debugger to step through the code).
This contains a function duration()with four parameters which takes in two times
(each in hours and minutes) and returns the number of hours and minutes from the
first time to the second. For example, from 9.45 to 12.10 is 2 hours and 25 minutes.
Use the 24-hour clock. If the second time is before the first time, then assume it is
the following day (so 22.35 to 16.15 is 17 hours and 40 minutes). Thus:
duration(10,55,16,05)should print “Duration is 5 hours 10 minutes”.
Please test this!
Design a class which implements the duration()functionality using a Python
class called MyTime to encapsulate the hours and minutes. Here, we’ve used two
parameters for each time (one for hours and one for minutes), but using a class we
can have a single object for each time. Create a MyTime class with attributes for
hours and minutes, and add suitable functions, constructor/initialiser etc., together
with a print() function to print a MyTime instance to the screen. Write code to test the
class
"""

class MyTime:
    timeHour = None
    timeMinutes = None
    
    
    def __init__(self, timeHour, timeMinutes):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        self.timeHour = timeHour
        self.timeMinutes = timeMinutes
        

    def duration(self, start_h, start_m, end_h, end_m):
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


    def output(self):
        print(f"The time is {self.timeHour}:{self.timeMinutes}")


    def __str__(self):
        returnText = f"{self.timeHour}:{self.timeMinutes}"
        return returnText


    def __sub__(self, otherTime):
        start_h = int(self.timeHour)
        start_m = int(self.timeMinutes)
        end_h = int(otherTime.timeHour)
        end_m = int(otherTime.timeMinutes)
        
        duration_hr, duration_min = self.duration(start_h, start_m, end_h, end_m)
        
        return MyTime(duration_hr, duration_min)