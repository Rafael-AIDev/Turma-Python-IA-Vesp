# lista
cidades = ['Brasília', 'Taguatinga', ' Planaltina', 'Ceilândia', 'Samambaia', 'Riacho Fundo', 'Canadangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaíso', 'Novo gama', 'Céu azul', 'Lago do sul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Arial', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo'] 

# usuário informa valor a ser pesquisado
cidade_pesquisa = input('Cidade a ser pesquisada: ').capitalize()

# verifica se a cidade existe
if cidade_pesquisa in cidades:
    print(f'Cidade {cidade_pesquisa} achada com sucesso.')
else: 
    print('Não foi possível encontrar a cidade.')