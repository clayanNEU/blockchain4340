n = 187

encrypted = 65**7%n
print("encrypted is " + str(encrypted))

d = pow(7, -1, 160)
print(d)

decrypted = 142**d%n
print("decrypted is " + str(decrypted))

# send 142 with {m, k, e}


# we picked "N" to encrypt
nASCII = 78
e= 7 # picked this after prime decomp
n = 52699
encrypted = nASCII**e%n
print("2nd encrypted is " + str(encrypted))

k = 52200
d = pow(e, -1, k)
print(d)

decrypted = encrypted**d%n
print("2nd decrypted is " + str(decrypted))


# 1-23 example digi signature
n = 91
k = 72
e = 11
msg1 = ord('T') + 5
msg2 = hex(msg1)
encrypt = 59**e%n
d = pow(e, -1, k)
decrypt = 54**d%n
print("here")
print (decrypt)

# check if signature 53 is valid
n = 527
k = 480
e = 13

msg1 = ord('R') + 5
msg2 = hex(msg1)
print(msg2)
#hash is 57
encrypt = 57**e%n
d = pow(e, -1, k)
# 53 here is the given signature we are seeing if valid
decrypt = 53**d%n
print("here")
print (decrypt)
# since 83 does not equal 57, signature is not valid




# check if signature 57 is valid
n = 527
k = 480
e = 13

msg1 = ord('R') + 5
msg2 = hex(msg1)
print(msg2)
#hash is 57
encrypt = 57**e%n
d = pow(e, -1, k)
# 57 here is the given signature we are seeing if valid
decrypt = 57**d%n
print("here")
print (decrypt)
# since 398 does not equal 57, signature is not valid




# check if signature 39 is valid
n = 527
k = 480
e = 13

msg1 = ord('R') + 5
msg2 = hex(msg1)
print(msg2)
#hash is 57
encrypt = 57**e%n
d = pow(e, -1, k)
# 39 here is the given signature we are seeing if valid
decrypt = 39**d%n
print("here")
print (decrypt)
# since 405 does not equal 57, signature is not valid