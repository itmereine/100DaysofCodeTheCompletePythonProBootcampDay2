print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Child tickets are ru50.")
    elif age <= 18:
        bill = 70
        print("Youth tickets are ru70.")
    else:
        bill = 100
        print("Adult tickets are ru100.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bill += 30

    print(f"Your final bill is ru{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
