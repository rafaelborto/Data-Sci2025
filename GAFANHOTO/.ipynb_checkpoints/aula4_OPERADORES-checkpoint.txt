'// = divide e resulta um número inteiro'
var1 = 13 / 2.4 # 5.42 = retornará 5.42
var2 = 13 // 2.4 # 5.42 = retornará 5.0

var3 = 13 // 2 # 6.5 = retornará 6

var4 = 12 / 2.1 # = 5.71 = retornará 5.71
var5 = 12 // 2.1 # 5.71 = retornará 5
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)


' ** = potenciação ou pow(numero, expoente)- perde a ordem de precedência'
'8 ** 1/3 = raiz cúbica de 8 = 2.0'

var6 = 2 ** 3 # 2^3 = 8
var7 = 2 ** 4 # 2^4 = 16
var8 = 2^5 # 2^5 = 32

print(var7)

print(var8)

"""  ele executa a operação XOR bit a bit (OU exclusivo) entre dois números inteiros.​

Por que 2 ^ 5 resulta em 7?
Vamos analisar os valores binários:​

2 em binário: 00000010

5 em binário: 00000101​

Aplicando o operador XOR bit a bit:​

00000010 ^  00000101 =  00000111

O resultado 00000111 em binário corresponde ao número decimal 7.​

O operador XOR retorna 1 apenas quando os bits correspondentes dos operandos são diferentes. Portanto, 2 ^ 5 resulta em 7 porque os bits correspondentes de 2 e 5 são diferentes em três posições, resultando em 7 (00000111).​

"""

" % = resto da divisão"

var9 = 13 % 2 # 1 = retornará 1


"PRECEDÊNCIA DOS OPERADORES"

# A precedência dos operadores determina a ordem em que as operações são realizadas em uma expressão. Os operadores com maior precedência são avaliados primeiro. Aqui estão alguns exemplos de operadores e sua precedência, do mais alto para o mais baixo:
# 1. Parênteses ( ) - A operação dentro dos parênteses é realizada primeiro.
# 2. Exponenciação ** - A exponenciação é realizada em seguida.
# 3. Multiplicação *, Divisão /, Módulo % - Essas operações têm a mesma precedência e são avaliadas da esquerda para a direita.
# 4. Adição +, Subtração - - Essas operações também têm a mesma precedência e são avaliadas da esquerda para a direita.
# 5. Comparação <, >, <=, >=, ==, != - Essas operações de comparação são avaliadas depois das operações aritméticas.
# 6. Atribuição = - A atribuição é realizada por último.
# 7. Operadores lógicos and, or, not - Esses operadores lógicos são avaliados após as operações de comparação.  
# 8. Operadores bit a bit & (E), | (OU), ^ (OU exclusivo) - Esses operadores são avaliados após os operadores lógicos.
# 9. Operadores de deslocamento << (deslocamento à esquerda), >> (deslocamento à direita) - Esses operadores são avaliados por último.
# 10. Operadores de identidade is, is not - Esses operadores são avaliados após os operadores de comparação.   
# 11. Operadores de associação in, not in - Esses operadores são avaliados após os operadores de identidade.
# 12. Operadores de atribuição compostos +=, -=, *=, /=, %=, //=, **= - Esses operadores são avaliados após os operadores de atribuição simples.
# 13. Operadores de atribuição bit a bit &=, |=, ^=, <<=, >>= - Esses operadores são avaliados após os operadores de atribuição compostos.
# 14. Operadores de atribuição de identidade is, is not - Esses operadores são avaliados após os operadores de atribuição bit a bit.
# 15. Operadores de atribuição de associação in, not in - Esses operadores são avaliados após os operadores de atribuição de identidade.
# 16. Operadores de atribuição de comparação <, >, <=, >=, ==, != - Esses operadores são avaliados após os operadores de atribuição de associação.  
# 17. Operadores de atribuição de lógica and, or, not - Esses operadores são avaliados após os operadores de atribuição de comparação.
# 18. Operadores de atribuição de bit a bit & (E), | (OU), ^ (OU exclusivo) - Esses operadores são avaliados após os operadores de atribuição de lógica.
# 19. Operadores de atribuição de deslocamento << (deslocamento à esquerda), >> (deslocamento à direita) - Esses operadores são avaliados por último.
# 20. Operadores de atribuição de identidade is, is not - Esses operadores são avaliados após os operadores de atribuição de deslocamento.
# 21. Operadores de atribuição de associação in, not in - Esses operadores são avaliados após os operadores de atribuição de identidade.
# 22. Operadores de atribuição de comparação <, >, <=, >=, ==, != - Esses operadores são avaliados após os operadores de atribuição de associação.
# 23. Operadores de atribuição de lógica and, or, not - Esses operadores são avaliados após os operadores de atribuição de comparação.
# 24. Operadores de atribuição de bit a bit & (E), | (OU), ^ (OU exclusivo) - Esses operadores são avaliados após os operadores de atribuição de lógica.
# 25. Operadores de atribuição de deslocamento << (deslocamento à esquerda), >> (deslocamento à direita) - Esses operadores são avaliados por último.
# 26. Operadores de atribuição de identidade is, is not - Esses operadores são avaliados após os operadores de atribuição de deslocamento.
# 27. Operadores de atribuição de associação in, not in - Esses operadores são avaliados após os operadores de atribuição de identidade.
# 28. Operadores de atribuição de comparação <, >, <=, >=, ==, != - Esses operadores são avaliados após os operadores de atribuição de associação.
# 29. Operadores de atribuição de lógica and, or, not - Esses operadores são avaliados após os operadores de atribuição de comparação.
# 30. Operadores de atribuição de bit a bit & (E), | (OU), ^ (OU exclusivo) - Esses operadores são avaliados após os operadores de atribuição de lógica.
# 31. Operadores de atribuição de deslocamento << (deslocamento à esquerda), >> (deslocamento à direita) - Esses operadores são avaliados por último.
# 32. Operadores de atribuição de identidade is, is not - Esses operadores são avaliados após os operadores de atribuição de deslocamento.
# 33. Operadores de atribuição de associação in, not in - Esses operadores são avaliados após os operadores de atribuição de identidade.