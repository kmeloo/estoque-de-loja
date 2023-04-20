from config.config import *
from rotas.listar_vendas import *
from rotas.incluir_venda import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run()#debug=True)
