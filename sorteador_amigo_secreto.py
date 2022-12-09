import random
print('---SORTEADOR DE AMIGO SECRETO---')
n_pessoas = int(input('Digite quantas pessoas irão participar: '))
nomes, lista1= [], []
codigos = list(range(0, n_pessoas))
random.shuffle(codigos)
for i in range(1, n_pessoas+1):
    nome = str(input(f'Digite o {i}º nome: '))
    nomes.append(nome)
while True:
    for i in range(0, n_pessoas):
        if codigos[i] == list(range(0, n_pessoas))[i]:
            random.shuffle(codigos)
    break

for i in range(0, n_pessoas):
    lista1.append(nomes[codigos[i]])

for i in range(0, n_pessoas):
    print(f'{nomes[i]} pegou {lista1[i]}')
