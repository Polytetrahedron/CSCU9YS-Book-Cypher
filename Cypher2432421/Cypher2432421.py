alphabet = "abcdefghijklmnopqrstuvwxyz"
bookphrase = "thisisaseretphrasedoadance"

import DecryptionEngine as decode
import EncryptionEngine as encode

userinput = input("Please enter a string: ")

inputIndexes = encode.generateindexes(userinput, alphabet)
cypherIndexes = encode.generateindexes(bookphrase, alphabet)
codedmod, codedmessage = encode.generatecypher(inputIndexes, cypherIndexes, alphabet)
message, plain = decode.decodecypher(codedmod, cypherIndexes, alphabet)

print("Input Indexes: " + str(inputIndexes))
print("Book Indexes: " + str(cypherIndexes))
print("Cypher Text: " + codedmessage)
print("Modulus of PlainText Message: " + str(codedmod))
print("Decoded Message: " + str(message))
print("Message Reads: " + str(plain))
input("Press Enter to exit")
