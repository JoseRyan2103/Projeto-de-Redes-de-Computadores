import os
import requests

SERVIDOR_URL = 'http://127.0.0.1:5555'

def enviar_mensagem():
    name = input('Digite seu nome: ')
    msg = input('Digite sua mensagem: ')
    mensagem_with_name = f'<{name}> {msg}'
    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'mensagem': msg})
    print(resposta.json()['status'])

def receber_mensagens():
    resposta = requests.get(f'{SERVIDOR_URL}/receber')
    mensagens = resposta.json()['mensagens']
    print("Mensagens recebidas:")
    for msg in mensagens:
        print(f"- {msg}")

def sair():
    print("Saindo do programa.")
    exit()

def limpar_tela():
    os.system('cls')

if __name__ == '__main__':

    while True:
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            enviar_mensagem()
        elif escolha == '2':
            receber_mensagens()
        elif escolha == '3':
            sair()
        else:
            print("Opção inválida.")
