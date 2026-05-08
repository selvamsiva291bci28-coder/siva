input_numbers = [1, 5, 7, 9, 11, 17, 19, 27, 45, 50]

# Initialize the lists
MyList1 = []
MyList2 = []

# Separate the numbers
for number in input_numbers:
    if number % 2 == 0 and number % 3 != 0:
        MyList1.append(number)
    if number % 9 == 0:
        MyList2.append(number)

# Print the results
print("MyList1:", MyList1)
print("MyList2:", MyList2)
