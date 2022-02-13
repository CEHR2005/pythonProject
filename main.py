def is_jumping(number: int) -> str:
    # write your code here
    num = []
    t = f"{number}"
    for x in range(len(t)):
        num.append(int(t[x]))
    if len(t) == 1:
        return "JUMPING"
    for i in range(len(t)-1):
        minus = num[i] - 1
        plus = num[i] + 1
        if minus == num[i + 1] or plus == num[i + 1]:
        return "JUMPING"
    else:
        return "NOT JUMPING"
    pass


print(is_jumping(12))
