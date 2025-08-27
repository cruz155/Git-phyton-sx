

# Entrada dos dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo
media = (nota1 + nota2) / 2

# conceito
if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

# SITUAÇÃO

if conceito in ["A", "B", "C"]:
    Situaçao  =  "APROVADO"
else:
    Situaçao = "REPROVADO"

# SAIDA
print(f"Aluno:" ,nome)
print(f"SITUAÇÃO:", Situaçao)
print("CONCEITO:", conceito)
print("Média:" ,media)



