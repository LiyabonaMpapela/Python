#simulate a simple BBS with one stored message and 2 fixed files
#Liyabona Mpapela
#24 August 2022
print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it''')
message=''
sel= input('Enter your selection:\n') # allows the user to choose what they want  to do in the program
while sel.upper()!='X':
 
 if sel.upper()=='E':
  message=input("Enter the message:\n")
 if sel.upper()=='V':
  if message!= '':
   print("The message is:",message)
  else:
   print("The message is: no message yet")
 if sel.upper()=='L':
  print("List of files: 42.txt, 1015.txt")
 if sel.upper()=='D':
  file_name = input("Enter the filename:\n") #allows the user to choose the file they want to see
  if file_name == "42.txt":
   print("The meaning of life is blah blah blah ...")
  elif file_name == "1015.txt":
   print('''Computer Science class notes ... simplified
Do all work
Pass course
Be happy''')
  else:
   print("File not found")# shows thet the chosen file does not exist
 print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it''')        
 sel= input('Enter your selection:\n') # allows the user to choose what they want  to do in the program

print("Goodbye!")
