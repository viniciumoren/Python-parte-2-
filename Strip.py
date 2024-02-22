nomeF = []


for x in range(5):
    nome = input('Digite o seu nome').strip().capitalize() 
    if nome.startswith('F'):
        nomeF.append(nome)
for nome in nomeF:
    if nome.startswith('F'):
        print(nome)    
    




