#translating sentences between English and a variant of Pig Latin
#Liyabona Mpapela
#22 September 2022
vowels= 'a','e','i','o','u'

def to_pig_latin(sentence):#converts an english sentence to Pig Latin
    dummy_sentence = ""#assigns dummy_sentence to an empty string
    word=sentence.split()#changes the string to a list
    for i in word:
        if i[0] in vowels:
            dummy_sentence = dummy_sentence +" " +i+'way'        
        
        else:
            cons=0
            for l in i:
                
                if l not in vowels:
                    cons=cons+1
                else:
                    break;
            dummy_sentence = dummy_sentence+ " " +i[cons:]+'a'+i[0:cons]+'ay'
           
                           
 
    return dummy_sentence.strip() 

def to_english(sentence):#converts a Pig Latin sentence to english
    dummy_sentence=""#assigns dummy_sentence to an empty string
    word=sentence.split()#changes the string to a list
    for i in word:
        if i[-3:]=='way' and i[0] in ('a','e','i','o','u'):
            dummy_sentence = dummy_sentence+ " "  + i[0:-3]
            
        elif i[-5]=='a'and i[-4] not in('a','e','i','o','u') and i[-3] not in('a','e','i','o','u') and i[-2:]=='ay':
            dummy_sentence = dummy_sentence+" "+i[-4:-2]+i[0:-5]  
            
        elif  i[-4]=='a' and i[-3] not in('a','e','i','o','u') and i[-2:]=='ay':
            dummy_sentence = dummy_sentence+" "+i[-3]+i[0:-4] 
            
        else:
            dummy_sentence = dummy_sentence+ " "  +i
            
    return dummy_sentence.strip()
