from config.config import *
from modelo.venda import *

@app.route("/listar_vendas")
def listar_vendas():
    try:
        # pega as vendas
        todos = db.session.query(Venda).all()

        # transforma as vendas em json
        lista_retorno = [x.json() for x in todos]
        
        # prepara o retorno
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        
        #jsonifica e retorna
        return jsonify(meujson)
        
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
