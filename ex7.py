val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if val1 < val2:
    while val1 < val2:
        val1 = val1 + 1
        print (val1)
else:
    while val2 < val1:
        val2 = val2 + 1
        print (val2)