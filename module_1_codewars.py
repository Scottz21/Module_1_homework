# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
  if number % 2 == 0:
    # If number divided by 2 is equal to zero then:
    return "Even"
    # If not:
  else:
    return "Odd"



# Convert a Number to a String!
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str (num)
# Returned string (num) 



# Remove string spaces
# Write a function that removes the spaces from the string, then return the resultant string.
# Examples (Input -> Output):

def no_space(x):
    a = x.replace(" ", "")
    return a   
# replaced spaces in x to a which equals x with no spaces
