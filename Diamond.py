alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',)

def diamond(test) -> str:
    result = ""
    for letter in alphabet:
        if letter == test:
            result+=test
        else:
            result+=" "
    return result

print(diamond('d'))