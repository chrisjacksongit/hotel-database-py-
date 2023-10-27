# Python version of the hotel database

print("[Hotel Database]")
print("\nSelect from the choices below:")
print("1) Book a hotel stay")
print("2) Leave a review")
print("3) Check out of a hotel")
print("4) Quit")

selection = int(input("\nEnter your selection: ")) # Allows the user to enter their selection

while selection == 1: 
    name = str(input("\nWhat is your name? - "))
    days = int(input("How many days are you staying? - "))
    hotel = str(input("What hotel are you staying at? - "))
    address = str(input("What is the address of the hotel? - "))
    print("Thank you! You have successfully been booked.")
    break
    
while selection == 2:
    name2 = str(input("\nWhat hotel do you want to interview? - "))
    stars = int(input("How many stars do you want to rate the hotel? - "))
    review = str(input("Can you please provide a description of your experience? - "))
    print("Thanks! Your review has been submitted.")
    break
    
while selection == 3:
    hotel2 = str(input("What hotel are you checking out of? - "))
    room = str(input("What is your room number? - "))
    address2 = str(input("What is the address of the hotel? - "))
    print("Thank you! You have successfully checked out.")
    break

while selection == 4:
    print("Thanks for visiting! Have a nice day!")
    break