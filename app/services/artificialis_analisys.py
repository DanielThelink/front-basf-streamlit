import requests 
import json

def get_nps_data ():
    return requests.get("https://artificialis-analisys-backend.herokuapp.com/nps").json()
    
def post_analisys ():
    return requests.post("https://artificialis-analisys-backend.herokuapp.com/analisar").json()

def get_search_word_cloud (filter_value: str):
    return requests.get(f"https://artificialis-analisys-backend.herokuapp.com/nuvemPalavras?filtro={filter_value}").json()   

def get_current_word_cloud():
    return requests.get("https://artificialis-analisys-backend.herokuapp.com/nuvemPalavras").json() 

def get_search_commentary (filter_type: str, filter_value):
    return requests.get(f'https://artificialis-analisys-backend.herokuapp.com/pesquisa?{filter_type}={filter_value}&size=3').json()

def get_current_commentary ():
    return requests.get(f'https://artificialis-analisys-backend.herokuapp.com/pesquisa?size=3').json()