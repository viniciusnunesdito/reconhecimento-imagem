def calcular_media(numeros):
    if not numeros:
        return None
    valores = []
    for n in numeros:
        try:
            valores.append(float(n))
        except (TypeError, ValueError):
            continue
    if not valores:
        return None
    return sum(valores) / len(valores)


def classificar_nota(nota):
    if nota is None:
        return "N/A"
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"


def processar_alunos(alunos):
    resultados = []
    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = calcular_media(notas)
        nota_final = round(media, 1) if media is not None else None
        classificacao = classificar_nota(nota_final)
        resultados.append({
            "nome": nome,
            "media": nota_final,
            "classificacao": classificacao
        })
    return resultados


def imprimir_relatorio(resultados):
    print("=== RELATÓRIO DE NOTAS ===")
    for r in resultados:
        media_display = f"{r['media']}" if r['media'] is not None else "N/A"
        print(f"Aluno: {r['nome']} | Média: {media_display} | Conceito: {r['classificacao']}")
    print(f"Total de alunos: {len(resultados)}")


alunos = [
    {"nome": "Ana",    "notas": [85, 90, 78, 92]},
    {"nome": "Bruno",  "notas": [60, 55, 70, 65]},
    {"nome": "Carla",  "notas": [95, 98, 100, 97]},
    {"nome": "Diego",  "notas": []},               
    {"nome": "Elena",  "notas": [70, "80", 75, 65]},
]

resultado = processar_alunos(alunos)
imprimir_relatorio(resultado)