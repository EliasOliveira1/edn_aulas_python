import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requestst.get(url)
        resposta.raise_for_status()
        dados = resposta.josn()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP : {dados['cep']}
        LOGRADOURO: {dados['logradouro']}
        BAIRRO: {dados['bairro']}
        CIDADE: {dados['localidade']}
        ESTADO: {dados['estado']}
        """
    except requests.RequestException as e:
        return f"Erro na consulta"
def main():
    cep = input("Digite um CEP valido (somente números):")
    print("consultando CEP..... ")
    resultado = consulta_cep(cep)
    print(resultado)
if __name__ == "__main__":

    consulta_cep()