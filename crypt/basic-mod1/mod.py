message = "165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138 "
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"


numbers = message.split(" ")


for i, n in enumerate(numbers):
    if n == "":
        numbers[i] = -1
    else:
        numbers[i] = int(n) % 37

for i, n in enumerate(numbers):
    if n < 0:
        numbers[i] = -1
        numbers.pop(i)
    elif n <= 36:
        numbers[i] = alphabet[n]
    else:
        numbers[i] = -1
    
print("".join(numbers))