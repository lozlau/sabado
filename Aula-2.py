print("boa noite, pessoal")










nome = 'Antonio'
nota = 9.5
print('A nota de', nome, 'foi', nota)





nome = 'Antonio'
nota = '9,5'
print('A nota de %s foi %s.' % (nome,nota))

nome = 'Antonio'
nota = '9,5'
print(f'A nota de {nome} foi {nota}.')




#Exercício 1 - variáveis
nota1 = 5
nota2 = 6
media = (nota1+nota2)/2
nome = "Antonio da Silva"
disciplina = "Programação de Computadores"
print("*******************************************")
print("Nome do Aluno: ", nome)
print("Disciplina: ", disciplina)
print("Primeira nota = %s \nSegunda nota = %s" %(nota1, nota2))
print("Nota média = ", media)
print("*******************************************")







#Exercício 2 - variáveis
nome = input("Digite o seu nome completo: ")
idade = input("Digite a sua idade: ")
print("*******************************************")
print("Nome do aluno: ", nome)
print("Idade do aluno: ", idade, "anos")
print("*******************************************")






#Exercício - conversão
a = input("Digite um número inteiro: ")
b = int(a)

a = input("Digite um número: ")
b = float(a)

a = input("Digite uma expressão: ")
b = eval(a)








a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("O resultado é", a + b)







#Exercício 3 - Calculadora
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print("*******************************************")
print("A soma é", a + b)
print("A subtração é", a - b)
print("A multiplicação é", a * b)
print("A divisão é", a / b)
print("O resto é", a % b)
print("Potencia", a ** b)
print("*******************************************")
