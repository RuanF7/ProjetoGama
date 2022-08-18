n = int(input('Digite um número: '))
esc = str(input("""Para BINÁRIO digite 1 
Para OCTAL digite 2 
Para HEXADECIMAL digite 3 
:"""))
if esc == '1':
    bn = str(bin(n)[2:])
    print('O número em BINÁRIO é: {}'.format(bn))
elif esc == '2':
    oc = str(oct(n)[2:])
    print('O número em OCTAL é: {}'.format(oc))
elif esc == '3':
    hx = str(hex(n)[2:])
    print('O número em HEXADECIMAL é: {}'.format(hx))
else:
    print('Você não digitou um número de 1 a 3!')
