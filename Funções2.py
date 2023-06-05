def somar(x: int, y: int):
    resultado = x + y
    return resultado

x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

res = somar(x, y)
print(f'A soma é: {res} ')
