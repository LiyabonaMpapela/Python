#print out the numbers n to n+41 as 6 rows of 7 numbers
#Liyabona Mpapela
#18 August 2022
original_n = eval(input("Enter the start number:\n"))
n = original_n
if n>-6 and n<2 :
    for s in range(1,7):
        for i in range(1,8):
            if n>(original_n+41):
                continue                    
            formatted = "{0:>2}".format (n)
            print(formatted,end=' ') 
            n = n+1
        print( )
            
            
            