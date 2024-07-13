#searches a file for anagrams of a given word, printing the results in alphabetical order
#Liyabona Mpapela
#12 october 2022
print("***** Anagram Finder *****")
try:
    file= open("EnglishWords.txt","r")#open file
    
    print("Enter a word: ",end="")
    
    sword= input()#receives word from the user
    
    print()
    sortedword=sorted(sword)#sorts words
    
    words=[]#creates an empty list
    for line in file:#loops through file
        if line=='SART':
            break#does not concider all information before the word START
        line=line.strip()#removes spacea after the word on each line
        words.append(line)#inserts the words to the list
    sorted_words=[]#creates an empty list
    for word in words:
        sorted_words.append(sorted(word))#inserts the word sorted in alphabetical form to the list
    anagrams=[]   
    for i in range(len(sorted_words)):
        if sorted_words[i]==sortedword :#checks for anagram words sorted in aplabetical form
            if words[i]!=sword:#checks for anagrams and exlude words that are the same
                anagrams.append(words[i])#add word to anagrms list
    if anagrams!=[]:#if the list is not empty
        print(anagrams)
    else:
        print("Sorry, anagrams of '"+sword+"' could not be found.")
        
            
except IOError:# if try fails
    print("Sorry, could not find file 'EnglishWords.txt'.")
        