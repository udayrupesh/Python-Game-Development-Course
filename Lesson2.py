#Restaurant Ordering System

menu = {
    1:{
        "Food" : "Burger",
        "Price" : 9.00
    },

    2:{
        "Food" : "Sandwich",
        "Price" : 4.00
    },

    3:{
        "Food" : "Pasta",
        "Price" : 8.00
    },

    4:{
        "Food" : "Large Pepparoni Pizza",
        "Price" : 14.00
    },

    5:{
        "Food" : "Tacos",
        "Price" : 7.00
    },

    6:{
        "Food" : "Caviar Dubai",
        "Price" : 45.00
        },
}

cart = {}

while True:
    print("-"*50)
    print("WELCOME TO THE UDAY HOUSE")
    print("-"*50)

    print("\nMENU")

    for item in menu:
        print(item,".", menu[item]["Food"], "- £" + str(menu[item]["Price"]))

    print("\n1. Add Food")
    print("2. View Cart")
    print("3. Remove food ")
    print("4. Generate Bill")
    print("5. Exit")


    choice = int(input("\nEnter your choice: "))    

    if choice ==1:
        foodNo = int(input("Enter the food number: "))

        if foodNo in menu:
            quantity = int(input("Enter the quantity:"))

            if foodNo in cart:
                cart[foodNo]["Quantity"] += quantity

            else:
                cart[foodNo] = {
                    "Food" : menu[foodNo]["Food"],
                    "Price": menu[foodNo]["Price"],
                    "Quantity" : quantity
                
                }

            print("Item added successfully!")

        else:

            print("Invalid food number. ")

    elif choice == 2:
        if len(cart) == 0:
            print("Your cart is empty!")

        else:
            print("\nYOUR CART")
            print("-" * 50)

            total = 0

            for item in cart:
                subtotal = cart[item]["Price"] * cart[item]["Quantity"]

                print(
                    cart[item]["Food"],
                    "| Qty: ", cart[item]["Quantity"],
                    "| Price: £" + str(cart[item]["Price"]),
                    "| Total: £" + str(subtotal)
                )

                total += subtotal

            print("-" * 50)
            print("Current Total : £",total)

    elif choice == 3:
        if len(cart) == 0:
            print("Your cart is empty!")

        else:
            print("\nItems in Cart")

            for item in cart:
                print(item, "-" , cart[item]["Food"])

            remove = int(input("Enter item number to remove:"))

            if remove in cart:
                del cart[remove]
                print("Item removed successfully")

            else:
                print("Item not found!")

    elif choice == 4:
        if len(cart) == 0:
            print("Your cart is empty!")

        else:

            print("\n" + "=" * 50)
            print(" FINAL BILL")
            print("=" * 50)

            total = 0

            for item in cart:
                subtotal = cart[item]["Price"] * cart[item]["Quantity"]

                print(
                    cart[item]["Food"],
                    "x",
                    cart[item]["Quantity"],
                    "=£" + str(subtotal)
                )

                total += subtotal

            print("-" * 50)

            gst = total * 0.05
            discount = 0

            if total >= 30:
                discount = total * 0.10

            final_amount = total + gst - discount

            print("Subtotal : £",total)
            print("GST (5%) : £", round(gst,2))
            print("Discount : £" , round(discount, 2))
            print("-" * 50)
            print("Grand Total : £", round(final_amount,2))
            print("=" * 50)

            print("\nThank you for visiting Python Restaurant!")

            break
    elif choice == 5:
        print("Thank you! Visit Again.")
        break
    else:
        print("Invalid Choice!")