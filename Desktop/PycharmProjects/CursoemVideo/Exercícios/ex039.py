ano = int(input('Em que ano você nasceu? '))
if ano > (2022 - 18):
    fal = 18 - (2022 - ano)
    print('Você deve se alistar em {} anos!'.format(fal))
elif ano < (2022 - 18):
    pas = (2022 - ano) - 18
    print('Você deveria ter se alistado a {} anos!'.format(pas))
else:
    print('Você deve se alistar esse ano!')
