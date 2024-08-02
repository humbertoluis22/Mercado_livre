from flask import Flask,render_template,request,redirect
from mercadoria import Mercadoria
from mercado_livre import MercadoLivre
from sqlite import *

app = Flask(__name__)

mercadorias_ = []


@app.route('/inicio')
def introducao():
    return render_template('pag1.html')

@app.route('/filtrar',methods=['GET','POST'])
def filtrar():
    
    produto = request.form['nome_produto']
    quantidade =request.form.get('quantidade')

    if quantidade == '' or produto == '':
        return render_template('pag1.html')

    quantidade = int(quantidade)
    mercado = MercadoLivre()
    mercado.acessar_ambiente()
    mercado.escolher_produto(produto) 

    banco_db = Sqlite('mercadorias.db','mercadorias')
    banco_db.dropar_tabela()
    banco_db.criar_banco()

    quantidade_produto = 1
    i = 1
    while quantidade_produto <= quantidade:
        if not mercado.valida_item_pag(i):
            mercado.trocar_pagina()
            i = 1   

        nome_produto = mercado.recolher_nome_produto(i) 
        avaliacao = mercado.recolher_avaliacao(i)
        valor = mercado.recolher_valor(i)
        vendedor= mercado.recolher_vendedor(i)
        parcelas = mercado.recolher_parcelas(i)

        banco_db.inserir_info(nome_produto,vendedor,
                            avaliacao,valor,parcelas)

        mercadoria = Mercadoria(nome_produto,vendedor,
                                avaliacao,valor,parcelas)
        mercadorias_.append(mercadoria)

        
        i += 1
        quantidade_produto += 1

    # return redirect('/inicio')
    return render_template('page2.html',mercadorias = mercadorias_)

@app.route('/page2')
def tabela():
    return render_template('page2.html')

app.run(debug=True)