#debugging
#Liyabona Mpapela
#12 October 2022
print('***** Program Trace Utility *****')
filename=input('Enter the name of the program file:')#receives name of file 
file=open(filename,"r")#opens the file
lines=file.readlines()#reads the lines in the file and creates a list containing them
file.close()#close file

if lines[0] == '"""DEBUG"""\n':#if the first line of the file is written """DEBUG"""
    
    for i,line in enumerate(lines):
        line = line.strip()#removes the spaces at the end of the line
        if 'DEBUG' in line:#if the line has a the word 'DEBUG'
            lines.pop(i) #remove the line
            
    myfile=open(filename,"w")#creates a new file
    for line in lines:#loop through the lines in the list 
        print(line, end = "",file=myfile)#write the new list to a a file
    print('Removing...Done')
else:
    lines.insert(0,'"""DEBUG"""\n')# insert ' """DEBUG""" ' on the first line of the array
    for i,line in enumerate(lines):
        if 'def' in line:
            bracket=line.find('(')#find position of opening bracket
            insert='    """DEBUG"""'+";print('"+line[4:bracket]+"')\n"
            lines.insert(i+1,insert)#insert in the next line
    myfile=open(filename,"w")#creates a new file
    for line in lines:#loop through the lines in the list
        print(line, end = "",file=myfile)#write the new list to a a file   
    print('Inserting...Done')
    
    
myfile.close()
    
    
        
            