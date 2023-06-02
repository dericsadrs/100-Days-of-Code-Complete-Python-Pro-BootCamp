#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#
#Given string
string1="This is Python"
 
print("The actual string:",string1)
 
#converting string1 into a list of strings
string1=string1.split()
 
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)