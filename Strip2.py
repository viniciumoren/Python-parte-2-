nomes = []

for x in range(5):
    nome = input('Digite o nome: ').strip().capitalize()
    nomes.append(nome)

for nome in nomes:
    if nome.startswith('F'):
        print(nome)
