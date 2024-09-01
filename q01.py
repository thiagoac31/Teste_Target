
# QUESTÃO 01: Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Declaração da função da sequencia de Fibonacci
def fibonacci(numero):
    sequencia = [0, 1]
    proximo_valor = 1
    while proximo_valor <= numero:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return sequencia

# Declaração da função que percorre a sequencia de Fibonacci
def is_in_fibonacci(numero, sequencia):
    return numero in sequencia


# Número a ser verificado
numero = input("Informe o numeror que deseja verificar:")

sequencia = fibonacci(int(numero))
print("Sequência de Fibonacci:", sequencia)


# Teste condicional
if is_in_fibonacci(int(numero), sequencia):
    print(f"O número {numero} faz parte da sequência de Fibonacci.")
else:
    print(f"O número {numero} não faz parte da sequência de Fibonacci.")


