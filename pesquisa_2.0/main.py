# lista
cidades = ['Brasília', 'Taguatinga', ' Planaltina', 'Ceilândia', 'Samambaia', 'Riacho Fundo', 'Canadangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaíso', 'Novo gama', 'Céu azul', 'Lago do sul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Arial', 'Sol nascente', 'Dvo', 'São sebastião', 'Dvo'] 

# usuário pesquisa pela cidade
cidade_pesquisada = input('Cidade a ser pesquisada: ').capitalize()

# verifica se a cidade existe
try:
    # pega o indice do item de pesquisa
    indice = cidades.index(cidade_pesquisada)
    print(f'{cidade_pesquisada} encontrada no indice {indice}.')
except:
    print(f'Não foi possível encontrar {cidade_pesquisada}.')