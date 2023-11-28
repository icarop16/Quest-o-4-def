# Faça um programa que pergunte quanto voc~e ganha por hora e o numero de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês
HoraV = float(input("Quanto você ganha por hora? "))
HoraT = int(input("Quantas horas você trabalhou esse mês? "))

def salario():
    HoraT2 = float(HoraT)
    salarioT = HoraV * HoraT2
    print (f"Seu salário é {salarioT}")

salario()