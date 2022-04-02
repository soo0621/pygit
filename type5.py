N = input("온도를 입력하시오 : ")
T = input("변환하고자 하는 단위를 고르시오(C or F) : ")

if(T == 'F'):
    fahrenheit = (9/5)*int(N)+32
    sum = fahrenheit
elif(T == 'C'):
    celsius = (5/9)*(int(N)-32)
    sum = celsius
print(sum)