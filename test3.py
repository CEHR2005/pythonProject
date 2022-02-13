def is_werewolf(target: str) -> bool:
    # write your code her
    if not target:
        return True
    else:
        if target[0] == " " or target[0] == "?" or target[0] == "," or target[len(target) - 1] == " " or target[len(target) - 1] == "?" or target[len(target) - 1] == ",":
            decrypt = ""
        else:
            decrypt = target[len(target) - 1]
        target2 = ""
        for char in range(len(target) - 1, 0, -1):
            if target[char - 1] == " " or target[char - 1] == "?" or target[char - 1] == ",":
                pass
            else:
                decrypt = decrypt + target[char - 1]
                # print(decrypt)

        for char in range(1, len(target) + 1):
            if target[char - 1] == " " or target[char - 1] == "?" or target[char - 1] == ",":
                pass
            else:
                target2 = target2 + target[char - 1]
        print(target2.lower())
        print(decrypt.lower())
        if decrypt.lower() == target2.lower():
            return True
        else:
            return False
    pass