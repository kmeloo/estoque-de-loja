from config.config import *
from testes import *

# aplicação de contexto
with app.app_context():

    teste_venda.run()
