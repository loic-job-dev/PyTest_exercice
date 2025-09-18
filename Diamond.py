import string
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}

def diamond(test) -> str:
    param = test.lower()
    index = alphabet[param]
    referenceBoucle = 0
    result = ""

    while (referenceBoucle < index):
        for letter in alphabet:
            if letter == param:
                result+=param
                print(index)
            else:
                result+=" "
        referenceBoucle+=1
    return result

print(diamond('d'))