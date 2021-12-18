rowsInput = int(input("Rows :"))
star = ""
countStar = 1

for rows in range(rowsInput):
    star = ""
    #if (rows) < rowsInput:
    #star += " " * (rowsInput-(rows+1))
    for space in range(rowsInput-(rows+1)):
        star += " "
    for colum in range(countStar):
        star += "*"
    countStar += 2
    print(star)