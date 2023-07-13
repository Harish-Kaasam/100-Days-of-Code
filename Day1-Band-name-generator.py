#input() will get user input in console 

#Then print() will print the word "Hello" and the user input.
# ' \n ' adds new line 

#1. Create a greeting for your program.
print("Welcome to the Bandname Generator")
#2. Ask the user for the city that they grew up in.
city_name = input("In which city did you grew up in?\n")

#3. Ask the user for the name of a pet.
pet_name = input("What is your pet name?\n")

#4. Combine the name of their city and pet and show them their band name.

band_name = city_name +" "+ pet_name
print(band_name)

#or

print("Your band name could be" +" "+ city_name + "-" + pet_name)

#5. Make sure the input cursor shows on a new line:
