import math

def equacao_1_grau(a, b):
    if a == 0:
        return "❌ O valor de 'a' não pode ser zero."
    x = -b / a
    return f"x = {x}"

def equacao_2_grau(a, b, c):
    if a == 0:
        return "❌ O valor de 'a' não pode ser zero (use equação de 1º grau)."
    delta = b**2 - 4*a*c
    if delta < 0:
        return "❌ Não existem raízes reais."
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return f"x₁ = {x1} | x₂ = {x2}"

def area_quadrado(lado):
    if lado <= 0:
        return "❌ O lado deve ser maior que zero."
    return f"Área = {lado**2}"

def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "❌ Base e altura devem ser maiores que zero."
    return f"Área = {(base * altura) / 2}"

def logaritmo(base, valor):
    if base <= 0 or base == 1 or valor <= 0:
        return "❌ Base deve ser > 0 e ≠ 1, e valor > 0."
    resultado = math.log(valor, base)
    return f"log₍{base}₎({valor}) = {resultado}"
