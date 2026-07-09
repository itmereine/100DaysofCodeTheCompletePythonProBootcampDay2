print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    #print("You can ride the rollercoaster")
    if age >= 18:
        print("You can ride the rollercoaster")

    elif age >= 15:
        print("u can ride with ur perents or any adult")

    else:
        print("the ride might be dengouruse for u ")
else:
    print("You can ride the rollercoaster but i suggest u to not go")


