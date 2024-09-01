# QUESTÃO 04: Descubra a lógica e complete o próximo elemento: 
# a) 1, 3, 5, 7, ___ 
# b) 2, 4, 8, 16, 32, 64, ____ 
# c) 0, 1, 4, 9, 16, 25, 36, ____ 
# d) 4, 16, 36, 64, ____ 
# e) 1, 1, 2, 3, 5, 8, ____ 
# f) 2,10, 12, 16, 17, 18, 19, ____

# Item A)
def item_a():
  n1 = 1
  while n1 <= 9 :
    if  n1 % 2 != 0 :
      print(n1)
    n1 += 1


# Item B)
def item_b():
  n2 = 2
  while n2 <= 128 :
    print(n2)
    n2 *= 2


# Item C)
def item_c():
  n3 = 0
  while n3 <= 7 :
    quadrado = n3 ** 2
    print(quadrado)
    n3 += 1


# Item D)
def item_d():
  n4 = 2 
  while n4 <= 10 :
    resultado = n4 ** 2
    print(resultado)
    n4 += 2


# Item E)
def item_e(numero):
    sequencia = [1, 1]
    proximo_valor = 2
    while proximo_valor < numero:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return print(sequencia)


# Item F)
def item_f(sequencia):
    numeros_com_d = ["dois", "dez", "doze", "dezesseis", "dezessete", "dezoito", "dezenove", "duzentos"]
    numeros_por_extenso = ["dois", "dez", "doze", "dezesseis", "dezessete", "dezoito", "dezenove"]
  
    for numero in numeros_com_d:
        if numero not in numeros_por_extenso:
            return print(f"O próximo número da sequência é {200}.") # O próximo número é 200


item_a()
print("--------------")
item_b()
print("--------------")
item_c()
print("--------------")
item_d()
print("--------------")
item_e(13)
print("--------------")
item_f([2, 10, 12, 16, 17, 18, 19])