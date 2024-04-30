from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de exemplo (substitua isso por uma base de dados real)
tickets = [
    {"id": 1, "title": "Problema na impressora", "description": "A impressora não está imprimindo corretamente."},
    {"id": 2, "title": "Problema no software", "description": "O software está apresentando erros ao iniciar."},
]

# Página inicial para visualização dos chamados
@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)

# Página para criação de um novo chamado
@app.route('/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        # Adicione o novo chamado à lista de tickets
        tickets.append({"id": len(tickets) + 1, "title": title, "description": description})
        return redirect(url_for('index'))
    return render_template('create_ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
