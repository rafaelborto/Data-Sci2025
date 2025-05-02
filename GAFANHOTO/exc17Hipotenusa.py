cateto = float(input("Digite o valor do cateto oposto: "))
cateto2 = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = (cateto ** 2 + cateto2 ** 2) ** (1/2)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')
# # O valor da hipotenusa é a raiz quadrada da soma dos quadrados dos catetos.

import math
print('Usando a biblioteca math: math.hypot()')

hipotenusa2 = math.hypot(cateto, cateto2)
print(f'O valor da hipotenusa é {hipotenusa2:.2f}')

