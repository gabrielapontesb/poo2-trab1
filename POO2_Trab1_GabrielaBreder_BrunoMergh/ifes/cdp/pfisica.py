from ifes.cdp.pessoa import Pessoa


class Pfisica(Pessoa):
    def __init__(self, cod, nome, tel, end, cpf):
        super(Pfisica, self).__init__(cod, nome, tel, end)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf
