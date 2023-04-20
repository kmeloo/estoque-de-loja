from config.config import *
from modelo.venda import *

@app.route("/incluir_venda", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        nova = Venda(**dados)
        db.session.add(nova)
        db.session.commit()

        return jsonify({"resultado": "ok", "detalhes":"ok"})
    except Exception as e:

        return jsonify({"resultado": "erro", "detalhes":str(e)})
