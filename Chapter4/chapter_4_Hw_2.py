'''Write a script that inputs a line of encrypted text and a distance value and outputs 
plaintext using a Caesar cipher. The script should work for any printable characters'''
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
        (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
print(plainText)