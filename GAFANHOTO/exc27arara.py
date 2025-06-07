nome = str(input("Digite o nome de um passaro: ")).upper().strip()

print(f'Esse nome contém {nome.count('A')} letras A')
print(f'A letra "A" aparece pela primeira vez na posição {nome.find('A')+1}')
print(f'A letra "A" aparece pela última vez na posição {nome.rfind('AAAa')+1}')