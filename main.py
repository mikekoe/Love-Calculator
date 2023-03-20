print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

addNames = name1 + name2
change_name_case = addNames.lower()

t = change_name_case.count("t")
r = change_name_case.count("r")
u = change_name_case.count("u")
e = change_name_case.count("e")

true = t+r+u+e

l = change_name_case.count("l")
o = change_name_case.count("o")
v = change_name_case.count("v")
e = change_name_case.count("e")

love = l+o+v+e

true_love_score = int(str(true) + str(love))

if (true_love_score < 10) or (true_love_score > 90):
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")

elif (true_love_score >= 40) or (true_love_score <= 50):
    print(f"Your score is {true_love_score}, you are alright together")

else:
    print(f"Your score is {true_love_score}")