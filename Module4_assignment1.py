#Defines what the function "send_message" is
def send_message():
    for _ in range(10):
        print("Yeah it is")

#asks the user if today is a good day
day = input("Is today a good day? y or n: ")

#Responds to the user input
if day == ("y"):
    send_message()