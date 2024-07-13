#Make a calender
#Liyabona Mpapela
#24 August 2022

month = input("Enter the month ('January', ..., 'December'): \n")
day = input("Enter the start day ('Monday', ..., 'Sunday'): \n")
print(month)# shows the month chosen
print("Mo Tu We Th Fr Sa Su")
if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    days_inmonth = 31 # the number of days in specific months
elif month == 'February':
    days_inmonth = 28
else: days_inmonth = 30
if day == 'Monday': # assigns start day values
    startday = 0
elif day == 'Tuesday':
    startday = 1
elif day == 'Wednesday':
    startday = 2
elif day == 'Thursday':
    startday = 3
elif day == 'Friday':
    startday = 4
elif day == 'Saturday':
    startday = 5
elif day == 'Sunday':
    startday = 6
for d in range(1-startday,days_inmonth+1):# to show range of days in month for which they will be iterated and make sure that by (1-startday) make the value of d negative so that
    if d <= 0:# the spaces printed correspond with start date
        print("  ", end=' ')# must not print vertically
    elif d > 0 and d < 10:# ensures that for  single digits
        print("",d, end=' ')# spaces are printed to be equal as those of 2 digits and so that the days fall straight below the correct column
    else:print(d, end=" ")   
    if d in range(-startday,days_inmonth,7):# this enusures that the coloumns do not exceed 7 columns

            print()# goes to the next line after coulumn 7     

