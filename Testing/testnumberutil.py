#set of 8 test cases that achieve path coverage
#Liyabona Mpapela
#22 September 2022

'''
>>> import numberutil
>>> numberutil.aswords(399)
'three hundred and ninety nine'
>>> numberutil.aswords(56)
'fifty six'
>>> numberutil.aswords(700)
'seven hundred'
>>> numberutil.aswords(119)
'one hundred and nineteen'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(8)
'eight'

'''
import doctest 
doctest.testmod(verbose=True)



