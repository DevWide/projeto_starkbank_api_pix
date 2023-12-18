# Projeto de Integração com a API da StarkBank
Esse projeto foi desenvolvido para o processo seletivo de engenheiro de qualidade de software na StarkBank. Ele utiliza a API da StarkBank para criar transferências PIX automáticas e gerar um relatório detalhado sobre os resultados dessas transferências.

# Objetivo
O objetivo deste projeto é criar 10 transferências PIX a cada 3 horas para pessoas aleatórias durante um período de 24 horas, utilizando o ambiente de emulação Sanbox da StarkBank. O projeto também inclui a geração de um relatório automatizado que detalha os resultados dos testes.

# Funcionalidades
* **Criação Automatizada de Transferência PIX:** Cria 10 transferências PIX a cada 3 horas para destinatários aleatórios.
* **Relatório de Resultados:** Gera um relatório detalhando:
    * Percentual de sucesso das transferências.
    * Possíveis erros nas transferências que falharam.
    * Tempo médio entre a criação da transferência PIX e o registro do resultado

# Tecnologias Utilizadas
* Python
* StarkBank SDK

# Configuração do Projeto
## Pré-requisitos:
* Python 3.x
* Acesso ao ambiente Sandbox da StarkBank

# Instalação
1. Clone o repositório para a sua máquina local.
2. Instale as dependências necessárias utilizando `pip`:
````
pip install starkbank
````

# Configuração
1. Obtenha suas credenciais de acesso (ID do projeto e chave privada, através deste link - https://starkbank.com/faq/how-to-create-ecdsa-keys). Utilizei a opção 3!
2. Insira suas credenciais no local apropriado dentro do script principal.

# Uso
Para executar o projeto, basta rodar o script principal:
````
python3 my_app1.py
````

# Testes Unitários
Este projeto inclui também testes unitários para garantir que as funcionalidades principais como a criação de transferências PIX e a obtenção do status das transferências, funcionem conforme o esperado. Os testes foram desenvolvidos utilizando a biblioteca *'unittest'* do Python.

Para executar os testes, use o seguinte comando:
````
python3 -m unittest tests_my_app.py
````

**Os testes cobrem os seguintes aspectos:**
*  `test_create_pix_transfers_successful`: Verifica se a função `create_pix_transfers` cria transferências corretamente quando não há erros.
*  `test_create_pix_transfers_exception`: Testa o comportamento da função `create_pix_transfers` em caso de erros durante a criação de transferências.

# Estrutura do Código:
O script principal deste projeto é responsável por criar transferências PIX automáticas usando a API da StarkBank e por gerar um relatório detalhado sobre os resultados dessas transferências. Abaixo está uma descrição das principais partes do código:

## Autenticação
O script inicia configurando a autenticação com a API da StarkBank. Isso é feito através do objeto Project que recebe o ambiente ("sandbox"), o ID do projeto e a chave privada.
````
project = starkbank.Project(
    environment="sandbox",
    id="",  # ID do projeto
    private_key="""-----BEGIN EC PRIVATE KEY-----
        -----END EC PRIVATE KEY-----
    """  # Chave privada
)
starkbank.user = project

````
## Função create_pix_transfers
Esta função cria 10 transferências PIX para destinatários aleatórios. Cada transferência é definida com um valor aleatório, dados bancários fixos e um nome aleatório. A função trata exceções para garantir a robustez do processo de criação de transferências.
````
def create_pix_transfers():
    # Criação de transferências PIX
    ...
    return created_transfers

````

## Loop Principal e Geração de Relatório
O script entra em um loop que dura 24 horas, criando transferências PIX a cada 3 horas. Cada transferência é registrada em transfer_logs. Após 24 horas, um relatório é gerado, incluindo o total de transferências, a taxa de sucesso, os tipos de erros e o tempo médio de processamento.
````
def main():
    # Loop principal e geração de relatório
    ...
````











