# tupla
paises = ('Brasil', 'Paraguai', 'Romênia', 'França', 'Espanha', 'Portugal', 'Argentina', 'China', 'Japão', 'Tailândia', 'Itália')

# exibe a tupla
for pais in paises:
    print(pais)

print('\n')

# exibe o tipo de coleção
print(type(paises))

# ordenação de uma tupla/ joga a tupla em uma lista e ordena

paises_lista = sorted(paises)

# exibe a tupla em forma de lista ordenada
for pais in paises_lista:
    print(pais)

print('\n')
print(type(paises_lista))