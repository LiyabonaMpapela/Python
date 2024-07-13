#set of 8 test cases that achieve path coverage
#Liyabona Mpapela
#22 September 2022
'''
>>> import timeutil
>>> timeutil.validate("111:01 p.m.")
False
>>> timeutil.validate("12:46 am")
False
>>> timeutil.validate("08 03 p.m.")
False
>>> timeutil.validate("01:01 a.m.")
False
>>> timeutil.validate("10:sp a.m.")
False

'''
import doctest 
doctest.testmod(verbose=True)

