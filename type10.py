a = []
b = []
def listProd(a, b):
    for steps in range(3):
        a1 = input("a에 첫번째 인수를 입력하시오. : ")
        a.append(a1)
    for steps in range(3):
        b1 = input("b에 첫번째 인수를 입력하시오. : ")
        b.append(b1)
    c = 0
    sum = 0
    for steps in range(3):
        sum += int(a[c])*int(b[c])
        c += 1
    print(sum)
listProd(a,b)