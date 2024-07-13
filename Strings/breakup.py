#outputs a sentence as a comma-separated list of lowercase words with a full-stop at the end
#Liyabona Mpapela
#29 August 2022
sentence=input("Enter a sentence:\n")#allows the user to enter a sentence
sentence1=sentence.lower()# converts the sentence to small letters
print("The word list:",sentence1.replace(' ',', ')+'.')#places a comma and a space in where there was a space so the the words can be separated by a comma followed by space
