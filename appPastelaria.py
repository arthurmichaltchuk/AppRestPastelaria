from flask import Flask, session
import os
from datetime import timedelta

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario
from mod_index.index import bp_index
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_erro.erro import bp_erro
from mod_login.login import bp_login

app = Flask(__name__)

# gerando uma chave randômica para secret_key
app.secret_key = os.urandom(12).hex()

# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_index)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_erro)
app.register_blueprint(bp_login)

# método para renovar o tempo da sessão
@app.before_request
def before_request():
    session.permanent = True
    _tempo = 15
    session['tempo'] = _tempo
    # o padrão é 31 dias...
    app.permanent_session_lifetime = timedelta(minutes=_tempo)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)