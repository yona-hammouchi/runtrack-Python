arrayNombre = list(range(0,101))

arrayNombre.remove(26)
arrayNombre.remove(37)
arrayNombre.remove(88)



print(arrayNombre)

arrayFiltre = [nombre for nombre in arrayNombre if nombre % 2 == 0]
