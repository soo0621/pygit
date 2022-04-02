N = input("자연수를 입력하시오 : ")
n = 0
sum = 0
while n <= int(N):
    if n%2 == 0:
        sum = sum + n
    n = n+1
print(sum)