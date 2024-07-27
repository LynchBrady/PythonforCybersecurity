#Module4_assignment2

#Creates a file called "hackme.txt"
hackme = open("hackme.txt")

#Asks for the user input
namequestion = input("What is your name? ")
colorquestion = input("What is your favorite color? ")
petquestion = input("What was your first pet's name? ")
motherquestion = input("What is your mother's maiden name? ")
schoolquestion = input("What elementary school did you attend? ")

#Saves code to "hackme.txt"
hackme.write(namequestion/n)
hackme.write(colorquestion/n)
hackme.write(petquestion/n)
hackme.write(motherquestion/n)
hackme.write(schoolquestion/n)

hackme.close()