dicio = {'nome': "ueslei", }
print(dicio.keys())
dicio.update({"nome": "joão"})
print(dicio["nome"])
dicio['nome'] = 'ciclano'

print(dicio["nome"])

for chave in  dicio.values():
    print(chave)