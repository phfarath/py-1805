import re   
erro=""
def validaçao(y1,y2,y3):
          #apenas caracteres
        if re.search("\d", y1):
            erro="O nome não pode conter números"
          #5 digitos + - + 3 digitos 
        if not re.search("\d{5}", y2) or len(y2)>8 :
            erro="O CEP não deve conter letras"
          #4 digitos 
        if not re.search("\d{4}", y3) or len(y3)>4:
            erro="A data não deve conter letras"
nome = input('Insira seu nome: ')
cep = int(input('Insira seu CEP: '))
ano = int(input('Insira seu ano de nascimento: '))
chama= validaçao(nome,cep,ano)
