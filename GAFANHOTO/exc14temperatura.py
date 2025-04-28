# F = (C × 9/5) + 32
# C = (F − 32) × 5/9

tempC = float(input("Digite a temperatura em Celsius: "))
tempF = (tempC * 9/5) + 32

print(f'A temperatura em Fahrenheit é: {tempF:.2f}°F')

tempF2 = float(input("Digite a temperatura em Fahrenheit: "))
tempC2 = (tempF2 - 32) * 5/9

print(f'A temperatura em Celsius é: {tempC2:.2f}°C')

