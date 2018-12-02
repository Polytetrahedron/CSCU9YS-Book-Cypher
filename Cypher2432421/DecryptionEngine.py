def decodecypher(coded, cypherIndexes, alphabet): # This could be in another script but it would achieve the same result 
    decoded = []
    messageback = ""
    for i in range(len(coded)):
        decoded.append(((coded[i] - cypherIndexes[i]) + 26) % 26)
        messageback += alphabet[decoded[i]]
    return decoded, messageback