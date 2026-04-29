"""Refatoracao da pratica 2 com nomes claros e estruturas mais legiveis."""

from math import sqrt


NUMEROS_DE_EXEMPLO = [10, 25, 3, 47, 8, 15, 30, 2, 19, 42]
NOME_DE_EXEMPLO = "Joao Silva"


def somar_elementos(valores):
    """Retorna a soma de todos os valores da lista."""
    total = 0
    for valor in valores:
        total += valor
    return total


def calcular_media(valores):
    """Retorna a media aritmetica dos valores recebidos."""
    return somar_elementos(valores) / len(valores)


def encontrar_maior_valor(valores):
    """Retorna o maior valor da lista."""
    maior = valores[0]
    for valor in valores[1:]:
        if valor > maior:
            maior = valor
    return maior


def encontrar_menor_valor(valores):
    """Retorna o menor valor da lista."""
    menor = valores[0]
    for valor in valores[1:]:
        if valor < menor:
            menor = valor
    return menor


def filtrar_pares(valores):
    """Retorna apenas os numeros pares."""
    return [valor for valor in valores if valor % 2 == 0]


def filtrar_impares(valores):
    """Retorna apenas os numeros impares."""
    return [valor for valor in valores if valor % 2 != 0]


def contem_valor(valores, valor_procurado):
    """Indica se o valor procurado existe na lista."""
    for valor in valores:
        if valor == valor_procurado:
            return True
    return False


def ordenar_crescente(valores):
    """Retorna uma nova lista ordenada em ordem crescente."""
    return sorted(valores)


def resumir_lista(valores):
    """Retorna um dicionario com soma, media, maior e menor valor."""
    return {
        "soma": somar_elementos(valores),
        "media": calcular_media(valores),
        "maior": encontrar_maior_valor(valores),
        "menor": encontrar_menor_valor(valores),
    }


def converter_para_maiusculas(texto):
    """Converte as letras para maiusculas sem alterar os espacos."""
    resultado = []
    for caractere in texto:
        if caractere == " ":
            resultado.append(caractere)
        else:
            resultado.append(caractere.upper())
    return "".join(resultado)


def atribuir_conceito(nota):
    """Converte uma nota numerica em conceito alfabetico."""
    if nota >= 90:
        return "A"
    if nota >= 80:
        return "B"
    if nota >= 70:
        return "C"
    if nota >= 60:
        return "D"
    return "F"


def calcular_distancia(ponto_a, ponto_b):
    """Calcula a distancia entre dois pontos em duas dimensoes."""
    return sqrt(((ponto_b[0] - ponto_a[0]) ** 2) + ((ponto_b[1] - ponto_a[1]) ** 2))


def main():
    """Executa os exemplos da pratica 2."""
    soma = somar_elementos(NUMEROS_DE_EXEMPLO)
    media = calcular_media(NUMEROS_DE_EXEMPLO)
    maior = encontrar_maior_valor(NUMEROS_DE_EXEMPLO)
    menor = encontrar_menor_valor(NUMEROS_DE_EXEMPLO)
    pares = filtrar_pares(NUMEROS_DE_EXEMPLO)
    impares = filtrar_impares(NUMEROS_DE_EXEMPLO)
    resumo = resumir_lista(NUMEROS_DE_EXEMPLO)

    print("soma:", soma)
    print("media:", media)
    print("maior:", maior)
    print("menor:", menor)
    print("pares:", pares)
    print("impares:", impares)
    print("contém 15:", contem_valor(NUMEROS_DE_EXEMPLO, 15))
    print("ordenado:", ordenar_crescente(NUMEROS_DE_EXEMPLO))
    print("resumo:", resumo)
    print("maiusculas:", converter_para_maiusculas(NOME_DE_EXEMPLO))
    print("conceito:", atribuir_conceito(85))
    print("distancia:", calcular_distancia([0, 0], [3, 4]))


if __name__ == "__main__":
    main()