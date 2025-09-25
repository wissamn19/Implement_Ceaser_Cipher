
message = input("Enter a message: ")
shift = int(input("Enter shift value: "))
P = "abcdefghijklmnopqrstuvwxyz"

for K in range(len(message)):
    if message[K].isalpha():
        index = P.index(message[K].lower())
        new_index = (index + shift) % 26
        if message[K].isupper():
            message = message[:K] + P[new_index].upper() + message[K+1:]
        else:
            message = message[:K] + P[new_index] + message[K+1:]
print('Cipher : ' + message)
            
for K in range(len(message)):
     if message[K].isalpha():
        index = P.index(message[K].lower())
        new_index = (index - shift) % 26
        if message[K].isupper():
            message = message[:K] + P[new_index].upper() + message[K+1:]
        else:
            message = message[:K] + P[new_index] + message[K+1:]
print('Decipher : ' + message)
