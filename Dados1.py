def iswhat(algo):
  count = 0
  if (algo.isnumeric()):
    print('Eh numerico')
    count += 1
  if (algo.isalpha()):
    print('Eh alfabetico')
    count += 1
  if (algo.isupper()):
    print('Eh maiusculo')
    count += 1
  if (algo.islower()):
    print('Eh minusculo')
    count += 1
  if count == 0:
    print('Nao reconhecido! ')





nome = input('Qual seu nome ? ')
print('Bem vindo ' + nome)
dia = input('Qual dia que voce nasceu ? ')
mes = input('Qual mes que voce nasceu ? ')
ano = input('Qual ano que voce nasceu ? ')
print(nome + ' nasceu em ' + dia + " de " + mes + " de " + ano)
numero1 = int(input(nome + ' digite um numero para somar: '))
numero2 = int(input(nome + ' digite um numero para somar: '))
soma = numero1 + numero2
print('O valor da soma entre',numero1,' e ',numero2,' eh: ' , soma)
print('O valor da soma entre {} e {} eh: {}'.format(numero1,numero2,soma))

algo = input('Digite algo para analise: ')

print('Seu tipo eh:')
iswhat(algo)
