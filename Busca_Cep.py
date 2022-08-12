# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:30:36 2022

@author: Everton Castro
"""
import requests

def CepValido(Cep):
    Cep = Cep.replace('-', '')
    if len(Cep) == 7 or 9:
        return True
    else:
        return False
        
def BuscaCep(sCep = '70150-903'):
    if CepValido(sCep):
        try:
            requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(sCep))
            if requisicao.status_code == 200 <= 299:
                try:
                    conteudo = requisicao.json()
                    return conteudo
                except Exception:
                    raise Exception('Ocorreu um erro não identificado, Verifique o cep informado')
            elif requisicao.status_code == 100 <= 199:
                print(f'resposta de informação: {requisicao.status_code}')
            elif requisicao.status_code == 300 <= 399:
                print(f'Redirecionamento: {requisicao.status_code}')
            elif requisicao.status_code == 400 <= 499:
                print(f'Erros do cliente: {requisicao.status_code}')
            elif requisicao.status_code == 500 <= 599:
                print(f'Erros do servidor: {requisicao.status_code}')
        except requests.ConnectionError as e:
            raise ConnectionError(f'Erro de conexão: {e}')
        except Exception:
            raise Exception('Ocorreu um erro não identificado, Verifique o cep informado')
        except:
            raise Exception('Ocorreu um erro não identificado, Verifique o cep informado')

if __name__ == '__main__':
    BuscaCep()