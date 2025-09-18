import string
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
inverse_alphabet = {index: letter for letter, index in alphabet.items()}

def diamond(test) -> str:
    param = test.lower()
    index = alphabet[param]

    result = ""

    for line in range(1, index+1):
        spaceBefore = " " * (index - line)
        letter = inverse_alphabet[index]

        if line == 1:
            result += spaceBefore + letter + "\n"
        else:
            spaceBetween = " " * (line * 2)
            result += spaceBefore + letter + spaceBetween + letter + "\n"
    return result

print(diamond("d"))