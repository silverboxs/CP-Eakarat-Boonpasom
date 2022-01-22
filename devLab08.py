upper, lower, dig, spec = 0, 0, 0, 0
psw = input()
if len(psw) >= 3:
    for i in psw:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

else:
    print("Invalid")