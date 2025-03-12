import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha
tamanho_senha = int(input("Digite o tamanhp da senha: "))
nova_senha = gerar_senha(tamanho_senha)
print(f"A senha gerada é: {nova_senha}")
