#complete the code for a 2048 program
#Liyabona Mpapela
#26 September 2022
fail=0
third=0
lower_second=0
upper_second=0
first=0
marks=input('Enter a space-separated list of marks:\n')
marks=marks.split(' ')
for i in marks:
    if eval(i)<50:
        fail+=1
    elif eval(i) >=50 and eval(i)<60:
        third+=1
    elif  eval(i)>=60 and eval(i)<70:
        lower_second+=1
    elif eval(i)>=70 and eval(i)<75:
        upper_second+=1
    else:
        eval(i)<=75
        first+=1
        
print('1 |'+'X'*first)
print('2+|'+'X'*upper_second)
print('2-|'+'X'*lower_second)
print('3 |'+'X'*third)
print('F |'+'X'*fail)
