#!/usr/bin/env python3
# Sample script that writes to a file
# By Brady Lynch

#Creates a file called "hackme.txt"
hackme = open("hackme.txt", "w")

#Asks for the user input
NameQuestion = input("What is your name? ")
ColorQuestion = input("What is your favorite color? ")
PetQuestion = input("What was your first pet's name? ")
MotherQuestion = input("What is your mother's maiden name? ")
SchoolQuestion = input("What elementary school did you attend? ")

#Saves code to "hackme.txt"
hackme.write(f"{NameQuestion}\n")
hackme.write(f"{ColorQuestion}\n")
hackme.write(f"{PetQuestion}\n")
hackme.write(f"{MotherQuestion}\n")
hackme.write(f"{SchoolQuestion}\n")

#Closes "hackme.txt"
hackme.close()