ano = int(input('Digite a idade do atleta: '))
if ano <= 9:
    print('Este atleta é da categoria \033[1:34mMIRIM\033[m!')
elif 9 < ano <= 14:
    print('Este atleta é da categoria \033[1:34mINFANTIL\033[m!')
elif 14 < ano <= 19:
    print('Este atleta é da categoria \033[1:34mJUNIOR\033[m!')
elif ano == 20:
    print('Este atleta é da categoria \033[1:34mSÊNIOR\033[m!')
else:
    print('Este atleta é da categoria \033[1:34mMASTER\033[m!')
