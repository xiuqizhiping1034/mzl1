
s=int(input(),2)

# 二进制 to 十六进制: hex(int(str,2))

bin_hex = hex(s)
print(bin_hex.split("x")[1].upper())
# print(hex(int(input(),2)).split("x")[1].upper())