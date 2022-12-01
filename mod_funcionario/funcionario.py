from flask import Blueprint, render_template, request
import requests
from funcoes import Funcoes
from mod_login.login import validaSessao

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
@validaSessao
def formListaFuncionario():
    response = requests.get(urlApiFuncionarios, headers=headers)
    result = response.json()
    return render_template('formListaFuncionario.html', result=result)

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
@validaSessao
def formFuncionario():
    return render_template('formFuncionario.html')

@bp_funcionario.route('/insert', methods=['POST'])
@validaSessao
def insert():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])

        # monta o JSON para envio a API
        payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone': telefone, 'grupo': grupo, 'senha': senha}
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()

        return render_template('formListaFuncionario.html', msg=result)
        
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e)