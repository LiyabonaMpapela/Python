#convert date and time
#Liyabona Mpapela
#29 August 2022
date=input("Enter the date and time (yyyy-mm-dd hh:mm):\n")# allows the user to enter the date
dash=date.find("-")# finds the position of the dash
year=date[0:dash]#extracts the year from the date provided by the user
year2= year[-2:]# takes the las two digits of the year
date1=date[dash+1:]# extracts the month and day from the date provided by the user
dash1=date1.find("-")# finds the position of the second dash which separates the moth and date
month=int(date1[0:dash1])# extracts the month from the date
space=date1.find(" ")# finds the podition of the space that separates the day from the hour
day=date1[dash1+1:space]# extracts the day of the date
colon=date1.find(":")# finds the position of the colon which separates the hour from minutes
hour=(date1[space+1:colon])# extracts the hour from the input provided by user
minutes=date1[colon:]# extracts the minutes from the input provided by user
# finds the name of the month on the date provided by user
if month==1:
    mon = 'January'
elif month==2:
    mon = 'February'
elif month==3:
    mon = 'March'
elif month==4:
    mon = 'April' 
elif month==5:
    mon = 'May'
elif month==6:
    mon = 'June'
elif month==7:
    mon = 'July'
elif month==8:
    mon = 'August'
elif month==9:
    mon = 'September'
elif month==10:
    mon = 'October'
elif month==11:
    mon = 'November'
elif month==12:
    mon = 'December'
#tells if the time in the morning(am) or at noon(pm)
if int(hour)>=12 and int(hour)<=23:
    period='pm'
else:
    period='am'
# tells the ordinal number of the day provided in date
if day[0]!='1':
    if day[1]=='1':
        ordinal='st'
    elif day[1]=='2':
        ordinal='nd'
    elif day[1]=='3':
        ordinal='rd'
    else:
        ordinal='th'    
else:
    ordinal='th'
# chages the format of the hour of the time to 12 hour format
if hour=='00':
    hour='12'
if hour=='13':
    hour='1'
if hour=='14':
    hour='2'
if hour=='15':
    hour='3'
if hour=='16':
    hour='4'
if hour=='17':
    hour='5'
if hour=='18':
    hour='6'
if hour=='19':
    hour='7'
if hour=='20':
    hour='8'
if hour=='21':
    hour='9'
if hour=='22':
    hour='10'
if hour=='23':
    hour='11'
print(str(int(hour))+minutes,period,'on the',str(int(day))+ordinal,'of',mon,"'"+year2)# displays the converted date format


    
        
    