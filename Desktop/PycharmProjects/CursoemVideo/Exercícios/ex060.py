n = int(input('Digite um número para saber o seu fatorial: '))
result = 1
count = 1
while count <= n:
    result *= count
    count += 1
print(result)
