from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}; razão entre o cateto oposto e a hipotenusa.')
print(f'O ângulo de {angulo} tem o COSSENO de {coseno:.2f}; razão entre o cateto adjacente e a hipotenusa.')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}; razão entre o cateto oposto e o cateto adjacente.')

# # O seno, cosseno e tangente de um ângulo são funções trigonométricas que podem ser calculadas usando a biblioteca math.
 
# # O seno é a razão entre o cateto oposto e a hipotenusa, o cosseno é a razão entre o cateto adjacente e a hipotenusa, e a tangente é a razão entre o cateto oposto e o cateto adjacente.

# # O ângulo deve ser convertido para radianos antes de usar as funções trigonométricas, pois elas esperam o ângulo em radianos.

# # A função radians() converte graus para radianos.
# # A função sin() calcula o seno, a função cos() calcula o cosseno e a função tan() calcula a tangente.

# # O resultado é formatado para mostrar duas casas decimais usando a formatação f-string.

