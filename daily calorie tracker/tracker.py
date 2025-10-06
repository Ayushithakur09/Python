# Name: Ayushi Thakur, Date: 3.10.25, Title: Calorie tracker
#Task 1!
print("Welcome to your personalised daily Calorie Tracker\n\tThis tool will help you track your health and cut down excess calories! ")

#Task 2!
meals = []
m = int(input("How many meals would you like to enter? "))

#Task 5!
for i in range(m):
    meal = input("Enter meal type: ")
    while True:
        try:
            calories = int(input("Enter calories: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    meals.append({
        "Meal": meal,
        "Calories": calories
    })

# Table
print("\nYour Meal and Calorie Table:\n")
print("Meal       Calories")
print("-----------------------")
for entry in meals:
    print(f"{entry['Meal']:10}  {entry['Calories']}")
    
#Task3!
a=sum(entry['Calories'] for entry in meals)
print("\nTotal Calories:", a)

b=a/m
print("Average:",b)

#Task4!
if a>2000:
    print("\nNow its time for some work out!")
else:
    print("\nyou're pretty healthy!")


