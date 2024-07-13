#o find all palindromic primes between two integers 
#Liyabona Mpapela
#6 October 2022
from palindrome import palindrome# imports the palindrome function in the palindrome file
import sys
sys.setrecursionlimit (30000)


start= int (input("Enter the starting point N:\n"))#recirves starting number from the uer
end = int (input("Enter the ending point M:\n"))#receives ending number from thr user
print('The palindromic primes are:')
def isPrime(n, i = 2):
    #checks if a number is a prime number
    if n == 1:
        return False
    if i> n/2:
        return True
    if n%i==0:
        return False        
    return isPrime(n,i+1)
    
def palindromic_primes(N,M):
    #checks if a number is palindromic and is a prime number
    if N>M:
        return
    if palindrome(str(N)):#checks if a number is palindromic
        if isPrime(N):#checks if a number is a prime number
            print(N)#prints the number if it is palindromic and is a prime number
    palindromic_primes(N+1, M)#repeats the function on the next number
    
     
palindromic_primes(start,end)# calls the function to check if a number is palindromic and is a function
        
    
    


     
    