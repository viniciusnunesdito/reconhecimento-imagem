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