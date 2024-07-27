#Opens "hackme.txt"
hackme = open("hackme.txt", "r")

#Reads and prints the information from "hackme.txt"
info = hackme.read()
print(f"Here is someone to hack \n{info}")

#Closes "hackme.txt"
hackme.close()