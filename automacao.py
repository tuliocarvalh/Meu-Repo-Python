import os
import pandas as pd
from gui import new_hub, clone_repo, enter_terminal, init, push_repo


diretorio = r"C:\portfolio\python" #Inclua o caminho específico.
caminho = os.listdir(diretorio)


lista = []

for repo in caminho :
    lista.append(repo)
repositorios = pd.DataFrame(lista, columns=['repositorio'])
print(repositorios)
#repositorios.to_excel("repositorios.xlsx")

init()

#for i in repositorios['repositorio']:
#    new_hub(i)
    

enter_terminal()

#for i in repositorios['repositorio']:
#    clone_repo(i)

for i in repositorios['repositorio']:
    push_repo(i)




