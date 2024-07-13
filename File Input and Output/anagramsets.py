#search the ‘EnglishWords.txt’ file for sets of words that are that length and are anagrams of each other, and will write the results to a file with the given filename.
#Liyabona Mpapela
#12 October 2022
print('***** Anagram Set Search *****')
Length=int(input('Enter word length:\n'))#receives length of words from the user
print('Searching...')
filename=input('Enter file name:\n')#receives name of file of the new file that will be created
print('Writing results...')
try:
    file=open("EnglishWords.txt","r")#opens the file
    words=file.readlines()#creates a list  of the lines of the file
    file.close()#closes file
    length_word=[]#craetes an empty list
    for i in words:#loops through the list 
        if len(i.strip())==Length:#checks for words with the length that the user entered
            length_word.append(i.strip())#inserts worlds with the length to the array
    
    list=[]#creates empty list
    for i in range(len(length_word)):
        anagramset=[length_word[i]]#assighns to the words of the lenth the user chose
        word = sorted(length_word[i])#sorts the words in alphabetibal form 
        
        for t in range(i+1,len(length_word)):
            if length_word[t]!='0':
                if word == sorted(length_word[t]):
                    anagramset.append(length_word[t])# insert the word to the list
                    length_word[t]='0'
                    
        if len(anagramset) > 1:
            list.append(sorted(anagramset))#insert the anagramset list in the listsorted alphahetically 
            
    list = sorted(list)#sort list
            
            
    myfile=open(filename,"w")#create new file
    for line in list:#loop through list
        print(line, file = myfile)#write list into file created
    myfile.close()
except:#if try fails
    print("Sorry, could not find file 'EnglishWords.txt'.")


