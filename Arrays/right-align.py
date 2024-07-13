#print out right-aligned with the longest string
#Liyabona Mpapela
#28 September 2022

word=input('Enter strings (end with DONE):\n')
print(' ')
print('Right-aligned list:')
max_length=len(word)
string=[]
while word!= 'DONE':
    string.append(word)
    word=input('')
    length=len(word)
    if length>max_length:
        max_length=length
for i in range(len(string)):  
    #print(5* " " + string[i],end='\n')
    print("{0:>{1}}".format(string[i],max_length))