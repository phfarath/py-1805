num1 =1
def numeros(y1):
    resto=y1%2
    if resto==0:
        print("esse numero é par")
    else:
        print("esse numero é impar")
while num1 !=0:
    print("digite um numero inteiro: ")
    num1=int(input())
    num2=numeros(num1)
    
