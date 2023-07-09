lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_indexes = range(26)

char_to_index = dict( zip(lower_alphabet, alpha_indexes) )
char_to_index.update( dict(zip(upper_alphabet, alpha_indexes)) )

username_file = open("usernames.txt") 
password_file = open("passwords.txt")

usernames = [x for x in username_file]
passwords = [x for x in password_file]

his_username = "cultiris"
his_hash = ""

for u, p in zip(usernames, passwords):
    # print(u, p)
    if "cultiris" in u:
        his_hash = p


flag = ""
for character in his_hash:
    if not character in char_to_index.keys():
        flag += character
        continue

    if character in lower_alphabet:
        initial_code = char_to_index[character]
        new_code = (initial_code + 13) % 26
        new_char = lower_alphabet[new_code]
        flag += new_char

    elif character in upper_alphabet:
        initial_code = char_to_index[character]
        new_code = (initial_code + 13) % 26
        new_char = upper_alphabet[new_code]
        flag += new_char

print(his_hash)
print(flag)