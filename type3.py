N = input("자연수를 입력하시오 : ")
n = 1
sum = 1
while n <= int(N):
    sum *= n
    n = n+1
print(sum)