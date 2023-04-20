from config.config import *
from modelo.produtos import *

@app.route("/incluir_venda", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        
        nova = Venda(**dados)

        lista.append(nova)

        return jsonify({"resultado": "ok", "detalhes":"ok"})
    except Exception as e:

        return jsonify({"resultado": "erro", "detalhes":str(e)})
