dog_points = 0
cat_points = 0
fish_points = 0

answer1 = input("do you prefer A runing, B walking, or C swiming?  ")
if answer1 == "A":
    dog_points += 1
elif answer1 == "B":
    cat_points += 1
elif answer1 == "C":
    fish_points += 1
("")
answer2 = input("do you prefer A sports, B school, C doing nothjing?  ")
if answer2 == "A":
    dog_points += 1
    fish_points +=1
elif answer2 == "B"or answer2 == "C":
    cat_points += 1
("")
answer3 = input("do you prefer A talking, B staying quite, or C staring at people?  ")
if answer3 == "A":
    dog_points += 1
elif answer3 == "B":
    cat_points += 1
elif answer3 == "C":
    fish_points += 1
("")
answer1 = input("do you prefer A tiktok, B movies, or C waching lofi?  ")
if answer1 == "A":
    dog_points += 1
elif answer1 == "B":
    cat_points += 1
elif answer1 == "C":
    fish_points += 1
("")

if dog_points >= fish_points and dog_points >= cat_points:
    print("you are a dog")
if fish_points >= dog_points and fish_points >= cat_points:
    print(" you are a fish")
if cat_points >= fish_points and cat_points >= dog_points:
    print("you are a cat")