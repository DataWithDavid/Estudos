'''
A função print serve para:

- Exibir coisas na tela
- Recebe argumentos (são valores que passamos para funções). Exemplo no primeiro Print

'''
# \r\n -> CRLF - WINDOWS
# \n -> LF - UNIX

print('Este é um argumento do tipo string') # O texto dentro das aspas simples é o valor que estamos passando para a função print

print(12, 34) # Argumentos não nomeados

print(45, 67, 89, sep='...') # utilizaremos um outro separador com o SEP, sendo ele (...)

print(00, 12, 34, sep='-', end='##') #Existem caracteres que não vimos porém que são executados, por exemplo os caracteres de quebra de linha - Vamos usar o end para mudar esta quebra de linha

'''
Argumentos nomeados são os argumentos que contem algum nome:

Exemplo usado foi o SEP e o END

- Lembrar que python é caseSensitive
'''