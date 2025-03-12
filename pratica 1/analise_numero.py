def analise_numero():
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para sair: ")
        if entrada.lower() == "fim":
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1  # Aqui você estava esquecendo de incrementar a variável impares
        except ValueError:
            print("Erro! Digite um número inteiro")
            continue
        
    print(f"\nResultado final:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Chama a função
analise_numero()
