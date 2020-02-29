room_num = 0
room_rent = 0
restaurant_bill = 0
laundry_bill = 0
game_bill = 0

def inputdata():
    global room_num
    global name
    global address
    global check_in_date
    global check_out_date

    name = input("\nEnter your name:")
    address = input("\nEnter your address:")
    check_in_date = input("\nEnter your check in date:")
    check_out_date = input("\nEnter your check out date:")
    print("Your room no.:", room_num, "\n")


def roomrent():
    global room_rent
    print("We have the following rooms for you:-")

    print("1.  type A---->rs 6000 Per Night")

    print("2.  type B---->rs 5000 Per Night")

    print("3.  type C---->rs 4000 Per Night")

    print("4.  type D---->rs 3000 Per Night")

    room_type = int(input("Enter Your Choice Please->"))

    nights_stayed = int(input("For how many nights did you stay ?:"))

    if (room_type == 1):

        print("you have opted room type A")

        room_rent = 6000 * nights_stayed

    elif (room_type == 2):

        print("you have opted room type B")

        room_rent = 5000 * nights_stayed

    elif (room_type == 3):

        print("you have opted room type C")

        room_rent = 4000 * nights_stayed

    elif (room_type == 4):
        print("you have opted room type D")

        room_rent = 3000 * nights_stayed

    else:

        print("please choose a room")

    print("your room rent is =", room_rent, "\n")


def restaurantbill():
    global restaurant_bill
    restaurant_bill = 0

    print("*****RESTAURANT MENU*****")

    print("1.water-------------Rs20",
          "2.tea---------------Rs10",
          "3.breakfast combo---Rs90",
          "4.lunch-------------Rs110",
          "5.dinner------------Rs150",
          "6.Exit", sep='\n')

    while (1):

        order = int(input("Enter your choice:"))

        if (order == 1):
            quantity = int(input("Enter the quantity:"))
            restaurant_bill += 20 * quantity

        elif (order == 2):
            quantity = int(input("Enter the quantity:"))
            restaurant_bill += 10 * quantity

        elif (order == 3):
            quantity = int(input("Enter the quantity:"))
            restaurant_bill += 90 * quantity

        elif (order == 4):
            quantity = int(input("Enter the quantity:"))
            restaurant_bill += 110 * quantity

        elif (order == 5):
            quantity = int(input("Enter the quantity:"))
            restaurant_bill += 150 * quantity

        elif (order == 6):
            break
        else:
            print("Invalid option")

        print("Total food Cost=Rs", restaurant_bill, "\n")


def laundrybill():
    global laundry_bill


    print("******LAUNDRY MENU*******")

    print("1.Shorts----Rs3",
          "2.Trousers--Rs4",
          "3.Shirt-----Rs5",
          "4.Jeans-----Rs6",
          "5.Girls suit--Rs8",
          "6.Exit", sep='\n')

    while (1):

        order = int(input("Enter your choice:"))

        if (order == 1):
            quantity = int(input("Enter the quantity:"))
            laundry_bill += 3 * quantity

        elif (order == 2):
            quantity = int(input("Enter the quantity:"))
            laundry_bill += 4 * quantity

        elif (order == 3):
            quantity = int(input("Enter the quantity:"))
            laundry_bill += 5 * quantity

        elif (order == 4):
            quantity = int(input("Enter the quantity:"))
            laundry_bill += 6 * quantity

        elif (order == 5):
            quantity = int(input("Enter the quantity:"))
            laundry_bill += 8 * quantity
        elif (order == 6):
            break
        else:

            print("Invalid option")

        print("Total Laundry Cost=Rs", laundry_bill, "\n")


def gamebill():
    global game_bill


    print("******GAME MENU*******")

    print("1.Table tennis--Rs60",
          "2.Bowling-------Rs80",
          "3.Snooker-------Rs70",
          "4.Video games---Rs90",
          "5.Pool----------Rs50",
          "6.Exit", sep='\n')

    while (1):

        game = int(input("Enter your choice:"))

        if (game == 1):
            hours = int(input("No. of hours:"))
            game_bill += 60 * h

        elif (game == 2):
            hours = int(input("No. of hours:"))
            game_bill += 80 * hours

        elif (game == 3):
            hours = int(input("No. of hours:"))
            game_bill += 70 * hours

        elif (game == 4):
            hours = int(input("No. of hours:"))
            game_bill += 90 * hours

        elif (game == 5):
            hours = int(input("No. of hours:"))
            game_bill += 50 * hours
        elif (game == 6):
            break

        else:

            print("Invalid option")

        print("Total Game Bill=Rs", game_bill, "\n")


def display():
    global room_num
    print("******HOTEL BILL******")
    print("Customer details:")
    print("Customer name:", name)
    print("Customer address:", address)
    print("Check in date:", check_in_date)
    print("Check out date", check_out_date)
    print("Room no.", room_num)
    print("Your Room rent is:", room_rent)
    print("Your Food bill is:", restaurant_bill)
    print("Your laundry bill is:", laundry_bill)
    print("Your Game bill is:", game_bill)

    services_bill = restaurant_bill + laundry_bill + game_bill
    total_bill = services_bill + room_rent

    print("Your sub total bill is:", room_rent)
    print("Additional Service Charges is", services_bill)
    print("Your grand total bill is:", total_bill, "\n")
    room_num += 1


def main():
    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate game bill")

        print("6.Show total cost")

        print("7.EXIT")

        option = int(input("\nEnter your choice:"))
        if (option == 1):
            inputdata()

        if (option == 2):
            roomrent()

        if (option == 3):
            restaurantbill()

        if (option == 4):
            laundrybill()

        if (option == 5):
            gamebill()

        if (option == 6):
            display()

        if (option == 7):
            quit()


main()

