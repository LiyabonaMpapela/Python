#print a sequence of 7 numbers
#Liyabona Mpapela
#18 August 2022
n = eval(input("Enter the start number:\n"))
if n>-6 and n<93 :
    for i in range(1,7+1):
        formatted = "{0:>2}".format (n)
        print(formatted,end=' ')
        n = n+1
    