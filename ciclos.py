for i in range(30):
    if i % 3 != 0:
        continue
    else:
          print('Primero ejemplo')
          print(i**2)



for i in range(30):
    if i % 3 == 0:
        print('Segundo ejemplo')
        print('', i**2)
    elif i == 22:
          break


for i in range(30):
    if i % 3 == 0:
        print('Tercer ejemplo')
        print(i)
    elif i == 22:
        break


r = 'programandoAndo'
for letter in r:
    print(letter)
