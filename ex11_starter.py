#!/usr/bin/python
# Exercise 11a
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(len(Belgium)) # printing the length/ number of characters in Belgium string variable
print(Belgium) # printing string alongside hyphens
print("-"*81) # running command in terminal to multiply hyphens by the length/ number of characters in string variable

print("-"*len(Belgium)) # tidied/ simplified version to multiply hyphens by length/ number of string characters by it doesn't show string length = 81
print(Belgium)

# Exercise 11b
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
Belgium_colon = Belgium.replace(',',':')
# created a new variable to display a new line of string for variable 'Belgium' with commas
# use of the replace method to change comma separators into colon
print(Belgium_colon)

# Exercise 11c
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium.split(','))

Belgium_list = ['Belgium', '10445852', 'Brussels', '737966', 'Europe', '1830', 'Euro', 'Catholicism', 'Dutch', 'French',
                'German']
# converted string into a mutable list to extract values from
population = int(Belgium_list[1]) + int(Belgium_list[3])
# created a new variable to add second and third integers in list starting from zero
print(population)
# use built-in function to command the sum of population variable in terminal
