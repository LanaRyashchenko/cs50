import cs50
import sys

def check():
    print("Please, enter the height of pyramide")
    height = cs50.get_int()
    while height < 0 or height > 23:
        print("Retry: ")
        height = cs50.get_int()
    if height == 0:
        return 0
    else: 
        for n in range(1,height+1):
            print(' ' * (height - n), end = '')
            print('#' * (n+1))
def main():
    check()
        
if __name__ == "__main__":
    main()
