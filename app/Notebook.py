from Computador import Computador

class Notebook(Computador):
    notebookList = []
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        if len(self.notebookList) == 0:
            print("Não há Notebooks cadastrados.")
        else:
            print("Notebooks Cadastrados:")
            for notebook in self.notebookList:
                print(f"Modelo: {notebook.modelo}, Cor: {notebook.cor}, Preço: R$ {notebook.preco:.2f}, Tempo de Bateria: {notebook.__tempoDeBateria}h")

    def cadastrar(self):
        self.notebookList.append(self)
