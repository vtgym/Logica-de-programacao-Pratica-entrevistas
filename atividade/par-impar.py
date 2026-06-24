"""

numero = int(input("Digite o número: "))

if numero % 2 == 0:
    print("Par")

else:
    print("Impar")

    
"""

"""

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    
    elif numero % 3 == 0:
        print("Fizz")
   
    elif numero % 5 == 0:
        print("Buzz")
   
    else:
        print(numero)


"""

"""


numero = int(input("Digite um número: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("fatorial de", numero, "é", fatorial)


"""