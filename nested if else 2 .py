starter_available = True
main_course_available = True
dessert_available = True

print("Menu:")
print("1. Starter")
print("2. Main Course")
print("3. Dessert")

order_type = input("Enter order type (Starter/Main Course/Dessert): ").strip().lower()

if order_type == "starter":
    if starter_available:
        print("Starter ordered successfully!")
    else:
        print("Sorry, starters are unavailable.")

elif order_type == "main course":
    if main_course_available:
        print("Main course ordered successfully!")
        print("Choose a side:")
        print("1. Raita")
        print("2. Salad")
        print("3. None")
        side_choice = input("Enter side choice (1/2/3): ")

        if side_choice == "1":
            print("You ordered main course with raita.")
        elif side_choice == "2":
            print("You ordered main course with salad.")
        else:
            print("You ordered main course without a side.")
    else:
        print("Sorry, main course is unavailable.")

elif order_type == "dessert":
    if dessert_available:
        print("Dessert ordered successfully!")
        print("Choose a topping:")
        print("1. Nuts")
        print("2. Chocolate Syrup")
        print("3. None")
        topping_choice = input("Enter topping choice (1/2/3): ")

        if topping_choice == "1":
            print("You ordered dessert with nuts.")
        elif topping_choice == "2":
            print("You ordered dessert with chocolate syrup.")
        else:
            print("You ordered dessert without a topping.")
    else:
        print("Sorry, desserts are unavailable.")

else:
    print("Invalid order type entered. Please choose Starter, Main Course, or Dessert.")