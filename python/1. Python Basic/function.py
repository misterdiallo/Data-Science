jan_expenses = [44344, 3533, 434, 343, 3, 4, 34, 3, 4, 3, 453, 5, 3, 4, 5, 34]
feb_expenses = [34, 3, 4, 3, 453, 5, 3, 4, 5, 34]


def calculate_total(exp):
    """
    this is a documentation strings
    :param exp:
    :return:
    """
    total = 0
    for item in exp:
        total += item
    return total

print("Total of january expenses:", calculate_total(jan_expenses))
print("Total of february expenses:", calculate_total(feb_expenses))