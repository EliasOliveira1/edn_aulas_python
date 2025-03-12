from datetime import datetime

def calcular_idade_em_dias(data_nascimento):
    # Converte a data de nascimento de string para um objeto datetime
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    
    # Obtém a data atual
    data_atual = datetime.today()
    
    # Calcula a diferença entre a data atual e a data de nascimento
    idade_em_dias = (data_atual - data_nascimento).days
    
    return idade_em_dias

# Exemplo de uso
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
idade_em_dias = calcular_idade_em_dias(data_nascimento)
print(f"Sua idade em dias é: {idade_em_dias} dias.")
