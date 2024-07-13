2# Gumatj arithmetic
#Liyabona Mpapela
#22 September 2022

def gumatj_to_decimal(a):#covert a gumatj number to a decimal number
    gum=a
    i=0
    dec=0
    while gum!=0:
        dec=dec+(5**i)*(gum%10)
        gum=gum//10
        i+=1
    return dec 
def decimal_to_gumatj(a):#convert a decimal to gumatj
    dec=a
    gum=0
    i=0
    while dec!=0:
        gum+=(dec%5)*(10**i)
        dec=dec//5
        i+=1
    return gum
        
def gumatj_add(a, b): #Add two gumatj numbers
    a=gumatj_to_decimal(a)
    b=gumatj_to_decimal(b)
    add=a+b#adds the two numbers
    gumatj=decimal_to_gumatj(add)#converts the number to gumatj
    return gumatj #returns the answer of two added Gumatj numbers

def gumatj_multiply(a, b):#multiply two gumatj numbers
    a=gumatj_to_decimal(a)
    b=gumatj_to_decimal(b)    
    multiple=a*b#multiplies two numbers
    gumatj=decimal_to_gumatj(multiple)#converts the number to gumatj
    return gumatj #returns the answer of two multiplied Gumatj numbers