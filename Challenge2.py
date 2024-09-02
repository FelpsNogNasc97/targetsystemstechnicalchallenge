1) Cálculo da variável SOMA

Em vez de usar um loop tradicional, podemos utilizar uma fórmula matemática conhecida para calcular a soma dos primeiros n números naturais. A soma de n números consecutivos pode ser calculada pela fórmula:

SOMA = 𝑛 × ( 𝑛 +1 ) / 2
 
Nesse caso, n = 13, então: 

indice = 13
soma = (indice * (indice + 1)) // 2
print(soma)


2) Sequência de Fibonacci

Em vez de gerar toda a sequência de Fibonacci e verificar se o número pertence à sequência, podemos usar uma propriedade matemática que diz que um número n é Fibonacci se e somente se um dos seguintes valores é um quadrado perfeito:

5𝑛^2 + 4 ou 5𝑛^2 − 4

Código:

import math

def is_fibonacci_number(n):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Testando o número
n = int(input("Informe um número: "))
if is_fibonacci_number(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")


3) Faturamento Diário

Podemos abordar esse problema usando uma abordagem funcional, onde utilizamos mapeamento, filtragem, e redução (map, filter, reduce) para calcular as estatísticas necessárias.

Código em Python:

import json
from functools import reduce

# Supondo os dados como uma string JSON
data = '''
{
  "faturamento": [220.5, 345.8, 0.0, 540.3, 125.4, 300.2, 450.0, 0.0, 350.7, 220.0]
}
'''

faturamento_mensal = json.loads(data)["faturamento"]

# Filtrando dias com faturamento > 0
faturamento_valido = list(filter(lambda x: x > 0, faturamento_mensal))

# Usando reduce para calcular soma, mínimo e máximo
soma = reduce(lambda x, y: x + y, faturamento_valido)
min_fat = reduce(lambda x, y: x if x < y else y, faturamento_valido)
max_fat = reduce(lambda x, y: x if x > y else y, faturamento_valido)

# Calculando a média
media_mensal = soma / len(faturamento_valido)

# Contando dias acima da média
dias_acima_da_media = len(list(filter(lambda x: x > media_mensal, faturamento_valido)))

print(f"Menor faturamento: R${min_fat:.2f}")
print(f"Maior faturamento: R${max_fat:.2f}")
print(f"Dias acima da média: {dias_acima_da_media} dias")


4) Percentual de Faturamento por Estado

Vamos usar uma abordagem baseada em dicionário com compreensão de listas para calcular os percentuais.

Código em Python:

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

# Usando compreensão de dicionários para calcular percentuais
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

5) Inversão de String

Em vez de construir a string invertida com laços tradicionais, podemos usar uma técnica de recursão para inverter a string.

Código em Python:

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# String de exemplo
string = input("Informe a string a ser invertida: ")
print(f"String invertida: {reverse_string(string)}")
