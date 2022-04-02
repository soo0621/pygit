import random

random.random()

count = 1
w = 0
while count != 0:
    r1 = random.randint(1, 9)
    r2 = random.randint(1, 9)
    a = int(r1)*int(r2)
    m = input(f"{r1}*{r2} = ")
    print(a)

    if a == int(m):
        print("정답입니다!!!")
        w += 1
        q = input("계속 하시겠습니까?((c)ontinue / (s)top): ")
        if q == 's':
            print("정답률은 %.f%%입니다."%(w/count*100))
            break;
        elif q == 'c':
            count += 1
    elif a != int(m):
        print('틀렸습니다...')
        q = input("계속 하시겠습니까?((c)ontinue / (s)top): ")
        if q == 's':
            print("정답률은 %.f%%입니다." % (w / count * 100))
            break;
        elif q == 'c':
            count += 1