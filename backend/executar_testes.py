from config.config import *
from teste import *

# aplicação de contexto
with app.app_context():

    teste_venda.run()
