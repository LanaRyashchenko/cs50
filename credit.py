import cs50
import sys

print("Please, enter the card number:")
number = cs50.get_int()
number = str(number)
number_rev = (number)[::-1]

y = 0
d = 0
for i in range(1,len(number),2):
    m = int(number_rev[i]) * 2
    for b in str(m):
        d += int(b)

for x in range(0,len(number),2):
    c = int(number_rev[x])
    y = c + y

checksum = d + y

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
