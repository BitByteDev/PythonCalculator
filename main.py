"""Import calculator module"""

from modules.calculator import *

options = ["Sum", "sub", "mult", "div"]

"""Function for show all methods from options array"""


def show_options():
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


"""Main function"""


def main():
    while True:
        try:
            print("Welcome to calculator!")
            show_options()
            user_input = float(input("Please, select operation >> "))

            match user_input:
                case 1:
                    sum()
                case 2:
                    sub()
                case 3:
                    mult()
                case 4:
                    div()
                case _:
                    print("Error: Selected option not exists!")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
