def fizzbuzz(num: int) -> str:
    result = ""
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz\n"
        elif i % 3 == 0:
            result += "fizz\n"
        elif i % 5 == 0:
            result += "buzz\n"
        else:
            result += f"{i}\n"
    return result

print(fizzbuzz(100))