
# QUESTÃO 03: Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

indice = 12
soma = 0
k = 1

while k < indice:
  k += 1
  soma += k
  
print(f"A soma eh igua a {soma}")


# Resultado final SOMA = 77