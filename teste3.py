import datetime

def calcular_ano_nascimento():
    """
    Este programa pergunta a idade de uma pessoa e calcula o ano de seu nascimento.
    """
    while True:
        try:
            idade = int(input("Por favor, digite sua idade: "))
            
            if idade < 0:
                print("Por favor, insira uma idade válida (um número positivo).")
                continue
            
            ano_atual = datetime.date.today().year
            
            ano_nascimento = ano_atual - idade
            
            print(f"Você nasceu em {ano_nascimento}.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Chama a função para executar o programa
calcular_ano_nascimento()