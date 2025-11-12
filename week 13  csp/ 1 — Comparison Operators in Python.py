# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4
print(a == b) #output False

print(a == b)   # checks for equality (false)
print(a != b)   # checks if it is not equal (true) 
print(a > b)    # cheks for greater than (false)
print(a < b)    # checks for less than (true)
print(a >= b)   # checks for greater than or equal to (false)
print(a <= b)   # checks for less that or equal to (true)


#predict the output of the following comparisons:
10 > 5 # True
7 == 2 * 3 + 1 # True
8 != 8 # False
4 <= 2 + 2 # True

# Write 3 examples that result in True and 3 that result in False.
10 >= 5 + 3 + 1 # True
6 != 2 * 2 # True
5 <= 3 + 2 # True




# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"



# asking student score
score = int(input("What is your score?"))
# make this program for all grading spectrums
# if the score is between 90 - 100 ... you got an A
if score >= 90 and score <= 100:
    print("You got an A!")
# if the score is between 80 - 90 ... you got a B
elif score >= 80 and score <= 90:
    print("You got a B")
# if the score is bwtween 70 - 79 ... you got a C
elif score >= 70 and score <= 79:
    print("You got a C")
# if the score is between 61 - 69 ... you got a D
elif score >= 61 and score <= 69:
    print("You got a D")
# else you failed
else:
    print("You failed, come for ACLAB")


# if score >= 60:
#     print("You passed the test")
# else:
#     print("You didn't pass")


# asking for password
password = input("What is your password?")
# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
if len (password) >= 8 and any (char.isdigit() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid. " \
          "It must be at least 8 characters long and contain at least one digit.")