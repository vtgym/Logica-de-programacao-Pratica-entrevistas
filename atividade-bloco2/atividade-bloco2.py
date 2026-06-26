'''


n = int(input("quantidade de termos: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    proximo = a + b
    a = b
    b = proximo

'''


'''
n = int(input("quantidade de termos: "))

fibonacci = []

for i in range(n):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print("Sequência de Fibonacci:")
for numero in fibonacci:
    print(numero, end=" ")

'''


''' 

def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


n = int(input("Digite um número: "))

if eh_primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")

'''


'''

def eh_primo(numero):
    if numero <= 1:
        return False

    i = 2
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 1

    return True


n = int(input("Digite um número: "))

if eh_primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")

'''


'''

numero = int(input("Digite um número: "))

numero = abs(numero)
soma = 0

while numero > 0:
    soma += numero % 10
    numero //= 10

print("soma dos dígitos: ", soma)

'''


'''

numero = input("Digite um número: ")

soma = 0

for digito in numero:
    if digito != "-":
        soma += int(digito)

print("soma dos dígitos:", soma)

'''