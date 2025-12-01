# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
weather = int(input("What is the weather?"))

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

if weather >= 50:
    print("Cold")

elif weather >= 70 and weather <= 87:
    print("Warm")

elif weather >= 80 and weather <= 90:
    print("Hot")

elif weather >= -10 or weather <= 110:
    print("Extreme temperature warning!")
