import os

path = "caminho para o arquivo"


lista_de_arquivos = os.listdir(path)


i = 1
for arquivos in lista_de_arquivos:
    nome_novo = f'exercício {i}.py'
    caminho_novo = os.path.join(path, nome_novo)

    caminho_completo = os.path.join(path,arquivos)

    if os.path.isfile(caminho_completo):
        os.rename(caminho_completo , caminho_novo)
        i+=1


os.startfile(path)
    