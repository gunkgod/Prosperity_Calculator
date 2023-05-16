
"""
The initial line asks for the name of the fictitious country. The prosperity of the country is determined by 3 variables that go into the country.
"""

# these varibales are global to be used later in the list

GDP = 0
Population = 0
inflation_rate = 0

# define country name

print("Hi. Welcome to Country Prosperity Simulator. Enter the name of your country:")

country_input = input()

# this function uses the country name from user input to ask questions pertaining to GDP, Population and Inflation Rate

def prosperity(country):
  GDP = float(input("Enter GDP for " + country + ": "))
  Population = float(input("Enter population for " + country + ": "))
  inflation_rate = float(input("Enter inflation rate for " + country + ": "))
  return GDP, Population, inflation_rate

prosperity(country_input)

# this list takes two elements for each index set, the global variables for the country and the criteria, that later determines the boolean statement concluding if user input is true or false

determine_propserity = [(GDP, 1000000.0), (Population, 100000.0), (inflation_rate, 2.0)]

"""
This for loop uses the boolean i variable to determine the user's country created by prsoperity(). It compares the value to the variable within the list for the index and determines wether i is true or false.
"""
i = True
for value, min_value in determine_propserity:
  if value > min_value:
    i = False

# the if statement will give a response to if the user's country is propserous or not determined by the i variable

if i == True:
  print("Congratulations. " + country_input + " is prosperous.")
else:
  print(country_input + " is not prosperous.")
  