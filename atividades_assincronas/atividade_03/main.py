# entradad de dados
nome: str = input('Informe seu nome: ')
cargo = input('Informe seu cargo: ')

# saída de dados
print('Parabéns por entrar no mundo do python ' + cargo +' ' + nome + '.')
print('Parabéns por entrar no mundo do python', cargo, nome,'.')
print('Parabéns por entrar no mundo do python {} {}.'.format(cargo, nome))
print(f'Parabéns por entrar no mundo do python {cargo} {nome}.')