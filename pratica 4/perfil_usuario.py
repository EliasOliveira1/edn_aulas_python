import requests

def usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()["resultado"]
        nome = f"{dados["Nome"]}"
        email = dados["email"]
        pais = dados["location"]["country"]
        return f"Nome: {nome}\n {email}\n {pais}"
    except requests.RequestException as e:
        return f"Erro {e}"
def main():
    print("Criando usuario")
    usuario = usuario_aleatorio()
    print(usuario)
