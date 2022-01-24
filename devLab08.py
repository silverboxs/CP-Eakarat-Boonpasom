def check_charecter(cha):
    chaList = ["!","@","#","$","/"]
    for cl in chaList:
        if cl == cha:
            return 1
        else:
            return 0

x = 0
x += check_charecter("#")
print(x)
x += check_charecter("@")
print(x)
x += check_charecter("!")
print(x)

'''
upper, lower, digi, spec = 0, 0, 0, 0
psw = input()
if len(psw) >= 3:
    for i in psw:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isdigit():
            digi += 1
        spec += int(check_charecter(i))
    
    if uper >=1 or lower >= 1 or digi >= 1 or spec >=1:
        print("Valid")
else:
    print("Invalid")
'''
