class Pessoa():

    def __init__(self, cod, nome, tel, end):
        self.__cod = cod
        self.__nome = nome
        self.__tel = tel
        self.__end = end
            
    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_tel(self):
        return self.__tel

    def set_tel(self, tel):
        self.__tel = tel

    def get_end(self):
        return self.__end

    def set_end(self, end):
        self.__end = end

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo   
