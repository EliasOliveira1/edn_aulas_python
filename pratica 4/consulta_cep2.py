import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)  # Corrigido para requests.get
        resposta.raise_for_status()
        dados = resposta.json()  # Corrigido para resposta.json()
        if "erro" in dados:
            return "CEP não encontrado."
        return f"""
        CEP: {dados['cep']}
        LOGRADOURO: {dados['logradouro']}
        BAIRRO: {dados['bairro']}
        CIDADE: {dados['localidade']}
        ESTADO: {dados['uf']}  # Corrigido para 'uf' (abreviação do estado)
        """
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"  # Mostrando a exceção para facilitar o diagnóstico

def main():
    cep = input("Digite um CEP válido (somente números): ")
    print("Consultando CEP... ")
    resultado = consulta_cep(cep)
    print(resultado)

if __name__ == "__main__":
    main()  # Corrigido para chamar main(), não consulta_cep()
