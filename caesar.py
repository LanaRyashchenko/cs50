import cs50
import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)

key = sys.argv[1]

print("please, enter a text:")     
plaintext = cs50.get_string()

for i in filter(str.isalpha, plaintext):
    if(i.islower()):
        ciphertext = ((ord(i) - 97) + int(key)) %26 + 97
        print(chr(ciphertext), end="")
    if(i.isupper()):
        ciphertext = ((ord(i) - 65) + int(key)) %26 + 65
        print(chr(ciphertext), end="")
 
