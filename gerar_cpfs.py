def gerar_cpfs():
    def calcula_digito(cpf):
        """Função para calcular os dois dígitos verificadores de um CPF"""
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = 11 - (soma % 11)
        if primeiro_digito >= 10:
            primeiro_digito = 0

        soma = sum(int(cpf[i]) * (11 - i) for i in range(9)) + (primeiro_digito * 2)
        segundo_digito = 11 - (soma % 11)
        if segundo_digito >= 10:
            segundo_digito = 0

        return f"{primeiro_digito}{segundo_digito}"

    parte_fixa = input("Digite os seis dígitos centrais do CPF (ex: 807728): ")
    if not (parte_fixa.isdigit() and len(parte_fixa) == 6):
        print("Por favor, insira exatamente seis dígitos.")
        return
    
    prefixos = [f"{i:03}" for i in range(1000)]
    
    with open('cpfvalido.txt', 'w') as file:
        for prefixo in prefixos:
            cpf_base = f"{prefixo}{parte_fixa}"
            digitos_verificadores = calcula_digito(cpf_base)
            cpf_completo = f"{cpf_base}{digitos_verificadores}"
            file.write(cpf_completo + "\n")

    print(f"CPFs válidos gerados e salvos em 'cpfvalido.txt'.")

# Executa a função para gerar e salvar os CPFs
gerar_cpfs()

# Confirmação do arquivo gerado
import os
if os.path.isfile('cpfvalido.txt'):
    print("Arquivo 'cpfvalido.txt' criado com sucesso!")
else:
    print("Erro ao criar o arquivo.")

