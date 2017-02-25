symbols = "+_)(*&^%$#@!./,;{}"

n = int(input())
for passn in range(n):
    size = int(input())
    pw = input()
    upper = 0
    lower = 0
    digit = 0
    symbol = 0
    for c in pw:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c in symbols:
            symbol += 1
    if (len(pw) >= 12 and
            upper > 0 and
            lower > 0 and
            digit > 0 and
            symbol > 0):
        print("valid")
    else:
        print("invalid")
