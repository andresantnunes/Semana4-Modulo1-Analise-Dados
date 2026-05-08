import pandas as pd

try:
    df = pd.read_csv("./aula2/file-read/vendas_modelo.csv")
    # cria uma estrutura dataFrame
    # temos menos controle
    # mais operações e rapizes
    # mais uso de memória
    print(df.head())
except FileNotFoundError:
    print("Error: File not found.")
except pd.errors.EmptyDataError:
    print("Error: File is empty.")
except Exception as e:
    print(f"An error occurred: {e}")