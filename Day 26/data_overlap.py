#
# Created on Sun Jun 11 2023
# Created by Software Engineer Deric San Andres
#


with open("file1.txt") as file1:
    file1_list = [int(n.strip()) for n in file1.readlines()]
with open("file2.txt") as file2:
    file2_list = [int(m.strip()) for m in file2.readlines()]

print(f"file 1: {file1_list} \nfile 2: {file2_list}")

result = [ num for num in file1_list if num in file2_list]

print(result)