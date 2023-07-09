import string
message = "268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131 "
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

numbers = message.split(" ")

flag = ""
for i, n in enumerate(numbers):
    if n == "" or n == " ":
        numbers[i] = -1
    else:
        modulo = pow(int(n), -1, 41)

        if modulo in range(1, 27):  # [1, 26]
            flag += string.ascii_uppercase[modulo - 1]
        elif modulo in range(27, 37):
            flag += string.digits[modulo - 27]
        else:
            flag += "_"


    
print("picoCTF{" + flag + "}")