# n1 = int(input('Digite o n1: '))
# n2 = int(input('Digite o n2: '))
# s = n1 + n2
# print('A soma entre o número', n1, 'e', n2, 'é', s)
# print(f'A soma entre o número {n1} e {n2} é {s}.')

# MÉTODO ISNUMERIC() isalpha() ISALNUM()

n3 = input('Digite algo: ')
n6 = n3.isnumeric()
if n6 == True:
    print('A variável que você digitou pode ser convertida em um int ou float.')
else:
    print('A variável não pode ser convertida em número.')

n4 = input('Digite algo: ')
n7 = n4.isalpha()
if n7 == True:
    print('A variável não pode ser convertida em número.')
else:
    print('A variável que você digitou pode ser convertida em um int ou float.')

n5 = input('Digite algo: ')
print(n5.isalnum())