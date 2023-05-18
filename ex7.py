def numeros(y1,y2,y3,y4):
    num=[-y1,-y2,-y3,-y4]
    for a in sorted(num):
        print(f'{a*-1:.3f}')
print("digite um numero real: ")
num1=float(input())
print("digite um numero real: ")
num2=float(input())
print("digite um numero real: ")
num3=float(input())
print("digite um numero real: ")
num4=float(input())
result=numeros(num1,num2,num3,num4)
