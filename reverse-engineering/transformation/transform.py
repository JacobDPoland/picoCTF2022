encoded_text = open("enc").read()

hex_text = ""
for c in encoded_text:
    hex_text += hex(ord(c)).lstrip("0x")

print(hex_text)
decoded = bytearray.fromhex(hex_text).decode()
print(decoded)
