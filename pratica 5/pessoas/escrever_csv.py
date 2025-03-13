import pandas
import csv

arquivo_csv = "dados_pessoas.csv"

dados = {
    ["Nome", "idade","cidade"],
    ["Elias","26","Itaboraí"]

}

with open(arquivo_csv, "w"):
    csv.dump(dados)
    print(f"Dados gravados em {arquivo_csv}")