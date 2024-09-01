
# QUESTÃO 02: Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# Declaraçao da função de busca
def contar(string):
    n = 0
    for char in string:
        if char.lower() == 'a':
            n += 1
    return n

# Entrada da string a ser verificada
texto = input("Informe a frase que deseja verificar:")
quantidade = contar(texto)

# Teste condicional
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
