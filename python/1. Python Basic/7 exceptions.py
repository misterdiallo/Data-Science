first_number = input("Enter a number:")
second_number = input("Enter a number:")
try:
    division = float(first_number) / float(second_number)

except ZeroDivisionError as e:
    print("Can not divide by 0")
    division = "error"

except ValueError as e:
    print("Error while converting value")
    division = "error"

except TypeError as e:
    print("Type of value are incorrect")
    division = "error"


except Exception as e:
    print("Exception occured:", type(e))
    division = "error"

print("Division is: ", division)
