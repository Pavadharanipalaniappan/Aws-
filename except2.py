while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except TypeError:
        print("Invalid input. Please enter a numerical value.")

print("The input is:", num)