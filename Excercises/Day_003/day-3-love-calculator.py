print("The Love Calculator is calculating your score...")
name1 = input(print("What is your name?: "))
name2 = input(print("What is their name?: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

merged_names = name1 + name2
merged_names_lower = merged_names.lower()

# Count T, R, U, E occurrence
count_t = merged_names_lower.count("t")
count_r = merged_names_lower.count("r")
count_u = merged_names_lower.count("u")
count_e = merged_names_lower.count("e")
true_count = count_t + count_r + count_u + count_e

# Count L, O, V, E occurrence
count_l = merged_names_lower.count("l")
count_o = merged_names_lower.count("o")
count_v = merged_names_lower.count("v")
count_e = merged_names_lower.count("e")
love_count = count_l + count_o + count_v + count_e

score = int(str(true_count) + str(love_count))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
