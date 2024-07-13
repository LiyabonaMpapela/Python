#program will print out every 7th number in the range n to n+41
#Liyabona Mpapela
#18 August 2022
n = eval(input("Enter a number:\n"))
if n>-6 and n<2 :
    w = n + 41
    while n <= w:
        formatted = "{0:>2}".format (n)
        print(formatted)
        n = n+7
    