print('-'*30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('Digite quantos termos da sequência de fibonacci gostaria de ver: '))
t1 = 0
t2 = 1
count = 3
print('-'*30)
print('{} -> {} -> '.format(t1, t2), end='')
while count <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    count += 1
    t1 = t2
    t2 = t3
print('FIM')
print('-'*30)
