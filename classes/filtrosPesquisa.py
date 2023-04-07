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
        try:
            data = data.replace('/', '-')
            self.__dataIda = datetime.strptime(data, '%d-%m-%Y')
        except:
            print('Data inválida')
            return False
        return True
    
    def setDataVolta(self, data: str):

        try:
            data = data.replace('/', '-')
            self.__dataVolta = datetime.strptime(data, '%d-%m-%Y')
        except:
            print('Data inválida')
            return False
        return True
    
    def getDataIda(self):
        return self.__dataIda
    
    def getDataVolta(self):
        return self.__dataVolta

    def getTipoViagem(self):
        return self.__tipoViagem
    