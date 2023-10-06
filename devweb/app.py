from flask import Flask, render_template

app = Flask('__name__')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quemsomos')
def quem():
    return render_template("quemsomos.html")

@app.route('/contato')
def contatos():
    return render_template("contato.html")


