expre = str(input('Digite uma expressão: '))
parent = []
for simb in expre:
    if simb == '(':
        parent.append('(')
    elif simb == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break
if len(parent) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
