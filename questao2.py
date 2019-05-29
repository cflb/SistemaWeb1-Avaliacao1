"""
    Faca uma funcao que receba o número de copos de água você bebeu durante o dia,
    leve em conta que cada copo tem 100ml, então descupra quantos litros de água você bebeu durante o dia.
"""

def quantosLitros(copos):
    quantidade_consumida = copos * 100
    quantos_litros = quantidade_consumida/1000
    return "Você consumiu %.2f L de água" % quantos_litros

copos = int(input("Quantos copos você bebeu hoje?  "))
print(quantosLitros(copos))