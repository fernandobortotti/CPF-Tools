# 🛠️ CPF Tools

Este repositório contém duas ferramentas úteis para a manipulação e consulta de CPFs. A primeira ferramenta gera uma lista de CPFs válidos com base em dígitos centrais fornecidos pelo usuário, enquanto a segunda realiza consultas automáticas de situação cadastral desses CPFs, utilizando um bot automatizado via Selenium para interagir com um site de consulta. Caso você já possua uma lista de CPFs, pode pular a etapa de geração e utilizar diretamente o bot de consulta.

Ambos os scripts foram testados em sistemas Linux.

## 📜 Ferramentas

### 1. **Gerador de CPFs Válidos** 📄

Este script gera CPFs válidos com base nos seis dígitos centrais fornecidos pelo usuário e calcula os dois dígitos verificadores. Os CPFs gerados são salvos em um arquivo de texto.

#### 🔧 Instruções de Uso

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/cpf-tools.git
   ```

2. Navegue até o diretório:

   ```bash
   cd cpf-tools
   ```

3. Execute o script:

   ```bash
   python gerar_cpfs.py
   ```

4. O programa solicitará que você insira os seis dígitos centrais do CPF (esse script foi criado para resolver o problema de quando o cpf está na forma: ???.123.456-??). Por exemplo:

   ```
   Digite os seis dígitos centrais do CPF (ex: 807728): 123456
   ```

5. O script gerará e salvará os CPFs no arquivo `cpfvalido.txt`.

#### 🚨 Observações:

- Certifique-se de inserir exatamente seis dígitos centrais.
- O arquivo `cpfvalido.txt` será salvo no mesmo diretório do script.

---

### 2. **Bot para Consultar Situação Cadastral de CPFs** 🤖

Este script utiliza o Selenium para consultar a situação cadastral de CPFs no site [https://www.situacao-cadastral.com/](https://www.situacao-cadastral.com/). O script lê uma lista de CPFs de um arquivo de entrada, realiza as consultas automaticamente e verifica se o nome encontrado corresponde ao nome fornecido pelo usuário. Caso o nome seja encontrado, o script permite ao usuário optar por continuar ou encerrar a execução. Além disso, o script salvará os CPFs e nomes, criando dois arquivos distintos: um para quando o nome encontrado `pessoa_encontrada.txt` e outro para os demais resultados `dados_nome_cpf.txt`, salvo no mesmo diretório.

---

### 🔧 Configuração do Ambiente Virtual

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações de bibliotecas Python no seu sistema.

1. Crie um ambiente virtual:

   ```bash
   python3 -m venv venv
   ```

2. Ative o ambiente virtual:

   - **Linux**

     ```bash
     source venv/bin/activate
     ```


3. **Instalação de Dependências:**

   Primeiro, certifique-se de que você tem o Python e as dependências necessárias instaladas. Execute:

   ```bash
   pip install -r requirements.txt
   ```

   Arquivo `requirements.txt`:

   ```txt
   selenium
   webdriver-manager
   ```

#### 🔧 Instruções de Uso


1. **Uso do Script:**

   O bot permite a consulta automática de CPFs e oferece a opção de lidar com CAPTCHA manualmente.

   - **Rodando sem CAPTCHA:**

     ```bash
     python bot.py cpfvalido.txt
     ```

   - **Rodando com CAPTCHA:**

     ```bash
     python bot.py cpfvalido.txt --captcha
     ```

2. **Como Funciona:**

   - O script solicitará o **primeiro nome** e o **último nome** da pessoa que você está procurando.
   - Durante as consultas, se o nome da pessoa for encontrado, o script perguntará se você deseja continuar a execução. Se escolher "N", o programa será encerrado.

#### 📂 Estrutura do Arquivo de Entrada

O arquivo `cpfvalido.txt` deve conter um CPF por linha, como no exemplo abaixo:

```txt
12345678901
12345678901
12345678901
```

#### 🔍 Exemplo de Uso

- **Quando o nome é encontrado:**

  ```
  Pessoa encontrada: Nome N. Sobrenome. Deseja continuar? (Y/N): N
  Nome encontrado: Nome N. Sobrenome. CPF: 12345678901
  ```

Aqui temos um problema, não consegui fazer o script encerrar de maneira correta. Então se a resposta for N, minha sugestão é usar o Ctrl+C para matar o script.

- **Quando o CPF não retorna um nome:**

  ```
  Consulta para o CPF 98765432100 falhou ou não retornou nome.
  ```

#### ⚙️ Argumentos:

- `cpfvalido`: Arquivo de texto contendo a lista de CPFs.
- `--captcha`: Habilita a opção de resolver CAPTCHA manualmente.

---

## 🚀 Tecnologias Utilizadas

- **Python** 🐍
- **Selenium** para automação de navegadores.
- **webdriver-manager** para gerenciar o ChromeDriver.

---

## Melhorias
- [ ] Opção com captcha não funciona por causa do Cloudflare, criar uma solução para esse problema.


## 📝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## ⚠️ Aviso Legal

O uso indevido desta ferramenta pode violar leis de privacidade, como a LGPD (Lei Geral de Proteção de Dados) no Brasil. Utilize estas ferramentas de forma responsável e apenas em cenários que respeitem os direitos de privacidade de terceiros.
