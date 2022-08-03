
# # # # # CALCULATION USING FOR
expenses = [500,30,44,2454,554,6544,6543,5,3,777,57]
total = 0
for i in expenses:
    total = total + i

print(total)


# # #  RANGE using for loop
for i in range(1,11):
    print(i)


# # # # # Manipulation in for loop
expenses = [500,30,44,2454,554,6544,6543,5,3,777,57]
total = 0
for i in range(len(expenses)):
    print("Month: ", (i+1), " Expense is: ", expenses[i])
    total = total + expenses[i]
print("Total is: ", total)


########## Search in Home using for loop
home = ["salon", "chambre1", "chambre2", "chambre3", "douche1", "douche2", "cuisine", "terasse"]
where_is_my_phone = "douche1"
for i in home:
    print("Please wait I'm Looking in:", i)
    if i==where_is_my_phone:
        print("Found in : ", i)
        break
    else:
        print("Not found in :", i )
