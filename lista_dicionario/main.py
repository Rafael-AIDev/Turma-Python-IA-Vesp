# tupla 
chaves = ('Nome', 'Idade', 'Profissão')


usuarios = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: 20,
        chaves[2]: 'Programador'
    },
    {
        chaves[0]: 'Cicrano',
        chaves[1]: 35,
        chaves[2]: 'Analista'

    },
    {
        chaves[0]: 'Beltrano',
        chaves[1]: 45,
        chaves[2]: 'Faxineiro'
    }
]

# adicionar novo usuário
usuario = {}

for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'Informe {chaves[i]}: ')

usuarios.append(usuario)
print(f'\nUsuário cadstrado com sucesso.')

#reexibindo a nova lista de usuários
print(f'{'='*10} Lista de Usuários{'='*10}')

for usuario in usuarios:
    print('\n')
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
