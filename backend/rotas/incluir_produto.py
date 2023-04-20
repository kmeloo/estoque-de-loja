from config.config import *
from modelo.produtos import *

@app.route("/incluir_produto", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        
        novo = Produto(**dados)

        lista.append(novo)

        return jsonify({"resultado": "ok", "detalhes":"ok"})
    except Exception as e:

        return jsonify({"resultado": "erro", "detalhes":str(e)})
