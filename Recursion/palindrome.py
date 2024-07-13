# checks whether or not a string is a palindrome
#Liyabona Mpapela
#6 October 2022


def palindrome(string):
    #checks if a string is a palindrome or not
    if len(string)==0:#checks if there is a word or if the string contains something
        return True
    if string[0]!=string[-1]:#checks if the first letter and last letter of the string are the same
        return False
    else:
        return palindrome(string[1:-1])#repeats the function cutting out the first and last letters
if __name__=='__main__':
    #calls the main function
    string=input('Enter a string:\n')#receives the string from the user
    if palindrome(string):# checks if the string is a palindrome
        print('Palindrome!')
    else:
        print('Not a palindrome!')

        
    