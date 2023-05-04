from config.config import *
from rotas.listar_vendas import *
from rotas.incluir_venda import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend estoque de loja'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True, host="0.0.0.0")
