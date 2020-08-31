camera = str(input('A camera que deseja verificar esta com imagem no dvr ? : \n s ou n ')).lower()
if ('n' or 'não' or 'nao') in camera :
   tensao = str(input('ja verificou se no cabo de alimentação chega a tensão correta?\n:'))
if ('n' or 'não' or 'nao') in camera :
    print('então vai la e testa ')
else:
        print('menos mal, vamos testar outra possibilidades')
else:
    print('então é só fazer a ordem de serviço ')