import string
alphabet = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
inverse_alphabet = {index: letter for letter, index in alphabet.items()}

def diamond2(param) -> str:
    input = param.lower()
    index = alphabet[input]

    result = ""

    for line in range(1, index+1):
        spaceBefore = " " * (index - line) #OK
        letter = inverse_alphabet[line]

        if line == 1:
            result += spaceBefore + letter + "\n"
        else:
            spaceBetween = " " * (((line-1)*2)-1)
            result += spaceBefore + letter + spaceBetween + letter + "\n"

    for line in range(index-1, 0, -1):
        spaceBefore = " " * (index - line)
        letter = inverse_alphabet[line]

        if line == 1:
            result += spaceBefore + letter + "\n"
        else:
            spaceBetween = " " * (((line-1)*2)-1)
            result += spaceBefore + letter + spaceBetween + letter + "\n"

    return result

print(diamond2("d"))