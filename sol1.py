#Touched by dh
# this file is touched by JJong-ss

def is_leapyear(x):                                 #윤년 구하는 알고리즘
    if(x%400==0):
        return True
    elif(x%100==0):
        return False
    elif(x%4==0):
        return True
    else:
        return False

a, b ,c = [int(x) for x in input().split()]   # 분리한 자료를 정수 자료형으로 반환 / 공백을 기준으로 자료를 분리

def GCD3(x,y,z):             # 두 정수의 최대공약수를 구하고 구한 값과 나머지 한 정수의 최대공약수를 구하기
	while(y):
		x, y = y, x%y
	while(z):
		x, z = z, x%z
	return x

def GCD2(x,y):               # 유클리드 알고리즘을 이용하여 두 정수의 최대공약수를 구하기
	while(y):
		x,y = y, x%y
	return x

def LCM3(x,y,z):                   # 유클리드 알고리즘을 사용하여 세 정수의 최소공배수를 구하기
	temp = (x*y)//GCD2(x,y)          # 먼저 두 정수의 최소공배수를 구하기
	lcm = (temp * z) //GCD2(temp,z)  # 구한 최소공배수와 나머지 정수의 최소공배수 구하기
	return lcm

print(GCD3(a,b,c))                 # 최대공약수 출력
print(LCM3(a,b,c))                 # 최소공배수 출력

gap = GCD3(a,b,c) - LCM3(a,b,c)
print("최대공약수와 최소공배수의 차이는 ", gap)

# 컴퓨터전자시스템공학부 201901060 김종현
# pullrequest를 위한 수정 
# pullrequest를 위한 동시수정
# pullrequest를 위한 동시수정 by JJOngss2
Touched by lsy
# pr용 
