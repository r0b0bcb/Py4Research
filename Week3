###############################################
#    Week 3: Caesar cipher                    #
#           r0b0bcb                           #
#           3/28/2018                         #
###############################################
# write your code here!
import string

###############################################
# Exercise 1: alphabet string

alphabet = ' ' + string.ascii_lowercase
print(alphabet)

###############################################
# Exercise 2: dictionary index of alphabet

positions = dict(zip(alphabet, range(0,27)))

###############################################
# Exercise 3: encode the message

message = "hi my name is caesar"

array = []
key = 1
for loop in range(len(message)):
    array.append(alphabet[(positions[message[loop]] + key) %27])
encoded_message = ''.join(array)

###############################################
# Exercise 4: Create def to encode given message and key

def encode(message, key):
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string


encoded_message = encode(message, 3)

###############################################
# Exercise 5: Take encoded message and decrypt it

decoded_message = encoding(encoded_message, -3) #encoded with 3 so decode with the opp
print(decoded_message)

