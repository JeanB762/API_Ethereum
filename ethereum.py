import requests
import datetime
import json


def requisicao():
    try:
        req = requests.get('https://www.mercadobitcoin.net/api/ETH/ticker/')
        ETH = json.loads(req.text)
        return ETH
        #return ETH['ticker']
    except:
        print("Erro de conexão")
        return None

def printar_detalhes(e):
    print(datetime.datetime.now())
    print('Maior alta do dia: R$', e['ticker']['high'])
    print('Menor baixa do dia: R$', e['ticker']['low'])
    print('Ultima cotação: R$', e['ticker']['last'])
    print('')


cotar = True
while cotar:
    cotar = input('Digite 1 para realizar a cotação e 0 para encerrar: ')
    if cotar == '1':
        cot = requisicao()
        printar_detalhes(cot)
    elif cotar == '0':
        print('Saindo...')
        cotar = False
    else:
        print('Opção inválida!')
