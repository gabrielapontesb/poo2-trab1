class Venda:


    def __init__(self, cliente, dt, prod, qtd):
        self.__cliente = cliente
        self.__dt = dt
        self.__prod = prod
        self.__qtd = qtd
        
    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self, cliente):
        self.__cliente = cliente
        
    def get_dt(self):
        return self.__dt
        
    def set_dt(self, dt):
        self.__dt = dt

    def get_prod(self):
        return self.__prod

    def set_prod(self, prod):
        self.__prod = prod

    def get_qtd(self):
        return self.__qtd

    def set_qtd(self, qtd):
        self.__qtd = qtd


