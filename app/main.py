from Desktop import Desktop
from Notebook import Notebook

meuDesktop = Desktop("Dell", "Preto", 3000.0, 500)
meuDesktop2 = Desktop("Dell", "Branco", 2000.0, 400)
meuDesktop.cadastrar()
meuDesktop2.cadastrar()
meuDesktop.getInformacoes()
print("===============================================")
meuNotebook = Notebook("Dell", "Preto", 3000.0, 500)
meuNotebook2 = Notebook("Dell", "Branco", 2000.0, 400)
meuNotebook.cadastrar()
meuNotebook2.cadastrar()
meuNotebook.getInformacoes()
