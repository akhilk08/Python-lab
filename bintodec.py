def binary_to_decimal(binary):
    decimal = 0
    power = 0

    for digit in binary[::-1]:  # Iterate from the rightmost digit
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("The decimal equivalent is:", decimal_number)
