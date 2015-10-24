class Produto:

    def __init__(self,cod, desc, estmin, qtdatual, custo, pctlucro):
        self.__cod = cod
        self.__desc = desc
        self.__estmin = estmin
        self.__qtdatual = qtdatual
        self.__custo = custo
        self.__pctlucro = pctlucro

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_desc(self):
        return self.__desc

    def set_desc(self, desc):
        self.__desc = desc

    def get_estmin(self):
        return self.__estmin

    def set_estmin(self, estmin):
        self.__estmin = estmin

    def get_qtdatual(self):
        return self.__qtdatual

    def set_qtdatual(self, qtdatual):
        self.__qtdatual = qtdatual

    def get_custo(self):
        return self.__custo

    def set_custo(self, custo):
        self.__custo = custo

    def get_pctlucro(self):
        return self.__pctlucro

    def set_pctlucro(self, pctlucro):
        self.__pctlucro = pctlucro