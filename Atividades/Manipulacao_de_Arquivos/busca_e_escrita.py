import fileinput

arquivo = 'C:/Users/tomas.sales/Documents/GitHub/python/Atividades/Manipulacao_de_Arquivos/teste.txt'
text_to_search = 'teste9'
replacement_text = 'teste10'

with fileinput.FileInput(arquivo, 'w') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')
        file.write(line.replace(text_to_search, replacement_text), end='')
