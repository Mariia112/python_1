#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(4):
    for y in range(4):
        for z in range(4):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истенно при x = {x}, y={y}, z={z}')