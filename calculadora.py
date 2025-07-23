def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

while True:
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = input("Digite o número da operação: ")

    if escolha == '5':
        print("Calculadora encerrada.")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        continue

    if escolha == '1':
        print(f"Resultado da soma: {somar(num1, num2)}")

    elif escolha == '2':
        print(f"Resultado da subtração: {subtrair(num1, num2)}")

    elif escolha == '3':
        print(f"Resultado da multiplicação: {multiplicar(num1, num2)}")

    elif escolha == '4':
        print(f"Resultado da divisão: {dividir(num1, num2)}")

    else:
        print("Opção inválida! Tente novamente.")