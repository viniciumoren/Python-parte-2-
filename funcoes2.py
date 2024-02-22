valores = [10,20,30,40,50]


def media(valores):
    soma = sum(valores)
    quantidade = len(valores)

    media = soma / quantidade

    return media


print(f'A média de valores é {media(valores)}')