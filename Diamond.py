import string
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
inverse_alphabet = {index: letter for letter, index in alphabet.items()}

def diamond(test) -> str:
    param = test.lower()
    index = alphabet[param]
    reference_boucle = 1
    reference_alphabet = 1
    result = ""

    #liste sur mesure pour boucler sur les lettres voulues seulement
    letters = list(alphabet.keys())[:index]
    reversed_letters = list(alphabet.keys())[:index]

    reversed_letters.reverse()

    while reference_boucle <= index*2-1:
        while reference_alphabet <= index: #Permet de boucler jusqu'à la lettre voulue

            for letter in reversed_letters:
                if letter == inverse_alphabet[reference_alphabet]:
                    result+=letter
                else:
                    result+=" "

            for letter in letters[1:]:
                if letter == inverse_alphabet[reference_alphabet]:
                    result+=letter
                else:
                    result+=" "
            reference_alphabet+=1
            result += "\n"
            reference_boucle+=1

        reference_alphabet-=2

        while reference_alphabet > 0:
            for letter in reversed_letters:
                if letter == inverse_alphabet[reference_alphabet]:
                    result+=letter
                else:
                    result+=" "

            for letter in letters[1:]:
                if letter == inverse_alphabet[reference_alphabet]:
                    result+=letter
                else:
                    result+=" "

            reference_alphabet-=1
            result += "\n"
            reference_boucle+=1

    return result

print(diamond('z'))