# Explicacao da funcao de numero primo

Este arquivo explica a versao otimizada da funcao que verifica se um numero e primo.

## Codigo final

```python
from math import isqrt


def eh_primo(numero: int) -> bool:
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = isqrt(numero)

    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False

    return True


def main() -> None:
    numero = 29
    resultado = eh_primo(numero)
    print(f"{numero} e primo? {resultado}")


if __name__ == "__main__":
    main()
```

## Explicacao linha a linha

1. `from math import isqrt` importa a funcao `isqrt`, que calcula a raiz quadrada inteira de forma eficiente.
2. `def eh_primo(numero: int) -> bool:` define a funcao `eh_primo`, com entrada inteira e saida booleana.
3. `if numero < 2:` verifica se o numero e menor que 2, pois nesses casos ele nao pode ser primo.
4. `return False` encerra a funcao imediatamente quando o numero e invalido para primalidade.
5. `if numero == 2:` trata o caso especial do numero 2, que e primo.
6. `return True` confirma que 2 e primo.
7. `if numero % 2 == 0:` verifica se o numero e par.
8. `return False` descarta todos os pares maiores que 2, porque nao sao primos.
9. `limite = isqrt(numero)` calcula ate onde e necessario testar divisores.
10. `for divisor in range(3, limite + 1, 2):` percorre os numeros impares a partir de 3 ate a raiz quadrada do numero.
11. `if numero % divisor == 0:` testa se o numero e divisivel por algum divisor.
12. `return False` indica que o numero nao e primo quando encontra um divisor exato.
13. `return True` informa que nenhum divisor foi encontrado e o numero e primo.
14. `def main() -> None:` cria uma funcao principal para organizar a execucao do programa.
15. `numero = 29` define um valor de exemplo para teste.
16. `resultado = eh_primo(numero)` chama a funcao e guarda o resultado.
17. `print(f"{numero} e primo? {resultado}")` exibe o resultado na tela.
18. `if __name__ == "__main__":` garante que o bloco abaixo so rode quando o arquivo for executado diretamente.
19. `main()` executa a funcao principal.

## Melhorias da versao otimizada

- Usa apenas testes ate a raiz quadrada, reduzindo o trabalho desnecessario.
- Ignora numeros pares depois de tratar o 2.
- Usa anotacoes de tipo para deixar a intencao do codigo mais clara.
- Separa a execucao do programa em `main()`, o que melhora organizacao e reutilizacao.