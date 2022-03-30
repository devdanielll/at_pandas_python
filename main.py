import pandas as pd

casos = pd.read_csv('Bairros Aracaju_26-03-2022.csv', index_col=False).drop([48,46,47])
casos2 = casos.set_index('BAIRRO')
print(casos2)

print('\n')

SomaObitos = casos['ÓBITO'].sum()
print('Total de óbitos: ', SomaObitos)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

FiltroObitos = casos.loc[[37,38]]
SomaObitos2 = FiltroObitos['ÓBITO'].sum()
print('A soma do número de óbitos dos bairros Siqueira Campos e São José é de: ', SomaObitos2)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

MaiorObito = casos.sort_values('ÓBITO')
F_MaiorObito2 = MaiorObito.tail(1)
F_MaiorObito3 = F_MaiorObito2['BAIRRO']
F_MaiorObito4 = F_MaiorObito2['ÓBITO']
print('O bairro com mais óbitos é: ', F_MaiorObito3.to_string(), 'com:', F_MaiorObito4.to_string(), 'óbitos')

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

MenorObito = casos.sort_values('ÓBITO')
F_MenorObito2 = MenorObito.head(1)
F_MenorObito3 = F_MenorObito2['BAIRRO']
F_MenorObito4 = F_MenorObito2['ÓBITO']
print('O bairro com menos óbitos é: ', F_MenorObito3.to_string(), 'com: ', F_MenorObito4.to_string(), 'óbitos')

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

MediaObitos = casos['ÓBITO'].mean()
print('Média de óbitos', MediaObitos)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

MediaConfirmados = casos['CONFIRMADO'].mean()
print('Média de confirmados', MediaConfirmados)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

MediaRecuperados = casos['RECUPERADO'].mean()
print('Média de recuperados', MediaRecuperados)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

TotalRecuperados = casos['RECUPERADO'].sum()
print('Total de recuperados: ', TotalRecuperados)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

TotalConfirmados = casos['CONFIRMADO'].sum()
print('Total de confirmados: ', TotalConfirmados)

print('\n')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\n')

casos3 = casos2.to_csv('teste.csv')