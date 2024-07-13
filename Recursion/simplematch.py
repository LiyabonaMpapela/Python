# determine if a given pattern matches a given word
#Liyabona Mpapela
#6 October 2022

pattern=input("Enter a pattern (or 'q' to quit):\n")#receives a pattern from the user
word=input("Enter a word:\n")#receives the word from thr user
def match(pattern, word):
    #Checks if the pattern and word match
    if pattern==word:#checks if the pattern and the word are the same 
        return True
    if len(pattern)==0 or len(word)==0:#checks if one of the word has ended or not
        return False
    if pattern[0]==word[0] or pattern[0]=='?':#checks if the letter of the word is the same as the letter of the pattern on a specific position or if there is a question mark on that position of the pattern
        return match(pattern[1:],word[1:])#reapeats the fuction starting on thr next letters of the pattern and of the word
    return False
if pattern!='q': #checks if the user wants to quit or exit  
    if match(pattern, word) : #Checks if the pattern and word match
        print("It's a match.")
    else:
        print("They don't match.")
            
        
    