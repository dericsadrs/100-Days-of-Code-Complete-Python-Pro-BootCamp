print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

name1_true_count = 0
name2_true_count = 0
name1_love_count = 0
name2_love_count = 0

for char in name1.lower():
    if char in true_list:
        name1_true_count += 1
    if char in love_list:
        name1_love_count += 1

for char in name2.lower():
    if char in true_list:
        name2_true_count += 1
    if char in love_list:
        name2_love_count += 1

total_true_love_count = name1_true_count + name2_true_count + name1_love_count + name2_love_count

print(f"Total TRUE count: {total_true_love_count}")

# Combining the counts to make a 2-digit number
love_score = int(str(name1_true_count + name2_true_count) + str(name1_love_count + name2_love_count))

print(f"Love score: {love_score}")

# Interpret the love score and give a compatibility message
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
