import requests


def buscar_avatar(usuario):
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']
