def remove_vowels(document: str) -> str:
    # write your code her
    document = document.lower()
    if not document:
        return ""
    else:
       if document[0] == "a" or document[0] == "e" or document[0] == "i" or document[0] == "o" or document[0] == "u" or document[0] == "y":
           decrypt = ""
       else:
           decrypt = ""
       for char in range(1, len(document) + 1):
            if document[char - 1] == "a" or document[char - 1] == "e" or document[char - 1] == "i" or document[char - 1] == "o" or document[char - 1] == "u" or document[char - 1] == "y":
                pass
            else:
                   decrypt = decrypt + document[char - 1]
       return decrypt


print(remove_vowels("I like my boss"))


def is_jumping(number: int) -> str:
    # write your code here
    num = []
    t = f"{number}"
    if len(num) == 1:
        return "JUMPING"
    for i in range(len(t)-1):
        minus = number[i] - 1
        plus = number[i] + 1
        if minus == num[i + 1] or plus == num[i + 1]:
            return "dsadas"
    pass


print(is_jumping(12))
