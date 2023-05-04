from modelo.venda import *

def executar():

    v1 = Venda(cpf = "050882548",
                produto = "caneta", 
                data = "12/05/2022",  
                quantidade = 2,
                preco_total = 15)
                
    print(v1)

    print(v1.json())
