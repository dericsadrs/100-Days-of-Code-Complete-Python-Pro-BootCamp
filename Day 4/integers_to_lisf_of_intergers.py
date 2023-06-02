#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#

#string with integers sepated by spaces
string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1))
 
#converting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
 
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)