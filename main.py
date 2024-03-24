user_height = float(input("Enter your height in centimeters: "))
user_weight = float(input("Enter your weight in kilograms: "))

user_bmi = user_weight / ((user_height / 100) ** 2)



# Check the BMI range and print the corresponding message)



if (user_bmi <= 16):
    print("You have a problem")
elif(user_bmi >= 16 and user_bmi <= 18.5):
    print("Deficit body weight")
elif(user_bmi >= 18.5 and user_bmi <= 25):
    print("You are ok bro")
elif(user_bmi >= 25 and user_bmi <= 30):
     print("You have a preobesity")
elif(user_bmi >= 30 and user_bmi <= 35):
    print("You have obesity type 1")
elif(user_bmi >= 35 and user_bmi <= 40):
    print("You have obesity type 2")
elif(user_bmi >= 40):
    print("You have obesity type 3")
else:
    print("Try again please")  

print("Your BMI is:", user_bmi)


input("Press enter to exit")