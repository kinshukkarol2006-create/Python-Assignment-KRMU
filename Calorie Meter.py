# Name Kinshuk Karol
#B.tech cse (aiml)
# Calorie Meter Program with Total, Average, and Limit Comparison

print("Welcome to the Calorie Meter ")
print("Enter the food items you eat and their calories.")
print("Type 'done' when you are finished.\n")

calorie_list = []  # list to store all calorie values

while True:
    food = input("Enter food item (or 'done' to finish): ").strip()

    if food.lower() == "done":
        break  # stop taking inputs

    try:
        calories = float(input(f"Enter calories for {food}: "))
        calorie_list.append(calories)
        print(f"Added {calories} calories from {food}.\n")
    except ValueError:
        print(" Please enter a valid number for calories.\n")
# Calculate total and average

if calorie_list:
    total_calories = sum(calorie_list)
    average_calories = total_calories / len(calorie_list)
    print("\n============================")
    print(f"Total meals entered: {len(calorie_list)}")
    print(f"Total Calorie Intake: {total_calories:.2f} kcal")
    print(f"Average Calories per Meal: {average_calories:.2f} kcal")
    print("============================")

    # Ask for daily calorie limit

    try:
        limit = float(input("\nEnter your daily calorie limit: "))
        print("----------------------------")
        if total_calories > limit:
            print(f" You exceeded your daily limit by {total_calories - limit:.2f} kcal.")
        elif total_calories < limit:
            print(f" You are {limit - total_calories:.2f} kcal below your daily limit.")
        else:
            print(" You met your daily calorie limit exactly!")
    except ValueError:
        print(" Invalid input for daily limit.")
else:
    print("No food items entered. Please run the program again.")

print("\nStay healthy and track your meals daily")