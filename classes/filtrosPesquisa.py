from datetime import datetime


class filtrosPesquisa():
    def __init__(self):
        self.__tipoViagem = ''
        self.origem = ''
        self.destino = ''
        self.__dataIda = ''
        self.__dataVolta = ''

    def setTipoViagem(self, tipo: str):
        if (tipo not in ('oneway', 'roundtrip')):
            return False
        self.__tipoViagem = tipo
        return True
    
    def setDataIda(self, data: str):
        if not data:
            print('Data inválida')
            return False
        self.__dataIda = data
        return True
    
    def setDataVolta(self, data: str):
        if not data:
            print('Data inválida')
            return False
        self.__dataVolta = data
        return True
    
    def getDataIda(self):
        return self.__dataIda
    
    def getDataVolta(self):
        return self.__dataVolta

    def getTipoViagem(self):
        return self.__tipoViagem
    