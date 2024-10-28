"""
    3. Override operators
Extend your solution for the duration class by overriding the __str__ function and
one operator (e.g. __sub__) to enable the MyTime objects to be manipulated with
the - operator and outputted directly with the print function. Write code to test this.
"""
import lab03

# firstTime = lab03.MyTime(16,45)
# secondTime = lab03.MyTime(8,55)

# firstTime.output()

# print(secondTime)


print('')

start_h, start_m = map(int, input("Enter the start time in hours and minutes (e.g. 10 45): ").split())
end_h, end_m = map(int, input("Enter the end time in hours and minutes: ").split())
# hours, minutes = duration(start_h, start_m, end_h, end_m)

startTime = lab03.MyTime(start_h, start_m)
stopTime = lab03.MyTime(end_h, end_m)
# print(f"Duration is {hours} hours {minutes} minutes.")

timeDiff = startTime - stopTime
print(f'Calculating time difference between {startTime} and {stopTime}: \n', timeDiff)

