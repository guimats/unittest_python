from src.calculadora import soma

# print(soma(12, 32))
# print(soma(-12, 32))
# print(soma(4.4, 7.1))
try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')
