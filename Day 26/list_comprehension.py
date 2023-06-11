#
# Created on Sun Jun 11 2023
# Created by Software Engineer Deric San Andres
#

# numbers = [1,2,3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)
#
# numbers = [1,2,3]

# new_list = [ n + 1 for n in numbers]
# print(new_list)

name = "Angela"
letters_list = [ letter for letter in name ]

print(letters_list)


range_list = [ num * 2 for num in range(1,5)]
names = [ "Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

long_names = [ long_name.upper() for long_name in names if len(long_name) > 5]
print(long_names)