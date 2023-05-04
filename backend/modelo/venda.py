from config.config import *

class Venda(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Text)  
    produto = db.Column(db.Text)
    data = db.Column(db.Text)
    quantidade = db.Column(db.Integer)
    preco_total = db.Column(db.Float)
    
    def __str__(self):
        return f'(id={self.id}) {self.cpf}, '+\
            f'{self.produto} , {self.data}, '+\
            f'{self.quantidade}, {self.preco_total}'
    
    def json(self):
            return {
                "id":self.id,
                "cpf": self.cpf,
                "produto": self.produto,
                "data": self.data,
                "quantidade":self.quantidade,
                "preco_total": self.preco_total
        }
