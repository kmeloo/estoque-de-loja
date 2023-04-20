from config.config import *

@app.route("/listar_produtos")
def listar_produtos():
    try:
       
        lista_retorno = [x.json() for x in lista]
        
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})