altura = float(input("Digite a altura em metros: "))
largura = float(input("Digite a largura em metros: "))
area = altura * largura
litros = area / 2
print(f'A área a ser pintada é de {area:.2f} m² e você precisará de {litros:.2f} litros de tinta para pintá-la.')
lata18l = litros / 18
lata5l = litros / 5
print(f'Você precisará de {lata18l:.2f} latas de 18 litros ou {lata5l:.2f} latas de 5 litros para pintar a área.')
# 1 litro de tinta cobre 2 m²
# 1 lata de tinta de 18 litros cobre 108 m²
# 1 lata de tinta de 5 litros cobre 30 m²
