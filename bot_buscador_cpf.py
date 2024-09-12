import time
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

continuar = True
TEMPO_ESPERA = 2  # tempo de espera, por padrão 2 segundos para cada consulta funciona bem.

def setup_driver():
    """Função para configurar o WebDriver (Chrome) sem o modo headless"""
    # Instala o ChromeDriver automaticamente
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def obter_nome_usuario():
    """Função para capturar o nome completo do usuário"""
    primeiro_nome = input("Digite o primeiro nome da pessoa: ").strip()
    ultimo_nome = input("Digite o último nome da pessoa: ").strip()
    return primeiro_nome, ultimo_nome

def verificar_nome(nome_encontrado, primeiro_nome, ultimo_nome, cpf):
    """Função para verificar se o nome encontrado corresponde ao nome do usuário"""
    global continuar
    if primeiro_nome.lower() in nome_encontrado.lower() and ultimo_nome.lower() in nome_encontrado.lower():
        resposta = input(f"Pessoa encontrada: {nome_encontrado}. Deseja continuar? (Y/N): ").strip().upper()
        if resposta == "N":
            print(f"Nome encontrado: {nome_encontrado}. CPF: {cpf}")
            continuar = False
        return True
    return False

def consultar_cpf(driver, cpf, captcha, primeiro_nome, ultimo_nome):
    """Função para realizar a consulta de CPF e capturar o nome da pessoa"""
    driver.get("https://www.situacao-cadastral.com/")
    if captcha:
        input("Por favor, resolva o CAPTCHA e pressione Enter para continuar...")

    cpf_field = driver.find_element(By.ID, "doc")
    cpf_field.send_keys(cpf)
    submit_button = driver.find_element(By.ID, "consultar")
    submit_button.click()
    time.sleep(TEMPO_ESPERA)

    try:
        nome_element = driver.find_element(By.CSS_SELECTOR, "span.dados.nome")
        nome = nome_element.text
        print(f"Nome encontrado: {nome}")
        if not verificar_nome(nome, primeiro_nome, ultimo_nome, cpf):
            return nome, False  # Retorna o nome e uma flag indicando que não houve match
        return nome, True  # Retorna o nome e uma flag indicando que houve match
    except Exception as e:
        print(f"Consulta para o CPF {cpf} falhou ou não retornou nome.")
        return None, False

def processar_lista_cpfs(arquivo_cpfs, captcha, primeiro_nome, ultimo_nome):
    """Processa a lista de CPFs"""
    driver = setup_driver()
    
    with open(arquivo_cpfs, 'r') as file:
        cpfs = file.readlines()

    with open('dados_nome_cpf.txt', 'w') as arquivo_todos, open('pessoa_encontrada.txt', 'w') as arquivo_encontrados:
        for cpf in cpfs:
            if not continuar:
                break

            cpf = cpf.strip()
            if cpf:
                print(f"Consultando CPF: {cpf}")
                nome, match = consultar_cpf(driver, cpf, captcha, primeiro_nome, ultimo_nome)
                if nome:
                    # Salva todos os CPFs e nomes no arquivo 'dados_nome_cpf.txt'
                    arquivo_todos.write(f"{cpf}: {nome}\n")
                    # Se o nome der match, salva também no arquivo 'pessoa_encontrada.txt'
                    if match:
                        arquivo_encontrados.write(f"{cpf}: {nome}\n")
    
    driver.quit()

def main():
    """Função principal para manipular os argumentos do script"""
    parser = argparse.ArgumentParser(description="Bot para consultar CPFs em https://www.situacao-cadastral.com/")
    parser.add_argument("arquivo_cpfs", help="Caminho para o arquivo contendo a lista de CPFs")
    parser.add_argument("--captcha", action="store_true", help="Ativa a opção para resolver CAPTCHA manualmente")
    args = parser.parse_args()
    
    primeiro_nome, ultimo_nome = obter_nome_usuario()
    
    processar_lista_cpfs(args.arquivo_cpfs, args.captcha, primeiro_nome, ultimo_nome)

if __name__ == "__main__":
    main()
