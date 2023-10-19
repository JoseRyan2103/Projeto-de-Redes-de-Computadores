from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = []
id_counter = 1

@app.route('/enviar', methods=['POST'])
def enviar():
    global id_counter
    msg = request.json.get('mensagem')
    if msg:
        mensagem = {"id": id_counter, "mensagem": msg}
        mensagens.append(mensagem)
        id_counter += 1
        print(f"Mensagem recebida: {msg}")
        return jsonify({'status': 'Mensagem enviada'}), 200
    return jsonify({'status': 'Erro ao enviar mensagem'}), 400

@app.route('/receber', methods=['GET'])
def receber():
    return jsonify({'mensagens': mensagens})

if __name__ == '__main__':
    app.run(debug=True, port=5555)