from Computador import Computador

class Desktop(Computador):
    desktopList = []
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        if len(self.desktopList) == 0:
            print("Não há Desktops cadastrados.")
        else:
            print("Desktops cadastrados:")
            for desktop in self.desktopList:
                print(f"Modelo: {desktop.modelo}, Cor: {desktop.cor}, Preço: R$ {desktop.preco:.2f}, Potência da Fonte: {desktop._potenciaDaFonte}W")

    def cadastrar(self):
         self.desktopList.append(self)
