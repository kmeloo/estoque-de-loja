from modelo.venda import *

def executar():

    v1 = Venda(pedido = "João da Silva", 
                data = "josilva@gmail.com",  
                quantidade = "47 99012 3232")
                
    print(v1)

    print(v1.json())
