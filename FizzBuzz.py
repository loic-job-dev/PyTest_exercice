def fizzbuzz(num: int) -> str:
    result = ""
    for i in range(1, num+1):
        if i % 3 != 0:
            result += f"{i}\n"
        else:
            result += "fizz\n"
    return result