#ProgramaPara determinar hora da Janta

almoco = input('Almoçou ? (S/N)')

if almoco == 'S':
       horax = input ('Que Horas (13 a 22)? ')
       horax = int(horax)
if horax >= 13 and horax <= 22: #precisei entrar com outro if para armazenar a entrada
    print('Almoçou porem, Precisa dar um intervalo de 6 horas após o almoço para jantar')
    horax = horax + 6
    print('Sua janta será  às ' + str(horax) + ' horas, favor nao atrasar') #converti o numero para string
elif almoco == 'N':  
    print('Precisa se Alimentar urgente')
else: 
    print('Informação não encontrada')
