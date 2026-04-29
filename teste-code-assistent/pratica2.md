# Pratica 2 - Refatoracao

Este exercicio compara a versao original do arquivo [pratica2.py](pratica2.py) com a versao refatorada e destaca as melhorias de legibilidade, nomenclatura e organizacao.

## Comparacao entre as versoes

Na versao original, as funcoes eram chamadas por nomes genericos como `f1`, `f2`, `f3` e assim por diante. Na versao refatorada, cada funcao recebeu um nome descritivo, como `somar_elementos`, `calcular_media`, `filtrar_pares` e `calcular_distancia`, o que deixa a intencao do codigo clara sem precisar interpretar o corpo da funcao.

Outro ponto importante foi a substituicao de `for i in range(len(lista))` por iteracao direta sobre os elementos. Isso reduz ruido visual, evita acesso repetitivo por indice e torna o codigo mais idiomatico em Python.

Tambem foi corrigida a funcao que retornava varios valores em tupla sem contexto. Agora `resumir_lista` devolve um dicionario com chaves nomeadas, o que facilita a leitura e o uso posterior dos dados.

## Melhorias realizadas

- Nomes de funcoes e variaveis passaram a descrever o que realmente fazem.
- As repeticoes foram simplificadas com iteracao direta sobre a lista.
- O retorno agregado foi estruturado com um dicionario, em vez de uma tupla sem significado explicito.
- Foram adicionadas docstrings para documentar o proposito de cada funcao.
- A execucao principal foi organizada em `main()`, separando definicao de funcoes e uso do programa.
- A ordenacao passou a usar `sorted()`, evitando a implementacao manual de bubble sort quando o objetivo e apenas demonstrar a operacao.

## Resultado esperado

O codigo refatorado continua produzindo os mesmos tipos de saida, mas agora esta mais facil de ler, manter e explicar em sala de aula.