import string
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}

def diamond(test) -> str:
    param = test.lower()
    index = alphabet[param]
    reference_boucle = 0
    reference_alphabet = 0
    result = ""

    while (reference_boucle < index*2-1):

            for letter in alphabet:
                if letter == param:
                    result+=param
                else:
                    result+=" "
            result+="\n"
            reference_boucle+=1

    return result

print(diamond('d'))

def diamond_boucle_ok(test) -> str:
    param = test.lower()
    index = alphabet[param]
    reference_boucle = 0
    reference_alphabet = 0
    result = ""

    while (reference_boucle < index*2-1):

            while (reference_alphabet < index):
                print(reference_alphabet)
                reference_alphabet+=1

            result+="\n"
            reference_boucle+=1

    return result

print(diamond('d'))