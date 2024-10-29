Assignment Tasks
DundeeZest Conveyor Belt System


DundeeZest, a company providing affordable luxury wear for University of Dundee students, plans to
upgrade its production line with a conveyor belt system. The system will operate every day from 9am
– 5pm and requires an operator's input to start daily production. It will produce a set number of items
per hour and requires a routine maintenance after a specified number of operating hours. Once this limit
is reached, the system will display a 'service required' message, showing the total number of items
produced since its last maintenance before the system shuts down. After maintenance, all production
data will reset, and the cycle will be repeated.


The company has consulted you to develop a prototype Python software system for the maintenance
component of the conveyor belt system so that it does not breakdown from lack of regular maintenance.


Below is an overview of the system requirements for your software:
1. It should allow an operator to start production for each day by typing in an input. You can decide
what this input will be. The input cannot change and operation for the day cannot commence
without it.
#---DONE---#

2. Once operation commences, the software will continue to monitor production until the daily
limit of operating hours is reached i.e. 9am – 5pm. Assume 1 hour to be equivalent to a single
count by the Python interpreter e.g. a count from 1 to 2 makes 1 hour.
#---DONE---#

3. It should be able to store the total operating hours in a .txt file and retrieve the value at the start
of the next day’s operation.
#---DONE---#

4. At the end of each day, it should update the total operating hours and store the updated value
in the .txt file in requirement 3 above.
#---DONE---#

5. Include in the software a set value for the number of items that can be produced in an hour (e.g.,
100 items/hour). This could be a fixed value.
#---DONE---#

6. The software should be able to store the total number of items produced either in the .txt file in
requirement 3 above or a separate file and retrieve the value at the start of the next day’s
operation.
#---DONE---#

7. It should be able to record the total number of items produced, in the appropriate file and
update the value at the end of each day.
#---DONE---#

8. It should display a 'Service Required' message when the maximum limit of operating hours is
reached (a value can be assumed for this). It should also display the total number of items
produced since the last maintenance.
#---DONE---#

9. It should reset all production and operational data, including total items produced and
operating hours, to prepare for the next production cycle. It is assumed that the routine
maintenance has been completed at this point.
#---DONE---#


Task A: Write a Python program that meets the above requirements for the conveyor belt system.

Task B: Briefly describe each variable and function you have used in one sentence. The descriptions can
be included as comments in your program.

Task C: Requirements 10 and 11 are optional. Attempting them means you can get additional marks, but
only proceed with them if you have successfully completed the main requirements above.


10. Assume that the conveyor belt will be used by 4 operators and only one of them operates it per
day. Your software should keep track of the number of items produced by each operator and
display their individual totals at the point of maintenance along with the other data in
requirement 8 above
#---DONE---#

11. Update requirement 8 above so that the information is displayed for exactly 10 seconds before
the system shuts down for maintenance
#---DONE---#

****************************************************************************************************************************************************************
****************************************************************************************************************************************************************
Deliverables

This is an individual assignment, and each student should please submit a single zip file to My Dundee
which contains the following:
    - A .py file that contains your program.
    - The .txt file(s) that are used for keeping the production records.
    - A Word / .docx file that provides a brief, 1-sentence description / explanation for each of the
    variables and functions in your code.

Please name your ZIP file as follows: AC51002_cw1_lastname_firstname.zip.


****************************************************************************************************************************************************************
****************************************************************************************************************************************************************
How to Submit

Assignments should be submitted to My Dundee in the ‘Assessment and Feedback’ area. You are only
required to submit one zip file.

****************************************************************************************************************************************************************
****************************************************************************************************************************************************************
