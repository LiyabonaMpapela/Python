# count the number of pairs of consecutive characters in a string
#Liyabona Mpapela 
#6 October 2021
message=input('Enter a message:\n')#receives string from the user
def pairs(message):
     #counts the number of consecutive characters in a string
     if len(message)<2: #cheks if the lenth of the string is greater or equal to 2
          return 0
     else:
          if message[0]==message[1]:#checks if two letters that are next to each other in the string are the same 
               return 1+pairs(message[2:]) #adds one and repeats the function starting on the third letter of the string
          else:
               return 0+pairs(message[1:])#repeats the function starting on the second letter of the string
print('Number of pairs:',pairs(message))#prints the number of pairs