def situacao(estado):
    if estado.lower()=="solteiro":
        print("vivendo bem")
    else:
        print("se fudeu")
print("digite seu estado civil: ")
ecivil=input()
situacao(ecivil)