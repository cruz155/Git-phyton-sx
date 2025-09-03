import os
os.system("cls")

numero = int(input("digite um numero de 1 a 12 para ver os meses correspondente"))

match numero:
        case 1:
            print("Domingo - Final de semana")
        case 2:
            print("Segunda-feira - Dia útil")
        case 3:
            print("Terça-feira - Dia útil")
        case 4:
            print("Quarta-feira - Dia útil")
        case 5:
            print("Quinta-feira - Dia útil")
        case 6:
            print("Sexta-feira - Dia útil")
        case 7:
            print("Sábado - Final de semana")
        case _:
            print("Dia inválido")
