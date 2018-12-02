def generateindexes(string, alphabet):
    pindex = []
    for x in range(len(string)):
        for i in range(len(alphabet)):
            if string[x] == alphabet[i]:
                pindex.append(i)
    return pindex


def generatecypher(inputIndexes, cypherIndexes, alphabet):
    mod = []
    textback = ""
    for i in range(len(inputIndexes)):
        mod.append((cypherIndexes[i] + inputIndexes[i]) % 26)
        textback += alphabet[mod[i]]
    return mod, textback