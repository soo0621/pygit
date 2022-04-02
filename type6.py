import math
r = input("반지름을 입력하세요 : ")

s = float(4*(math.pi)*(math.pow(int(r),2)))
v = float((4/3)*(math.pi)*(math.pow(int(r),3)))

print("구의 겉면적은 %.3f입니다."%float(s))
print("부피는 %.3f 입니다."%float(v))