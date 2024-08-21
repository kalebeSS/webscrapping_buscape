# Web Scraping de Preços de TVs LED 50 polegadas 4K

Este projeto realiza web scraping dos preços de TVs LED 50 polegadas 4K no site Buscapé. Os dados coletados são salvos em um arquivo CSV e enviados por email como um anexo.

## Funcionalidades

- Raspa os títulos e preços das TVs de uma página de busca do Buscapé.
- Salva os dados coletados em um arquivo CSV.
- Envia o arquivo CSV por email como um anexo.

## Requisitos

- Python 3.6+
- Acesso à internet
- Conta de email no Gmail (com uma senha de app configurada se a autenticação de dois fatores estiver habilitada)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   cd nome_do_repositorio

   pip install -r requirements.txt

2. **Verifique suas credenciais no codigo**
   ```bash
   email_usuario = 'seu_email@gmail.com'
   email_senha = 'sua_senha_de_app'

3> **Verifique o Destinatário e o Assunto**
   ```bash
   destinatario = 'email_destinatario@gmail.com'
   assunto = 'Preços de TVs LED 50 polegadas 4K'
