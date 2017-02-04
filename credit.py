import cs50
import sys

print("Please, enter the card number:")
number = cs50.get_int()
number = str(number)
number_rev = (number)[::-1]

checksum = 0
for (i, sym) in enumerate(number_rev):
    if i % 2:
        sym = int(sym) * 2
        while sym:
            checksum += sym % 10
            sym //= 10
    else:
        checksum += int(sym)

checkvalid = checksum % 10

if checkvalid == 0:
    if int(number[0]) == 4 and (len(number) == 13 or len(number) == 16):
        print("VISA")
    elif (int(number[0:2]) == 34 or int(number[0:2]) == 37) and len(number) == 15:
        print("AMEX")
    elif (int(number[0]) == 5 and int(number[1]) in range(1,6)) and len(number) == 16:
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")
