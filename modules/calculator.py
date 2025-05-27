"""Function for search numbers amount"""


def sum():
    try:
        a = int(input("Enter the first number >> "))
        b = int(input("Enter the second number >> "))

        answer = a + b
        print(answer)
    except Exception as e:
        print(f"Error: {e}")


"""Function for search numbers difference """


def sub():
    try:
        a = int(input("Enter the first number >> "))
        b = int(input("Enter the second number >> "))

        answer = a - b
        print(answer)
    except Exception as e:
        print(f"Error: {e}")


"""Function for numbers multiply"""


def mult():
    try:
        a = int(input("Enter the first number >> "))
        b = int(input("Enter the second number >> "))

        answer = a * b
        print(answer)
    except Exception as e:
        print(f"Error: {e}")


"""Function for numbers divide"""


def div():
    try:
        a = int(input("Enter the first number >> "))
        b = int(input("Enter the second number >> "))

        if b != 0:
            answer = a / b
            print(answer)
        else:
            print("Error: You can't divide on 0!")
    except Exception as e:
        print(f"Error: {e}")
