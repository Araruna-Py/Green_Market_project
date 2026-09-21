# Difining the main goals:
# - Create a program that a user can use to buy products in the market:
# (function goal) > (functions name)
#       - Menu > main()
#                "The main function open the products file and let the user
#                 choose one of these options: Buy a product; Shopping cart 
#                 list; Payment method; and Log off"
#              > get_pim() - return dictionary "pim_file"
#                "This function open the Product Information Management 
#                 file and return the variable to the mainc function."
#              > get
#       - Client Cart > client_cart(user_products_cart) - return dictionary "updated_cart"
#       - Payment method > payment_method(green_name_account, account_m_payment) return bool
#       - Log in > user_account() - return "green_name_account" and "account_m_payment"
#       - Historic > historic()
#
# Phases of the program:
# - Phase 1: Create the goals and plans for the project;
# - Phase 2: Develop the functions according to the plan;
# - Phase 3: Write the errors type to each function;
# - Phase 4: Test the functions of their error type;
# - Phase 5: Adapt the program to GUI (Learning process);
#
# Historical access
# 09/07/2026 10:53am - 12:05pm - Creating the project (goals and functions plans and the funcions).
# 09/12/2026 11:00am - 1:08pm - Continue creating the functions plan and config the Git Hub.
# 09/14/2026 06:34pm - 07:42pm - Update the plans, create the menu options and the variables in the 
# main function program the log off option to end the program.
# 09/17/2026 10:19am - 10:56am - Update the functions plan and the functions.
# 09/21/2026 10:18am - 11:00am - Create the PIM csv file. 
# 09/21/2026 11:39am - 12:55pm - Add 6 products at the PIM file.


def get_pim():
    """
    This function open the Product Information Management 
    file and return the variable to the mainc function.
    """
    pass
def client_cart(user_products_cart):
    pass
def payment_method(green_name_account, account_m_payment):
    pass
def user_account():
    pass
def historic(user_products_cart):
    pass
def main():
    """
    The main function open the products file and let the user 
    choose one of these options: Buy a product; Shopping cart 
    list; Payment method; and Log off.
    """
    pim_file = get_pim()

    menu = ["Log in", "Search and Buy", "Cart", "Pay", "Log off"]
    user_option = ""
    client_account = ""
    log_off = True
    last_chance = ""
    present_log_in = False

    while log_off == True:
        option_number = 0
        if present_log_in == True:
            print(f"Hello, {client_account}")
        else:
            print("Welcome!")
        print()
        for main_option in menu:
            option_number += 1
            print(f"{option_number}. {main_option}")
        print()
        user_option = int(input("Type only the number of the option: "))
        print()

        if user_option == 1:
            pass
        elif user_option == 2:
            pass
        elif user_option == 3:
            pass
        elif user_option == 4:
            pass
        elif user_option == 5:
            # Log off
            last_chance = input("Are you sure? (Y/N): ")
            last_chance = last_chance.capitalize()
            print()
            if last_chance == "Y":
                log_off = False
            elif last_chance == "N":
                last_chance = ""
            else:
                print("Invalid answer")
                print()
        else:
            print("Invalid number or character.")
            print()


if __name__ == "__main__":
    main()