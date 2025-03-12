def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou SAIR para encerrar): ")
        if senha.lower() == "sair":  # Melhor fazer a comparação com 'sair' em minúsculas
            print("Programa encerrado")
            break
        if len(senha) < 8:
            print("Senha fraca: deve ter no mínimo 8 caracteres")
            continue
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número")
            continue
        print("Senha forte e válida!")
        break

verifica_senha()  # Chamada da função corrigida