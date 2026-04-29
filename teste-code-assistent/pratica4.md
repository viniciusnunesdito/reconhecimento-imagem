# Prática 4 — Explicação linha a linha

Abaixo está a explicação do arquivo `pratica2.py`, frase por frase (linha por linha). Cada entrada mostra a linha original seguida de uma explicação curta em português.

1. """Refatoracao da pratica 2 com nomes claros e estruturas mais legiveis."""
   - Docstring do módulo: descreve que o arquivo é uma refatoração da prática 2, com nomes e estruturas mais legíveis.

2. (linha em branco)
   - Linha em branco para separar a docstring do restante do código.

3. `from math import sqrt`
   - Importa a função `sqrt` do módulo padrão `math`, usada para calcular raiz quadrada.

4. (linha em branco)
   - Separador visual.

5. `NUMEROS_DE_EXEMPLO = [10, 25, 3, 47, 8, 15, 30, 2, 19, 42]`
   - Define uma constante (lista) chamada `NUMEROS_DE_EXEMPLO` contendo números usados nos exemplos.

6. `NOME_DE_EXEMPLO = "Joao Silva"`
   - Define uma constante `NOME_DE_EXEMPLO` com uma string usada nos exemplos.

7. (linha em branco)
   - Separador visual.

8. `def somar_elementos(valores):`
   - Início da definição da função `somar_elementos`, que recebe um parâmetro `valores` (espera-se uma lista).

9. `    """Retorna a soma de todos os valores da lista."""`
   - Docstring da função: explica que ela retorna a soma dos elementos.

10. `    total = 0`
    - Inicializa a variável `total` com zero; será usada para acumular a soma.

11. `    for valor in valores:`
    - Inicia um loop que percorre cada elemento `valor` na lista `valores`.

12. `        total += valor`
    - Adiciona o `valor` atual ao acumulador `total` (mesma coisa que `total = total + valor`).

13. `    return total`
    - Retorna o valor final de `total`, a soma de todos os elementos.

14. (linha em branco)
    - Separador visual.

15. `def calcular_media(valores):`
    - Define a função `calcular_media` que recebe `valores` (lista) e calcula a média aritmética.

16. `    """Retorna a media aritmetica dos valores recebidos."""`
    - Docstring: descreve o propósito da função.

17. `    return somar_elementos(valores) / len(valores)`
    - Calcula a média chamando `somar_elementos(valores)` e dividindo pelo comprimento da lista `len(valores)`.

18. (linha em branco)
    - Separador visual.

19. `def encontrar_maior_valor(valores):`
    - Define a função `encontrar_maior_valor` que retorna o maior elemento da lista `valores`.

20. `    """Retorna o maior valor da lista."""`
    - Docstring da função.

21. `    maior = valores[0]`
    - Inicializa `maior` com o primeiro elemento da lista, usado como referência inicial.

22. `    for valor in valores[1:]:`
    - Loop sobre os elementos da lista a partir do segundo (slicing `valores[1:]`).

23. `        if valor > maior:`
    - Compara o `valor` atual com `maior`.

24. `            maior = valor`
    - Se `valor` for maior, atualiza `maior`.

25. `    return maior`
    - Retorna o maior valor encontrado.

26. (linha em branco)
    - Separador visual.

27. `def encontrar_menor_valor(valores):`
    - Define a função `encontrar_menor_valor` que retorna o menor elemento da lista.

28. `    """Retorna o menor valor da lista."""`
    - Docstring da função.

29. `    menor = valores[0]`
    - Inicializa `menor` com o primeiro elemento da lista.

30. `    for valor in valores[1:]:`
    - Loop pelos elementos a partir do segundo.

31. `        if valor < menor:`
    - Compara o `valor` atual com `menor`.

32. `            menor = valor`
    - Se `valor` for menor, atualiza `menor`.

33. `    return menor`
    - Retorna o menor valor encontrado.

34. (linha em branco)
    - Separador visual.

35. `def filtrar_pares(valores):`
    - Define a função `filtrar_pares` que retorna apenas os números pares da lista.

36. `    """Retorna apenas os numeros pares."""`
    - Docstring da função.

37. `    return [valor for valor in valores if valor % 2 == 0]`
    - Retorna uma list comprehension que inclui `valor` se `valor % 2 == 0` (número par).

38. (linha em branco)
    - Separador visual.

39. `def filtrar_impares(valores):`
    - Define a função `filtrar_impares` que retorna apenas números ímpares.

40. `    """Retorna apenas os numeros impares."""`
    - Docstring da função.

41. `    return [valor for valor in valores if valor % 2 != 0]`
    - Retorna lista com valores cujo resto da divisão por 2 é diferente de 0 (ímpares).

42. (linha em branco)
    - Separador visual.

43. `def contem_valor(valores, valor_procurado):`
    - Define `contem_valor` que verifica se `valor_procurado` está presente em `valores`.

44. `    """Indica se o valor procurado existe na lista."""`
    - Docstring da função.

45. `    for valor in valores:`
    - Loop que percorre cada `valor` na lista.

46. `        if valor == valor_procurado:`
    - Compara o `valor` atual com `valor_procurado`.

47. `            return True`
    - Se encontrar igualdade, retorna `True` imediatamente.

48. `    return False`
    - Se o loop terminar sem encontrar o valor, retorna `False`.

49. (linha em branco)
    - Separador visual.

50. `def ordenar_crescente(valores):`
    - Define função `ordenar_crescente` que retorna a lista ordenada.

51. `    """Retorna uma nova lista ordenada em ordem crescente."""`
    - Docstring da função.

52. `    return sorted(valores)`
    - Retorna uma nova lista com os elementos de `valores` ordenados em ordem crescente usando `sorted`.

53. (linha em branco)
    - Separador visual.

54. `def resumir_lista(valores):`
    - Define função `resumir_lista` que constrói um dicionário resumo com estatísticas básicas.

55. `    """Retorna um dicionario com soma, media, maior e menor valor."""`
    - Docstring da função.

56. `    return {`
    - Início do dicionário retornado.

57. `        "soma": somar_elementos(valores),`
    - Chave `soma`: valor obtido chamando `somar_elementos`.

58. `        "media": calcular_media(valores),`
    - Chave `media`: valor obtido chamando `calcular_media`.

59. `        "maior": encontrar_maior_valor(valores),`
    - Chave `maior`: maior valor via `encontrar_maior_valor`.

60. `        "menor": encontrar_menor_valor(valores),`
    - Chave `menor`: menor valor via `encontrar_menor_valor`.

61. `    }`
    - Fecha o dicionário.

62. (linha em branco)
    - Separador visual.

63. `def converter_para_maiusculas(texto):`
    - Define função que converte letras de uma string para maiúsculas sem alterar espaços.

64. `    """Converte as letras para maiusculas sem alterar os espacos."""`
    - Docstring da função.

65. `    resultado = []`
    - Inicializa uma lista vazia `resultado` para construir a nova string.

66. `    for caractere in texto:`
    - Loop que percorre cada caractere na string `texto`.

67. `        if caractere == " ":`
    - Verifica se o caractere é um espaço em branco.

68. `            resultado.append(caractere)`
    - Se for espaço, adiciona o espaço à lista `resultado` sem alteração.

69. `        else:`
    - Caso o caractere não seja espaço.

70. `            resultado.append(caractere.upper())`
    - Converte o caractere para maiúscula com `.upper()` e adiciona a `resultado`.

71. `    return "".join(resultado)`
    - Une a lista `resultado` em uma única string e retorna.

72. (linha em branco)
    - Separador visual.

73. `def atribuir_conceito(nota):`
    - Define função que atribui um conceito (A-F) baseado numa nota numérica.

74. `    """Converte uma nota numerica em conceito alfabetico."""`
    - Docstring da função.

75. `    if nota >= 90:`
    - Condição: se `nota` for maior ou igual a 90.

76. `        return "A"`
    - Retorna o conceito "A".

77. `    if nota >= 80:`
    - Se a primeira condição falhar, verifica se `nota >= 80`.

78. `        return "B"`
    - Retorna "B".

79. `    if nota >= 70:`
    - Verifica `nota >= 70`.

80. `        return "C"`
    - Retorna "C".

81. `    if nota >= 60:`
    - Verifica `nota >= 60`.

82. `        return "D"`
    - Retorna "D".

83. `    return "F"`
    - Se nenhuma das condições acima for satisfeita, retorna "F".

84. (linha em branco)
    - Separador visual.

85. `def calcular_distancia(ponto_a, ponto_b):`
    - Define função que calcula a distância euclidiana entre dois pontos 2D.

86. `    """Calcula a distancia entre dois pontos em duas dimensoes."""`
    - Docstring da função.

87. `    return sqrt(((ponto_b[0] - ponto_a[0]) ** 2) + ((ponto_b[1] - ponto_a[1]) ** 2))`
    - Calcula a distância usando a fórmula da distância euclidiana: sqrt((dx)^2 + (dy)^2), onde `dx` e `dy` são as diferenças de coordenadas.

88. (linha em branco)
    - Separador visual.

89. `def main():`
    - Define a função `main`, que contém exemplos de uso das funções definidas.

90. `    """Executa os exemplos da pratica 2."""`
    - Docstring da função `main` explicando seu propósito.

91. `    soma = somar_elementos(NUMEROS_DE_EXEMPLO)`
    - Chama `somar_elementos` com a lista de exemplo e armazena em `soma`.

92. `    media = calcular_media(NUMEROS_DE_EXEMPLO)`
    - Calcula a média e armazena em `media`.

93. `    maior = encontrar_maior_valor(NUMEROS_DE_EXEMPLO)`
    - Obtém o maior valor da lista de exemplo.

94. `    menor = encontrar_menor_valor(NUMEROS_DE_EXEMPLO)`
    - Obtém o menor valor.

95. `    pares = filtrar_pares(NUMEROS_DE_EXEMPLO)`
    - Filtra os números pares e guarda em `pares`.

96. `    impares = filtrar_impares(NUMEROS_DE_EXEMPLO)`
    - Filtra os números ímpares e guarda em `impares`.

97. `    resumo = resumir_lista(NUMEROS_DE_EXEMPLO)`
    - Cria um dicionário resumo com soma, média, maior e menor.

98. (linha em branco)
    - Separador visual.

99. `    print("soma:", soma)`
    - Imprime o texto "soma:" seguido do valor de `soma`.

100. `    print("media:", media)`
    - Imprime a média calculada.

101. `    print("maior:", maior)`
    - Imprime o maior valor.

102. `    print("menor:", menor)`
    - Imprime o menor valor.

103. `    print("pares:", pares)`
    - Imprime a lista de pares.

104. `    print("impares:", impares)`
    - Imprime a lista de ímpares.

105. `    print("contém 15:", contem_valor(NUMEROS_DE_EXEMPLO, 15))`
    - Imprime se a lista contém o valor 15, chamando `contem_valor`.

106. `    print("ordenado:", ordenar_crescente(NUMEROS_DE_EXEMPLO))`
    - Imprime a lista ordenada em ordem crescente.

107. `    print("resumo:", resumo)`
    - Imprime o dicionário `resumo` criado anteriormente.

108. `    print("maiusculas:", converter_para_maiusculas(NOME_DE_EXEMPLO))`
    - Imprime o nome de exemplo convertido para maiúsculas (preservando espaços).

109. `    print("conceito:", atribuir_conceito(85))`
    - Imprime o conceito atribuído à nota 85 (espera-se "B").

110. `    print("distancia:", calcular_distancia([0, 0], [3, 4]))`
    - Imprime a distância entre os pontos [0,0] e [3,4] (resultado 5.0, triângulo 3-4-5).

111. (linha em branco)
    - Separador visual.

112. `if __name__ == "__main__":`
    - Checagem padrão: se o módulo for executado como script principal, executa o bloco seguinte.

113. `    main()`
    - Chama a função `main` para executar os exemplos.

114. (linha final em branco)
    - Fim do arquivo.


Observações finais rápidas:
- O código é claro e didático; poderia usar funções built-in como `sum()` em vez de `somar_elementos` para simplicidade.
- Algumas funções não tratam casos de borda (ex.: `calcular_media` assume que `valores` não está vazio).

Se quiser, adapto este `.md` para incluir trechos de código formatados, sumarizo apenas as funções principais ou traduzo as explicações para inglês.
