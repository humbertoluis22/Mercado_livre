# Raspagem de Tela com Selenium e Flask

Este projeto realiza a raspagem de informações de produtos do Mercado Livre utilizando Selenium. As informações obtidas são armazenadas em um banco de dados local (SQLite). O framework utilizado para a automação e gerenciamento das requisições é o Flask.

## Funcionalidades

- Raspagem de dados de produtos do Mercado Livre
- Armazenamento das informações raspadas em um banco de dados SQLite
- Interface web em Flask para iniciar e monitorar a raspagem de dados

## Tecnologias Utilizadas

- Selenium: Para a automação da raspagem de dados.
- Flask: Framework web para gerenciar as requisições e servir a interface web.
- SQLite: Banco de dados local para armazenar as informações raspadas.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.11.8
- Navegador (Chrome, Firefox, etc.) e o respectivo WebDriver (Chromedriver, Geckodriver, etc.)

### Executando o codigo 
-certifique-se de ter criando uma ambiente virtual e feito feito as instalações dos pacotes que estão no requirements.txt
```
pip install -r requirements.txt
```
- Executar o arquivo rotas.py
- copiar o link do localHost gerado e adicionar ao final '/inicio'

### Utilizando o projeto 
- Informe o nome do produto 
- Informe a quantidade de produtos para busca
