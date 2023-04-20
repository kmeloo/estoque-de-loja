from modelo.produtos import *

def executar():

    p1 = Produto(pedido = "João da Silva", 
                data = "josilva@gmail.com",  
                quantidade = "47 99012 3232")
                
    print(p1)

    print(p1.json())
