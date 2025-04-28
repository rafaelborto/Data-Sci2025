medidametros = float(input("Ingrese la medida en metros: "))
medidaDecimetros = medidametros * 10
medidaCentimetros = medidametros * 100
medidaMillimetros = medidametros * 1000

medidaemQuilometros = medidametros / 1000
medidaemHectometros = medidametros / 100
medidaemDecametros = medidametros / 10


print(
    f"la medida en decimetros es: {medidaDecimetros:.2f} dm,\n"
    f"la medida en centimetros es: {medidaCentimetros:.2f} cm,\n"
    f"la medida en milimetros es: {medidaMillimetros:.2f} mm,\n"
    f"la medida es hectometro es: {medidaemHectometros:.2f} hm,\n"
    f"la medida en decametros es: {medidaemDecametros:.2f} dam,\n"
    f"la medida en kilometros es: {medidaemQuilometros:.2f} km,\n")

""" Ingrese la medida en metros: 56
la medida en decimetros es: 560.00 dm,
la medida en centimetros es: 5600.00 cm,
la medida en milimetros es: 56000.00 mm,


la medida es hectometro es: 0.56 hm,
la medida en decametros es: 5.60 dam,
la medida en kilometros es: 0.06 km, """








