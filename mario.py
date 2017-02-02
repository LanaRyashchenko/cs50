import cs50
import sys


height = int(input("Height: "))
while height < 0 or height > 23:
    height = int(input("Retry "))
    if height == 0:
        print("0")
else:
    for n in range(1,height+1):
        print(' ' * (height - n), end = '')
        print('#' * (n+1))
       


        
    

