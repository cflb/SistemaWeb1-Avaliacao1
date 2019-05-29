"""
    1. Faça um Programa que peça os lados de um retangulo e mostre a sua área.
    Area = LadaMenor * LadoMaior.
"""

ladoMenor = float(input("Digite o tamanho do ladoMenor: "))
ladoMmaior = float(input("Digite o tamanho do ladoMaior: "))
area = ladoMenor * ladoMmaior

print("A área do seu retangulo é: %.2f m2" % (area))