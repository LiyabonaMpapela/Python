#reformat references
#Liyabona Mpapela
#29 August 2022
ref = input("Enter the reference:\n")#allows the user to input reference
start_year = ref.find("(")# finds the position of the first bracket of of the year 
authours = ref[0:start_year-1]# extracts the names of the authour from thr reference
comma=authours.find(",")# finds the position of comma in the authour names which separates the names of the authours
print("Reformatted reference:")
while comma!=-1:# while there is a comma on the authours names
    print(authours[0].upper()+authours[1:comma+1].lower(),end=' ')#prints the separate name of the authour with thw first letter written in capital letter
    authours=authours[comma+2:]# cahges the name of the outhour by removing the name thet is already printed
    comma=authours.find(",")# finds the position of the comma to check if there is more that one authour name that has not been printed in the new format or not
print(authours[0].upper()+authours[1:].lower(),end=' ')# prints the name of the last authour in the authours listed
end_year = ref.find(")")# finds the podition of the closing bracket of the year 
title = ref[end_year+2:]# extracts thae tittle from the refernce
comma2= title.find(',')#finds the position tittle ends 
title_new = title[0].upper()+title[1:comma2].lower()# makes the firts letter of the title to be written in capita letters
print(ref[start_year:end_year+1],title_new+title[comma2:])# prints the reference in the correct format


