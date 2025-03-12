import requests
from datetime import datetime

def cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Corrigido para "resposta"
        dados = resposta.json()
        cotacao = dados.get(f"{moeda}BRL")  # Certificando-se de que a chave está correta
        if not cotacao:
            return "Cotação não encontrada"
        
        valor = float(cotacao['bid'])
        maximo = float(cotacao['high'])
        minimo = float(cotacao['low'])
        
        # A data de cotação é fornecida no formato ISO 8601, então não é necessário usar fromtimestamp
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data e hora atual
        
        return {
            'valor': valor,
            'maximo': maximo,
            'minimo': minimo,
            'data_hora': data_hora
        }
        
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter dados: {e}"

# Exemplo de uso:
moeda = "USD"  # Aqui você pode passar qualquer moeda disponível
resultado = cotacao(moeda)
print(resultado)
